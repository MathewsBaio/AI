import random

def f(x):
    # y = 03x + 0.2
    return 0.3*x + 0.2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = self._get_label()

    def _get_label(self):
        # Se o ponto está acima da linha (y > x), label 1, senão -1
        return 1 if self.y > self.x else -1

    def debug(self):
        print(f"label: {self.label} x {self.x} y {self.y}")