import matplotlib.pyplot as plt
import numpy as np


# import pandas as pd


def print_demo1():
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
    # 创建figure
    plt.figure(figsize=(8, 4))
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.plot(x, y * y)


def print_demo3():
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
    x = np.linspace(-3, 3, 50)  # 50为生成的样本数
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure(num=1, figsize=(8, 5))  # 定义编号为1 大小为(8,5)
    plt.plot(x, y1, color='red', linewidth=2, linestyle='--')  # 颜色为红色，线宽度为2，线风格为--
    plt.plot(x, y2)  # 进行画图
    plt.show()  # 显示图


def print_demo():
    print_demo1()
    print_demo2()
    print_demo3()
    print_demo4()
