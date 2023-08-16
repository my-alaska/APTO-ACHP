from dimacs import *
from os import listdir
from copy import copy
from pycosat import solve
from sat_utility import *


def getSingularClause(CNF):
    for i, C in enumerate(CNF):
        if len(C) == 1:
            return C[0], i
    return None


def unitPropagate(CNF, V):
    if CNF is None:
        return None
    clause_tuple = getSingularClause(CNF)
    while clause_tuple is not None:
        l, i = clause_tuple
        if l in V and V[l] == -1:
            return None
        V[l] = 1
        V[-l] = -1
        CNF = CNF[:i] + CNF[i + 1 :]
        clause_tuple = getSingularClause(CNF)
    return CNF


def remove_val(CNF, v):
    new_CNF = []
    for i, clause in enumerate(CNF):
        for j, val in enumerate(clause):
            if val == v:
                clause = clause[:j] + clause[j + 1 :]
        if len(clause) != 0:
            new_CNF.append(clause)
    return new_CNF


def fixConst(CNF, V):
    if CNF is None:
        return None
    val_set = set()
    for clause in CNF:
        for v in clause:
            val_set.add(v)
    for v in val_set:
        if -v not in val_set:
            V[v] = 1
            # CNF = remove_val(CNF, v)
    return CNF


def solve_SAT(CNF, V=None):
    """Improvement to SAT solver from better_backtracking.py
    improvement enables pruning the recursion tree

    This algorithm sets a valie of cnf variables that only appear with one logical value
    Because of that all cnf clauses that they appear in are positive and can be removed

    In addition it removes all clauses of length one
    by setting proper value of the variables that appear in them
    """

    if V is None:
        V = dict()

    CNF = unitPropagate(CNF, V)
    CNF = fixConst(CNF, V)
    CNF = simplifyCNF(CNF, V)

    if CNF is None:
        return "UNSAT"

    if check(CNF, V):
        res = {v for v in V.keys() if V[v] == 1}
        return sorted(list(res), key=abs)

    for i, v in enumerate(CNF[0]):
        for j in range(i):
            V[CNF[0][j]], V[-CNF[0][j]] = -1, 1
        V[v], V[-v] = 1, -1
        solve = solve_SAT(CNF.copy(), V.copy())
        if solve != "UNSAT":
            return solve

    return "UNSAT"


if __name__ == "__main__":
    CNF_dir = "sat"

    # print(listdir(CNF_dir))

    CNFs = [
        "1-FullIns_3.3.sat",
        "1-FullIns_3.4.sat",
        "1-FullIns_4.4.sat",
        "1-FullIns_4.5.sat",
        "1-Insertions_4.4.sat",
        "1-Insertions_4.5.sat",
        "anna.11.sat",
        "anna.15.sat",
        "10.no.sat",
        "10.yes.sat",
        "100.no.sat",
        "100.yes.sat",
        "20.no.sat",
        "20.yes.sat",
        "30.no.sat",
        "30.yes.sat",
        "35.no.sat",
        "35.yes.sat",
        "40.no.sat",
        "40.yes.sat",
        "5.no.sat",
        "5.yes.sat",
        "50.no.sat",
        "50.yes.sat",
        "60.no.sat",
        "60.yes.sat",
        "70.no.sat",
        "70.yes.sat",
        "80.no.sat",
        "80.yes.sat",
        "90.no.sat",
        "90.yes.sat",
    ]

    for name in CNFs:
        cnf = loadCNF(CNF_dir + "/" + name)[1]
        print(name)

        solution = solve_SAT(cnf)

        if solution != "UNSAT":
            if not test_solution(cnf, solution):
                print("wrong solution")
            else:
                print("valid solution")
        else:
            print("unsat")

        print()
