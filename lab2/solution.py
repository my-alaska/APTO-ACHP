from random import choice
from utils.dimacs import edgeList


def two_n_VC(G):
    """
    2n approximation of vertex cover
    The algorithm finds an edge that hasn't been covered yet and adds both vertices to the solution
    :param G: input graph. List of sets of neighbouring vertices
    :return: vertex cover of size at most 2 times the size of optimal vertex cover
    """

    E = edgeList(G)
    result = set()
    for e in E:
        if e[0] not in result and e[1] not in result:
            result.update({e[0], e[1]})
    return result


def log_n_VC(G):
    """
    the idea behind the algorithm is to always add the vertex with the largest number of neighbours to the solution
    :param G: input graph. List of sets of neighbouring vertices
    :return: vertex cover of size at most nlogn where n is the optimal size of the VC
    """
    result = set()
    while True:
        best = set()
        best_n = 0
        for i, g in enumerate(G):
            if i not in result and len(g) > best_n:
                best.add(i)
                best_n = len(g)
        if len(best) == 0:
            break
        best = choice(list(best))
        for g in G:
            if best in g:
                g.remove(best)
        result.add(best)
    return result
