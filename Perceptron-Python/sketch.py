import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from perceptron import Perceptron
from point import Point

perceptron = Perceptron(2)
points = [Point(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(100)]
training_index = [0]

fig, ax = plt.subplots(figsize=(6, 6))

def draw_line():
    # Desenha a linha diagonal de (-1,-1) a (1,1) que representa x = y
    ax.plot([-1, 1], [-1, 1], 'k-', linewidth=2, label="Linha x=y")

def train_single_point():
    pt = points[training_index[0]]
    inputs = [pt.x, pt.y]
    perceptron.train(inputs, pt.label)
    training_index[0] = (training_index[0] + 1) % len(points)

def draw(frame):
    ax.clear()
    # Define o intervalo fixo de -1 a 1
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    # Adiciona linhas de grade e eixos centrais para clareza
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', lw=0.5)

    # Desenhar pontos
    for pt in points:
        face_color = 'black' if pt.label == 1 else 'white'
        ax.plot(pt.x, pt.y, 'o', color='black', markerfacecolor=face_color,
                markersize=10, markeredgewidth=1, zorder=2)

        guess = perceptron.guess([pt.x, pt.y])
        color = 'green' if guess == pt.label else 'red'
        ax.plot(pt.x, pt.y, 'o', color=color, markersize=5, zorder=3)

    draw_line()
    train_single_point()
    ax.set_title("Perceptron: Classificação no intervalo [-1, 1]")

ani = animation.FuncAnimation(fig, draw, interval=50, cache_frame_data=False)
plt.show()