# this is a program for Simple Reflex Agent

# the scenario is a room with a door and a light switch and the agent is supposed to turn on the light switch every time it detects a dark room.

# the agent has a simple rule: if the room is dark, turn on the light switch.

import random


class SimpleReflexAgent:

    states = ['dark', 'light']

    def __init__(self):
        self.room = random.choice(self.states)

    def scanroom(self):
        return self.room

    def handle_action(self):
        if self.room == 'dark':
            print('The room is dark. Turning on the light switch.')
            self.room = 'light'  # Update the actual room state
        else:
            print('The room is already light.')

    def run(self):
        while True:
            self.handle_action()
            input('Press Enter to continue...')


if __name__ == '__main__':

    agent = SimpleReflexAgent()
    agent.run()
