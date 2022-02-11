'''import math
def triarea(a,b,c):
    assert a+b>c and b+c>a and a+c>b
    p=(a+b+c)/2.0
    s=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
    return s
def getsum(m,n):
    return sum(range(m,n+1))

if  __name__=='__main__':
    print('模块作为主程序执行')
    s=triarea(2,3,4)
    print('%d%d%d三边构成的三角形面积为:%.2f' % (2,3,4,s))
    s=getsum(1,10)
    print('{}到{}的累加和为{}'.format(1,10,s))'''


'''f=open('tel.txt','r')
di={}
while True:
    s=f.readline()
    if s=="":
        break
    li=s.split()
    di[li[0]]=li[1]
f.close()

print('电话本如下:')
for x in di:
    print(x,di[x])

print('\n')
while True:
    name=input('请输入查询名称（直接按回车键结束查询):')
    if name=="":
        break
    if name in di:
        print(name,'的电话号码是',di[name])
    else:
        print('查无此人',name)

print("\n测试字典更新/添加操作")
name=input('please input name')
newtel=input('please input'+name+'new number:')
di[name]=newtel
print(name+'number has updated,the number is:',di[name])
f=open('tel.txt','w')
for x in di:
      f.write(x+' '+di[x]+'\n')
f.close()'''

import random
f=open('toupiao.txt','w')
li1=['@','#','$','%','^','&','*']
num=3000
for x in range(num):
    f.write(random.choice(li1)+'\n')
f.close()
print('task is finished,in total{}tickets'.format(num))
f=open('toupiao.txt','r')
di={}
while True:
    s=f.readline()
    if s=="":
        break
    s=s.strip()
    if len(s)>0:
        di[s]=di.get(s,0)+1
f.close()
print('\n统计结果如下：')

for  x  in  di:
    print(x, di[x])

print('\n总票数：',sum(di.values()))    #di.values()返回字典的所有值，sum求和

#对字典排序 ，lambda定义匿名函数, x代表字典中的一项例如{"张三":450}, 则 x[1]对应票数
li=sorted(di.items(), key=lambda x:x[1], reverse=True)  #按x[1]票数的逆序排列
print('\n按票数排序后，结果如下:')  
for  x  in li:
    print(x[0],x[1])  #x[0]姓名, x[1]票数
 

