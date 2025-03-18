graph = {'A': {'B': 2, 'C': 1},
         'B': {'D': 4, 'E': 3}, 'C': {'F': 1, 'G': 5}, 'D': {'H': 2}, 'E': {}, 'F': {'I': 6}, 'G': {}, 'H': {}, 'I': {}}

heuristic = {'A': 7, 'B': 6, 'C': 5, 'D': 4,
             'E': 7, 'F': 3, 'G': 6, 'H': 2, 'I': 0}


def greedy_bfs(graph, start, goal):
    frontier = [(start, heuristic[start])]
    visited = set()  # Set to keep track of visited nodes
    came_from = {start: None}
    # Sort frontier manually by heuristic value (ascending order)
    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue
        print(current_node, end=" ")

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with GBFS. Path: {path}")

            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic[neighbor]))

    print("\nGoal not found")


print("\nFollowing is the Greedy Best-First Search (GBFS):")
greedy_bfs(graph, 'A', 'I')
