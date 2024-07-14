import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1
epochs = 10000

np.random.seed(1)
weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))

for epoch in range(epochs):
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    output = sigmoid(output_layer_input)

    error = y - output
    d_output = error * sigmoid_derivative(output)

    error_hidden_layer = d_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

test_input = np.array([[0, 0],
                       [0, 1],
                       [1, 0],
                       [1, 1]])
predicted_output = sigmoid(np.dot(sigmoid(np.dot(test_input, weights_input_hidden)), weights_hidden_output))

print("Input:")
print(test_input)
print("\nPredicted Output:")
print(predicted_output)