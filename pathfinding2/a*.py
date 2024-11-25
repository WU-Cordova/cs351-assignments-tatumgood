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
