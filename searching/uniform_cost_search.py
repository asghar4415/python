graph = {
    'A': {'B': 2, 'C': 1}, 'B': {'D': 4, 'E': 3}, 'C': {'F': 1, 'G': 5},
    'D': {'H': 2}, 'E': {}, 'F': {'I': 6}, 'G': {}, 'H': {}, 'I': {}
}


def ucs(graph, start, goal):
    frontier = [(start, 0)]  # List of (node, cost)
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        # Sort manually before popping (lowest cost first)
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

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
