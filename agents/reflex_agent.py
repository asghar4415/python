# this is a program for Simple Reflex Agent

# the scenario is a room with a door and a light switch and the agent is supposed to turn on the light switch every time it detects a dark room.

# the agent has a simple rule: if the room is dark, turn on the light switch.

class environment:
    def __init__(self):
        self.grid = [
            'dirty', 'clean', 'dirty',
            'clean', 'dirty', 'clean',
            'dirty', 'clean', 'clean'
        ]

    def scan(self):
        return self.grid

    def clean(self, i):
        self.grid[i] = 'clean'


class SimpleReflexAgent:
    def __init__(self, environment):
        self.environment = environment
        self.grid = self.environment.scan()

    def scanroom(self):
        return self.grid

    def act(self):
        for i in range(9):
            if self.grid[i] == 'dirty':
                print('Vacuuming at position', i)
                self.environment.clean(i)

            else:
                print('Position', i, 'is already clean.')


if __name__ == '__main__':
    env = environment()
    agent = SimpleReflexAgent(env)
    agent.act()
    print('All positions are clean now.')
