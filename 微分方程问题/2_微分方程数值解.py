#!/usr/bin/env python
# coding: utf-8

# # 微分方程数值解

# ## 2.1 场线图与数值解

# 当ODE无法求得解析解时，可以用scipy中的intergrate.odeint求数值解来探索其解的部分性质，并辅以可视化，能直观的展现ODE解的函数表达

# 以如下一阶非线性ODE为例

# In[1]:


from scipy import integrate
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import *
plt.rcParams['font.sans-serif']=['Microsoft YaHei']


# In[2]:


x =sympy.symbols('x')
y=sympy.Function('y')
diffeq = Eq(y(x).diff(x),x-y(x)**2)
diffeq


# 先尝试用dsolve解决

# In[3]:


dsolve(diffeq)


# 现用odeint求其数值解
# > odeint()函数是scipy库中一个数值求解微分方程的函数
# > odeint()函数需要至少三个变量，第一个是微分方程函数，第二个是微分方程初值，第三个是微分的自变量

# In[4]:


def diff(y, x):
	return np.array(x-y**2)
	# dy/dx = x-y^2
# 给出自变量x的范围
x =np.linspace(0,10,100)
# 设定初值为0，此时y为一个数组
y = odeint(diff,0,x)
# 画图
plt.plot(x, y[:, 0])  # y数组（矩阵）的第一列，（因为维度相同，plt.plot(x, y)效果相同）
plt.grid()
plt.show()  


# **场线图的画法暂时没看懂**

# In[5]:


# 一个例子
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def diff(y, x):
	return np.array(x)
	# 上面定义的函数在odeint里面体现的就是dy/dx = x
x = np.linspace(0, 10, 100)  # 给出x范围
y = odeint(diff, 0, x)  # 设初值为0 此时y为一个数组，元素为不同x对应的y值
# 也可以直接y = odeint(lambda y, x: x, 0, x)
plt.plot(x, y[:, 0])  # y数组（矩阵）的第一列，（因为维度相同，plt.plot(x, y)效果相同）
plt.title('dy/dx = x')
plt.grid()
plt.show()  


# ## 2.2 洛伦兹曲线与数值解

# **代码例**

# In[6]:


def move(P,steps,sets):
    x,y,z = P
    sgima,rho,beta = sets
    #各方向的速度近似
    dx = sgima*(y-x)
    dy = x*(rho-z)-y
    dz = x*y - beta*z
    return [x+dx*steps,y+dy*steps,z+dz*steps]
 
# 设置sets参数
sets = [10.,28.,3.]
t = np.arange(0,30,0.01)
 
# 位置1：
P0 = [0.,1.,0.]
 
P = P0
d = []
for v in t:
    P = move(P,0.01,sets)
    d.append(P)
dnp = np.array(d)
 
# 位置2：
P02 = [0.,1.01,0.]
 
P = P02
d = []
for v in t:
    P = move(P,0.01,sets)
    d.append(P)
dnp2 = np.array(d)
# 画图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
 
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(dnp[:,0],dnp[:,1],dnp[:,2])
ax.plot(dnp2[:,0],dnp2[:,1],dnp2[:,2])
plt.title('洛伦兹曲线')
plt.show()


# **使用odeint解决**

# In[7]:


# 定义函数
def dmove(w,t,p,r,b):
    # 给出 位置矢量w 和三个参数p,r,b计算出
    # dx/dt,dy/dt,dp/dt
    x,y,z = w
    return np.array([p*(y-x),x*(r-z),x*y-b*z])

# 创建时间点
t = np.arange(0,30,0.01)
# 初始点
s1 = (0.,1.,0.)
s2 = (0.,1.01,0.)
# 超参集合
args = (10.,28.,3.)

# p1 p2
p1 =odeint(dmove,s1,t,args=args)
p2 =odeint(dmove,s2,t,args=args)

# 画图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(p1[:,0],p1[:,1],p1[:,2],label = 'P1')
ax.plot(p2[:,0],p2[:,1],p2[:,2],label = 'P2')
plt.title('洛伦兹曲线 by odeint')
plt.legend(loc='best')
plt.show()


# ## 2.3 传染病模型

# **六种传染病模型 SI,SIS,SIR,SIRS,SEIR,SEIRS**

# ### 2.3.1 SI-Model

# 在 SI 模型里面，只考虑了易感者和感染者，并且感染者不能够恢复，此类病症有 HIV 等；
# 由于艾滋传染之后不可治愈，所以该模型为：易感染者被感染

# In[8]:


import scipy.integrate as spi
import numpy as np
import pylab as pl
alpha=1.4247
beta=0.14286
TS=1.0 #观察间隔
ND=70.0 #观察结束日期
S0=1-1e-6 #初始易感人数
I0=1e-6 #初始感染人数
INPUT = (S0, I0, 0.0)
def diff_eqs(INP,t):
    '''The main set of equations'''
    Y=np.zeros((3))
    V = INP
    Y[0] = - alpha * V[0] * V[1]
    Y[1] = alpha * V[0] * V[1] - beta * V[1]
    Y[2] = beta * V[1]
    return Y
t_start = 0.0
t_end = ND
t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc) #生成日期范围
RES = spi.odeint(diff_eqs,INPUT,t_range)
pl.subplot(111)
pl.plot(RES[:,0], '-g', label='Susceptible')
pl.plot(RES[:,1], '-r', label='Infective')
pl.plot(RES[:,2], '-k', label='Removal')
pl.legend(loc=0)
pl.title('SIR_Model')
pl.xlabel('Time')
pl.ylabel('Numbers')
pl.xlabel('Time')


# ### 2.3.2 SIS-Model

# 除了 HIV 这种比较严重的病之外，还有很多小病是可以恢复并且反复感染的，例如日常的感冒，发烧等。在这种情况下，感染者就有一定的几率重新转化成易感者

# ### 2.3.3 SIR-Model

# 有的时候，感染者在康复之后，就有了抗体，于是后续就不会再获得此类病症，这种时候，考虑SIS模型就不再合适了，需要考虑SIR模型。此类病症有麻疹，腮腺炎，风疹等

# ### 2.3.4 SEIR-Model

# SEIR模型加入了扰动因子v，前面三种模型也可以加入扰动因子，加入扰动因子的模型往往更合理\
# 原因：就拿SEIR模型来说，它不是万能的，总有一些异常状况，如有的人潜伏期短，有的人潜伏期长，还可能有超级感染者，有的潜伏者可能就直接痊愈了，变成了抵抗者。方程并没有单独处理这些情况，因为一定程度内这些异类都可以被扰动因子所包含。研究一个固定的模型加扰动项，比不断地往模型里加扰动项好研究的多
# 
# 通过对 SEIR 模型的研究, 可以预测一个封闭地区疫情的爆发情况, 最大峰值, 感染人数等等
# 
# 但是显然没有任何地区是封闭的, 所以就要把各个地区看成图的节点, 地区之间的流动可以由马尔可夫转移所刻画, 对每个结点单独跑 SEIR 模型
# 
# 最后整个仿真模型就可以比较准确的反应疫情的散播和爆发情况
# 
# 当然可以再加入更多的决策因素

# ### 2.3.5 SIRS-Model

# ### 2.3.6 SIERS-Model

# In[ ]:




