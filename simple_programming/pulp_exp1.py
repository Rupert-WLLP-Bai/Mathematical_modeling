# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 0:28
# @Author  : Laobai
# @File    : pulp_exp1.py

import pulp

# 1. 建立问题
AlloyModel = pulp.LpProblem("钢材生产问题", pulp.LpMinimize)
# 2. 建立变量
material = ['废料1', '废料2', '废料3', '废料4', '镍', '铬', '钼']
mass = pulp.LpVariable.dicts("原料", material, lowBound=0, cat='Continuous')
# 3. 设置目标函数
cost = {
    '废料1': 16,
    '废料2': 10,
    '废料3': 8,
    '废料4': 9,
    '镍': 48,
    '铬': 60,
    '钼': 53}
AlloyModel += pulp.lpSum([cost[item] * mass[item] for item in material]), "总生产成本"
# # 4. 施加约束
carbonPercent = {
    '废料1': 0.8,
    '废料2': 0.7,
    '废料3': 0.85,
    '废料4': 0.4,
    '镍': 0,
    '铬': 0,
    '钼': 0}
NiPercent = {
    '废料1': 18,
    '废料2': 3.2,
    '废料3': 0,
    '废料4': 0,
    '镍': 100,
    '铬': 0,
    '钼': 0}
CrPercent = {
    '废料1': 12,
    '废料2': 1.1,
    '废料3': 0,
    '废料4': 0,
    '镍': 0,
    '铬': 100,
    '钼': 0}
MoPercent = {
    '废料1': 0,
    '废料2': 0.1,
    '废料3': 0,
    '废料4': 0,
    '镍': 0,
    '铬': 0,
    '钼': 100}
AlloyModel += pulp.lpSum([mass[item] for item in material]) == 1000, "质量约束"
AlloyModel += pulp.lpSum([carbonPercent[item] * mass[item] for item in material]) >= 0.65 * 1000, "碳最小占比"
AlloyModel += pulp.lpSum([carbonPercent[item] * mass[item] for item in material]) <= 0.75 * 1000, "碳最大占比"
AlloyModel += pulp.lpSum([NiPercent[item] * mass[item] for item in material]) >= 3.0 * 1000, "镍最小占比"
AlloyModel += pulp.lpSum([NiPercent[item] * mass[item] for item in material]) <= 3.5 * 1000, "镍最大占比"
AlloyModel += pulp.lpSum([CrPercent[item] * mass[item] for item in material]) >= 1.0 * 1000, "铬最小占比"
AlloyModel += pulp.lpSum([CrPercent[item] * mass[item] for item in material]) <= 1.2 * 1000, "铬最大占比"
AlloyModel += pulp.lpSum([MoPercent[item] * mass[item] for item in material]) >= 1.1 * 1000, "钼最小占比"
AlloyModel += pulp.lpSum([MoPercent[item] * mass[item] for item in material]) <= 1.3 * 1000, "钼最大占比"
AlloyModel += mass['废料1'] <= 75, "废料1可用量"
AlloyModel += mass['废料2'] <= 250, "废料2可用量"
# 5. 求解
AlloyModel.solve()
# 6. 打印结果
print(AlloyModel)  # 输出问题设定参数和条件
print("优化状态:", pulp.LpStatus[AlloyModel.status])
for v in AlloyModel.variables():
    print(v.name, "=", v.varValue)
print("最优总成本 = ", pulp.value(AlloyModel.objective))
