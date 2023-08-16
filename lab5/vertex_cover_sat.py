import dimacs
import pycosat



def limit_k(n, k):
    def f(i, j):
        return n+1 + (j + i * (k + 2))

    result = []

    for i in range(n + 1):
        result.append([f(i, 0)])

    for j in range(1, k + 2):
        result.append([-f(0, j)])

    for i in range(1,n+1):
        for j in range(k + 2):
            result.append([-f(i-1, j), f(i, j)])

    for i in range(1,n+1):
        for j in range(1,k + 2):
            result.append([-f(i-1, j-1), -(i), f(i, j)])

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
    result.extend(limit_k(n-1,k))
    return result


def solve(G, k):
    sat = convert_to_sat(G, k)
    return pycosat.solve(sat) [:len(G)-1]


G = dimacs.loadGraph("graph/e5")

print(solve(G, 2))

# n = 7
# k = 2
# for i in range(7+1):
#     for j in range(2+2):
#         print(n + (j + i * (k + 2)))