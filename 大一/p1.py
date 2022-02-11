'''n=int(input('斐波拉契数列的项数n='))
li=[1,1]
for x in range (2,n):
    li.append(li[-1]+li[-2])
print('斐波拉契数列：',li)
input()'''


'''f=open('phone.txt','r')
while True:
    s=f.readline()
    if s=="":
        break
    li=s.split()
    s='尊敬的顾客{0:<4},您好！您{1:>2}月的话费是{2:8.2f}元，目前金额{3:8.2f}元'
    name=li[0]
    name=name+(4-len(name))*chr(0x3000)
    print(s.format(name,li[1],float(li[2]),float(li[3])))
f.close()'''
def output(li):
    print('学号 姓名       语文    数学    总评')
    for x in li:
        print('{:<4s}{:<6s}{:8.1f}{:8.1f}{:8.1f}'.format(*x))
f=open('score.txt','r')
s=f.readline()
stu=[]
while True:
    s=f.readline()
    if s=="":
        break
    li=s.split()
    li[2]=float(li[2])
    li[3]=float(li[3])
    if len(li)==4:
        avg=round(li[2]+li[3]/2,1)
        yz=(li[0],li[1],li[2],li[3],avg)
        stu.append(yz)
f.close()

print('\n学生记录如下:')
output(stu)

print('\n按语文由低到高:')
li2=sorted(stu,key=lambda x:x[2])
output(li2)

print('\n按数学由高到低:')
li3=sorted(stu,key=lambda x:x[3],reverse=True)
output(li3)

print('\n按总分由高到低:')
li4=sorted(stu,key=lambda x:x[4],reverse=True)
output(li4)

