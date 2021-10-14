# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 13:50
# @Author  : Laobai
# @File    : demo2.py

# 高阶样条插值
import numpy as np
import pylab as pl
from scipy import interpolate

# 创建数据点集
x = np.linspace(0, 10, 11)
y = np.sin(x)

# 绘制数据点集
pl.figure(figsize=(12, 9))
pl.plot(x, y, 'ro')

# 根据kind创建interp1d对象f,计算插值结果
x_new = np.linspace(0, 10, 101)
for kind in ['nearest', 'zero', 'linear', 'quadratic']:
    f = interpolate.interp1d(x, y, kind=kind)
    y_new = f(x_new)
    pl.plot(x_new, y_new, label=str(kind))
pl.xticks(fontsize=20)
pl.yticks(fontsize=20)
pl.legend(loc='lower right')
pl.show()
