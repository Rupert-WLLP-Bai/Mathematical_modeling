# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 9:45
# @Author  : Laobai
# @File    : Non-linear_programming_exp4.py

# 求x+1/x的最小值
from scipy.optimize import minimize
import numpy as np


def fun(args_):
    a = args_
    return lambda x: a / x[0] + x[0]


if __name__ == "__main__":
    args = 1
    x0 = np.asarray(2)  # 初始猜测值
    res = minimize(fun(args), x0, method='SLSQP')
    print(res.fun)
    print(res.success)
    print(res.x)
