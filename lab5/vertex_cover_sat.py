from dimacs import *
import pycosat
from os import listdir


def limit_k(n, k):
    def f(i, j):
        return n + 1 + (j + i * (k + 2))

    result = []

    for i in range(n + 1):
        result.append([f(i, 0)])

    for j in range(1, k + 2):
        result.append([-f(0, j)])

    for i in range(1, n + 1):
        for j in range(k + 2):
            result.append([-f(i - 1, j), f(i, j)])

    for i in range(1, n + 1):
        for j in range(1, k + 2):
            result.append([-f(i - 1, j - 1), -(i), f(i, j)])

    result.append([-f(n, k + 1)])

    return result


def f_inv(l, k, n):
    return ((l - n) // (k + 2), (l - n) % (k + 2))


def convert_to_sat(G, k):
    n = len(G)
    result = []
    for i, v_neighbors in enumerate(G):
        for j in v_neighbors:
            if i < j:
                result.append([i, j])
    result.extend(limit_k(n - 1, k))
    return result


def solve(G, k):
    sat = convert_to_sat(G, k)
    return pycosat.solve(sat)[: len(G) - 1]


graph_dir = "graph"
# names = listdir(graph_dir)
names = [
    "b20",
    "b30",
    "e10",
    "e20",
    "e40",
    "e5",
    "f30",
    "f35",
    "f40",
    "f56",
    "m20",
    "m30",
    "m40",
    "m50",
    "b100",
    "e150",
    "k330_a",
    "k330_b",
    "k330_c",
    "k330_d",
    "k330_e",
    "k330_f",
    "m100",
    "p150",
    "p20",
    "p200",
    "p35",
    "p60",
    "r100_005",
    "r100_01",
    "r200_001",
    "r200_005",
    "r30_01",
    "r30_05",
    "r50_001",
    "r50_01",
    "r50_05",
    "s25",
    "s50",
    "s500",
]

if __name__ == "__main__":
    for name in names:
        print(name)
        G = loadGraph(graph_dir + "/" + name)
        k = 0
        solution = solve(G, k)
        while solution == "UNSAT":
            k += 1
            solution = solve(G, k)
        solution_set = {i for i in solution if i > 0}
        print(k, "out of", len(G), "vertices")
        if not isVC(edgeList(G), solution_set):
            print("WRONG SOLUTION")
        print()
