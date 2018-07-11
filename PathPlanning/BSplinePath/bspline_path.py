#!/usr/bin/env python
"""

Path Plannting with B-Spline

author: Atsushi Sakai (@Atsushi_twi)

"""

import numpy as np

import matplotlib.pyplot as plt
import scipy.interpolate as si

# import sys
# sys.setrecursionlimit(1500)

from os.path import expanduser


# parameter
N = 3  # B Spline order


def bspline_planning(x, y, sn):
    t = range(len(x))
    x_tup = si.splrep(t, x, k=N)
    y_tup = si.splrep(t, y, k=N)

    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

    ipl_t = np.linspace(0.0, len(x) - 1, sn)
    rx = si.splev(ipl_t, x_list)        #error
    ry = si.splev(ipl_t, y_list)

    return rx, ry


def main():
    print(__file__ + " start!!")
    # way points

    home = expanduser("~")
    x = np.array([])
    y = np.array([])
    with open(home+"/Dropbox/180503_194829.txt") as file:
        for idx, line in enumerate(file):
            _str = line.split()
            if not len(_str) == 0:
                x = np.append(x, float(_str[0]))
                y = np.append(y, float(_str[1]))

    print(x.shape)

    print("debug")

    sn = 50  # sampling number
    rx, ry = bspline_planning(x, y, sn)

    print(rx.shape)

    # show results
    plt.plot(x, y, '-og', label="Waypoints")
    plt.plot(rx, ry, '-r', label="B-Spline path")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.show()


if __name__ == '__main__':
    main()
