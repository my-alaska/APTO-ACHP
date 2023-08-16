import random
import pycosat
import numpy as np
import matplotlib.pyplot as plt


def random_k(n):
    S = [1, -1]  # +/-
    V = range(1, n + 1)  # 1...n
    return random.choice(V) * random.choice(S)


def get_cnf(n_variables, in_clause, n_clauses):
    return [[random_k(n_variables) for i in range(in_clause)] for j in range(n_clauses)]


if __name__ == "__main__":
    n = 100
    T = 1000
    k = 3
    a_vals = np.arange(1, 10, 0.1)

    results = []
    for a in a_vals:
        print(round(a, 1))
        clauses = [get_cnf(n, k, int(a * n)) for _ in range(T)]
        S = 0
        for clause in clauses:
            sol = pycosat.solve(clause)
            if sol != "UNSAT":
                S += 1
        results.append(S / T)

    plt.scatter(a_vals, results)
    plt.title("SAT-3CNF, 100 variables, 1000 repeats")
    plt.xlabel("number of clauses to variables ratio")
    plt.ylabel("probablility of satisfiability")
    plt.savefig("results.png")
    plt.show()
