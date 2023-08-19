from os import listdir
from lab3.utils.dimacs import *
import pycosat


def solve_coloring(G, k):
    """
    SAT reduction solution of graph k-coloring problem
    This algorithm finds such graph coloring with at most k colours
    that for all edges, none of their vertices are of the same colour

    reduction:
    we have n*k (n is a number of vertices) SAT variables
    each representing if one of vertices is of one of the colours
    we can't
    1. exactly one colour must be chose for each vertex
    so all positive variables describing a coloring of one vertex must create a clause
    and all combinations of their negated values must create clauses of size 2
    2. ends of one edg must be of different colour
    so for each of them and for each colour we add a clause of it's edge's negated SAT variables
    """
    n = len(G)

    # map vertex and color to cnf variable
    def coloring(i, j):
        return i * k + j + 1

    # get back vertex and color from cnf variable
    def decoloring(c):
        c -= 1
        return (c // k, c % k)

    form = []
    for i in range(n):
        form.append([coloring(i, j) for j in range(k)])
        for j1 in range(k):
            for j2 in range(j1):
                form.append([-coloring(i, j1), -coloring(i, j2)])

    E = edgeList(G)

    for e in E:
        for j in range(k):
            form.append([-coloring(e[0], j), -coloring(e[1], j)])

    print("form length", len(form))
    solution = pycosat.solve(form)

    if solution == "UNSAT":
        return "UNSAT"

    result = [None for i in range(n)]
    for c in solution:
        if c > 0:
            i, j = decoloring(c)
            result[i] = j

    return result


def check_coloring(G, coloring):
    E = edgeList(G)
    for e in E:
        if coloring[e[0]] == coloring[e[1]]:
            return False
    return True


if __name__ == "__main__":
    graph_dir = "coloring-test-data"

    graphs = listdir(graph_dir)

    for name in graphs:
        print(name)
        G = loadGraph(graph_dir + "/" + name)
        result = solve_coloring(G, 4)
        print(result)
        if result == "UNSAT":
            print(result)
        elif not check_coloring(G, result):
            print("WRONG COLORING")

        print()
