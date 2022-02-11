'''n=10
for raw in range(1,n+1):
    print(' '*(n-raw)+'X'*(2*raw-1))'''
''''print("X"*10,)
print('X'+' '*8+'X')
print('X'+' '*8+'X')
print('X'+' '*8+'X')
print('X'+' '*8+'X')
print('X'+' '*8+'X')
print('X'+' '*8+'X')
print('X'+' '*8+'X')
print('X'+' '*8+'X')
print('X'*10)'''
'''x,y,z=eval(input('输入三个数:'))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)'''

'''n=10
print('X '*n)                #为屏幕上排列整齐，X的后面加了一个空格
for  m  in  range(0,n-2):
    print('X'+'  '*(n-2)+' X')
print('X '*n)'''
'''n=10
print(chr(0x2605)*n)
print(chr(0x2605),end='')              #end='' 的作用是print后不换行
print('我喜欢计算机导论',end='')
print(chr(0x2605))
print(chr(0x2605)*n)'''
'''print(chr(0x2605)*9)
print(chr(0x2605)+'旋姐,生日快乐!'+chr(0x2605))
print(chr(0x2605)*9)'''
'''def factor(n):
    if n<0:
        print('error')
    elif n==0:
        return 1
    else:
        x=1
        for x in range(1,n+1):
            x=x*i
        return x
def f(n,k):
    c=factor(n)/(factor(n-k)*factor(k))
    return int(x)'''

