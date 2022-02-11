'''x=int(input('请输入一个-127到127范围内的十进制整数:'))
assert -127<=x<=127
if x<0:
    m=256+x
else:
    m=x
s=bin(m)
s=s[2:]
if x>=0:
    s='0'*(8-len(s))+s
print('{}的二进制补码形式是{}'.format(x,s))'''


'''print('BMI=体重/(身高的平方)')
f=open('BMI.txt','a+');
while True:
    weight=float(input('体重(公斤)_='));
    if weight<=0:
        break
    height=float(input('身高(米)='));
    bmi=round(weight/(height**2),2)
    if bmi<18.5:
        s='过轻'
    elif bmi<24.99:
        s='正常'
    elif bmi<28:
        s='过重'
    elif bmi<32:
        s='肥胖'
    else:
        s='非常肥胖'
    print('BMI=',bmi,s)
    line='体重'+str(weight)+',身高='+str(height)+'bmi='+str(bmi)+','+s+'\n'
    f.write(line)
f.close()'''

'''while True:
    seconds=int(input('输入秒数(0-86400)='))
    if not (0<=seconds<=86400):
        print('输入有误')
        break;
    hour=seconds//3600
    minute=(seconds-hour*3600)//60
    second=seconds-hour*3600-minute*60
    print('%d秒折合时间为 %02d:%02d:%02d' % (seconds,hour,minute,second))
    print('{}秒折合时间为{:02d}:{:02d}:{:02d}'.format(seconds,hour,minute,second))
   '''
'''wheat=0
for x in range(0,64):
    wheat=wheat+2**x
print('64格棋盘共可放麦粒:',wheat,'颗')
print('合计重量为:',wheat*50*(10**-9),'吨')'''


'''import random
li=[]
for x in range(50):
    li.append(random.randint(40,100))
print('原始顺序为:',li,'\n')
li.sort(reverse=True)
print('排序后的顺序为:',li,'n')
print('数据个数:',len(li),'最高分:',max(li),'最低分:',min(li),'平均数:',round(sum(li)*1.0/len(li),1))
    

print('将列表数据写入文件:\stu.txt')
f=open(r'd:\stu.txt','w')
for x in li:
    f.write(str(x)+'\n')
f.close()
print('读取数据文件d:\stu.txt')
li3=[]
f=open(r'd:\stu.txt','r')
for x in f:
    li3=li3+[int(x)]
f.close()
print('读取的数据为:',li3)'''
    


