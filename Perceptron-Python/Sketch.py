import random 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from Point import Point

WIDTH, HEIGHT = 550, 550

points = [Point(random.uniform(-1,1), random.uniform(-1,1)) for _ in range(100)]

fig, ax = plt.subplots(figsize = (6,6))

def draw(frame):
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_facecolor("white")

    for pt in points: 
        px = pt._get_pixel_x(WIDTH)
        py = pt._get_pixel_y(HEIGHT)
        face_color = "purple" if pt.label == 1 else "green"
        ax.plot(px,py,'o', color="black", markerfacecolor=face_color,
                markersize=11, markeredgewidth=1)

ani = animation.FuncAnimation(fig, draw, interval=50)
plt.show()