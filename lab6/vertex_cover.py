from pulp import *
from dimacs import *


def VC_ILP(G, p=0):
    E = edgeList(G)

    model = LpProblem("VC", LpMinimize)
    X = [None for _ in G]
    for i in range(len(G)):
        X[i] = LpVariable(f"x{i}", cat="Binary")

    Xp = [x * max((len(G[i]) ** p), 1) for i, x in enumerate(X)]

    model += lpSum(Xp)

    for e in E:
        model += X[e[0]] + X[e[1]] >= 1

    model.solve()
    for var in model.variables():
        print(var.name, "=", var.varValue)
    return model.variables()


def VC_ILP_rlx(G, p=0):
    E = edgeList(G)

    model = LpProblem("VC", LpMinimize)
    X = [None for _ in G]
    for i in range(len(G)):
        X[i] = LpVariable(f"x{i}", lowBound=0, upBound=1, cat="Continuous")

    Xp = [x * max((len(G[i]) ** p), 1) for i, x in enumerate(X)]
    model += lpSum(Xp)

    for e in E:
        model += X[e[0]] + X[e[1]] >= 1

    model.solve()
    for var in model.variables():
        print(var.name, "=", 1.0 if var.varValue >= 0.5 else 0.0)
    return model.variables()


G = loadGraph("graph\\p60")

p = 2

# V1 = VC_ILP(G,2)
V2 = VC_ILP_rlx(G)

# print("==================================")
# for v1,v2 in zip(V1,V2):
#     print(v1.name, "=", v1.varValue ,"    ",v2.name, "=", 1. if v2.varValue > 0.5 else 0.)
