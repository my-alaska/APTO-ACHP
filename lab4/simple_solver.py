from dimacs import *
from os import listdir
from copy import copy
from pycosat import solve
from sat_utility import *


def solve_SAT(CNF, V=None):
    """Simple sat solver that takes a CNF clause input
    and returns solution or UNSAT string if no solution exists

    The algorithm checks a binary tree of all possible solutions until it finds a correct one
    It chooeses one variable, and recursively checks both solutions -
    - with that variable set for True and for False
    """

    if V is None:
        V = dict()

    simplifyCNF(CNF, V)

    if CNF is None:
        return "UNSAT"

    if check(CNF, V):
        res = {v for v in V.keys() if V[v] == 1}
        return sorted(list(res), key=abs)

    v = CNF[0][0]

    V[v], V[-v] = 1, -1
    solve = solve_SAT(simplifyCNF(CNF.copy(), V), V.copy())
    if solve != "UNSAT":
        return solve

    V[v], V[-v] = -1, 1
    solve = solve_SAT(CNF.copy(), V.copy())
    if solve != "UNSAT":
        return solve

    return "UNSAT"


if __name__ == "__main__":
    CNF_dir = "sat"

    CNFs = [
        "10.no.sat",
        "10.yes.sat",
        "100.no.sat",
        "100.yes.sat",
        "20.no.sat",
        "20.yes.sat",
        "30.no.sat",
        "30.yes.sat",
    ]

    for name in CNFs[:2]:
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
