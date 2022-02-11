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


'''b1=input('请输入第一个八位二进制数串:')
x=int(b1,2)
b2=input('请输入第二个八位二进制数串:')
y=int(b2,2)
assert x<=255 and y<=255
z=x+y
s=bin(z)[2:]
s='0'*(8-len(s))+s
s=s[-8:]
if z>255:
    print('溢出,False',s)
else:
    print('正确,True',s)'''

'''b1=input('请输入一个八位长的二进制补码:')
assert len(b1)==8
if b1[0]=='1':
    x=int(b1,2)-256
else:
    x=int(b1,2)
print('{}补码对应的十进制真值是{}'.format(b1,x))'''

'''for c in '沙老师':
    print(c,hex(ord(c)))'''

'''def convert(b):
    if len(b)==1:
        return int(b[0])
    x=int(b[-1])
    return convert(b[:-1])*2+x
b=input("请输入一个二进制串:")
print('{}二进制串转十进制,结果为:{}'.format(b,convert(b)))
'''

'''m=input('输入待转换的小数部分(例如0.123只输入123);')
m='0.'+m
x=float(m)
n=8
s=''
for _ in range(n):
    x=x*2
    s=s+str(int(x))
    x=x-int(x)
s='0.'+s
print('十进制小数:',m,'转二进制小数:',s)'''


'''b=input('请输入b进制(2-9进制)的b:')
m=input('请输入'+b+'进制的数(带小数点):')
b=int(b)
li=m.split('.')
num=0
s=reversed(li[0])
for i,x in enumerate(s):
    f=int(x)*(b**i)
    num=num+f

if len(li)==2:
    for i,x in enumerate(li[1]):
        f=int(x)*(b**(-(i+1)))
        num=num+f
print('{}进制数{}转十进制结果为{}'.format(b,m,num))'''

    
'''m=input('请输入八进制的小数(带小数点):')
li=m.split('.')
result=''
for i in range(0,2):
    for x in li[i]:
        s=bin(int(x))
        s=s[2:]
        s='0'*(3-len(s))+s
        result=result+s
    if i==0:
        result=result+'.'
print('八进制数{}采用三位一并法转为二进制小数,结果为{}'.format(m,result))
h=''
li=result.split('.')
for i in range(0,2):
    if i==0:
        if len(li[0])%4:
             li[0]='0'*(4-len(li[0])%4) + li[0] #整数部分，在前面补0，凑足4的倍数长
    if i==1:
        if len(li[1])%4:
            li[1]= li[1]+'0'*(4-len(li[1])%4) #小数部分，在后面补0，凑足4的倍数长
    
    for  x  in  range(len(li[i])//4):       
        s=li[i][x*4:(x+1)*4]
        m=int(s,2)
        if  m>9:
            h=h+ chr(ord('A')+m-10)
        else:
            h=h+str(m)
    if i==0:
        h=h+'.'

print('二进制数{} 采用四位一并法转为十六进制,结果为{}'.format(result,h))
'''
    
   


