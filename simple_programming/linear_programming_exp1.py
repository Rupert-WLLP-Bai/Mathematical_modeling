# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 20:14
# @Author  : Laobai
# @File    : linear_programming_exp1.py

# 规划问题
from scipy import optimize
import numpy as np


def exp1():
    """
    样例1 用scipy求解
    :return:
    """

    # 确定c.A,b,Aeq,beq
    c = np.array([2, 3, -5])
    A = np.array([[-2, 5, -1], [1, 3, 1]])  # 两层[]
    b = np.array([-10, 12])

    # the number of columns in A_eq must be equal to the size of c
    Aeq = np.array([[1, 1, 1]])  # 两层维度
    beq = np.array([7])

    # 求解
    res = optimize.linprog(-c, A, b, Aeq, beq)
    print(res)


exp1()
