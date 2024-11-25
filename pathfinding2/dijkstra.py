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
