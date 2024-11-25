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

#dijkstra program
def dijkstra(graph, start, goal):
    pq = []  # Priority queue
    heapq.heappush(pq, (0, start))  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parents = {start: None}

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight
            if cost < distances[neighbor]:
                distances[neighbor] = cost
                parents[neighbor] = current_node
                heapq.heappush(pq, (cost, neighbor))

    # Reconstruct path
    path = []
    while goal:
        path.append(goal)
        goal = parents[goal]
    return path[::-1], distances[path[0]]

#greedy first search program
def greedy_best_first(graph, start, goal, heuristic):
    pq = []  # Priority queue
    heapq.heappush(pq, (heuristic[start], start))  # (heuristic, node)
    visited = set()
    parents = {start: None}

    while pq:
        _, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                parents[neighbor] = current_node
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    # Reconstruct path
    path = []
    while goal:
        path.append(goal)
        goal = parents[goal]
    return path[::-1]

#a* program
def a_star(graph, start, goal, heuristic):
    pq = []  # Priority queue
    heapq.heappush(pq, (0 + heuristic[start], start))  # (f = g + h, node)
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0
    parents = {start: None}

    while pq:
        _, current_node = heapq.heappop(pq)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node].items():
            tentative_g_score = g_scores[current_node] + weight
            if tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                parents[neighbor] = current_node
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(pq, (f_score, neighbor))

    # Reconstruct path
    path = []
    while goal:
        path.append(goal)
        goal = parents[goal]
    return path[::-1], g_scores[path[0]]

start, goal = 'A', 'E'

# Run Dijkstra
dijkstra_path, dijkstra_cost = dijkstra(graph, start, goal)
print(f"Dijkstra Path: {dijkstra_path}, Cost: {dijkstra_cost}")

# Run Greedy Best-First
greedy_path = greedy_best_first(graph, start, goal, heuristic)
print(f"Greedy Best-First Path: {greedy_path}")

# Run A*
a_star_path, a_star_cost = a_star(graph, start, goal, heuristic)
print(f"A* Path: {a_star_path}, Cost: {a_star_cost}")






