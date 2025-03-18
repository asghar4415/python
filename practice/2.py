# pp 1

# que 2

import heapq

# Heuristic function: Manhattan distance


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Generate neighbors


def get_neighbors(pos, grid, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for d in directions:
        nr, nc = pos[0] + d[0], pos[1] + d[1]
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid.get((nr, nc)) != '#':
                neighbors.append((nr, nc))
    return neighbors

# Greedy Best First Search


def gbfs(grid, start, goal):
    rows = max(pos[0] for pos in grid) + 1
    cols = max(pos[1] for pos in grid) + 1

    visited = set()
    parent = {}
    heap = []

    heapq.heappush(heap, (heuristic(start, goal), start))
    visited.add(start)

    while heap:
        _, current = heapq.heappop(heap)

        if current == goal:
            break

        for neighbor in get_neighbors(current, grid, rows, cols):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                heapq.heappush(heap, (heuristic(neighbor, goal), neighbor))

    # Reconstruct path
    if goal not in parent:
        print("No path found.")
        return

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    print("Path from start to goal:")
    for p in path:
        print(p)


# Grid as a dictionary
grid = {
    (0, 0): 'S', (0, 1): '.', (0, 2): '#', (0, 3): '.', (0, 4): 'K',
    (1, 0): '.', (1, 1): '#', (1, 2): '.', (1, 3): '.', (1, 4): '.',
    (2, 0): '.', (2, 1): '.', (2, 2): '.', (2, 3): '#', (2, 4): '.',
    (3, 0): '#', (3, 1): '.', (3, 2): '#', (3, 3): '.', (3, 4): '#',
    (4, 0): '.', (4, 1): '.', (4, 2): '.', (4, 3): '.', (4, 4): '.'
}

start = (0, 0)
goal = (0, 4)

gbfs(grid, start, goal)
