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
