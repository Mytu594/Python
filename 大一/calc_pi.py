# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import  numpy as  np
import  matplotlib.pyplot as plt
x=[ 1,1,-1,-1,1]
y=[-1,1, 1,-1,-1]

plt.plot(x,y)      # 

        
plt.axis('equal')  # 将X/Y轴 单位长度挑战为相同

x2=np.linspace(0,1,100)   # 在[0, 1] 之间产生 100个等距离的点
y2= (1 - x2**2)**0.5      # 根据 x^2 + y^2 =1 计算对应的  y 值
plt.fill_between(x2,0,y2,color='g')  # 在 x2 所指的范围内， 从 0到y2 填充

x3=np.random.rand(100)  #(0,1)
y3=np.random.rand(100)

plt.scatter(x3,y3,color='r',s=1)  # 做散点图
plt.show()



%matplotlib 魔术命令
%matplotlin inline
