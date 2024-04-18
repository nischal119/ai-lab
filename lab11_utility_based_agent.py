class UtilityBasedAgent:
    def __init__(self, goals, utility_function):
        self.goals = goals
        self.utility_function = utility_function

    def perceive_and_act(self, percept):
        best_action = None
        max_utility = float("-inf")

        for action in self.available_actions(percept):
            utility = self.expected_utility(action, percept)
            if utility > max_utility:
                max_utility = utility
                best_action = action

        return best_action

    def available_actions(self, percept):
        # Define the set of available actions based on the current percept
        return ["action1", "action2", "action3"]  # Example: List of actions

    def expected_utility(self, action, percept):
        # Compute the expected utility of taking the given action based on the current percept
        # This could involve considering the potential outcomes and their associated utilities
        return self.utility_function(action, percept)


# Example usage:
def utility_function(action, percept):
    # Define the utility function based on the agent's goals and preferences
    # This function could take into account factors such as the action's cost, the expected outcome, etc.
    return 0  # Placeholder utility value


goals = ["goal1", "goal2", "goal3"]  # Example: Agent's goals
agent = UtilityBasedAgent(goals, utility_function)

# Example scenario
percept = {"percept": "value"}  # Percept from the environment
action = agent.perceive_and_act(percept)
print("Selected action:", action)
