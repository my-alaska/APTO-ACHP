from copy import copy

from utils.dimacs import isVC
from itertools import combinations


def bruteforceVC(E, k):
    """
    :param E: List of edges of a graph. As tuples of pairs of vertices
    :param k: number of vertices to cover the graph
    :return: set of vertex indices satisfying the requirements
    """

    V = 0
    for e in E:
        if e[0] > V:
            V = e[0]
        if e[1] > V:
            V = e[1]

    for C in combinations(range(1, V + 1), k):
        if isVC(E, C):
            return C
    return None


def recursiveVC(E, k, S=None):
    """
    Simplest recursive solution to vertex cover problem.
    For a selected edge either one or the other vertex belongs to the solution
    we simply check both of these options

    :param E: List of edges in the graph
    :param k: number of vertices to cover the graph
    :param S: potential part of solution. passed to recursion calls
    :return: complete solution or none in case of no solution with this k or S
    """

    if S is None:
        S = set()
    if len(E) == 0:
        return S  # found solution
    if k == 0:
        return None  # no solution

    u, v = E[0]

    S1 = recursiveVC([e for e in E if e[0] != u and e[1] != u], k - 1, copy(S) | {u})
    if S1:
        return S1

    S2 = recursiveVC([e for e in E if e[0] != v and e[1] != v], k - 1, copy(S) | {v})
    if S2:
        return S2

    return None


def better_recursiveVC(E, k, S=None):
    """
    Recursive solution to vertex cover problem.
    If vertex u is not a part of the solution, all of it's neighbours must be
    We can use this observation to limit the number of recursion calls by covering more cases at once

    :param E: List of edges in the graph
    :param k: number of vertices to cover the graph
    :param S: potential part of solution. passed to recursion calls
    :return: complete solution or none in case of no solution with this k or S
    """

    if S is None:
        S = set()
    if k < 0:
        return None  # no solution
    if len(E) == 0:
        return S  # found solution
    if k == 0:
        return None  # no solution

    u, v = E[0]

    S1 = better_recursiveVC(
        [e for e in E if e[0] != u and e[1] != u], k - 1, copy(S) | {u}
    )
    if S1:
        return S1

    new_set = {e[0] for e in E if e[1] == u} | {e[1] for e in E if e[0] == u}

    S2 = better_recursiveVC(
        [e for e in E if e[0] not in new_set and e[1] not in new_set],
        k - len(new_set),
        copy(S) | new_set,
    )
    if S2:
        return S2

    return None


def best_recursiveVC(E, k, S=None):
    """
    Recursive solution to vertex cover problem.
    This solution uses the vertex with the largest number of neighbours
    We never take a vertex of degree 1 as part of our solution - always it's neighbour
    Otherwise we choose a vertex with the largest degree

    :param E: List of edges in the graph
    :param k: number of vertices to cover the graph
    :param S: potential part of solution. passed to recursion calls
    :return: complete solution or none in case of no solution with this k or S
    """

    def _remove(E, u, S, deg):
        v = -1
        for e in E:
            if e[1] == u:
                v = e[0]
                break
            elif e[0] == u:
                v = e[1]
                break
        S.add(v)
        new_E = []
        for e in E:
            if e[1] != v and e[0] != v:
                new_E.append(e)
            else:
                deg[e[1]] -= 1
                deg[e[0]] -= 1
        return new_E

    if S is None:
        S = set()
    if k < 0:
        return None
    if len(E) == 0:
        return S
    if k == 0:
        return None

    deg = dict()
    for e in E:
        deg[e[0]] = deg.get(e[0], 0) + 1
        deg[e[1]] = deg.get(e[1], 0) + 1

    while 1 in set(deg.values()):
        for u, d in deg.items():
            if d == 1:
                E = _remove(E, u, S, deg)
                k -= 1

    d_max, u = -1, -1
    for v, d in deg.items():
        if d > d_max:
            d_max = d
            u = v

    S1 = best_recursiveVC(
        [e for e in E if e[0] != u and e[1] != u], k - 1, copy(S) | {u}
    )
    if S1:
        return S1

    new_set = {e[0] for e in E if e[1] == u} | {e[1] for e in E if e[0] == u}

    S2 = best_recursiveVC(
        [e for e in E if e[0] not in new_set and e[1] not in new_set],
        k - len(new_set),
        copy(S) | new_set,
    )
    if S2:
        return S2

    return None


def _kernelize(E, k):
    G = dict()
    for u, v in E:
        if not u in G.keys():
            G[u] = set()
        if not v in G.keys():
            G[v] = set()
        G[v].add(u)
        G[u].add(v)

    def _remove(G, v):
        if v not in G.keys():
            return
        v_neighbors = G[v]
        for u in v_neighbors:
            G[u].remove(v)
            if not G[u]:
                del G[u]
        del G[v]

    S = set()

    removing = True
    while removing and k != 0:
        removing = False
        for v, neighbors in G.items():
            if len(neighbors) == 1:
                u = list(neighbors)[0]
                S.add(u)
                _remove(G, v)
                _remove(G, u)
                k -= 1
                removing = True
                break
            elif len(neighbors) > k:
                _remove(G, v)
                S.add(v)
                k -= 1
                removing = True
                break

    new_E = []
    for v, neighbors in G.items():
        for u in neighbors:
            if u < v:
                new_E.append((u, v))

    if len(new_E) <= k * k:
        return new_E, k, S

    return None


def kernel_VC(E, k):
    kernel = _kernelize(E, k)
    if not kernel:
        return None
    return best_recursiveVC(*kernel)
