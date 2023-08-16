from utils.dimacs import *
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
    ("m20"),
    ("m30"),
    ("m40"),
    ("m50"),
    ("m100"),
    ("p20"),
    ("p35"),
    ("p60"),
    ("p150"),
    ("r30_01"),
    ("r30_05"),
    ("r50_001"),
    ("r50_01"),
    ("r50_05"),
    ("r100_005"),
]

solution_functions = [
    bruteforceVC,
    recursiveVC,
    better_recursiveVC,
    best_recursiveVC,
    kernel_VC,
]

if __name__ == "__main__":
    data_dir = "graph"
    result_dir = "result"

    results1 = []
    for name in graphs:
        print(name)
        full_name = data_dir + "/" + name
        G = loadGraph(full_name)
        for k in range(len(G)):
            kernel = kernelize(edgeList(G), k)
            if not kernel:
                continue
            C = best_recursiveVC(*kernel)
            if C != None:
                print("best", name, len(C), C)
                results1.append(len(C))
                saveSolution(result_dir + "/" + name + ".sol", set(C))
                break

    results2 = []
    for name in graphs:
        print(name)
        full_name = data_dir + "/" + name
        G = loadGraph(full_name)
        for k in range(len(G)):
            C = best_recursiveVC(edgeList(G), k)
            if C != None:
                print("best", name, len(C), C)
                results2.append(len(C))
                saveSolution(result_dir + "/" + name + ".sol", set(C))
                break
