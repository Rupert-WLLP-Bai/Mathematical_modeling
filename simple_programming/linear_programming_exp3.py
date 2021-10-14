# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 0:29
# @Author  : Laobai
# @File    : linear_programming_exp3.py

# 运输问题求解

# 数据
import pulp
import numpy as np

# 可以考虑封装成一个函数
fruits_name = np.array(['小麦', '玉米', '水果', '蔬菜'])  # 水果类型
place_name = np.array(['地块1', '地块2', '地块3', '地块4', '地块5', '地块6'])  # 地块

costs = np.array([[500, 530, 630, 1000, 800, 700],
                  [800, 700, 600, 950, 900, 930],
                  [1000, 960, 840, 650, 600, 700],
                  [1200, 1040, 980, 860, 880, 780]])  # 收益
max_plants = np.array([76, 88, 96, 40])  # 每种水果的最大种植量
max_size = np.array([42, 56, 44, 39, 60, 59])  # 地块最大面积

# 定义问题
Problem = pulp.LpProblem("种植最大收益问题", sense=pulp.LpMaximize)  # 求最大值
# 数据表的行列数
row = len(costs)  # 行
col = len(costs[0])  # 列
# 定义决策变量 从x{i}{j}中遍历加入 最小值为0 离散型变量
var = np.array([[pulp.LpVariable(f'x{i}{j}', lowBound=0, cat=pulp.LpInteger) for j in range(col)] for i in range(row)])
# 转为一维 设置目标函数
Problem += pulp.lpDot(var.flatten(), costs.flatten())
# 加入约束
for i in range(row):
    Problem += (pulp.lpSum(var[i]) <= max_plants[i])
for j in range(col):
    Problem += (pulp.lpSum((var[i][j] for i in range(row))) <= max_size[j])
# 求解
Problem.solve()
# 打印结果
print(Problem)  # 输出问题设定参数和条件
print("优化状态:", pulp.LpStatus[Problem.status])
for v in Problem.variables():
    print(v.name, "=", v.varValue)
print("最优收益 = ", pulp.value(Problem.objective))
