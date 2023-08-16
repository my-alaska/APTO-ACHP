import pycosat
from lab3.utils.dimacs import *

graphs = [
    "10.no.x3c",
    "10.yes.x3c",
    "50.no.x3c",
    "50.yes.x3c",
    "100.no.x3c",
    "200.no.x3c",
    "200.yes.x3c",
    "350.no.x3c",
    "350.yes.x3c",
    "500.no.x3c",
    "500.yes.x3c",
    "600.no.x3c",
    "600.yes.x3c",
]


def solve_x3c(n, sets):
    """
    Solve an exact 3 set cover problem
    This solution reduces the problem to SAT and uses pycosat solver

    reduction - creating a form:
    variable's sign confirms whether or not a set defined by it is a part of the result
    1. for each elements we need at least one set that covers it
    so we'll create a clause that includes all sets that contain it
    2. none of these sets(from one clause) can be in the result at the same time
    so for all pairs from one clause we create a clause with a negation of both of them
    (at least one from such pair is not chosen)
    """

    # list of variables representing sets that number belongs to
    include = [[] for _ in range(n)]

    for i, set in enumerate(sets):
        for var in set:
            include[var - 1].append(i + 1)

    exclude = []
    for set_of_sets in include:
        listed = list(set_of_sets)
        for i in range(len(listed)):
            for j in range(i):
                exclude.append([-listed[i], -listed[j]])

    result = pycosat.solve(exclude + include)
    return result


if __name__ == "__main__":
    for name in graphs:
        n, sets = loadX3C("graphs/" + name)

        print()
        print(n, name)

        if name.split(".")[1] == "yes":
            real_result = True
        else:
            real_result = False

        solution = solve_x3c(n, sets)
        if solution != "UNSAT":
            check = set()
            for i, st in enumerate(sets):
                if solution[i] > 0:
                    for element in st:
                        check.add(element)
            if len(check) != n or not all(
                [val == i + 1 for i, val in enumerate(list(check))]
            ):
                print("wrong solution")
                continue

        result = solution != "UNSAT"

        if result != real_result:
            print("Wrong reslut")
        else:
            print("Correct result")
