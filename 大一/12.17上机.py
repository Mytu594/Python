# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for j in range(1,n):
    print(' '*j+'*'*(2*(n-j)-1))'''
    
'''         
li=[1,2,3,3,3,5,8,9,12,2,3,18,21,23,4,6,8,30]
li1=sorted(li)
li2=[]
n=0
m=len(li1)
if m%2==0:
    zws=(li[m//2-1]+li[m//2])/2
else:
    zws=li[(m-1)/2]
pjs=(sum(li1[:]))/m
for i in range(m):
    for j in range(m):
        if li1[i]==li1[j]:
            n=+1
        li2.append(n)'''
'''        
li=[1,2,3,3,3,5,8,9,12,2,3,18,21,23,4,6,8,30]
li.sort()
length=len(li)
pos=int(length/2)  #取中间位置，因为该值用于下标，注意要转为int
if  length%2==0:
    print('中位数是:', (li[pos-1]+li[pos])/2 )
else:
    print('中位数是:', li[pos] )'''
 
'''li=[1,2,3,3,3,5,8,9,12,2,3,18,21,23,4,6,8,30]
li.sort()
length=len(li)
pos=int(length/2)
if length%2==0:
    print('中位数是:'(li[pos-1]+li[pos])/2)
else:
    print('中位数是:',li[pos])

avg=sum(li)/len(li)
li2=[(x-avg)** for x in li]
var=sum(li2)/len(li)
std=var**0.5
print('方差:',var,'标准差:',std)'''

#3
'''
import random
ci=50000
num=0
for _ in range(ci):
    x=random.random()
    y=random.random()
    if(x**2+y**2)<=1:
        num+=1
p=num/ci
pi=4*p
print('估计的圆周率pi=',pi)'''

#4
'''
def fac(n):
    if n==1:return 1
    return n*fac(n-1)
for x in [1,4,10]:
    print(x,'!=',fac(x))'''
#5
'''def copyfile(src,dst):
    f1=open(src,'rb')
    data=f1.read()
    f1.close()
    f2=open(dst,'wb')
    f2.write(data)
    f2.close()
    
copyfile('data.txt','new.txt')
copyfile('1.jpg','2.jpg')'''

#6
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2*np.pi,2*np.pi,100)
y1=x+1
y2=x**2
sy=np.sin(x)
cy=np.cos(x)

plt.subplot(1,2,1)
plt.plot(x,y1,label='y=x+1')
plt.plot(x,y2,label='y=x**2')
plt.legend()

plt.subplot(1,2,2)
plt.plot(x,sy,label='y=sin(x)')
plt.plot(x,cy,label='y=cos(x)')
plt.legend()
plt.show()'''

import numpy as np
import matplotlib.pyplot as plt
x=[1,1,-1,-1,1]
y=[-1,1,1,-1,-1]     
plt.plot(x,y)

plt.axis('equal')
x2=np.linspace(0,1,100)
y2=(1-x2**2)**0.5
plt.fill_between(x2,0,y2,color='g')

x3=np.random.rand(100)
y3=np.random.rand(100)

plt.scatter(x3,y3,color='r',s=1)
x4=np.linspace(0,1,100)
y4=np.log(x)
plt.show()