maze = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 1, 1]
]

directions = [(0, 1), (1, 0)]  # Right and Down


def create_graph(maze):
    graph = {}
    rows = len(maze)
    col = len(maze[0])

    for i in range(rows):
        for j in range(col):
            if maze[i][j] == 1:
                neighbors = []
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < col and maze[nx][ny] == 1:
                        neighbors.append((nx, ny))
                graph[(i, j)] = neighbors  # Moved outside inner loop
    return graph


def bfs(graph, start, goal):
    visited = []
    queue = []

    queue.append(start)
    visited.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=", ")

        if goal == node:
            print(" -> Goal is found")
            return

        for neighbour in graph.get(node, []):  # use .get() to avoid KeyError
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)


start = (0, 0)
goal = (2, 2)

graph = create_graph(maze)
# print("Graph:", graph)
bfs(graph, start, goal)
