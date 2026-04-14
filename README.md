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