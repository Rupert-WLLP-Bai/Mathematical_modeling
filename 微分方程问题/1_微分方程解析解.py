#!/usr/bin/env python
# coding: utf-8

# # 微分方程解析解

# 用SymPy求解

# ### 一个例子

# In[1]:


from sympy.abc import *
from sympy import *
import sympy


# In[2]:


f= sympy.Function('f') # f标记为变量
diffeq = Eq(f(x).diff(x, 2) - 2*f(x).diff(t) + f(x), sin(x))


# In[3]:


diffeq


# In[4]:


dsolve(diffeq,f(x))


# ### 阻尼谐振子的二阶ODE

# 包含initial conditions

# In[5]:


t,gamma,omega0=symbols('t,gamma,omega_0') # 定义符号


# In[6]:


x= sympy.Function('x') # x标记为变量


# In[7]:


# 设置ODE
ODE = Eq(x(t).diff(t, 2) + 2*omega0*gamma*x(t).diff(t) + omega0**2*x(t), 0)
# 定义初始条件
con={x(0):1,diff(x(t),t).subs(t,0): 0}


# In[8]:


ODE


# In[9]:


dsolve(ODE,ics=con)

