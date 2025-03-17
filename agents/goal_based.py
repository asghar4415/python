# this is a program for a Goal-Based Agent

# A delivery robot operates in a 5x5 warehouse grid. It must deliver a package from its starting location to a specific goal location (delivery point). The robot can move up, down, left, right and must avoid obstacles (blocked cells). The robot has a goal: reach the delivery point as efficiently as possible.


class Warehouse:
    def __init__(self):
        self.grid_size = 5
        self.obstacles = {(1, 2), (2, 2), (3, 1)}  # Blocked cells
        self.start = (0, 0)
        self.goal = (4, 4)

    def is_valid(self, position):
        x, y = position
        return (0 <= x < self.grid_size and
                0 <= y < self.grid_size and
                position not in self.obstacles)


class GoalBasedAgent:
    def __init__(self, env):
        self.env = env
        self.position = env.start
        self.goal = env.goal
        self.path = []

    def bfs_path_to_goal(self):
        visited = []
        queue = []

        queue.append((self.position, [self.position]))

        while queue:
            current_pos, path = queue.pop(0)

            if current_pos in visited:
                continue
            visited.append(current_pos)

            if current_pos == self.goal:
                self.path = path
                return

        # Possible moves
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_pos = (current_pos[0] + dx, current_pos[1] + dy)
                if self.env.is_valid(next_pos) and next_pos not in visited:
                    queue.append((next_pos, path + [next_pos]))

    def move_to_goal(self):
        self.bfs_path_to_goal()
        print(f"Path to goal: {self.path}")
        for step in self.path[1:]:  # Skip the start position
            self.position = step
            print(f"Moved to {self.position}")
        print("Goal reached!")


# Run the simulation
env = Warehouse()
agent = GoalBasedAgent(env)
agent.move_to_goal()
