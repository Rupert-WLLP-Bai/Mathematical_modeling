# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 15:40
# @Author  : Laobai
# @File    : matplotlib_demo.py

import matplotlib.pyplot as plt
import numpy as np


def print_demo1():
    """
    创建x,y关系 并画图
    :return:
    """
    # np.linspace方法生成0~2pi的50个均匀分布的x
    x = np.linspace(0, 2 * np.pi, 50)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

    # 绘制多个图;
    plt.plot(x, y)
    plt.plot(x, y ** 3)
    plt.show()

    # 调整样式
    plt.plot(x, y, 'y*-')
    plt.plot(x, y ** 3, 'm--')
    plt.show()


def print_demo2():
    """
    创建figure
    :return:
    """
    # 创建figure
    plt.figure(figsize=(8, 4))
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.plot(x, y * y)


def print_demo3():
    """
    设置坐标轴刻度和范围，设置label图例
    :return:
    """
    plt.figure(figsize=(8, 4))
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.cos(x)
    plt.title("cos(x) & cos^2(x)")
    # 设置坐标轴刻度和范围
    plt.xlim(0, 2 * np.pi)
    plt.ylim(-1, 1)
    # label设置轴的名称
    plt.xlabel('X')
    plt.ylabel('Y')
    # 设置label
    plt.plot(x, y, label="cos(x)")
    plt.plot(x, y * y, label="cos^2(x)")
    plt.legend(loc='best')
    plt.show()


def print_demo4():
    """
    更改x,y轴的标签
    :return:
    """
    x = np.linspace(-3, 3, 100)  # 100为生成的样本数
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure(num=1, figsize=(8, 5))  # 定义编号为1 大小为(8,5)
    plt.plot(x, y1, color='red', linewidth=2, linestyle='--')  # 颜色为红色，线宽度为2，线风格为--
    plt.plot(x, y2)  # 进行画图
    plt.xlim(-1, 2)  # 设置x轴最值
    plt.ylim(-2, 3)  # 设置y轴最值
    plt.xlabel("I'm x")  # 设置x轴标签
    plt.ylabel("I'm y")  # 设置y轴标签
    new_ticks = np.linspace(-1, 2, 5)  # 小标从-1到2分为5个单位
    # print(new_ticks)
    # [-1.   -0.25  0.5   1.25  2.  ]
    plt.xticks(new_ticks)  # 进行替换新下标
    plt.yticks([-2, -1, 1, 2, ],
               [r'$really\ bad$', '$bad$', '$well$', '$really well$'])
    plt.show()  # 显示图


def print_demo5():
    """
    设置边框属性
    :return:
    """
    x = np.linspace(-3, 3, 50)  # 50为生成的样本数
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure(num=1, figsize=(8, 5))  # 定义编号为1 大小为(8,5)
    plt.plot(x, y1, color='red', linewidth=2, linestyle='--')  # 颜色为红色，线宽度为2，线风格为--
    plt.plot(x, y2)  # 进行画图

    plt.xlim(-1, 2)  # 设置x轴最值
    plt.ylim(-2, 3)  # 设置y轴最值
    plt.xlabel("I'm x")  # 设置x轴标签
    plt.ylabel("I'm y")  # 设置y轴标签

    new_ticks = np.linspace(-1, 2, 5)  # 小标从-1到2分为5个单位
    # print(new_ticks)
    # [-1.   -0.25  0.5   1.25  2.  ]
    plt.xticks(new_ticks)  # 进行替换新下标
    plt.yticks([-2, -1, 1, 2, ],
               [r'$really\ bad$', '$bad$', '$well$', '$really well$'])

    # 设置边框属性
    ax = plt.gca()  # gca=get current axis
    ax.spines['right'].set_color('none')  # 边框属性设置为none 不显示 'right'、'left'、'top'、'bottom'
    ax.spines['top'].set_color('none')
    plt.show()  # 显示图


def print_demo6():
    """
    移动坐标轴
    :return:
    """
    x = np.linspace(-3, 3, 50)  # 50为生成的样本数
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure(num=1, figsize=(8, 5))  # 定义编号为1 大小为(8,5)
    plt.plot(x, y1, color='red', linewidth=2, linestyle='--', label="y=2x+1")  # 颜色为红色，线宽度为2，线风格为--
    plt.plot(x, y2, label="y=x^2")  # 进行画图
    plt.legend(loc='best')  # 最佳位置
    plt.xlim(-1, 2)  # 设置x轴最值
    plt.ylim(-2, 3)  # 设置y轴最值
    plt.xlabel("I'm x")  # 设置x轴标签
    plt.ylabel("I'm y")  # 设置y轴标签

    new_ticks = np.linspace(-1, 2, 5)  # 小标从-1到2分为5个单位
    # print(new_ticks)
    # [-1.   -0.25  0.5   1.25  2.  ]
    plt.xticks(new_ticks)  # 进行替换新下标
    plt.yticks([-2, -1, 1, 2, ],
               [r'$really\ bad$', '$bad$', '$well$', '$really well$'])

    # 设置边框属性
    ax = plt.gca()  # gca=get current axis
    ax.spines['right'].set_color('none')  # 边框属性设置为none 不显示 'right'、'left'、'top'、'bottom'
    ax.spines['top'].set_color('none')

    # 移动坐标轴
    ax.xaxis.set_ticks_position('bottom')  # 使用xaxis.set_ticks_position设置x坐标刻度数字或名称的位置 所有属性为top、bottom、both、default、none
    ax.spines['bottom'].set_position(
        ('data', 0))  # 使用.spines设置边框x轴；使用.set_position设置边框位置，y=0位置 位置所有属性有outward、axes、data
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))  # 坐标中心点在(0,0)位置

    plt.show()  # 显示图


def print_demo7():
    """
    画折线图
    :return:
    """
    x1 = range(0, 10, 1)
    y1 = [10, 12, 14, 17, 20, 25, 30, 35, 37, 40]
    plt.plot(x1, y1, linewidth=3, color='g', marker='o', markerfacecolor='blue', markersize=1)
    plt.show()


def print_demo8():
    """
    随机条形图
    :return:
    """
    mean, sigma = 0, 1
    x = mean + sigma * np.random.randn(10000)
    plt.hist(x, 50)
    plt.show()


def print_demo():
    print_demo1()
    print_demo2()
    print_demo3()
    print_demo4()
    print_demo5()
    print_demo6()
    print_demo7()
    print_demo8()
    print("simple demo done")


def print_scatter_demo1(num):
    n = num
    x = np.random.normal(0, 1, n)  # 每一个点的X值
    y = np.random.normal(0, 1, n)  # 每一个点的Y值
    t = np.arctan2(y, x)  # arctan2返回给定的X和Y值的反正切值
    # scatter画散点图 size=10 颜色为t 透明度为50% 利用xticks函数来隐藏x坐标轴
    plt.scatter(x, y, s=10, c=t, alpha=0.5)
    plt.xlim(-1.5, 1.5)
    plt.xticks(())  # 忽略x_ticks
    plt.ylim(-1.5, 1.5)
    plt.yticks(())  # 忽略y_ticks
    plt.show()
    print("散点的个数为" + str(num))


def print_scatter_demo():
    print_scatter_demo1(2000)
    print("scatter demo done")


print_scatter_demo()
print_demo()
