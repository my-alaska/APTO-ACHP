from lab5.utils.dimacs import *
import pycosat


def limit_k(n, k):
    def f(i, j):
        return n + 1 + (j + i * (k + 2))

    k_CNF = []

    for i in range(n + 1):
        k_CNF.append([f(i, 0)])

    for j in range(1, k + 2):
        k_CNF.append([-f(0, j)])

    for i in range(1, n + 1):
        for j in range(k + 2):
            k_CNF.append([-f(i - 1, j), f(i, j)])

    for i in range(1, n + 1):
        for j in range(1, k + 2):
            k_CNF.append([-f(i - 1, j - 1), -(i), f(i, j)])

    k_CNF.append([-f(n, k + 1)])

    return k_CNF


def threshold_VC(G, k):
    """
    Algorithm to solve vertex cover problem by SAT reduction
    and using thresholding function

    Each vertex get it's own sat variable
    All edges represent a CNF clause - one of it's vertices must be included in the solution
    Thresholding function is used is used to create a CNF formula
    that makes sure that at most k variables are used
    """

    k_CNF = edgeList(G) + limit_k(len(G) - 1, k)
    result = pycosat.solve(k_CNF)
    if result != "UNSAT":
        result = {i for i in result if i > 0}
    return result


if __name__ == "__main__":
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

    for name in names:
        print(name)
        G = loadGraph(graph_dir + "/" + name)
        k = 0
        solution = threshold_VC(G, k)
        while solution == "UNSAT":
            k += 1
            solution = threshold_VC(G, k)

        if not isVC(edgeList(G), solution):
            print("WRONG SOLUTION")
        else:
            print(k, "out of", len(G), "vertices")

        print()
