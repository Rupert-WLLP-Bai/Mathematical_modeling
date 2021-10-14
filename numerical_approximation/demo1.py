# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 13:28
# @Author  : Laobai
# @File    : demo1.py

# demo1
# 一维插值
# 线性插值与样条插值

import numpy as np
from numpy import pi as pi
import pylab as pl
from scipy import interpolate
import matplotlib.pyplot as plt

# 设置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

x = np.linspace(0, 2 * pi + pi / 4, 10)
y = np.sin(x)
x_new = np.linspace(0, 2 * pi + pi / 4, 100)
f_linear = interpolate.interp1d(x, y)
tck = interpolate.splrep(x, y)
y_bspline = interpolate.splev(x_new, tck)

# 可视化
plt.xlabel(u'安培/A')
plt.ylabel(u'伏特/V')
plt.plot(x, y, "o", label=u"原始数据")
plt.plot(x_new, f_linear(x_new), label=u"线性插值")
plt.plot(x_new, y_bspline, label=u"B-spline插值")
pl.legend()
pl.show()
