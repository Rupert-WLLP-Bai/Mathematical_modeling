# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 14:41
# @Author  : Laobai
# @File    : demo4.py

# 二维插值的三维图
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from scipy import interpolate

# 设置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


def func(_x, _y):
    return (_x + _y) * np.exp(-5.0 * (_x ** 2 + _y ** 2))


# xy轴分割为20*20的网格
x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1 - 20)
x, y = np.meshgrid(x, y)
fvals = func(x, y)

# 画分图1
plt.figure(figsize=(12, 8))
ax = plt.subplot(1, 2, 1, projection='3d')
# rstride行跨度，cstride列跨度
surf = ax.plot_surface(x, y, fvals, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'), linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
# 颜色条标注
plt.colorbar(surf, shrink=0.5, aspect=5)
# 二维插值
newfunc = interpolate.interp2d(x, y, fvals, kind='cubic')
# 计算100*100网格上的插值
x_new = np.linspace(-1, 1, 100)
y_new = np.linspace(-1, 1, 100)
f_new = newfunc(x_new, y_new)
x_new, y_new = np.meshgrid(x_new, y_new)
ax2 = plt.subplot(1, 2, 2, projection='3d')
surf2 = ax.plot_surface(x_new, y_new, f_new, rstride=1, cstride=1, cmap=pl.get_cmap('rainbow'), linewidth=0.5)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('f(x,y)')
plt.colorbar(surf2, shrink=0.5, aspect=5)  # 标注
# 画图
plt.show()
