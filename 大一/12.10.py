#1
n=int(input('请输入层数n='))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for j in range(1,n):
    print(' '*j+'*'*(2*(n-j)-1))

#2
'''
li=[1,2,3,3,3,5,8,9,12,2,3,18,21,23,4,6,8,30]
li1=sorted(li)
n=(len(li1)-1)/2
print(li[n])
for x in li1:
    a[x]=0
for x in li1:
    a[x]+=1
for x in li1:
    m=max(a[x])'''

#2
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
        li2.append(n)
'''

#3
'''
import random
n=0
for i in range(10000):
    a=random.uniform(0,2)
    b=random.uniform(0,2)
    if a*a+b*b<=1:
        n+=1
pi=4*(n/10000)
print(n)
print(pi)'''

#4
'''
def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)

n=int(input("please enter a number:"))
print(fac(n))'''



    

  
