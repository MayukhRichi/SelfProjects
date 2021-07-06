import math
import matplotlib.pyplot as plt
from tkinter import filedialog


def theta(p):
    if p[0] == start_x:
        k = math.pi / 2
    else:
        k = math.atan((p[1] - start_y) / (p[0] - start_x))
    if k < 0:
        k = math.pi + k
    return k


def theta_sort(x):
    less = []
    more = []
    if len(x) > 1:
        pivot = x[0]
        for i in range(1, len(x)):
            if theta(x[i]) < theta(pivot):
                less.append(x[i])
            elif theta(x[i]) > theta(pivot):
                more.append(x[i])
            elif math.pow((x[i][0] - start_x), 2) + math.pow((x[i][1] - start_y), 2) > math.pow((x[0][0] - start_x), 2) + math.pow((x[0][1] - start_y), 2):
                pivot = x[i]
        return theta_sort(less) + [pivot] + theta_sort(more)
    else:
        return x


def is_ccw(i):
    if (points[i][0] * (points[i+1][1] - points[i+2][1]) - points[i][1] * (points[i+1][0] - points[i+2][0]) + points[i+1][0] * points[i+2][1] - points[i+1][1] * points[i+2][0]) < 0:
        return False
    else:
        return True


def draw_hull():
    global points
    points = [pt for pt in points if pt != (start_x, start_y)]
    points = theta_sort(points)
    points.insert(0, (start_x, start_y))
    i = 1
    while i < len(points) - 2:
        if is_ccw(i):
            i += 1
        else:
            points.pop(i + 1)
            i -= 1
    for pt in points:
        plt.scatter(pt[0], pt[1], s=25, color='r')
        plt.annotate('({},{})'.format(pt[0], pt[1]), xy=(pt[0], pt[1]), color='r', fontsize=15)
    plt.plot([pt[0] for pt in points] + [start_x], [pt[1] for pt in points] + [start_y], color='r', alpha=0.2)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.axhline(y=0, color='k', alpha=0.2)
ax.axvline(x=0, color='k', alpha=0.2)
ax.grid(alpha=0.4)
plt.title('C O N V E X - H U L L', fontname='monospace', fontsize=22, color='k', alpha=0.6)
points = []
start_x = 'null'
start_y = 'null'
print("INPUT POINTS USING COMMA AS DELIMITER & USE ANY INVALIDS TO STOP ...")
while True:
    try:
        (a, b) = eval(input(">> "))
        points.append((a, b))
        if start_y == 'null':
            start_x = a
            start_y = b
        elif (b < start_y) or (b == start_y and a < start_x):
            start_x = a
            start_y = b
        plt.scatter(a, b, s=25, color='g')
        plt.annotate('({},{})'.format(a, b), xy=(a, b), color='g', fontsize=15)
    except Exception:
        break
if start_x != 'null':
    draw_hull()
name = filedialog.asksaveasfilename(defaultextension='.pdf')  # from tkinter
plt.savefig(name)