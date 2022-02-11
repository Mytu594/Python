'''def hello(info,num):
    for x in range(num):
        print(info)
hello('smile',5)'''

'''def hello(info,num):
    print(info*num)
hello('a',5)'''


'''import math
def zhishu(m,n):
    """返回[m,n]之间的所有质数列表"""
    li=[]
    for x in range(m,n+1):
        i=0
        for j in range(2,int(math.sqrt(x))+1):
            if x%j==0:
                i=1
                break
        if i==0:
            li=li+[x]
    print(li)
zhishu(101,201)'''


'''def countfile(filename):
    f=open(filename,'r')
    shuzi,kongge,zimu,other=0,0,0,0
    for line in f:
        for x in line:
            if x.isdigit():
                shuzi+=1
            elif x.isspace():
                kongge+=1
            elif x.isalpha():
                zimu+=1
            else:
                other+=1
    f.close()
    return shuzi,kongge,zimu,shuzi+kongge+zimu+other
if __name__=="__main__":
    fname='data.txt'     #这里要替换为你的实际的文件名，data.txt 和程序应在同一文件夹中
    yz=countfile(fname)
    print  ('{} 文件中:  数字数 {}, 空格数{},  字母数{},  总字符数 {}'.format(fname,yz[0],yz[1],yz[2],yz[3]))
  '''
f=open('600000.txt','r')
f.readline()
stock=[]
for s in f:
    li=s.split()
    if len(li)>=5:
        stock.append((li[0],float(li[4])))
f.close()
fivedays=[]
for x in range(4,len(stock)):
    s=0
    for i in range(5):
        s=stock[x-i][1]+s
    avg=round(s/5,2)
    fivedays.append((stock[x][0],avg))
print('五日均线数据如下:')
for x in fivedays:
    print(x)
        

                
