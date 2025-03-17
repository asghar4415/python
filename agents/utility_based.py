# this is a program for Simple Reflex Agent

# A smart thermostat controls the temperature in a house. The agent's goal is to maximize comfort while minimizing energy usage. It must decide between actions:

# Heat
# Cool
# Do Nothing
# The agent uses a utility function to assign a score to each action based on:

# How close the temperature is to the desired range (20°C to 24°C)
# Energy cost of heating/cooling.


class SmartThermostat:
    def __init__(self, current_temp):
        self.current_temp = current_temp
        self.desired_min = 20
        self.desired_max = 24

    def utility(self, temp, energy_cost):
        # Higher utility for comfort (closer to desired temp), lower for high energy cost
        comfort_score = max(
            0, 10 - abs((self.desired_min + self.desired_max)/2 - temp))
        utility_value = comfort_score - energy_cost
        return utility_value

    def decide_action(self):
        actions = {
            # temp after heating, energy cost
            'heat': (self.current_temp + 1, 2),
            # temp after cooling, energy cost
            'cool': (self.current_temp - 1, 2),
            'do_nothing': (self.current_temp, 0)    # temp unchanged, no cost
        }

        utilities = {}
        for action, (new_temp, cost) in actions.items():
            u = self.utility(new_temp, cost)
            utilities[action] = u
            print(f"Utility for {action}: {u}")

        best_action = max(utilities, key=utilities.get)
        print(f"Best action: {best_action}")
        return best_action


if __name__ == '__main__':

    agent = SmartThermostat(26)
    agent.decide_action()
