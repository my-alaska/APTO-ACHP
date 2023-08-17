from utils.sortnet import *
from utils.dimacs import *
import pycosat


def get_insertion_CNF(first, last):
    """Creating insertion sort net
    for lines from 'first' to 'last' (exclusive)

    """
    lines = list(range(first, last))
    n = last - first
    net = sorterNet(start=last, lines=lines, equiv=False)

    for i in range(1, n):
        for j in range(i, 0, -1):
            net.comp(j, j - 1)

    return net


def sortnet_VC(G, k):
    """
    Algorithm to solve vertex cover problem by SAT reduction
    and using insertion sorting net

    Each vertex get it's own sat variable
    All edges represent a CNF clause - one of it's vertices must be included in the solution
    Sorting network is used to create a CNF formula
    that makes sure that at most k variables are used
    """

    # ensure that at most k vertices are selected
    net_CNF = get_insertion_CNF(1, len(G))
    k_CNF = net_CNF.CNF + [[-net_CNF.lines[k]]]

    # adding edgelist ensures that all edges are covered
    formula = edgeList(G) + k_CNF

    result = pycosat.solve(formula)

    if result == "UNSAT":
        return "UNSAT"

    return {v for v in result if v > 0}


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
        solution = sortnet_VC(G, k)
        while solution == "UNSAT":
            k += 1
            solution = sortnet_VC(G, k)

        if not isVC(edgeList(G), solution):
            print("WRONG SOLUTION")
        else:
            print(k, "out of", len(G), "vertices")

        print()
