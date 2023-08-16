from utils.dimacs import loadGraph, saveSolution
from solution import *

graphs = [
    ("e5"),
    ("e10"),
    ("e20"),
    ("e40"),
    ("e150"),
    ("s25"),
    ("s50"),
    ("s500"),
    ("b20"),
    ("b30"),
    ("b100"),
    ("k330_a"),
    ("k330_b"),
    ("k330_c"),
    ("k330_d"),
    ("k330_e"),
    ("k330_f"),
    ("f30"),
    ("f35"),
    ("f40"),
    ("f56"),
    ("m20"),
    ("m30"),
    ("m40"),
    ("m50"),
    ("m100"),
    ("p20"),
    ("p35"),
    ("p60"),
    ("p150"),
    ("p200"),
    ("r30_01"),
    ("r30_05"),
    ("r50_001"),
    ("r50_01"),
    ("r50_05"),
    ("r100_005"),
    ("r100_01"),
    ("r200_001"),
    ("r200_005"),
]

if __name__ == "__main__":
    for name in graphs:
        G = loadGraph("graph/" + name)
        print(name, "size:", len(G))
        two_n_sol = two_n_VC(G)
        log_n_sol = log_n_VC(G)
        print("2n size  :", len(two_n_sol))
        print("logn size:", len(log_n_sol))
        print()
        saveSolution("result/" + name + ".sol", log_n_sol)
