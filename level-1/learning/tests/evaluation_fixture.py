"""Fixed synthetic C fixture; no arbitrary runner, native host or acceptance gate."""

from hashlib import sha256
import json
from pathlib import Path
from tempfile import TemporaryDirectory


def merge_fixture(master, lookup, version):
    """Three fixed association variants sharing the required ID validation."""
    if version not in ("baseline", "regression", "correction"):
        raise ValueError("unknown fixture version")
    master_ids = [row[0] for row in master]
    lookup_ids = [row[0] for row in lookup]
    if len(set(master_ids)) != len(master_ids) or len(set(lookup_ids)) != len(lookup_ids):
        raise ValueError("duplicate IDs")
    if set(master_ids) != set(lookup_ids):
        raise ValueError("unequal ID sets")
    if version == "baseline":
        return [(key, quantity, label) for (key, quantity), (_, label) in zip(master, lookup)]
    quantities, labels = dict(master), dict(lookup)
    order = sorted(master_ids) if version == "regression" else master_ids
    return [(key, quantities[key], labels[key]) for key in order]


def withdraw_fixture_step(current, baseline_step, candidate_step):
    """Guarded inverse for this fixture's one exact step, not a general rollback tool."""
    if current.count(candidate_step) != 1:
        raise ValueError("candidate step changed; preserve current file and resolve overlap")
    return current.replace(candidate_step, baseline_step, 1)


def main():
    cases = [
        ("original", [("N", 3), ("S", 7)], [("S", "South"), ("N", "North")],
         [("N", 3, "North"), ("S", 7, "South")]),
        ("transfer", [("S", 7), ("E", 2), ("N", 3)],
         [("N", "North"), ("S", "South"), ("E", "East")],
         [("S", 7, "South"), ("E", 2, "East"), ("N", 3, "North")]),
        ("aligned-order", [("S", 7), ("N", 3)], [("S", "South"), ("N", "North")],
         [("S", 7, "South"), ("N", 3, "North")]),
        ("empty", [], [], []),
        ("duplicate-master", [("N", 3), ("N", 7)], [("N", "North")], "duplicate IDs"),
        ("duplicate-lookup", [("N", 3)], [("N", "North"), ("N", "Other")], "duplicate IDs"),
        ("unequal-sets", [("N", 3)], [("S", "South")], "unequal ID sets"),
    ]
    for name, master, lookup, expected in cases:
        before = json.dumps([master, lookup])
        results = {}
        for version in ("baseline", "regression", "correction"):
            try:
                actual = merge_fixture(master, lookup, version)
            except ValueError as error:
                actual = str(error)
            supported = actual == expected
            results[version] = {"check": "supported" if supported else "FAILED", "output": actual}
            known_failure = (version == "baseline" and name in ("original", "transfer")) or (
                version == "regression" and name in ("transfer", "aligned-order"))
            assert supported != known_failure, (name, version, actual, expected)
            assert json.dumps([master, lookup]) == before
        print(json.dumps({"case": name, "results": results}, sort_keys=True))

    baseline_step = "Associate records by position.\n"
    candidate_step = "Associate by ID and sort master IDs.\n"
    base = "# Fixture merge\n\n" + baseline_step + "\nOutput encoding: UTF-8.\n"
    unrelated = "\nContributor note: retain original quantity units.\n"
    with TemporaryDirectory(prefix="learning-c-") as directory:
        path = Path(directory) / "operation.md"
        path.write_text(base, encoding="utf-8")
        path.write_text(base.replace(baseline_step, candidate_step, 1), encoding="utf-8")
        path.write_text(path.read_text(encoding="utf-8") + unrelated, encoding="utf-8")
        current = path.read_text(encoding="utf-8")
        restored = withdraw_fixture_step(current, baseline_step, candidate_step)
        path.write_text(restored, encoding="utf-8")
        assert path.read_text(encoding="utf-8") == base + unrelated
        assert candidate_step not in restored and unrelated in restored
        print("rollback: candidate step removed; unrelated same-file note preserved; sha256=" +
              sha256(path.read_bytes()).hexdigest())

        overlap = current.replace(candidate_step, "Associate by ID with a contributor's changed step.\n")
        path.write_text(overlap, encoding="utf-8")
        before = path.read_bytes()
        try:
            proposal = withdraw_fixture_step(path.read_text(encoding="utf-8"), baseline_step, candidate_step)
        except ValueError as error:
            print("overlap: inverse refused; " + str(error))
        else:
            path.write_text(proposal, encoding="utf-8")
            raise AssertionError("overlap was overwritten")
        assert path.read_bytes() == before
        print("overlap: current bytes preserved; sha256=" + sha256(before).hexdigest())

    print("Fixture assertions completed; expected regressions above remain failures, not accepted changes.")


if __name__ == "__main__":
    main()
