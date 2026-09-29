# KD-Tree Implementation

This project implements a k-dimensional tree (KD-tree) in Python for efficient multidimensional spatial search.

## Features
- Insertion of k-dimensional points
- Exact point search
- Nearest neighbour queries using recursive backtracking and pruning
- Input validation to ensure all points match the specified dimensionality (k)
- Benchmark comparison against brute-force nearest neighbour search

## Motivation
I built this for data structures and algorithms practice, focusing on implementing search structures and understanding performance trade-offs in high-dimensional data.

## Structure
- `src/kdtree.py` — core KD-tree implementation
- `main.py` — demo and performance benchmark

## Usage
Run the demo and benchmark:

```bash
python main.py
```

## Benchmark scope and complexity

The demo times one nearest-neighbour query on 10,000 random two-dimensional points. It is an illustrative timing comparison, not a systematic scaling study or a guarantee of a speedup. Results vary between runs.

Insertion and exact lookup take O(h), where h is tree height: typically O(log n) for a well-shaped tree, but O(n) in the worst case. This implementation inserts points without rebalancing, so ordered inputs can create a deep tree. Nearest-neighbour search uses backtracking and pruning; its worst case is O(n), with performance depending on point distribution and dimensionality. Brute-force nearest-neighbour search is O(nk) for n points in k dimensions, or O(n) for fixed k.
