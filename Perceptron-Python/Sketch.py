from Perceptron import Perceptron
from Point import Point

percep = Perceptron()

inputs = [-1,0.5]

chute = percep.guess(inputs)

print (f"O chute do perceptron foi: {chute}")


ponto = Point(4,2)
ponto.debug()