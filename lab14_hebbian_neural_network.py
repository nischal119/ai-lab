import numpy as np


class HebbianNetwork:
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(
            input_size, output_size
        )  # Initialize synaptic weights

    def train(self, input_pattern):
        # Compute the activation of each neuron
        activation = np.dot(input_pattern, self.weights)

        # Update synaptic weights using the Hebbian learning rule
        self.weights += np.outer(input_pattern, activation)


# Example usage:
input_pattern = np.array([0.1, 0.2, 0.5])  # Example input pattern
network = HebbianNetwork(input_size=len(input_pattern), output_size=3)

# Train the network with the input pattern
network.train(input_pattern)

# Example scenario: Present another input pattern and train the network again
input_pattern2 = np.array([0.3, 0.4, 0.6])
network.train(input_pattern2)

# After training, the network's synaptic weights are updated to capture the input patterns' correlations
print("Updated synaptic weights:")
print(network.weights)
