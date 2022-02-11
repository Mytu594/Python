m=input('请输入八进制的小数(带小数点):')
# 分隔为整数和小数部分 例如 56.23 分隔后 li[0]='56', li[1]='23'
li=m.split('.')     
result=''
for  i in  range(0,2):
    for  x  in  li[i]:       
        s=bin(int(x))        
        s=s[2:]
        s='0'*(3-len(s))+s
        result=result+s
    if i==0:
        result=result+'.'
print('八进制数{} 采用三位一并法转为二进制小数,结果为{}'.format(m,result))
h=''
li=result.split('.')     
for  i in  range(0,2):
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
