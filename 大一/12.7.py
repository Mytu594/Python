#1(1)
'''x=int(input("请输入一个字母a的ascii码(65):"))
for i in range(x,x+26):
    print('%s' % (chr(i)))'''

#1(2)
'''import random
li=[]
for i in range(1,51):
    x=random.randrange(40,101)
    li.append(x)
print(li)'''

#1(3)
'''L=[]
L=[x for x in 'abcdefghijklmnopqrstuvwxyz']
print(L)'''

'''L=[]
for i in range(97,123):
    L.append(chr(i))
print(L)'''

#1(4)
'''
file=open('C://Users/10317/Desktop/data.txt','w')
file.write('abcdefg')
file.close()'''

#1(5)
'''
li1=[1,2,3,4,5,6,7,8,9,10]
li2=[2,4,6,8,10]
li3=[]
for i in range(0,len(li1)):
    for j in range(0,len(li2)):
        if(li1[i]==li2[j]):
            li3.append(li1[i])
print(li3)'''

#1(6)
'''dic={'a':'apple','b':'banana'}
print(dic)'''

#1(7)
'''
s='abcdefg'
print(s[1])
print(s[1:4])
print(s[-1])
print(s[:])
print(s[0::2])'''

#1(8)
'''li=[x for x in range(100,201) if x%3==0]
print(li)'''

#2
'''
n=int(input("请输入年份:"))
if((n%4==0 and (n%100)!=0) or (n%400==0)):
    print("%d 是闰年" % (n))
else:
    print("%d 不是闰年" % (n))'''

'''
def isleapyear(year):
    if((year%4==0 and (year%100)!=0) or (year%400==0)):
        return True
    else:
        return False
x=0
while x!=-1:
    x=int(input("请输入年份:"))
    if isleapyear(x):
        print('闰年')'''

#3

import math
def factor(n):
    li=[]
    n=int(input("请输入年份:"))
    for i in range(1,n+1):
        for j in range(1,n+1):
            zhishu(i)
            zhushu(j)
            if(i*j==n):
                li.append(i)
    return sorted(li)
def zhishu(x):
     
     for x in range(2,100):
        for y in range(2,x):
            if(x%y==0):
                return 0
            else:
                return 1
                









    
        
    






    




