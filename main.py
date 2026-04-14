from src.kdtree import KDTree
import random
import time

# Brute-force vs KD-tree NN comparison

# Generate random dataset
N = 10000
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(N)]

tree = KDTree(2)
for p in points:
    tree.insert(p)

target = (50.1, 50.2)

# KD-tree NN
start = time.time()
kd_result = tree.nearest_neighbour(target)
kd_time = time.time() - start

# Brute-force NN
start = time.time()
bf_result = KDTree.brute_force_nearest(points, target)
bf_time = time.time() - start

print("\n--- Benchmark ---")
print("Target:", target)
print("KD-tree result:", kd_result, f"Time: {kd_time:.6f}s")
print("Brute-force result:", bf_result, f"Time: {bf_time:.6f}s")