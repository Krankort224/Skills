"""Replay recorded subscription-agent outputs; this is not fresh inference."""
from __future__ import annotations
import copy
import contextlib
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

TOOLS = Path(__file__).resolve().parent
TARGET = 'skills/context/references/graphify'
NAMES = ('graph.json', 'graph.html', 'GRAPH_REPORT.md')

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

d = module('structural_probe', TOOLS / 'probe_graphify_structure.py')
v = module('context_validator', TOOLS / 'validate_context_fragments.py')
book = (TOOLS / 'graphify.md').read_text(encoding='utf-8')
def block(name):
    found = re.search(r'```python\n(# context-' + name + r'\n.*?)\n```', book, re.S)
    assert found, name
    return found.group(1)
ASSEMBLE = block('semantic-assemble')
PUBLISH = block('publish-trio')

def clean_env():
    env = {k: val for k, val in os.environ.items() if not any(
        word in k.upper() for word in ('API_KEY', 'TOKEN', 'SECRET', 'PASSWORD', 'PROVIDER', 'AWS_', 'GOOGLE_', 'GEMINI_', 'OPENAI_', 'ANTHROPIC_', 'GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_COMMON_DIR', 'GIT_OBJECT_DIRECTORY', 'GIT_ALTERNATE_OBJECT_DIRECTORIES', 'GIT_REPLACE_REF_BASE'))}
    env.update(GRAPHIFY_BACKEND='none', GRAPHIFY_QUERY_LOG_DISABLE='1',
               PYTHONDONTWRITEBYTECODE='1', GIT_AUTHOR_NAME='Probe', GIT_AUTHOR_EMAIL='probe@example.invalid',
               GIT_COMMITTER_NAME='Probe', GIT_COMMITTER_EMAIL='probe@example.invalid',
               GIT_CONFIG_NOSYSTEM='1', GIT_TERMINAL_PROMPT='0', GIT_OPTIONAL_LOCKS='0',
               OPENAI_API_KEY='forbidden-synthetic', GEMINI_API_KEY='forbidden-synthetic')
    return env

def git(root, *args, data=None):
    return subprocess.run(['git', '-C', str(root), *args], input=data, capture_output=True,
                          env=clean_env(), check=True, timeout=60).stdout

def gt(root, *args):
    return git(root, *args).decode().strip()

def clone(remote, path):
    subprocess.run(['git', 'clone', '--quiet', str(remote), str(path)], env=clean_env(), check=True, timeout=60)
    return path

def materialize(repo, commit, path):
    path.mkdir()
    for name in NAMES:
        (path / name).write_bytes(git(repo, 'show', f'{commit}:{TARGET}/{name}'))

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def env_for(root, stage):
    return dict(clean_env(), CONTEXT_ROOT=str(root), CONTEXT_TOOLS=str(TOOLS),
                CONTEXT_STAGE=str(stage), CONTEXT_EXCLUDES='[]', GRAPHIFY_OUT=str(stage / 'native-cache'))

def publish(root, stage, remote, *, expected=None, ref='refs/heads/main', before='', success=True, reason=None):
    env = dict(env_for(root, stage), CONTEXT_EXPECTED=expected or gt(root, 'rev-parse', 'HEAD'),
               CONTEXT_REMOTE=str(remote), CONTEXT_REMOTE_REF=ref)
    return d.execute(PUBLISH, env, before=before, success=success, reason=reason)

def bind_labels(members, interpretation):
    return {'input_identity': members['input_identity'], 'evidence_identity':members['evidence_identity'], 'communities': interpretation}

def annotate(oldStage, newStage, text):
    from graphify.paths import write_json_atomic
    shutil.copytree(oldStage, newStage)
    report = newStage / 'GRAPH_REPORT.md'
    report.write_text(report.read_text(encoding='utf-8') + '\n' + text + '\n', encoding='utf-8')
    path = newStage / 'graph.json'
    graph = json.loads(path.read_text(encoding='utf-8'))
    graph['graph']['context']['artifacts']['GRAPH_REPORT.md'] = sha(report)
    write_json_atomic(path, graph, compact=True)

def build(root, case, work, *, assignments_override=None, dependency_reviews_override=None, fragments_override=None):
    """Fresh D plus explicitly recorded fragments; no provider or inferred labels."""
    work.mkdir()
    structural = work / 'structural'
    env = env_for(root, structural)
    env['CONTEXT_EXCLUDES'] = json.dumps(case['exclusions'])
    original = d.snapshot(root)
    d.run('profile-check', env)
    d.run('structural-build', env)
    assert d.snapshot(root) == original
    baseline = structural / 'artifacts/graph.json'
    structure = json.loads(baseline.read_text(encoding='utf-8'))
    names = set(structure['graph']['context']['sources'])
    assignments = assignments_override or {'grant': ['docs/policy.md', 'src/guard.py'],
        'note': [n for n in ('docs/note.md', 'docs/operator-note.md') if n in names],
        'extra': [n for n in ('docs/extra.md',) if n in names]}
    assignments = {k: files for k, files in assignments.items() if files}
    assert set().union(*map(set, assignments.values())) == names
    assert sum(map(len, assignments.values())) == len(names)
    sources, ranges = {}, {}
    for sid, files in assignments.items():
        ranges[sid] = []
        for name in files:
            raw = (root / name).read_bytes()
            lines = raw.decode('utf-8-sig').splitlines(keepends=True)
            sources[name] = {'sha256': hashlib.sha256(raw).hexdigest(), 'line_count': len(lines)}
            ranges[sid].append({'source_file': name, 'start': 1 if lines else 0, 'end': len(lines),
                                'sha256': hashlib.sha256(''.join(lines).encode('utf-8')).hexdigest()})
    plan = {'schema': 'context-semantic-v1', 'prompt_version': 'context-semantic-v1',
            'graphify_revision': '16218bfc80d4ca2799734d045039f7ed1a5fa9fb', 'scope': case['scope'],
            'structural_sha256': sha(baseline), 'sources': sources,
            'shards': [{'id': sid, 'ranges': rs} for sid, rs in ranges.items()],
            'expected_profile': v.profile(TOOLS), 'authority_sources': case['authority_sources'],
            'dependency_reviews': dependency_reviews_override if dependency_reviews_override is not None else case['dependency_reviews']}
    plan_path = work / 'plan.json'
    dump(plan_path, plan)
    fragments = fragments_override if fragments_override is not None else case['fragments']
    if isinstance(fragments, dict):
        fragments = list(fragments.values())
    paths = []
    for fragment in fragments:
        path = work / ('fragment-' + fragment['shard_id'] + '.json')
        dump(path, fragment)
        paths.append(path)
    assert {p.stem.removeprefix('fragment-') for p in paths} == set(assignments)
    output = work / 'mixed'
    env.update(CONTEXT_STRUCTURAL=str(baseline), CONTEXT_PLAN=str(plan_path),
               CONTEXT_FRAGMENTS=json.dumps(list(map(str, paths))), CONTEXT_MIXED_STAGE=str(output))
    members = json.loads(d.execute(ASSEMBLE, env).stdout)
    labels = bind_labels(members, case['community_interpretation'])
    label_path = work / 'labels.json'
    dump(label_path, labels)
    d.execute(ASSEMBLE, dict(env, CONTEXT_LABELS=str(label_path)))
    validated = v.validate_trio(output, root=root, require_current=True)
    assert d.snapshot(root) == original
    return output, validated, plan, paths

def init_repo(root, files):
    root.mkdir()
    subprocess.run(['git', 'init', '-q', '-b', 'main', str(root)], env=clean_env(), check=True)
    for name, contents in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents, encoding='utf-8')
    (root / '.gitignore').write_text('.env\ngraphify-out/\n', encoding='utf-8')
    (root / '.env').write_text('SECRET=fixture-only-never-publish\n', encoding='utf-8')
    placeholder = root / TARGET / '.gitkeep'
    placeholder.parent.mkdir(parents=True, exist_ok=True)
    placeholder.write_bytes(b'')
    git(root, 'add', '.')
    git(root, 'commit', '-qm', 'Fixture sources')
    assert '.env' not in gt(root, 'ls-files').splitlines()
    return gt(root, 'rev-parse', 'HEAD')

def assess_cases(cases, results):
    state = results['baseline'][1]['graph']['graph']['context']['maintenance']
    old = state['snapshot']
    current_profile = v.profile(TOOLS)
    expected = {'baseline':'noop', 'isolated-zero':'reuse_some', 'mixed-edit':'reextract_all',
                'addition':'reextract_all', 'rename':'reextract_all', 'deletion':'reextract_all',
                'exclusion':'reextract_all', 'edge-only':'reextract_all', 'branch-48-zero':'reextract_all'}
    assessments = {}
    for name, case in cases.items():
        root, validated = results[name][0], results[name][1]
        snap = validated['snapshot']
        # Observe missing/excluded old paths against the actual current root.
        snap = v.snapshot(root, snap['exclusions'], snap['authority_sources'],
                          previous_sources=old['sources'], scope=snap['scope'])
        first = v.assess_reuse(state, snap, current_profile)
        if name in ('rename', 'deletion'):
            assert first['status'] == 'blocked' and first['required_removal_confirmations']
            confirmations = {p: {'kind':'coordinator', 'evidence':'Fixture case explicitly confirms removal',
                                  'previous_sha256':old['sources'][p]}
                             for p in first['required_removal_confirmations']}
            first = v.assess_reuse(state, snap, current_profile, confirmed_removals=confirmations)
        if name == 'exclusion':
            assert snap['previous_status']['docs/note.md'] == 'excluded'
            assert (root / 'docs/note.md').is_file()
        assert first['status'] == expected[name], (name, first)
        if name == 'isolated-zero':
            assert set(first['reusable']) == {'grant'}
        if name == 'edge-only':
            assert 'note' in first['invalidated']
        assessments[name] = first['status']
    for field in ('schema', 'prompt_schema', 'requirements_sha256', 'graphify_revision'):
        changed = copy.deepcopy(current_profile)
        changed[field] = str(changed[field]) + '-changed'
        assert v.assess_reuse(state, old, changed)['status'] == 'reextract_all'
    changed = copy.deepcopy(old)
    changed['scope'] += ' changed'
    assert v.assess_reuse(state, changed, current_profile)['status'] == 'reextract_all'
    for previous in (None, {}, {'schema':state['schema']}, dict(state, integrity_sha256='corrupt')):
        assert v.assess_reuse(previous, old, current_profile)['status'] == 'reextract_all'
    return assessments

def check_order_and_labels(base, results):
    # Native ordered last-match policy, including idempotent exact duplicates.
    root = base / 'ordered-rules'
    root.mkdir()
    git(root, 'init', '-q', '-b', 'main')
    (root / 'a.md').write_text('# A\n')
    (root / 'code.py').write_text('value = 1\n')
    left = v.snapshot(root, ['*.md', '!a.md'], scope='Ordered native exclusion control')
    right = v.snapshot(root, ['!a.md', '*.md'], scope='Ordered native exclusion control')
    assert 'a.md' in left['sources'] and 'a.md' not in right['sources'] and left['identity'] != right['identity']
    again = v.snapshot(root, left['exclusions'], scope=left['scope'])
    assert again['identity'] == left['identity']
    duplicate = v.snapshot(root, ['*.md', '!a.md', '*.md'], scope=right['scope'])
    assert duplicate['identity'] == right['identity']
    before = left['identity']
    (root / '.env').write_text('SECRET=never-export-this-value\n')
    assert v.snapshot(root, left['exclusions'], scope=left['scope'])['identity'] == before
    (root / '.env').write_text('SECRET=another-private-value\n')
    assert v.snapshot(root, left['exclusions'], scope=left['scope'])['identity'] == before
    # Same sources/profile and IDs but changed valid semantic rationale must not
    # silently reuse the old community interpretation file.
    repo, checked, stage, plan, paths = results['baseline']
    work = base / 'changed-semantic-evidence'
    work.mkdir()
    altered = []
    for source in paths:
        payload = json.loads(source.read_text())
        if payload['shard_id'] == 'grant':
            payload['edges'][0]['rationale'] += ' Source-backed wording reviewed again.'
        target = work / source.name
        dump(target, payload)
        altered.append(target)
    original_work = paths[0].parent
    env = env_for(repo, original_work / 'structural')
    env.update(CONTEXT_PLAN=str(original_work / 'plan.json'), CONTEXT_STRUCTURAL=str(original_work / 'structural/artifacts/graph.json'), CONTEXT_FRAGMENTS=json.dumps(list(map(str, altered))), CONTEXT_MIXED_STAGE=str(work / 'rejected-stage'))
    members = json.loads(d.execute(ASSEMBLE, env).stdout)
    old = json.loads((original_work / 'labels.json').read_text())
    assert members['input_identity'] == old['input_identity'] and members['evidence_identity'] != old['evidence_identity']
    assert {cid:sorted(n['id'] for n in nodes) for cid,nodes in members['communities'].items()} == {cid:item['members'] for cid,item in old['communities'].items()}
    d.execute(ASSEMBLE, dict(env, CONTEXT_LABELS=str(original_work / 'labels.json')), success=False, reason='Interpretation must match actual semantic evidence')
    assert not (work / 'rejected-stage').exists()
    return {'ordered_native_rules':True,'duplicate_policy_idempotent':True,'secret_presence_excluded':True,'stale_labels_same_input_ids_refused':True}


def check_worktrees_and_export(base, remote, stage, cases, old_build):
    owner = clone(remote, base / 'branch-owner')
    main_tip = gt(owner, 'rev-parse', 'HEAD')
    # Isolated fixture branches only. The source Skills checkout stays on main.
    git(owner, 'branch', 'trial-48')
    tree = base / 'worktree Связи 48'
    git(owner, 'worktree', 'add', '--quiet', str(tree), 'trial-48')
    branch_case = cases['branch-48-zero']
    for name in ('docs/policy.md','src/guard.py'):
        (tree / name).write_text(branch_case['files'][name])
    git(tree,'add','docs/policy.md','src/guard.py')
    git(tree,'commit','-qm','Change scoped 48-hour branch inputs')
    branch_source = gt(tree,'rev-parse','HEAD')
    assert branch_source != main_tip and gt(owner,'rev-parse','HEAD') == main_tip
    git(tree,'push','-q',str(remote),'HEAD:refs/heads/trial-48')
    rebuilt, checked, plan, paths = build(tree, branch_case, base / 'branch-build')
    assert any(n.get('label') == 'Current 48-hour original-issue grant' for n in checked['graph']['nodes'])
    done = json.loads(publish(tree,rebuilt,remote,expected=branch_source,ref='refs/heads/trial-48').stdout)
    assert done['status']=='published'
    assert gt(owner,'ls-remote','--refs',str(remote),'refs/heads/main').split()[0]==main_tip
    assert gt(owner,'rev-parse','HEAD')==main_tip and gt(tree,'rev-parse','HEAD')==branch_source
    view = base/'branch-view'
    materialize(tree,done['commit'],view)
    v.validate_trio(view,root=tree,require_current=True)
    try:
        v.validate_trio(view,root=owner,require_current=True)
    except ValueError as error:
        assert 'differs from staged trio' in str(error)
    else:
        raise AssertionError('Different branch inputs accepted as fresh')
    # Native exporter failure after the initial JSON must leave a visibly
    # incomplete new stage, never a complete/published replacement.
    original_root, original_checked, original_stage, original_plan, original_paths = old_build
    old_work = original_paths[0].parent
    failed = base/'interrupted-export'
    env = env_for(original_root,old_work/'structural')
    env.update(CONTEXT_PLAN=str(old_work/'plan.json'),CONTEXT_STRUCTURAL=str(old_work/'structural/artifacts/graph.json'),CONTEXT_FRAGMENTS=json.dumps(list(map(str,original_paths))),CONTEXT_MIXED_STAGE=str(failed),CONTEXT_LABELS=str(old_work/'labels.json'))
    d.execute(ASSEMBLE,env,before='import graphify.exporters.html as _html\n_html.to_html=lambda *a,**kw:False',success=False,reason='AssertionError')
    assert (failed/'graph.json').is_file() and not (failed/'graph.html').exists()
    publish(owner,failed,remote,expected=main_tip,success=False,reason='Incomplete/unexpected trio')
    assert gt(owner,'ls-remote','--refs',str(remote),'refs/heads/main').split()[0]==main_tip
    return {'actual_linked_worktrees':True,'branch_ref_isolation':True,'cross_branch_freshness_refused':True,'native_interrupted_export_retained_last_good':True}


def run_more(base, remote, current_commit, stage, api):
    """Use only the supplied bare fixture and new children of base.

    Caller supplies the actual maintenance probe APIs and valid reviewed stage.
    Each fault hook is prepended to the real publisher in a separate process.
    """
    base, remote, stage = map(Path, (base, remote, stage))
    work = base / "publication-more-proof"
    work.mkdir()  # fresh, task-owned directory only
    git, gt = api["git"], api["gt"]
    publish, clone = api["publish"], api["clone"]
    annotate, materialize = api["annotate"], api["materialize"]
    target, names = api["TARGET"], api["NAMES"]
    ref = "refs/heads/main"

    def tip(repo):
        lines = gt(repo, "ls-remote", "--refs", str(remote), ref).splitlines()
        assert len(lines) == 1
        oid, actual = lines[0].split("\t")
        assert actual == ref
        return oid

    def check_commit(repo, child, parent, approved):
        assert gt(repo, "rev-parse", child + "^") == parent
        for name in names:
            assert git(repo, "show", f"{child}:{target}/{name}") == (approved / name).read_bytes()

    def index(repo):
        path = Path(gt(repo, "rev-parse", "--git-path", "index"))
        return (repo / path).read_bytes() if not path.is_absolute() else path.read_bytes()

    def hook(body):
        # Inserted before d.GUARD and the unmodified publisher. The hook runs
        # only in its subprocess, and its paths are under this test directory.
        return '''import subprocess, time\nfrom pathlib import Path\n_real_run = subprocess.run\ndef _intercept(*args, **kwargs):\n    argv = args[0]\n    if isinstance(argv, (list, tuple)) and "push" in argv:\n''' + body + '''\n    return _real_run(*args, **kwargs)\nsubprocess.run = _intercept\n'''

    # Two independent clones both reach the actual push after all publisher
    # prechecks. Release them only after both are waiting; one lease wins.
    a, b = work / "race-a", work / "race-b"
    clone(remote, a); clone(remote, b)
    stage_a, stage_b = work / "stage-a", work / "stage-b"
    annotate(stage, stage_a, "Approved race annotation A")
    annotate(stage, stage_b, "Approved race annotation B")
    indexes = (index(a), index(b))
    barrier = work / "barrier"
    barrier.mkdir()
    def barrier_hook(name):
        return hook(f'''        folder = Path({str(barrier)!r})
        (folder / {name!r}).write_text("ready")
        deadline = time.monotonic() + 5
        while len(list(folder.iterdir())) < 2 and time.monotonic() < deadline:
            time.sleep(0.01)
        if len(list(folder.iterdir())) != 2:
            raise RuntimeError("writer barrier timed out")''')
    def attempt(repo, approved, name):
        try:
            result = publish(repo, approved, remote, expected=current_commit, before=barrier_hook(name))
            return json.loads(result.stdout)
        except AssertionError as error:
            # Reject unrelated failures: the loser must reach the publisher push.
            assert "Push failed or outcome uncertain" in str(error), str(error)
            return None
    with ThreadPoolExecutor(max_workers=3) as pool:
        fa = pool.submit(attempt, a, stage_a, "a")
        fb = pool.submit(attempt, b, stage_b, "b")
        # Reader pins old commit, so a concurrent ref advance cannot mix files.
        reader = pool.submit(materialize, a, current_commit, work / "old-view")
        results = [fa.result(timeout=20), fb.result(timeout=20)]
        reader.result(timeout=20)
    winners = [r for r in results if r is not None]
    assert len(winners) == 1 and winners[0]["status"] == "published", results
    winner = winners[0]["commit"]
    assert tip(a) == winner
    expected_stage = stage_a if results[0] else stage_b
    git(a, "fetch", "--quiet", str(remote), winner)  # winner may belong to the other clone
    check_commit(a, winner, current_commit, expected_stage)
    for name in names:
        assert (work / "old-view" / name).read_bytes() == git(a, "show", f"{current_commit}:{target}/{name}")
    assert index(a) == indexes[0] and index(b) == indexes[1]
    assert gt(a, "rev-parse", "HEAD") == gt(b, "rev-parse", "HEAD") == current_commit
    assert not gt(a, "status", "--porcelain") and not gt(b, "status", "--porcelain")

    # Move the branch with a distinct empty fast-forward commit exactly inside
    # the publisher's push call, after its remote-tip check and candidate build.
    moving = work / "moving"
    clone(remote, moving)
    move_stage = work / "move-stage"
    annotate(stage, move_stage, "Approved lease race annotation")
    moving_index = index(moving)
    actor_path = work / "actor-oid"
    race_hook = hook(f'''        repo = {str(moving)!r}
        old = {winner!r}
        tree = _real_run(["git", "-C", repo, "rev-parse", old + "^{{tree}}"], capture_output=True, check=True).stdout.decode().strip()
        actor = _real_run(["git", "-C", repo, "commit-tree", tree, "-p", old], input=b"Competing fast-forward\\n", capture_output=True, check=True).stdout.decode().strip()
        _real_run(["git", "-C", repo, "push", {str(remote)!r}, actor + ":{ref}"], capture_output=True, check=True)
        Path({str(actor_path)!r}).write_text(actor)''')
    publish(moving, move_stage, remote, expected=winner, before=race_hook, success=False)
    actor = actor_path.read_text()
    assert tip(moving) == actor and gt(moving, "rev-parse", actor + "^") == winner
    check_commit(moving, winner, current_commit, expected_stage)
    assert index(moving) == moving_index and gt(moving, "rev-parse", "HEAD") == winner

    # On an otherwise successful real push, simulate the client losing the ack.
    # Inspect the remote immediately; never retry an uncertain result.
    lost = work / "lost-ack"
    clone(remote, lost)
    lost_stage = work / "lost-stage"
    annotate(stage, lost_stage, "Approved lost acknowledgment annotation")
    lost_index = index(lost)
    lost_hook = hook('''        result = _real_run(*args, **kwargs)
        if result.returncode == 0:
            raise subprocess.TimeoutExpired(argv, 1)
        return result''')
    publish(lost, lost_stage, remote, expected=actor, before=lost_hook, success=False, reason="TimeoutExpired")
    published = tip(lost)
    assert published != actor
    check_commit(lost, published, actor, lost_stage)
    assert index(lost) == lost_index and gt(lost, "rev-parse", "HEAD") == actor

    # A changed tracked source after candidate creation must fail the final
    # validation, before the remote ref changes. Only this isolated clone is edited.
    mutation = work / "mutation"
    clone(remote, mutation)
    mutate_stage = work / "mutate-stage"
    annotate(stage, mutate_stage, "Approved source-race annotation")
    snapshot = api["v"].validate_trio(mutate_stage, root=mutation, require_current=True)["snapshot"]
    source = mutation / next(iter(snapshot["sources"]))
    before = source.read_bytes()
    mutation_hook = f'''import subprocess\nfrom pathlib import Path\n_real_run = subprocess.run\ndef _intercept(*args, **kwargs):\n    argv = args[0]\n    result = _real_run(*args, **kwargs)\n    if isinstance(argv, (list, tuple)) and "commit-tree" in argv and result.returncode == 0:\n        with Path({str(source)!r}).open("ab") as stream:\n            stream.write(b"\\n# isolated race test\\n")\n    return result\nsubprocess.run = _intercept\n'''
    mutation_index = index(mutation)
    publish(mutation, mutate_stage, remote, expected=published, before=mutation_hook, success=False)
    assert tip(mutation) == published and source.read_bytes() != before
    assert index(mutation) == mutation_index and gt(mutation, "rev-parse", "HEAD") == published

    # Restore a previously approved stage as a NEW child, never by moving a ref
    # backward. It is accepted only if the validator confirms same source inputs.
    rollback = work / "rollback"
    clone(remote, rollback)
    restored = json.loads(publish(rollback, stage, remote, expected=published).stdout)
    assert restored["status"] == "published" and tip(rollback) == restored["commit"]
    check_commit(rollback, restored["commit"], published, stage)
    check_commit(rollback, winner, current_commit, expected_stage)
    check_commit(rollback, published, actor, lost_stage)
    return {"two_clone_cas": True, "pinned_reader": True, "between_check_lease": True,
            "lost_ack_checked_no_retry": True, "source_mutation_refused": True,
            "rollback_fast_forward": True, "real_validator": True}


def main():
    assert __debug__
    cases = json.loads((TOOLS / 'graphify-maintenance-cases.json').read_text(encoding='utf-8'))['cases']
    retained = os.environ.get('CONTEXT_MAINTENANCE_EVIDENCE')
    if retained:
        destination = Path(retained).resolve()
        assert not destination.is_relative_to(TOOLS) and not TOOLS.is_relative_to(destination)
        destination.mkdir()  # Never overwrite prior evidence.
        workspace = contextlib.nullcontext(str(destination))
    else:
        workspace = tempfile.TemporaryDirectory(prefix='context-maintenance-proof-')
    with workspace as tmp:
        base = Path(tmp)
        results = {}
        for name, case in cases.items():
            root = base / (name + '-repo')
            init_repo(root, case['files'])
            stage, checked, plan, paths = build(root, case, base / (name + '-build'))
            graph = checked['graph']
            ids = {n['id'] for n in graph['nodes']}
            if name in ('isolated-zero', 'deletion', 'exclusion', 'rename'):
                assert 'docs_note_shift_checklist' not in ids
            if name == 'edge-only':
                assert 'docs_policy_grant_window' not in ids
            for p in stage.iterdir():
                assert b'fixture-only-never-publish' not in p.read_bytes()
            func = {}
            exec(compile((root / 'src/guard.py').read_text(), str(root / 'src/guard.py'), 'exec'), func)
            accepts = func['accepts']
            limit = 48 if name in ('mixed-edit','branch-48-zero') else 24
            assert accepts(0, limit, False) and not accepts(0, limit + 1, False)
            assert not accepts(1, 0, False) and not accepts(0, 0, True)
            if name == 'mixed-edit':
                assert any('48' in str(n) for n in graph['nodes'] if n.get('_origin') == 'semantic')
            results[name] = (root, checked, stage, plan, paths)
        assessments = assess_cases(cases, results)
        controls = check_order_and_labels(base, results)
        seed, baseline, stage, _, _ = results['baseline']
        expected = gt(seed, 'rev-parse', 'HEAD')
        remote = base / 'remote.git'
        subprocess.run(['git', 'init', '--bare', '-q', str(remote)], env=clean_env(), check=True)
        git(seed, 'push', '-q', str(remote), 'HEAD:refs/heads/main')
        git(remote, 'symbolic-ref', 'HEAD', 'refs/heads/main')
        source = clone(remote, base / 'publish-clone')
        index = (source / '.git/index').read_bytes()
        original = {k:v for k,v in d.snapshot(source).items() if not k.startswith('.git/')}
        first = json.loads(publish(source, stage, remote).stdout)
        commit = first['commit']
        assert first['status'] == 'published' and first['parent'] == expected
        assert gt(source, 'ls-remote', '--refs', str(remote), 'refs/heads/main').split()[0] == commit
        assert gt(source, 'rev-parse', commit + '^') == expected
        for name in NAMES:
            assert git(source, 'show', f'{commit}:{TARGET}/{name}') == (stage / name).read_bytes()
        assert set(gt(source, 'ls-tree', '--name-only', commit + ':' + TARGET).splitlines()) == set(NAMES)
        assert (source / '.git/index').read_bytes() == index and {k:v for k,v in d.snapshot(source).items() if not k.startswith('.git/')} == original
        publish(source, stage, remote, success=False, reason='Remote moved')
        current = clone(remote, base / 'current-clone')
        assert json.loads(publish(current, stage, remote).stdout)['status'] == 'unchanged'
        # No-op must recheck current sources and exact trio buffers too.
        no_op_race = clone(remote, base / 'no-op-race')
        race_source = no_op_race / next(iter(baseline['snapshot']['sources']))
        hook = f'''import subprocess
from pathlib import Path
_real_run = subprocess.run
def _intercept(*args, **kwargs):
    result = _real_run(*args, **kwargs)
    argv = args[0]
    if isinstance(argv, (list, tuple)) and "write-tree" in argv and result.returncode == 0:
        with Path({str(race_source)!r}).open("ab") as stream:
            stream.write(b"\\n# isolated no-op mutation\\n")
    return result
subprocess.run = _intercept
'''
        publish(no_op_race, stage, remote, before=hook, success=False)
        assert gt(current, 'ls-remote', '--refs', str(remote), 'refs/heads/main').split()[0] == commit
        publish(current, stage, seed, success=False, reason='Local destination must be bare')
        (current / 'dirty.txt').write_text('dirty')
        publish(current, stage, remote, success=False, reason='Task clone is not clean')
        (current / 'dirty.txt').unlink()
        for defect in ('corrupt', 'truncated', 'incomplete'):
            broken = base / ('bad-' + defect)
            shutil.copytree(stage, broken)
            if defect == 'corrupt': (broken / 'graph.html').write_text('corrupt')
            elif defect == 'truncated': (broken / 'graph.json').write_text('{')
            else: (broken / 'GRAPH_REPORT.md').unlink()
            publish(current, broken, remote, success=False)
            assert gt(current, 'ls-remote', '--refs', str(remote), 'refs/heads/main').split()[0] == commit
        cold = clone(remote, base / 'moved-cold-root')
        assert not (cold / '.env').exists()
        oldview = base / 'cold-view'
        materialize(cold, commit, oldview)
        portable = v.validate_trio(oldview, root=cold, require_current=True)
        state = portable['graph']['graph']['context']['maintenance']
        snap = v.snapshot(cold, state['snapshot']['exclusions'], state['snapshot']['authority_sources'],
                          previous_sources=state['snapshot']['sources'], scope=state['snapshot']['scope'])
        assert v.assess_reuse(state, snap, v.profile(TOOLS))['status'] == 'noop'
        # Change only the note; use old portable policy and reviewed dependencies.
        (cold / 'docs/note.md').write_text(cases['isolated-zero']['files']['docs/note.md'])
        git(cold, 'add', 'docs/note.md'); git(cold, 'commit', '-qm', 'Update note')
        changed_commit = gt(cold, 'rev-parse', 'HEAD')
        git(cold, 'push', '-q', str(remote), 'HEAD:refs/heads/main')
        snap = v.snapshot(cold, state['snapshot']['exclusions'], state['snapshot']['authority_sources'],
                          previous_sources=state['snapshot']['sources'], scope=state['snapshot']['scope'])
        assessment = v.assess_reuse(state, snap, v.profile(TOOLS))
        assert assessment['status'] == 'reuse_some' and set(assessment['reusable']) == {'grant'}
        retained = copy.deepcopy(assessment['reusable']['grant']['payload'])
        retained['reuse_provenance'] = {'source_commit':commit, 'input_identity':portable['input_identity'],
                                       'generation_identity':portable['generation_identity'],
                                       'origin_sha256':state['groups']['grant']['origin_sha256'],
                                       'payload_sha256':state['groups']['grant']['payload_sha256']}
        note = next(f for f in cases['isolated-zero']['fragments'] if f['shard_id'] == 'note')
        portable_case = dict(cases['isolated-zero'], scope=snap['scope'], exclusions=snap['exclusions'],
                             authority_sources=snap['authority_sources'])
        reviews = {sid:g['dependency_review'] for sid,g in assessment['reusable'].items() if g['dependency_review']}
        # New zero-findings work must not inherit an old local-positive review.
        assignments = {sid:[r['source_file'] for r in g['payload']['receipts']] for sid,g in state['groups'].items()}
        fresh, reviewed, _, _ = build(cold, portable_case, base / 'cold-build', assignments_override=assignments,
                                       dependency_reviews_override=reviews, fragments_override=[retained,note])
        assert 'docs_note_shift_checklist' not in {n['id'] for n in reviewed['graph']['nodes']}
        second = json.loads(publish(cold, fresh, remote, expected=changed_commit).stdout)
        assert second['status'] == 'published' and second['parent'] == changed_commit
        api = {name:globals()[name] for name in ('git','gt','publish','clone','materialize','annotate','v','d','clean_env','PUBLISH','TARGET','NAMES')}
        more = run_more(base, remote, second['commit'], fresh, api)
        isolation = check_worktrees_and_export(base, remote, fresh, cases, results["baseline"])
        assert not d.ATTEMPTS
        print(json.dumps({'status':'PASS','recorded_model_replay_only':True,'cases':assessments,
                          'publication':True,'no_op_mutation_refused':True,'cold_changed_only_reuse':True,'race':more,'controls':controls,'isolation':isolation,
                          'network_or_provider_attempts':len(d.ATTEMPTS)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
