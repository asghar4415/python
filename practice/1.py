# pp 1

# que 1

class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.rows = max(pos[0] for pos in grid) + 1
        self.cols = max(pos[1] for pos in grid) + 1


class GoalBasedAgent:
    def __init__(self, environment, start, goal):
        self.env = environment
        self.start = start
        self.goal = goal

    def bfs(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = []
        visited = set()
        parent = {}

        queue.append(self.start)
        visited.add(self.start)

        while queue:
            current = queue.pop(0)
            if current == self.goal:
                break
            for d in directions:
                nr, nc = current[0] + d[0], current[1] + d[1]
                if 0 <= nr < self.env.rows and 0 <= nc < self.env.cols:
                    if self.env.grid.get((nr, nc)) != '#' and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        parent[(nr, nc)] = current

        # Reconstruct path
        path = []
        node = self.goal
        while node != self.start:
            path.append(node)
            node = parent[node]
        path.append(self.start)
        path.reverse()
        return path

    def run(self):
        path = self.bfs()
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

environment = Environment(grid)
agent = GoalBasedAgent(environment, start, goal)
agent.run()
