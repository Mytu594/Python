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
'''
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
                return 1'''

'''def factor(n):
    if n<0:
        return None
    li=[]
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            li.append(x)
            li.append(n//x)
    li.sort()
    return li

for n in [1,2,-5,13,16,24]:
    print(n,'的因子为',factor(n))'''
        



#4
'''
import random
li=['大王','小王','红1','红2','红3','红4','红5','红6','红7','红8','红9','红10','红J','红Q','红K',
    '黑1','黑2','黑3','黑4','黑5','黑6','黑7','黑8','黑9','黑10','黑J','黑Q','黑K',
    '方1','方2','方3','方4','方5','方6','方7','方8','方9','方10','方J','方Q','方K',
    '草1','草2','草3','草4','草5','草6','草7','草8','草9','草10','草J','草Q','草K']
random.shuffle(li)
li1=li[0:13]
li2=li[14:27]
li3=li[28:41]
li4=li[42:55]
print(li1)
print(li2)
print(li3)
print(li4)'''

'''import random
def getcard():
    suit='红黑方草'
    seq=[str(x) for x in range(1,10)]+['10','J','Q','K']
    li=[s+y for s in suit for y in seq]
    li=['大王','小王']+li
    random.shuffle(li)
    return li

cards=getcard()
player=[[],[],[],[]]
for index,x in enumerate(cards):
    player[index%4].append(x)

for pid,li in enumerate(player):
    print('玩家',pid,li)'''


#5
'''import random
li1=[]
li1=random.sample(range(1,33),6)
li2=[]
m=random.randint(1,16)
li2.append(m)
li=li1+li2
li3=[ '{:02}'.format(x) for x in li  ]
print(li3)'''

'''import random
def ball():
    li=[]
    while len(li)!=6:
        x=random.randict(1,33)
        if x not in li:
            li.append(x)
    li.append(random.randict(1,16))
    li=['{:02}'.format(x) for x in li]
    s=' '.join(li)
    return s'''
              



'''import random
def Red(number,start,end):
    a = []
    while True:
        a.append(random.randint(start,end))
        if len(a) == number:
            break
    return a[0]
def Blue(number,start,end):
    a = []
    while True:
        a.append(random.randint(start,end))
        if len(a) == number:
            break
    return a[0]
for i in range(1,7):
    print (Red(1,1,34))
print (Blue(1,1,16))'''



    
    
    
    



                









    
        
    






    




