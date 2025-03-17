graph = {
    'A': {'B': 2, 'C': 1}, 'B': {'D': 6, 'G': 3}, 'C': {'D': 5, 'A': 1},
    'D': {'C': 5, 'B': 6, 'G': 4, 'F': 2, 'I': 1}, 'G': {'D': 4, 'B': 3}, 'F': {'I': 4, 'D': 2}, 'I': {'F': 4, 'D': 1}
}


def ucs(graph, start, goal):
    frontier = [(start, 0)]  # List of (node, cost)
    visited = []
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        # Sort manually before popping (lowest cost first)
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        if current_node in visited:
            continue

        visited.append(current_node)

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Goal found with UCS. Path: {path}, Cost: {current_cost}")
            return

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.append((neighbor, new_cost))
                came_from[neighbor] = current_node

    print("Goal not found with UCS")


# Test cases
ucs(graph, 'A', 'I')  # Should find the shortest path to I
ucs(graph, 'A', 'G')  # Should find the shortest path to G
