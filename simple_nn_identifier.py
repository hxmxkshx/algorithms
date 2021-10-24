## Identifies the formula 2*(a+b) from just inputs and output matrices
import numpy as np

class Network:
	def __init__(self):
		np.random.seed(1)
		self.weights = 2 * np.random.random((2, 1)) - 1
	
	def train(self, inputs, outputs, num):
		for i in range(num):
			output = self.think(inputs)
			loss = outputs - output
			adjustment = 0.01 * np.dot(inputs.T, loss)
			self.weights += adjustment

	def think(self, inputs):
		return np.dot(inputs, self.weights)

network = Network()
inputs = np.array([[2, 3], [1, 1], [5, 2], [12, 3]])
outputs = np.array([[10, 4, 14, 30]]).T
network.train(inputs, outputs, 1000)
print(np.around(network.think(np.array([5, 7]))))