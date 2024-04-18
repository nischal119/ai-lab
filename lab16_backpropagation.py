import numpy as np


class MLP:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.zeros(hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.zeros(output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        # Forward pass
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output_input = (
            np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        )
        self.output_output = self.sigmoid(self.output_input)
        return self.output_output

    def backward(self, inputs, targets):
        # Backward pass
        output_error = targets - self.output_output
        output_delta = output_error * self.sigmoid_derivative(self.output_output)

        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)

        # Update weights and biases
        self.weights_hidden_output += self.learning_rate * np.dot(
            self.hidden_output.T, output_delta
        )
        self.bias_output += self.learning_rate * np.sum(output_delta, axis=0)
        self.weights_input_hidden += self.learning_rate * np.dot(inputs.T, hidden_delta)
        self.bias_hidden += self.learning_rate * np.sum(hidden_delta, axis=0)

    def train(self, inputs, targets, epochs):
        for _ in range(epochs):
            for i in range(len(inputs)):
                output = self.forward(
                    inputs[i : i + 1]
                )  # Use slicing to get a row vector
                self.backward(
                    inputs[i : i + 1], targets[i : i + 1]
                )  # Similarly, use slicing for targets


# Example usage:
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])

mlp = MLP(input_size=2, hidden_size=2, output_size=1)
mlp.train(inputs, targets, epochs=1000)

# Test the trained MLP
for i in range(len(inputs)):
    print(
        "Input:",
        inputs[i],
        "Target:",
        targets[i],
        "Predicted output:",
        mlp.forward(inputs[i : i + 1]),
    )
