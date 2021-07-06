import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animate
import matplotlib.transforms as mtrans
from tkinter import filedialog

print("\nTo input | x1  x2 | matrix input x1, y1, x2, y2 >>> \n         | y1  y2 |\n")
arr = re.split('[ ,;]+', input('INPUT >>> '))
coord = [eval(each_str) for each_str in arr]
coord = coord[:4]
(a, b) = eval(input("INPUT a point using comma as delimiter >>> "))
fig = plt.figure()
ax = fig.add_subplot(111)
xx, yy = np.meshgrid(np.linspace(-10, 10, 21), np.linspace(-10, 10, 21))  # dots in the diagram


def update(frame):
    ax.clear()
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.axhline(y=0, color='k', alpha=0.1)
    ax.axvline(x=0, color='k', alpha=0.1)
    ax.set_xticks(np.linspace(-10, 10, 21))
    ax.set_yticks(np.linspace(-10, 10, 21))
    ax.grid(alpha=0.2)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('Old X Axis', fontname='DejaVu Sans', fontsize=15, color='k', alpha=0.3)
    plt.ylabel('Old Y Axis', fontname='DejaVu Sans', fontsize=15, color='k', alpha=0.3)
    c1 = 0
    c2 = 0
    c3 = 1
    if frame <= 25:
        c0 = (1 + frame * (coord[0] - 1) / 25)
    elif frame <= 50:
        c0 = coord[0]
        c3 = (1 + (frame - 25) * (coord[3] - 1) / 25)
    elif frame <= 75:
        c0 = coord[0]
        c3 = coord[3]
        c1 = ((frame - 50) * (coord[1]) / 25)
    elif frame <= 100:
        c0 = coord[0]
        c3 = coord[3]
        c1 = coord[1]
        c2 = ((frame - 75) * (coord[2]) / 25)
    else:
        c0 = coord[0]
        c3 = coord[3]
        c1 = coord[1]
        c2 = coord[2]
    # updating old matrix
    matrix = np.array([[c0, c2, 0], [c1, c3, 0], [0, 0, 1]])
    # updating old diagram
    plt.scatter(xx.flat, yy.flat, s=10, alpha=0.3, transform=mtrans.Affine2D(matrix) + ax.transData, color='g')
    plt.plot([0, 0, 0], [-10, 0, 10], transform=mtrans.Affine2D(matrix) + ax.transData, color='g', alpha=0.5)
    plt.plot([-10, 0, 10], [0, 0, 0], transform=mtrans.Affine2D(matrix) + ax.transData, color='g', alpha=0.5)
    plt.plot([a, 0, 0], [0, 0, b], transform=mtrans.Affine2D(matrix) + ax.transData, color='b', alpha=0.8)
    plt.plot([a, a, 0], [0, b, b], transform=mtrans.Affine2D(matrix) + ax.transData, color='b', linestyle='dashed',
             alpha=0.5)
    plt.scatter(a, b, s=15, transform=mtrans.Affine2D(matrix) + ax.transData, color='r')
    plt.annotate('({},{})'.format(round((a * c0 + b * c2), 2), round((a * c1 + b * c3), 2)),
                 xy=((a * c0 + b * c2), (a * c1 + b * c3)),
                 color='r', alpha=0.8, fontsize=12)
    plt.title('|  ' + str(round(c0, 1)) + '   ' + str(round(c2, 1)) + '  |\n|  ' + str(round(c1, 1)) + '   ' + str(
        round(c3, 1)) + '  |',
              fontsize=15, color='b', alpha=0.8)
    if frame > 100:
        plt.figtext(0.22, 0.85, "made by\nMAYUKH-RICHI",
                    horizontalalignment='center', verticalalignment='center', wrap=True,
                    fontname='DejaVu Sans', fontsize=8, style='italic', color='r', alpha=0.3)
        plt.figtext(0, 1, "New Y Axis",
                    transform=mtrans.Affine2D(matrix) + ax.transData,
                    horizontalalignment='center', verticalalignment='center', wrap=True,
                    fontname='DejaVu Sans', fontsize=12, color='g', alpha=0.3)
        plt.figtext(1, 0, "New X Axis",
                    transform=mtrans.Affine2D(matrix) + ax.transData,
                    horizontalalignment='center', verticalalignment='center', wrap=True,
                    fontname='DejaVu Sans', fontsize=12, color='g', alpha=0.3)


matrixAnimate = animate.FuncAnimation(fig, update, frames=105, interval=33.33, repeat=False)  # 30 fps
# use <<< print(matplotlib.animation.writers.list()) >>> to check the writers already installed
plt.rcParams['animation.ffmpeg_path'] = 'C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe'
name = filedialog.asksaveasfilename(defaultextension='.mp4')  # from tkinter
matrixAnimate.save(name, writer=animate.FFMpegWriter())
