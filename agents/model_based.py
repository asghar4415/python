# this is a program for a Model-Based Reflex Agent

# A robot vacuum cleaner operates in a 2x2 grid room. Each cell can be clean or dirty. The robot can move up, down, left, right, and perform the action clean. The robot does not see the full grid but remembers where it has cleaned using a model of the environment.


class Environment:
    def __init__(self):
        self.grid = {
            (0, 0): 'dirty', (0, 1): 'dirty',
            (1, 0): 'dirty', (1, 1): 'dirty'
        }

    def sense(self, position):
        return self.grid[position]

    def clean(self, position):
        self.grid[position] = 'clean'

    def is_all_clean(self):
        return all(state == 'clean' for state in self.grid.values())


class ModelBasedAgent:
    def __init__(self):
        self.position = (0, 0)
        self.model = {
            (0, 0): 'unknown', (0, 1): 'unknown',
            (1, 0): 'unknown', (1, 1): 'unknown'
        }
        self.visited = []

    def perceive_and_update(self, env):
        current_state = env.sense(self.position)
        self.model[self.position] = current_state

    def decide_action(self):
        if self.model[self.position] == 'dirty':
            return 'clean'
        else:
            for pos in self.model:
                if self.model[pos] != 'clean':
                    return self.move_towards(pos)
            return 'done'

    def move_towards(self, target):
        x, y = self.position
        tx, ty = target
        if x < tx:
            self.position = (x + 1, y)
        elif x > tx:
            self.position = (x - 1, y)
        elif y < ty:
            self.position = (x, y + 1)
        elif y > ty:
            self.position = (x, y - 1)
        return 'move'

    def act(self, action, env):
        if action == 'clean':
            env.clean(self.position)
        if self.position not in self.visited:
            self.visited.append(self.position)


# Run simulation
env = Environment()
agent = ModelBasedAgent()

while not env.is_all_clean():
    agent.perceive_and_update(env)
    action = agent.decide_action()
    if action == 'done':
        break
    agent.act(action, env)

print("Final Agent Model:", agent.model)
print("Environment State:", env.grid)
