from dimacs import *
from os import listdir
from copy import copy
from pycosat import solve
from sat_utility import *


def solve_SAT(CNF, V=None):
    """Improvement to SAT solver from simple_solver.py
    improvement enables pruning the recursion tree

    the basic solver takes one variable from the first clause of CNF
    and then makes 2 recursion calls -
    - one with that variable as False, and the other as True

    Improved solution iterates like that through all variables
    in the 1st clause and makes recursion calls however,
    it sets the last variable to True when all previous ones to False

    It's easy to prove that no possible solution is omitted in that process
    while on average, the algorithm enters the recursion calls
    with more information about the solution
    """

    if V is None:
        V = dict()

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

    CNFs = [
        "10.no.sat",
        "10.yes.sat",
        "20.no.sat",
        "20.yes.sat",
        "30.no.sat",
        "30.yes.sat",
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
