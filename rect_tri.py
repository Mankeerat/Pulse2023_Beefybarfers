import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as stat
import matplotlib.animation as animation
import get_distances as gd

def getcoords(a,b,c,d,x,y):
    a_pos = (0,y)
    b_pos = (x,y)
    c_pos = (x,0)
    d_pos = (0,0)

    ab = get_intersections(a_pos,b_pos,a,b)
    dc = get_intersections(d_pos,c_pos,d,c)
    bc = get_intersections(b_pos,c_pos,b,c)
    ac = get_intersections(a_pos,c_pos,a,c)

    all = [ab[0],ab[1],dc[0],dc[1],bc[0],bc[1],ac[0],ac[1]]
    return(stat.mode(all))

def plot_circles(a,b,c,d,x,y):
    a_pos = (0,y)
    b_pos = (x,y)
    c_pos = (x,0)
    d_pos = (0,0)
    # Plot the circles
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.set_aspect(1)
    ax.add_patch(plt.Circle(a_pos, a, fill=False, color='r'))
    ax.add_patch(plt.Circle(b_pos, b, fill=False, color='g'))
    ax.add_patch(plt.Circle(c_pos, c, fill=False, color='b'))
    ax.add_patch(plt.Circle(d_pos, d, fill=False, color='y'))
    ax.set_xlim(-1, x+1)
    ax.set_ylim(-1, y+1)
    plt.show()

def get_intersections(c1, c2, r0, r1):
    x0,y0 = c1
    x1,y1 = c2
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        
        return ((round(x3), round(y3)), (round(x4), round(y4)))
    
def animate(i, xs, ys, ax, x, y):
    a,b,c,d = gd.read_serial()
    # dist = math.sqrt((x/2)**2 + (y/2)**2)
    # a, b, c, d = dist, dist, dist, dist
    pos = getcoords(float(a),float(b),float(c),float(d),x,y)
    xs.append(pos[0])
    ys.append(pos[1])

    xs = xs[-20:]
    ys = ys[-20:]

    ax.clear()
    ax.scatter(xs, ys)

    
def track_point(x,y):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, ax, x, y), interval=1000)
    plt.show()

def main():
    x = 20
    y = 10
    dist = math.sqrt((x/2)**2 + (y/2)**2)
    plot_circles(dist,dist,dist,dist,x,y)
    # print(getcoords(dist,dist,dist,dist,x,y))
    track_point(x,y)

if __name__ == "__main__":
    main()