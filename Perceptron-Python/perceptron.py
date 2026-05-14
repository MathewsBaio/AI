import random

class Perceptron:
    def __init__(self, num_weights):
        self.weights = [random.uniform(-1, 1) for _ in range(num_weights)]
        self.lr = 0.01 

    def guess(self, inputs):
        total = sum(inputs[i] * self.weights[i] for i in range(len(self.weights)))
        return self._sign(total)

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.lr

    def _sign(self, num):
        return 1 if num >= 0 else -1