
def dfs(graph, start, goal):
    visited = []
    stack = []

    visited.append(start)
    stack.append(start)

    while stack:
        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            break

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)


graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'],
    'D': ['H'], 'E': [], 'F': ['I'], 'G': [],
    'H': [], 'I': []
}
start = 'A'
goal = 'I'

dfs(graph, start, goal)
