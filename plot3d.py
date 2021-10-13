# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 16:14
# @Author  : Laobai
# @File    : plot3d.py


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot3d_demo1():
    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)

    # Z是高度值
    Z = np.sin(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))  # stride表示跨度
    # ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
    # ax.set_zlim(-2,2)
    plt.show()


plot3d_demo1()
