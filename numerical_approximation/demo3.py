# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 14:07
# @Author  : Laobai
# @File    : demo3.py

# 二维插值
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from scipy import interpolate

# import matplotlib as mpl
# 设置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


def func(_x, _y):
    return (_x + _y) * np.exp(-5.0 * (_x ** 2 + _y ** 2))


# x-y轴分为15*15的网格
x, y = np.mgrid[-1:1:15j, -1:1:15j]
# 计算每个网格点上的函数值
fvals = func(x, y)
# 三次样条二维插值
newfunc = interpolate.interp2d(x, y, fvals, kind='cubic')
# 计算1000*1000网格上插值
x_new = np.linspace(-1, 1, 1000)
y_new = np.linspace(-1, 1, 1000)
f_new = newfunc(x_new, y_new)

# 可视化
# 让imshow的参数interpolation设置为'nearest'方便比较插值处理
fig = plt.figure()
ax1 = fig.add_subplot(121)  # 分割成几个格子
im1 = ax1.imshow(fvals, extent=[-1, 1, -1, 1], cmap=pl.get_cmap('hot'), origin="lower")
plt.colorbar(im1)
plt.title("原始数据")

ax2 = fig.add_subplot(122)
im2 = ax2.imshow(f_new, extent=[-1, 1, -1, 1], cmap=pl.get_cmap('hot'), origin="lower")
plt.colorbar(im2)
plt.title("插值数据")

# 显示
plt.show()
