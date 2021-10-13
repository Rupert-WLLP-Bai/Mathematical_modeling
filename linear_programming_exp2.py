# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 22:03
# @Author  : Laobai
# @File    : linear_programming_exp2.py

from scipy import optimize
import numpy as np
import pulp


def exp2_by_scipy():
    """
    用scipy解决线性规划
    :return:
    """
    c = np.array([2, 3, 1])
    A = np.array([[-1, -4, -2], [-3, -2, 0]])
    b = np.array([-8, -6])
    Aeq = np.array([[1, 2, 4]])
    beq = np.array([101])
    # solve
    res = optimize.linprog(-c, A, b, Aeq, beq)
    print(res)
    print("---------------\nsolved by scipy\n---------------")


def exp2_by_pulp():
    """
    用pulp解决线性规划
    :return:
    """
    # 定义问题
    MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMaximize)
    # 决策变量
    # Continuous连续 Integer离散 lowBound和upBound默认为无穷
    x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
    x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')
    x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')
    MyProbLP += 2 * x1 + 3 * x2 + x3  # 设置目标函数
    MyProbLP += (x1 + 4 * x2 + 2 * x3 >= 8)  # 不等式约束
    MyProbLP += (3 * x1 + 2 * x2 >= 6)  # 不等式约束
    MyProbLP += (x1 + 2 * x2 + 4 * x3 == 101)  # 等式约束
    # 求解
    MyProbLP.solve()
    # 输出结果
    print("Status:", pulp.LpStatus[MyProbLP.status])  # 输出求解状态
    for v in MyProbLP.variables():
        print(v.name, "=", v.varValue)  # 输出每个变量的最优值
    print("F(x) = ", pulp.value(MyProbLP.objective))  # 输出最优解的目标函数值
    print("solved by pulp")


exp2_by_scipy()
exp2_by_pulp()
