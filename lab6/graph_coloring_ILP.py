from pulp import *
from os import listdir
from dimacs import *

def check_coloring(G, coloring):
    E = edgeList(G)
    for e in E:
        if coloring[e[0]] == coloring[e[1]]:
            return False
    return True

def coloring_ILP(G, k):
    n = len(G)

    model = LpProblem("VC",LpMinimize)
    X = [
        [LpVariable(f"x{i},{j}", cat="Binary")for j in range(k)]
        for i in range(n)
    ]

    for i in range(n):
        model += (lpSum(X[i]) == 1)

    for e in edgeList(G):
        for c in range(k):
            model += (X[e[0]][c] + X[e[1]][c] <= 1)

    model.solve(PULP_CBC_CMD(msg=0))

    result = [-1 for i in range(n)]
    for v in range(len(G)):
        feasible = False
        for c in range(k):
            if X[v][c].varValue == 1:
                result[v] = c
                feasible = True
                break
        if not feasible:
            return None


    return result

if __name__ == "__main__":
    graph_dir = "coloring-test-data"

    graphs = listdir(graph_dir)
    # graphs = ["1-FullIns_4.col"]

    for name in graphs:
        print(name)
        G = loadGraph(graph_dir + "/" + name)
        result = coloring_ILP(G, 4)
        print(result)
        if result == "UNSAT":
            print(result)
        elif not check_coloring(G, result):
            print("WRONG COLORING")
        print()
