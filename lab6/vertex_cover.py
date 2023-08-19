from pulp import *
from dimacs import *
from os import listdir

from lab1.solution import kernel_VC


def VC_ILP(G, p=0):
    E = edgeList(G)

    model = LpProblem("VC", LpMinimize)
    X = [LpVariable(f"x{i}", cat="Binary") for i in range(len(G))]

    Xp = [x * max((len(G[i]) ** p), 1) for i, x in enumerate(X)]

    model += lpSum(Xp)

    for e in E:
        model += X[e[0]] + X[e[1]] >= 1

    model.solve(PULP_CBC_CMD(msg=0))

    result = set()
    for v in range(len(G)):
        if X[v].varValue == 1:
            result.add(v)

    return result


def VC_ILP_rlx(G, p=0):
    E = edgeList(G)

    model = LpProblem("VC", LpMinimize)
    X = [
        LpVariable(f"x{i}", lowBound=0, upBound=1, cat="Continuous")
        for i in range(len(G))
    ]

    Xp = [x * max((len(G[i]) ** p), 1) for i, x in enumerate(X)]
    model += lpSum(Xp)

    for e in E:
        model += X[e[0]] + X[e[1]] >= 1

    model.solve(PULP_CBC_CMD(msg=0))

    result = set()
    for v in range(len(G)):
        if X[v].varValue >= 0.5:
            result.add(v)

    return result


if __name__ == "__main__":
    graph_dir = "graph"

    # graphs = listdir(graph_dir)
    graphs = [
        "b100",
        "b20",
        "b30",
        "e10",
        "e150",
        "e20",
        "e40",
        "e5",
        # "f30",
        # "f35",
        # "f40",
        # "f56",
        "k330_a",
        "k330_b",
        "k330_c",
        "k330_d",
        "k330_e",
        "k330_f",
        "m100",
        "m20",
        "m30",
        "m40",
        "m50",
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

    for name in graphs:
        G = loadGraph(graph_dir + "/" + name)

        p = 0

        print(name)

        # for k in range(len(G)):
        #     C0 = kernel_VC(edgeList(G), k)
        #     if C0 != None:
        #         print("size of algorithm solution:   ", len(C0))
        #         break

        C1 = VC_ILP(G, p)
        C2 = VC_ILP_rlx(G, p)

        if not isVC(edgeList(G), C1):
            print("WRONG SOLUTION!!!")
        else:
            print("size of ILP solution:         ", len(C1))

        if not isVC(edgeList(G), C2):
            print("WRONG RELAXED SOLUTION!!!")
        else:
            print("size of relaxed solution:     ", len(C1))

        print()
