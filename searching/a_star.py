graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

heuristic = {
    'A': 7, 'B': 6, 'C': 5, 'D': 4,
    'E': 7, 'F': 3, 'G': 6, 'H': 2, 'I': 0
}


def a_star(graph, start, goal):
    frontier = [(start, heuristic[start])]  # (node, f(n))
    g_costs = {start: 0}
    came_from = {start: None}
    visited = set()

    while frontier:
        frontier.sort(key=lambda x: x[1])  # Sort by f(n)
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=" ")
        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return

        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost
            f_cost = new_g_cost + heuristic[neighbor]

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))

    print("\nGoal not found")


# Run A* Search
print("\nFollowing is the A* Search:")
a_star(graph, 'A', 'I')
