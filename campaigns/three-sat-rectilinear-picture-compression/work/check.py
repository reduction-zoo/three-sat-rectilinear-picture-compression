"""Independent finite oracles for the fixed source and target definitions."""

import argparse
import itertools
import json
import subprocess
import sys
from pathlib import Path

import z3

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NO = "NO-SOLUTION"


def valid_source(source, output):
    n = source["n"]
    if output == NO:
        return source_solution(source) == NO
    if not isinstance(output, list) or len(output) != n or any(type(v) is not bool for v in output):
        return False
    return all(any((output[abs(lit) - 1] if lit > 0 else not output[-lit - 1]) for lit in clause)
               for clause in source["clauses"])


def source_solution(source):
    n = source["n"]
    assert type(n) is int and n >= 0
    variables = [z3.Bool(f"x{i}") for i in range(n)]
    solver = z3.Solver()
    for clause in source["clauses"]:
        assert isinstance(clause, list) and len(clause) == 3
        assert all(type(lit) is int and lit != 0 and abs(lit) <= n for lit in clause)
        solver.add(z3.Or(*[(variables[lit - 1] if lit > 0 else z3.Not(variables[-lit - 1])) for lit in clause]))
    result = solver.check()
    if result == z3.unsat:
        return NO
    if result != z3.sat:
        raise RuntimeError(f"source solver returned {result}")
    model = solver.model()
    answer = [z3.is_true(model.eval(variable, model_completion=True)) for variable in variables]
    assert valid_source_witness(source, answer)
    return answer


def valid_source_witness(source, output):
    n = source["n"]
    return (isinstance(output, list) and len(output) == n
            and all(type(v) is bool for v in output)
            and all(any((output[abs(lit) - 1] if lit > 0 else not output[-lit - 1]) for lit in clause)
                    for clause in source["clauses"]))


def valid_target_witness(target, output):
    matrix, budget = target["matrix"], target["K"]
    if not isinstance(output, list) or len(output) > budget:
        return False
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    covered = set()
    for rect in output:
        if (not isinstance(rect, list) or len(rect) != 4
                or any(type(v) is not int for v in rect)):
            return False
        r0, r1, c0, c1 = rect
        if not (0 <= r0 <= r1 < rows and 0 <= c0 <= c1 < cols):
            return False
        for r in range(r0, r1 + 1):
            for c in range(c0, c1 + 1):
                if matrix[r][c] != 1:
                    return False
                covered.add((r, c))
    return covered == {(r, c) for r in range(rows) for c in range(cols) if matrix[r][c] == 1}


def target_solutions(target, limit=2):
    matrix, budget = target["matrix"], target["K"]
    assert type(budget) is int and budget >= 0
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    assert all(isinstance(row, list) and len(row) == cols and all(v in (0, 1) and type(v) is int for v in row) for row in matrix)
    ones = {(r, c) for r in range(rows) for c in range(cols) if matrix[r][c] == 1}
    if not ones:
        return [[]]
    rectangles = []
    for r0 in range(rows):
        for r1 in range(r0, rows):
            for c0 in range(cols):
                for c1 in range(c0, cols):
                    if all(matrix[r][c] == 1 for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)):
                        rectangles.append([r0, r1, c0, c1])
    chosen = [z3.Bool(f"rectangle_{i}") for i in range(len(rectangles))]
    solver = z3.Solver()
    solver.add(z3.PbLe([(var, 1) for var in chosen], budget))
    for r, c in ones:
        solver.add(z3.Or(*[chosen[i] for i, (r0, r1, c0, c1) in enumerate(rectangles)
                            if r0 <= r <= r1 and c0 <= c <= c1]))
    outputs = []
    for _ in range(limit):
        result = solver.check()
        if result == z3.unsat:
            break
        if result != z3.sat:
            raise RuntimeError(f"target solver returned {result}")
        model = solver.model()
        selected = [z3.is_true(model.eval(var, model_completion=True)) for var in chosen]
        witness = [rect for rect, use in zip(rectangles, selected) if use]
        assert valid_target_witness(target, witness)
        outputs.append(witness)
        solver.add(z3.Or(*[var != use for var, use in zip(chosen, selected)]))
    return outputs or [NO]


def valid_target(target, output):
    return (target_solutions(target, 1) == [NO]) if output == NO else valid_target_witness(target, output)


def self_test():
    subprocess.run([sys.executable, str(ROOT / "research/validate_preparation.py"), str(HERE / "cases.json")], check=True)
    from generate_cases import source_for_seed

    cases = json.loads((HERE / "cases.json").read_text())
    for case in cases:
        source = case["source"]
        if case["kind"] == "random":
            assert source == source_for_seed(case["seed"])
        result = source_solution(source)
        exhaustive = next((list(bits) for bits in itertools.product((False, True), repeat=source["n"])
                           if valid_source_witness(source, list(bits))), NO)
        assert (result == NO) == (exhaustive == NO)
        assert (result == NO) == (case["expected"] == NO)
        assert valid_source(source, case["expected"])
        if result != NO:
            assert valid_source_witness(source, result)
    assert source_solution({"n": 0, "clauses": []}) == []
    assert source_solution({"n": 1, "clauses": [[1, 1, 1], [-1, -1, -1]]}) == NO
    assert not valid_source({"n": 1, "clauses": [[1, 1, 1]]}, NO)
    assert not valid_source_witness({"n": 1, "clauses": [[1, 1, 1]]}, [False])
    assert not valid_source_witness({"n": 1, "clauses": []}, [1])
    full = {"matrix": [[1, 1], [1, 1]], "K": 1}
    diagonal = {"matrix": [[1, 0], [0, 1]], "K": 1}
    assert target_solutions(full, 1) != [NO]
    assert target_solutions(diagonal, 1) == [NO]
    assert target_solutions({"matrix": [[1, 0, 1]], "K": 1}) == [NO]
    assert target_solutions({"matrix": [[1, 0, 1]], "K": 2}) != [NO]
    assert valid_target(full, [[0, 1, 0, 1]])
    assert not valid_target_witness(diagonal, [[0, 1, 0, 1]])
    assert not valid_target_witness(full, [[0, 0, 0, 0]])
    assert valid_target({"matrix": [], "K": 0}, [])
    assert not valid_target({"matrix": [], "K": 0}, NO)
    print(f"self-test passed: {len(cases)} source cases, target positive/negative/malformed fixtures")


def candidate_check(candidate):
    cases = json.loads((HERE / "cases.json").read_text())
    positive = negative = outputs = 0
    for index, case in enumerate(cases):
        source = case["source"]
        run = subprocess.run([sys.executable, str(candidate)], input=json.dumps(source), text=True, capture_output=True, check=True)
        target = json.loads(run.stdout)
        witnesses = target_solutions(target)
        for witness in witnesses:
            if not valid_target(target, witness):
                raise AssertionError((index, "invalid target output", witness))
            recovered = subprocess.run([sys.executable, str(candidate), "--extract"],
                                       input=json.dumps({"source": source, "target_solution": witness}),
                                       text=True, capture_output=True, check=True)
            answer = json.loads(recovered.stdout)
            if not valid_source(source, answer) or (answer == NO) != (case["expected"] == NO):
                raise AssertionError((index, source, target, witness, answer, case["expected"]))
            outputs += 1
        positive += witnesses != [NO]
        negative += witnesses == [NO]
    print(f"candidate passed: {len(cases)} instances, {positive} target YES, {negative} target NO, {outputs} outputs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--candidate", type=Path)
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.candidate:
        candidate_check(args.candidate.resolve())
    else:
        parser.error("choose --self-test or --candidate")
