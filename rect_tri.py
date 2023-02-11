import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as stat
import matplotlib.animation as animation
import get_distances as gd
import pent_tri as pt
from scipy.optimize import minimize


def animate(i, xs, ys, ax, sensors):
    x0 = np.array([20, 20])
    dist, ss = gd.read_serial()
    pos = minimize(pt.residuals, x0, args=(ss, dist))["x"]
    print(pos)
    print(round(sum(pos)%77))
    xs.append(pos[0])
    ys.append(pos[1])

    xs = xs[-20:]
    ys = ys[-20:]

    ax.clear()
    ax.scatter(pos[0], pos[1])
    for x in range(len(ss)):
        i = sensors[x]
        ax.scatter(i[0],i[1])
        ax.annotate(dist[x], i)
    ax.set_xlim(-20,50)
    ax.set_ylim(-30,80)

def main():
    sensors = [[-17,33],[45,39],[36,0],[0,0],[8,69]]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    xs = []
    ys = []
    
    for i in sensors:
        ax.scatter(i[0],i[1])

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, ax, sensors), interval=1000)
    ax.set_xlim(-20,50)
    ax.set_ylim(-30,80)
    plt.show()

if __name__ == "__main__":
    main()