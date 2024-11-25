import heapq

# Graph structure: Adjacency list with edge weights
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 1},
    'C': {'A': 5, 'D': 3, 'E': 2},
    'D': {'B': 1, 'C': 3, 'E': 4},
    'E': {'C': 2, 'D': 4}
}

# Heuristic for A* and Greedy Best-First (straight-line distances)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 0
}
