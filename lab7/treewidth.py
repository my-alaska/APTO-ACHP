from dimacs import *

G = loadGRGraph("graphtw/e5.gr")

DG = loadDecomposition("graphtw/e5.tw")

print(G)

for bag in DG:
    print(bag.id, bag.children, bag.parent, bag.bag)


def checkVC(G, X, Y):
    E = []
    for v in X:
        for u in G[v]:
            if v < u and u in X:
                E += (v, u)
    if isVC(E, Y & X):
        return True
    return False


def f(y, C):
    return float("inf")
