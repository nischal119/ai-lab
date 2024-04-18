class SimpleReflexAgent:
    def __init__(self, rules):
        self.rules = rules

    def perceive_and_act(self, percept):
        for condition, action in self.rules:
            if condition(percept):
                return action()  # Call the action function
        return self.default_action()

    def default_action(self):
        return "Do nothing"  # Default action if no rule matches


# Example usage:
def temperature_above_threshold(percept):
    return percept["temperature"] > 25


def turn_on_air_conditioner():
    return "Turn on the air conditioner"


def turn_off_air_conditioner():
    return "Turn off the air conditioner"


rules = [
    (temperature_above_threshold, turn_on_air_conditioner),
    (
        lambda percept: not temperature_above_threshold(percept),
        turn_off_air_conditioner,
    ),
]

agent = SimpleReflexAgent(rules)

# Example scenario
percept = {"temperature": 28}  # Percept indicating high temperature
action = agent.perceive_and_act(percept)
print("Action:", action)  # Output should be: Turn on the air conditioner
