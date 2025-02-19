tree = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'],
    'D': ['H'], 'E': [], 'F': ['I'], 'G': [],
    'H': [], 'I': []
}

goal = 'I'
start = 'A'


def bfs(tree, start, goal):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            break

        for neighbour in tree[node]:  # Fixed the variable name
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(tree, start, goal)
