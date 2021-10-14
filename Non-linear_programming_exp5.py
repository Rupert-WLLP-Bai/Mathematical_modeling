# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 10:08
# @Author  : Laobai
# @File    : Non-linear_programming_exp5.py

# 非线性规划样例5

# 定义表达式
import numpy as np
from scipy.optimize import minimize


def fun(_args):
    a, b, c, d = _args
    return lambda x: (a + x[0]) / (b + x[1]) - c * x[0] + d * x[2]


# 定义约束条件 分为eq和ineq eq表示等于0 ineq表示大于等于0
def con(_args):
    x1min, x1max, x2min, x2max, x3min, x3max = _args
    _cons = ({'type': 'ineq', 'fun': lambda x: x[0] - x1min},
             {'type': 'ineq', 'fun': lambda x: -x[0] + x1max},
             {'type': 'ineq', 'fun': lambda x: x[1] - x2min},
             {'type': 'ineq', 'fun': lambda x: -x[1] + x2max},
             {'type': 'ineq', 'fun': lambda x: x[2] - x3min},
             {'type': 'ineq', 'fun': lambda x: -x[2] + x3max})
    return _cons


if __name__ == '__main__':
    # 定义常量值
    args = (2, 1, 3, 4)
    # 设置约束
    args1 = (0.1, 0.9, 0.1, 0.9, 0.1, 0.9)
    cons = con(args1)
    # 设置初始猜测值
    x0 = np.asarray((0.5, 0.5, 0.5))
    # 解决问题
    # noinspection PyTypeChecker
    res = minimize(fun(args), x0, method='SLSQP', constraints=cons)
    # 输出结果
    print(res.fun)
    print(res.success)
    print(res.x)
