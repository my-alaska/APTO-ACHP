from dimacs import *
from itertools import combinations
from os import listdir


def checkVC(G, bag, C):
    for v in bag:
        for u in G[v]:
            if v not in C and u in bag and u not in C:
                return False

    return True






def treewidth_VC(G, decomp, y, C):
    """
    G: graph
    decomp: graph's decomposition
    y: current vertex
    C: considered vertex cover

    return: minimal size of vertex cover
    """
    dynamic_tab = {}

    def f(y,C):
        VC_to_str = "_".join([str(v) for v in sorted(C)])
        key = f"{y}|{VC_to_str}"

        if not checkVC(G, decomp[y].bag, C):
            dynamic_tab[key] = float("inf")

        if not key in dynamic_tab:
            k = len(C)

            for z in decomp[y].children:
                # possible vertices that will be added to the new vertex cover
                extending_vertices = decomp[z].bag - decomp[y].bag

                # bag overlap between y and z vertices
                B = decomp[z].bag
                BnC = B & C
                k -= len(BnC)

                # value to be minimized
                best = float("inf")
                for size in range(len(extending_vertices) + 1):
                    for child_vc in combinations(extending_vertices, size):
                        # new vertex cover to be considered
                        D = BnC | set(child_vc)
                        current = f(z, D)
                        best = min(current, best)
                k += best
            dynamic_tab[key] = k

        return dynamic_tab[key]

    return f(y,C)



if __name__ == "__main__":

    graph_dir = "graphtw"

    graphs = listdir(graph_dir)

    # graphs = ["e5.gr"]

    for i in range(0,len(graphs),2):
        name = graphs[i]
        print(name)
        G = loadGRGraph(graph_dir + "/" + name)
        DG = loadDecomposition(graph_dir + "/" + name[:-2]+"tw")
        tree_bag = DG[1].bag
        best_k = float("inf")
        for s in range(len(tree_bag)+1):
            for VC in combinations(tree_bag,s):
                k = treewidth_VC(G, DG, 1, set(VC))
                best_k = min(k,best_k)
        print(best_k)
        print()