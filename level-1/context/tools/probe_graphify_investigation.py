"""Exercise G native investigation/views with recorded F inputs, not new inference.

Builds fresh baseline/versioned mixed fixtures using the accepted maintenance
probe, publishes only to local bare fixtures, and leaves shared artifacts alone.
Optional SVG rendering is a separate environment/browser check.
"""
from __future__ import annotations
import contextlib
import copy
import hashlib
import importlib.metadata
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import sys
import tempfile
import textwrap
import unittest

TOOLS = Path(__file__).resolve().parent
ATTEMPTS = []
attempts = ATTEMPTS

def forbidden(*args, **kwargs):
    ATTEMPTS.append('network/backend')
    raise RuntimeError('network/backend forbidden')

def module(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

def block(name):
    match=re.search(r'```python\n(# context-'+name+r'\n.*?)\n```',(TOOLS/'graphify.md').read_text(),re.S)
    assert match,name
    return match.group(1)

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')

def graph_data(g):
    return nx.node_link_data(g, edges='links')

def mixed():
    raw=json.loads(SOURCE.read_text())
    g=load_node_link_graph(raw)
    cs={}
    labels={}
    for n,d in g.nodes(data=True):
        cs.setdefault(d['community'],[]).append(n)
        labels[d['community']]=d['community_name']
    return g,cs,labels

def collision_graph(reverse=False):
    g=nx.MultiDiGraph()
    for n in ('same','second'):
        g.add_node(n,label=n,source_file='same.py',file_type='code',community=0,_origin='ast')
    g.add_node('ext::typing',label='typing',external=True,file_type='code')
    g.add_edge('same','second',key='a',relation='calls',confidence='EXTRACTED',source_file='same.py',_src='same',_tgt='second')
    g.add_edge('same','second',key='b',relation='documents',confidence='INFERRED',source_file='same.py',_src='same',_tgt='second')
    g.add_edge('second','same',key='back',relation='returns',confidence='AMBIGUOUS',source_file='same.py',_src='second',_tgt='same')
    g.add_edge('same','ext::typing',key='ext',relation='imports',confidence='EXTRACTED',source_file='same.py')
    g.graph['hyperedges']=[{'id':'same-hyperedge','nodes':['same','second','ext::typing'],'relation':'bundle','source_file':'same.py'}]
    g.graph['context']={'input_identity':'second' if reverse else 'first','source_commit':('b' if reverse else 'a')*40,'graphify_revision':'16218bfc80d4ca2799734d045039f7ed1a5fa9fb'}
    return g

class ExportTests(unittest.TestCase):
    def test_01_identity(self):
        d=importlib.metadata.distribution('graphifyy')
        direct=json.loads(d.read_text('direct_url.json'))
        self.assertEqual(d.version,'0.9.103')
        self.assertEqual(direct['vcs_info']['commit_id'],'16218bfc80d4ca2799734d045039f7ed1a5fa9fb')
        self.assertIn('Graphify-Labs/graphify',direct['url'])
    def test_02_mixed_graphml(self):
        g,cs,_=mixed(); target=OUT/'mixed.graphml'
        before=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        to_graphml(g,cs,str(target)); r=nx.read_graphml(target)
        self.assertTrue(r.is_directed()); self.assertEqual(set(r),set(g))
        self.assertEqual(r.number_of_edges(),g.number_of_edges())
        for n,d in g.nodes(data=True):
            self.assertEqual(r.nodes[n]['label'],d['label'])
            self.assertEqual(r.nodes[n]['source_file'],d['source_file'])
            self.assertNotIn('_origin',r.nodes[n])
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(),before)
        self.assertIsInstance(r.graph['context'],str)
        self.assertEqual(json.loads(r.graph['context'])['input_identity'],g.graph['context']['input_identity'])
    def test_03_multigraph_graphml_types(self):
        g=collision_graph(); g.nodes['same'].update(metadata={'why':['one',2]},optional=None,score=0.75,active=True,label='Same\x00')
        to_graphml(g,{0:list(g)},str(OUT/'parallel.graphml'))
        r=nx.read_graphml(OUT/'parallel.graphml')
        self.assertTrue(r.is_directed()); self.assertTrue(r.is_multigraph()); self.assertEqual(r.number_of_edges(),4)
        self.assertEqual({d['relation'] for d in r['same']['second'].values()},{'calls','documents'})
        self.assertEqual(r['second']['same']['back']['relation'],'returns')
        self.assertEqual(json.loads(r.nodes['same']['metadata']),{'why':['one',2]})
        self.assertEqual(r.nodes['same']['label'],'Same')
        self.assertEqual(r.nodes['same']['score'],0.75); self.assertIs(r.nodes['same']['active'],True)
        self.assertEqual(r.nodes['same']['optional'],'') # None and empty string become indistinguishable
        self.assertEqual(json.loads(r.graph['hyperedges']),g.graph['hyperedges'])
        self.assertNotIn('_src',r['same']['second']['a'])
        self.assertEqual(g.nodes['same']['label'],'Same\x00') # exporter works on copy
    def test_04_undirected_direction_loss(self):
        g=nx.Graph(); g.add_nodes_from(['a','b']); g.add_edge('a','b',relation='calls',_src='b',_tgt='a')
        to_graphml(g,{0:list(g)},str(OUT/'undirected.graphml'))
        r=nx.read_graphml(OUT/'undirected.graphml')
        self.assertFalse(r.is_directed()); self.assertNotIn('_src',r['a']['b']); self.assertNotIn('_tgt',r['a']['b'])
    def test_05_obsidian_mixed_and_ownership(self):
        g,cs,labels=mixed(); vault=OUT/'obsidian'; vault.mkdir(exist_ok=True)
        (vault/'handwritten.md').write_text('LOCAL KEEP',encoding='utf-8')
        (vault/'.obsidian').mkdir(exist_ok=True)
        (vault/'.obsidian/graph.json').write_text('{"local":true}',encoding='utf-8')
        warnings=io.StringIO()
        with contextlib.redirect_stderr(warnings): n=to_obsidian(g,cs,str(vault),community_labels=labels)
        self.assertEqual(n,len(g)+len(cs)); self.assertEqual((vault/'handwritten.md').read_text(),'LOCAL KEEP')
        self.assertEqual(json.loads((vault/'.obsidian/graph.json').read_text()),{'local':True})
        manifest=json.loads((vault/'.graphify_obsidian_manifest.json').read_text())['files']
        notes=[x for x in manifest if x.endswith('.md') and not x.startswith('_COMMUNITY_')]
        self.assertEqual(len(notes),len(g))
        sem=[n for n,d in g.nodes(data=True) if d.get('_origin')=='semantic']
        self.assertTrue(sem)
        self.assertTrue(any(g.nodes[sem[0]]['label'] in (vault/n).read_text() for n in notes))
        edited=vault/notes[0]; edited.write_text(edited.read_text()+'\nLOCAL EDIT TO GENERATED\n')
        with contextlib.redirect_stderr(io.StringIO()): to_obsidian(g,cs,str(vault),community_labels=labels)
        self.assertNotIn('LOCAL EDIT TO GENERATED',edited.read_text())
        stale=vault/'owned-stale.md'; stale.write_text('OLD',encoding='utf-8')
        dump(vault/'.graphify_obsidian_manifest.json',{'files':manifest+['owned-stale.md']})
        with contextlib.redirect_stderr(io.StringIO()): to_obsidian(g,cs,str(vault),community_labels=labels)
        self.assertFalse(stale.exists()); self.assertTrue((vault/'handwritten.md').exists())
    def test_06_wiki_mixed_and_owned_directory(self):
        g,cs,labels=mixed(); wiki=OUT/'wiki'; wiki.mkdir(exist_ok=True)
        (wiki/'handwritten.md').write_text('EXPECTED DELETED',encoding='utf-8')
        n=to_wiki(g,cs,wiki,community_labels=labels,god_nodes_data=[{'id':next(iter(g)),'label':g.nodes[next(iter(g))]['label'],'degree':g.degree(next(iter(g)))}])
        self.assertEqual(n,len(cs)+1); self.assertTrue((wiki/'index.md').exists()); self.assertFalse((wiki/'handwritten.md').exists())
        articles='\n'.join(p.read_text() for p in wiki.glob('*.md'))
        self.assertIn('docs/policy.md',articles); self.assertIn('Current 24-hour original-issue grant',articles); self.assertIn('INFERRED',articles)
    def test_07_native_prefix_exact_composition(self):
        a=collision_graph(); b=collision_graph(True)
        pa=prefix_graph_for_global(a,'service-a',0); pb=prefix_graph_for_global(b,'service-b',1)
        self.assertEqual(a.graph['hyperedges'][0]['nodes'][0],'same')
        self.assertEqual(pa.nodes['service-a::same']['local_id'],'same'); self.assertEqual(pb.nodes['service-b::same']['community'],1)
        self.assertNotIn('repo',pa.nodes['ext::typing'])
        merged=nx.compose(pa,pb)
        merged.graph.clear() # inherited last-input context would falsely identify the whole view
        attach_hyperedges(merged,pa.graph['hyperedges']+pb.graph['hyperedges'])
        merged.graph['cross_repository_view']={'schema':'context-cross-repository-view-v1','inputs':[
            {'repo':'service-a','source_commit':a.graph['context']['source_commit'],'graph_sha256':'a'*64},
            {'repo':'service-b','source_commit':b.graph['context']['source_commit'],'graph_sha256':'b'*64}],
            'limits':['synthetic API test; no inferred cross-repository links']}
        self.assertEqual(len(merged),5); self.assertEqual(merged.number_of_edges(),8); self.assertTrue(merged.is_directed()); self.assertTrue(merged.is_multigraph())
        self.assertFalse(merged.has_edge('service-a::same','service-b::same'))
        self.assertEqual(len(merged.graph['hyperedges']),2)
        self.assertEqual({h['id'] for h in merged.graph['hyperedges']},{'service-a::same-hyperedge','service-b::same-hyperedge'})
        self.assertTrue(all(n in merged for h in merged.graph['hyperedges'] for n in h['nodes']))
        self.assertEqual(merged['service-b::second']['service-b::same']['back']['_src'],'service-b::second')
        dump(OUT/'cross-repository-view.json',graph_data(merged))
        r=load_node_link_graph(OUT/'cross-repository-view.json')
        self.assertTrue(r.is_directed()); self.assertTrue(r.is_multigraph()); self.assertEqual(r.number_of_edges(),8)
        tags=distinct_repo_tags([Path('/left/repo/graphify-out/graph.json'),Path('/right/repo/graphify-out/graph.json')])
        self.assertEqual(len(set(tags)),2); self.assertNotEqual(tags,['repo','repo'])
        # Arbitrary context references/attribute dictionaries are not recursively namespaced.
        self.assertEqual(pa.nodes['service-a::same']['source_file'],'same.py')
    def test_08_native_cli_loss_control(self):
        paths=[]
        for parent,reverse in [('left',False),('right',True)]:
            p=OUT/parent/'repo/graphify-out/graph.json'; dump(p,graph_data(collision_graph(reverse))); paths.append(p)
        runner="""import socket,sys,json,pathlib
attempt=[]
def fail(*a,**k):
 attempt.append('network/backend'); raise RuntimeError('forbidden')
socket.socket.connect=fail; socket.create_connection=fail
import graphify.extract as e
e.extract_semantic=fail
from graphify.__main__ import main
sys.argv=['graphify']+sys.argv[1:]
try: main()
finally:
 pathlib.Path(sys.argv[-1]+'.attempts.json').write_text(json.dumps(attempt))
"""
        target=OUT/'lossy-native-cli.json'
        env={k:v for k,v in os.environ.items() if not any(w in k.upper() for w in ('API_KEY','TOKEN','SECRET','PASSWORD','PROVIDER'))}
        env.update(GRAPHIFY_OUT=str(OUT/'native-out'),GRAPHIFY_BACKEND='none',PYTHONDONTWRITEBYTECODE='1')
        p=subprocess.run([sys.executable,'-B','-c',runner,'merge-graphs',*(str(x) for x in paths),'--out',str(target)],env=env,cwd=OUT,capture_output=True,text=True,timeout=30)
        self.assertEqual(p.returncode,0,p.stderr); self.assertEqual(json.loads(Path(str(target)+'.attempts.json').read_text()),[])
        raw=json.loads(target.read_text()); self.assertFalse(raw['directed']); self.assertFalse(raw['multigraph'])
        self.assertEqual(len(raw['nodes']),5); self.assertEqual(len(raw['links']),4) # 8 arcs -> 4 unordered pairs
        self.assertEqual(len(raw['hyperedges']),2)
        (OUT/'native-cli.log').write_text(p.stdout+p.stderr,encoding='utf-8')
    def test_09_svg_optional_dependency_gate(self):
        if importlib.util.find_spec('matplotlib') is None:
            with self.assertRaisesRegex(ImportError,'matplotlib not installed'):
                to_svg(nx.Graph([('a','b')]),{0:['a','b']},str(OUT/'unavailable.svg'))
            self.assertFalse((OUT/'unavailable.svg').exists())
        else:
            self.skipTest('Base-only missing dependency control; optional plotting is separate')
    def test_10_actual_versioned_input_view(self):
        paths=[SOURCE,SOURCE.parents[2]/'branch-build/mixed/graph.json']
        merged=nx.MultiDiGraph(); inputs=[]; hes=[]
        for index,(tag,path) in enumerate(zip(('baseline','branch'),paths)):
            raw=json.loads(path.read_text()); g=load_node_link_graph(raw)
            self.assertTrue(g.is_directed())
            h=prefix_graph_for_global(nx.MultiDiGraph(g),tag,community_offset=100*index)
            merged=nx.compose(merged,h); hes.extend(h.graph.get('hyperedges',[]))
            c=raw['graph']['context']
            inputs.append({'repo':tag,'source_commit':c['source_commit'],
                           'input_identity':c['input_identity'],'generation_identity':c['generation_identity'],
                           'graph_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                           'graphify_revision':c['graphify_revision']})
        merged.graph.clear(); attach_hyperedges(merged,hes)
        merged.graph['cross_repository_view']={'schema':'context-cross-repository-view-v1','inputs':inputs,
           'limits':['two recorded F versions used as independent namespace controls; no fresh model inference']}
        self.assertNotEqual(inputs[0]['graph_sha256'],inputs[1]['graph_sha256'])
        self.assertEqual(len(merged),sum(len(json.loads(p.read_text())['nodes']) for p in paths))
        self.assertFalse(merged.has_edge('baseline::src_guard_accepts','branch::src_guard_accepts'))
        dump(OUT/'actual-versioned-view.json',graph_data(merged))
        to_graphml(merged,{d['community']:[n for n,a in merged.nodes(data=True) if a['community']==d['community']] for _,d in merged.nodes(data=True)},str(OUT/'actual-versioned-view.graphml'))
        r=nx.read_graphml(OUT/'actual-versioned-view.graphml')
        self.assertTrue(r.is_directed()); self.assertEqual(r.number_of_edges(),merged.number_of_edges())
    def test_11_obsidian_collision_is_partial(self):
        g=nx.DiGraph(); g.add_node('a',label='same',source_file='a.md'); g.add_node('b',label='other',source_file='b.md')
        g.add_edge('a','b',relation='depends_on',confidence='INFERRED')
        out=OUT/'obsidian-foreign-collision'; out.mkdir(exist_ok=True)
        (out/'same.md').write_text('LOCAL COLLISION')
        errors=io.StringIO()
        with contextlib.redirect_stderr(errors): count=to_obsidian(g,{0:list(g)},str(out),community_labels={0:'Test'})
        self.assertEqual((out/'same.md').read_text(),'LOCAL COLLISION'); self.assertEqual(count,2)
        self.assertIn('skipped 1 pre-existing',errors.getvalue())
    def test_12_obsidian_frontmatter_adoption(self):
        g=nx.Graph(); g.add_node('a',label='current')
        out=OUT/'obsidian-adoption'; out.mkdir(exist_ok=True)
        (out/'.graphify_obsidian_manifest.json').unlink(missing_ok=True)
        tagged=out/'local-but-graphify-tagged.md'
        tagged.write_text('---\ntags:\n  - graphify/document\n---\nLOCAL\n')
        with contextlib.redirect_stderr(io.StringIO()): to_obsidian(g,{0:['a']},str(out))
        self.assertFalse(tagged.exists()) # tag heuristic adopted and pruned an otherwise local note
    @classmethod
    def tearDownClass(cls):
        assert not ATTEMPTS,ATTEMPTS


def check_investigation(root, stage):
    from graphify.serve import _query_graph_text, _shortest_path_text, _resolve_single_node, _neighbor_lines, _cut_lines_to_budget
    from graphify.affected import affected_nodes, resolve_seed_outcome
    from graphify.analyze import god_nodes, surprising_connections
    ROOT, STAGE = root, stage
    # Explicit selected evidence and stage: no secret file content or Git internals.
    watched = [ROOT/'src/guard.py', ROOT/'docs/policy.md', ROOT/'docs/note.md'] + sorted(STAGE.iterdir())
    def snap():
        return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in watched}
    before = snap()
    stage_names = sorted(p.name for p in STAGE.iterdir())
    module_spec = importlib.util.spec_from_file_location('context_validator', TOOLS/'validate_context_fragments.py')
    validator = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(validator)
    trio = validator.validate_trio(STAGE, root=ROOT, require_current=True)
    G = load_node_link_graph(trio['graph'])
    assert G.is_directed()
    seed, err = _resolve_single_node(G, 'src_guard_accepts')
    assert not err and seed == 'src_guard_accepts'
    node = G.nodes[seed]
    assert node['source_file'] == 'src/guard.py' and node['source_location'] == 'L1'
    assert '0 <= now - issued <= 24' in (ROOT/'src/guard.py').read_text()
    assert '24 elapsed hours from original issuance' in (ROOT/'docs/policy.md').read_text()
    assert 'does not extend the grant window' in (ROOT/'docs/note.md').read_text()

    queries = {}
    for mode in ('bfs', 'dfs'):
        out = _query_graph_text(G, 'archive grant', mode=mode, seeds=[seed], seed_root=ROOT, depth=2, token_budget=1200)
        assert 'implements_current_grant_window' in out and 'INFERRED' in out and 'src/guard.py' in out, out
        queries[mode] = out
    path = _shortest_path_text(G, {'source': seed, 'target': 'docs_policy_grant_window', 'max_hops': 8})
    assert 'implements_current_grant_window' in path and 'INFERRED' in path, path
    reverse = _shortest_path_text(G, {'source': 'docs_policy_grant_window', 'target': seed, 'max_hops': 8})
    assert 'No directed path' in reverse, reverse
    neighbors = _neighbor_lines(G, seed)
    assert any('implements_current_grant_window' in line and 'src/guard.py:L1-L2' in line for line in neighbors), neighbors
    communities = {}
    for nid, data in G.nodes(data=True):
        cid = data.get('community')
        if cid is not None: communities.setdefault(cid, []).append(nid)
    assert set().union(*map(set, communities.values())) == set(G)
    components = sorted(sorted(group) for group in nx.weakly_connected_components(G))
    isolates = list(nx.isolates(G))
    assert sorted(map(len, components)) == [2,2,4] and not isolates
    isolated_control=G.copy();isolated_control.add_node('synthetic_isolate',label='Synthetic isolated source')
    assert list(nx.isolates(isolated_control))==['synthetic_isolate']
    hubs = god_nodes(G, top_n=5)
    bridges = surprising_connections(G, communities, top_n=5)
    # Native default relations exclude the custom semantic relation: no affected hit.
    default_hits = affected_nodes(G, 'docs_policy_grant_window', depth=2)
    assert not default_hits, default_hits
    custom_hits = affected_nodes(G, 'docs_policy_grant_window', relations=('implements_current_grant_window',), depth=1)
    assert any(h.node_id == seed and h.via_file == 'src/guard.py' and h.via_location == 'L1-L2' for h in custom_hits), custom_hits

    # Synthetic duplicate identity and budget negative controls, not the F graph.
    S = nx.DiGraph()
    S.add_node('a', label='duplicate()', source_file='one.py', source_location='L1')
    S.add_node('b', label='duplicate()', source_file='two.py', source_location='L2')
    nid, refusal = _resolve_single_node(S, 'duplicate()')
    assert nid is None and refusal and ('ambiguous' in refusal.lower() or 'multiple' in refusal.lower()), refusal
    nid2, rivals = resolve_seed_outcome(S, 'duplicate()')
    assert nid2 is None and rivals, (nid2, rivals)
    # Directed path permits an implied reverse contains hop; output must show it.
    C = nx.DiGraph()
    C.add_node('file', label='file.py', source_file='file.py')
    C.add_node('symbol', label='symbol()', source_file='file.py')
    C.add_edge('file', 'symbol', relation='contains', confidence='EXTRACTED')
    contains_path = _shortest_path_text(C, {'source': 'symbol', 'target': 'file', 'max_hops': 8})
    assert '<--contains' in contains_path, contains_path
    # A graph claim that conflicts with a known policy is not canonical truth.
    conflicting_graph_claim = '48 elapsed hours'
    conflict = nx.DiGraph()
    conflict.add_node('stale', label=conflicting_graph_claim, source_file='docs/note.md', source_location='L1')
    conflict_view = _query_graph_text(conflict, 'grant', seeds=['stale'], depth=1, token_budget=100)
    assert conflicting_graph_claim in conflict_view and conflicting_graph_claim not in (ROOT/'docs/policy.md').read_text()
    missing = _resolve_single_node(S, 'not-present')[1]
    assert missing and 'No node matching' in missing
    T = nx.DiGraph()
    for i in range(90):
        T.add_node(str(i), label='node_' + str(i) + '_' + 'x'*35, source_file='f.py', source_location='L1')
        if i: T.add_edge('0',str(i), relation='calls', confidence='EXTRACTED')
    out = _query_graph_text(T, 'node', seeds=['0'], depth=1, token_budget=20)
    assert 'TRUNCATED' in out or 'over budget' in out, out
    assert 'TRUNCATED' in _cut_lines_to_budget(['x'*100 for _ in range(10)], 20, 'narrow')
    assert before == snap() and stage_names == sorted(p.name for p in STAGE.iterdir())
    assert not attempts
    return {'status':'PASS','input_identity':trio['input_identity'],'generation_identity':trio['generation_identity'],
            'nodes':len(G),'edges':G.number_of_edges(),'bfs':queries['bfs'],'dfs':queries['dfs'],
            'path':path,'reverse_path':reverse,'neighbors':neighbors,'communities':communities,
            'hubs':hubs,'bridges':bridges,'weak_components':components,'isolates':isolates,'custom_affected':[h.node_id for h in custom_hits],
            'source_bytes_unchanged':True,'synthetic_ambiguity_budget_contains_conflict':True}


def check_guide_cross(checked_inputs, expected_edges):
    namespace={'checked_inputs':checked_inputs}
    exec(compile(block('cross-repository-view'),'documented-cross-view','exec'),namespace)
    result=namespace['merged']
    assert result.is_directed() and result.is_multigraph() and result.number_of_edges()==expected_edges
    assert len(result.graph['cross_repository_view']['inputs'])==len(checked_inputs)
    assert 'context' not in result.graph
    assert all(item['artifact_commit'] for item in result.graph['cross_repository_view']['inputs'])
    return result

def check_cross_guards():
    def checked(g):
        return {'graph':graph_data(g),'input_identity':'synthetic','generation_identity':'synthetic',
                'digests':{'graph.json':'a'*64}}
    # Exact native composition refuses conflicting shared external attributes.
    a=collision_graph();b=collision_graph(True)
    b.nodes['ext::typing']['label']='different identity'
    try: check_guide_cross([('a','a'*40,checked(a)),('b','b'*40,checked(b))],8)
    except AssertionError as error: assert 'Conflicting external identity' in str(error)
    else: raise AssertionError('External identity conflict accepted')
    # Both endpoints shared: same native edge key would otherwise be overwritten.
    a=collision_graph();b=collision_graph(True)
    for g in (a,b):
        g.add_node('ext::other',label='other',external=True,file_type='code')
        g.add_edge('ext::typing','ext::other',key='same',relation='imports')
    try: check_guide_cross([('a','a'*40,checked(a)),('b','b'*40,checked(b))],10)
    except AssertionError as error: assert 'External-only arcs' in str(error)
    else: raise AssertionError('Shared external edge overwritten')
    # A local prefix must not merge into an external ID already in that input.
    a=collision_graph();a.add_node('a::same',label='external collision',external=True)
    try: check_guide_cross([('a','a'*40,checked(a)),('b','b'*40,checked(collision_graph(True)))],8)
    except AssertionError as error: assert 'prefix/external ID collision' in str(error)
    else: raise AssertionError('Local/external node collision accepted')
    # Distinct external-only edge keys also refuse rather than losing owner provenance.
    a=collision_graph();b=collision_graph(True)
    for index,g in enumerate((a,b)):
        g.add_node('ext::other',label='other',external=True,file_type='code')
        g.add_edge('ext::typing','ext::other',key=str(index),relation='imports')
    try: check_guide_cross([('a','a'*40,checked(a)),('b','b'*40,checked(b))],10)
    except AssertionError as error: assert 'External-only arcs' in str(error)
    else: raise AssertionError('External-only ownerless arc accepted')
    return {'external_identity_conflict_refused':True,'external_only_same_and_distinct_keys_refused':True,'prefix_collision_refused':True}

def check_presentation(stage):
    from graphify.exporters.html import to_html
    output=BASE/'presentation';output.mkdir()
    g=load_node_link_graph(json.loads((stage/'graph.json').read_text()))
    cs={}
    for n,d in g.nodes(data=True):cs.setdefault(d['community'],[]).append(n)
    labels={int(c):d['label'] for c,d in g.graph['context']['community_interpretation'].items()}
    assert to_html(g,cs,str(output/'aggregated.html'),community_labels=labels,node_limit=3,learning_overlay={})
    def embedded(path,name):
        return json.JSONDecoder().raw_decode(path.read_text().split('const '+name+' = ',1)[1])[0]
    assert len(embedded(output/'aggregated.html','RAW_NODES'))==3
    s=nx.DiGraph()
    for i in range(6):s.add_node(str(i),label='synthetic-'+str(i),source_file='synthetic.py')
    s.add_edge('0','3',relation='calls',confidence='EXTRACTED');s.add_edge('3','0',relation='returns',confidence='EXTRACTED')
    split={0:['0','1','2'],1:['3','4','5']}
    assert to_html(s,split,str(output/'opposing-summary.html'),community_labels={0:'A',1:'B'},node_limit=3,learning_overlay={})
    rows=embedded(output/'opposing-summary.html','RAW_EDGES')
    assert len(rows)==1 and rows[0]['confidence']=='AGGREGATED' and rows[0]['label']=='2 cross-community edges'
    assert not to_html(s,{0:list(s)},str(output/'skipped.html'),community_labels={0:'One'},node_limit=3,learning_overlay={})
    assert not (output/'skipped.html').exists()
    # Default limit refusal is executed at a small environment-selected cap.
    old=os.environ.get('GRAPHIFY_VIZ_NODE_LIMIT');os.environ['GRAPHIFY_VIZ_NODE_LIMIT']='3'
    try:
        try:to_html(s,split,str(output/'cap-refusal.html'),learning_overlay={})
        except ValueError as error: assert 'too large' in str(error)
        else:raise AssertionError('Default visualization cap ignored')
    finally:
        if old is None:os.environ.pop('GRAPHIFY_VIZ_NODE_LIMIT',None)
        else:os.environ['GRAPHIFY_VIZ_NODE_LIMIT']=old
    return {'aggregation_controls':True,'single_community_refuses_trio':True,'default_cap_refuses':True,'large_corpus_performance_tested':False}

def main():
    global OUT,SOURCE,BASE,nx,to_graphml,to_obsidian,to_svg,attach_hyperedges,to_wiki,prefix_graph_for_global,distinct_repo_tags,load_node_link_graph
    assert __debug__
    retained=os.environ.get('CONTEXT_INVESTIGATION_EVIDENCE')
    if retained:
        destination=Path(retained).resolve()
        assert not destination.is_relative_to(TOOLS) and not TOOLS.is_relative_to(destination)
        destination.mkdir()
        workspace=contextlib.nullcontext(str(destination))
    else:workspace=tempfile.TemporaryDirectory(prefix='context-investigation-')
    with workspace as temporary:
        BASE=Path(temporary);OUT=BASE/'exports';OUT.mkdir()
        os.environ.update(GRAPHIFY_OUT=str(BASE/'native-cache'),GRAPHIFY_BACKEND='none',GRAPHIFY_QUERY_LOG_DISABLE='1',PYTHONDONTWRITEBYTECODE='1')
        socket.socket.connect=socket.create_connection=forbidden
        import networkx as nx
        from graphify import llm
        llm._call_llm=llm.extract_corpus_parallel=forbidden
        from graphify.build import prefix_graph_for_global,distinct_repo_tags
        from graphify.export import to_graphml,to_obsidian,to_svg,attach_hyperedges
        from graphify.paths import load_node_link_graph
        from graphify.wiki import to_wiki
        f=module('context_maintenance_probe',TOOLS/'probe_graphify_maintenance.py')
        cases=json.loads((TOOLS/'graphify-maintenance-cases.json').read_text())['cases']
        checked_inputs=[];cross_records=[];built=[]
        for tag,name in [('baseline','baseline'),('branch','branch-48-zero')]:
            root=BASE/(tag+'-repo');f.init_repo(root,cases[name]['files'])
            stage,checked,_,_=f.build(root,cases[name],BASE/(tag+'-build'))
            remote=BASE/(tag+'.git')
            subprocess.run(['git','init','--bare','-q',str(remote)],env=f.clean_env(),check=True)
            f.git(root,'push','-q',str(remote),'HEAD:refs/heads/main')
            published=json.loads(f.publish(root,stage,remote).stdout)
            view=BASE/(tag+'-view');f.materialize(root,published['commit'],view)
            verified=f.v.validate_trio(view,root=root,require_current=True)
            checked_inputs.append((tag,published['commit'],verified));cross_records.append({'tag':tag,'repository':str(root),'artifact_commit':published['commit'],'checked':verified});built.append((root,stage))
        SOURCE=built[0][1]/'graph.json'
        query=check_investigation(*built[0])
        native_env=dict(f.env_for(built[0][0],built[0][1]),CONTEXT_TRIO=str(built[0][1]),CONTEXT_SEED='src_guard_accepts',CONTEXT_QUESTION='archive grant',CONTEXT_TARGET='docs_policy_grant_window')
        watched={str(p):p.read_bytes() for p in [*built[0][1].iterdir(),*(built[0][0]/name for name in cases['baseline']['files'])]}
        printed=f.d.execute(block('investigate'),native_env).stdout
        assert 'implements_current_grant_window' in printed and 'INFERRED' in printed
        assert watched=={p:Path(p).read_bytes() for p in watched}
        binding_before=[(f.gt(root,'rev-parse','HEAD'),(root/'.git/index').read_bytes(),f.d.snapshot(stage)) for root,stage in built]
        binding={'cross_records':cross_records,'validator':f.v}
        exec(compile(block('bind-cross-inputs'),'documented-input-binding','exec'),binding)
        assert binding['checked_inputs']==checked_inputs
        assert binding_before==[(f.gt(root,'rev-parse','HEAD'),(root/'.git/index').read_bytes(),f.d.snapshot(stage)) for root,stage in built]
        bad=copy.copy(cross_records[0]);bad['artifact_commit']=bad['checked']['graph']['graph']['context']['source_commit']
        try:exec(compile(block('bind-cross-inputs'),'swapped-commit-binding','exec'),{'cross_records':[bad],'validator':f.v})
        except (AssertionError,subprocess.CalledProcessError):pass
        else:raise AssertionError('Unrelated existing commit/view pair accepted')
        bad=copy.deepcopy(cross_records[0]);bad['checked']['graph']['graph']['context']['source_commit']=None
        try:exec(compile(block('bind-cross-inputs'),'missing-source-binding','exec'),{'cross_records':[bad],'validator':f.v})
        except AssertionError as error:assert 'version provenance' in str(error)
        else:raise AssertionError('Unversioned source accepted as pinned')
        # A real blob-filtered partial clone must fail without lazy object fetch.
        remote=BASE/'baseline.git'
        f.git(remote,'config','uploadpack.allowFilter','true')
        partial=BASE/'partial-input'
        subprocess.run(['git','clone','--quiet','--filter=blob:none','--no-checkout',remote.as_uri(),str(partial)],env=f.clean_env(),check=True,timeout=30)
        f.git(partial,'remote','set-url','origin',str(BASE/'missing-promisor-remote.git'))
        missing_before=f.d.snapshot(partial/'.git/objects')
        partial_record=dict(cross_records[0],repository=str(partial))
        try:exec(compile(block('bind-cross-inputs'),'no-lazy-binding','exec'),{'cross_records':[partial_record],'validator':f.v})
        except subprocess.CalledProcessError as error:
            assert 'fetch' not in error.stderr.decode().lower(), error.stderr
        else:raise AssertionError('Blob-filtered view unexpectedly had all objects')
        assert missing_before==f.d.snapshot(partial/'.git/objects')
        merged=check_guide_cross(checked_inputs,sum(len(c[2]['graph']['links']) for c in checked_inputs))
        dump(BASE/'cross-guide-view.json',graph_data(merged))
        reopened=load_node_link_graph(json.loads((BASE/'cross-guide-view.json').read_text()))
        assert dict(reopened.nodes(data=True))==dict(merged.nodes(data=True))
        assert {(u,v,k):d for u,v,k,d in reopened.edges(keys=True,data=True)}=={(u,v,k):d for u,v,k,d in merged.edges(keys=True,data=True)}
        assert reopened.graph==merged.graph
        guards=check_cross_guards()
        presentation=check_presentation(built[0][1])
        result=unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(ExportTests))
        assert result.wasSuccessful()
        assert not ATTEMPTS and not f.d.ATTEMPTS
        summary={'status':'PASS','recorded_model_replay_only':True,'investigation':query,'documented_read_block':True,'cross_guard_controls':guards,'real_artifact_source_binding_and_negatives':True,'partial_clone_no_lazy_fetch':True,'complete_cross_roundtrip':True,'cross_immutable_inputs':[x[1] for x in checked_inputs],'export_tests':result.testsRun,'presentation':presentation,'network_or_provider_attempts':0}
        dump(BASE/'results.json',summary)
        print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
