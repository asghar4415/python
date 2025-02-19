def dls(graph, start, goal, depth_limit):
    visited = []

    def dfs(node, depth):
        if depth > depth_limit:
            return False  # Stop if depth exceeds limit
        visited.append(node)
        if node == goal:
            print(f"Goal found with DLS. Path: {visited}")
            return True
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, depth + 1):  # Recursive DFS with depth
                    return True
        visited.pop()  # Backtrack if not found
        return False

    if not dfs(start, 0):
        print("Goal was not found within the depth limit.")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Test cases
dls(graph, 'A', 'F', 2)  # Should find the goal
dls(graph, 'A', 'F', 1)  # Should print "Goal was not found within the depth limit."
