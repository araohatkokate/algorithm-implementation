# Graph Algorithms Implementation

This repository contains Python implementations of three fundamental graph algorithms: Dijkstra's algorithm, Bellman-Ford algorithm, and Floyd-Warshall algorithm. These algorithms are tested with example graphs and can be easily extended for other test cases.

## Algorithms Included

1. **Dijkstra's Algorithm**
   - Finds the shortest path from a source vertex to all other vertices in a graph.
   - Requires non-negative edge weights.
   - Efficiently implemented using a priority queue.

2. **Bellman-Ford Algorithm**
   - Finds the shortest path from a source vertex to all other vertices in a graph.
   - Supports graphs with negative edge weights.
   - Detects negative weight cycles and raises an exception if one is found.

3. **Floyd-Warshall Algorithm**
   - Computes shortest paths between all pairs of vertices.
   - Supports graphs with negative edge weights.
   - Does not work with negative weight cycles.

## File Structure

- **`dijkstra.py`**: Contains the implementation of Dijkstra's algorithm.
- **`bellman_ford.py`**: Contains the implementation of the Bellman-Ford algorithm.
- **`floyd_warshall.py`**: Contains the implementation of the Floyd-Warshall algorithm.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/graph-algorithms.git
   cd graph-algorithms```
   ```
2. Run the code:
   ```bash
   python filename.py
   ```
