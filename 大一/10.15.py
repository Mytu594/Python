'''1!=0 and 2==1'''

'''1==1 or 2!=1'''

'''n=5
while n<20:
    print(n*2)
    n+=1'''
'''def factor(n):
 if n<0:
    print('参考错误，n应为非负整数')
 elif  n==0:
    return 1
 else:
          x=1
          for i in range(1,n+1):
            x=x*i
          return x
def combination(n,k):
    if k<0 or n<=0 or k>n:
      print('error')
    elif k==0:
      return 1
    else:
        X=factor(n)/(factor(n+k)*factor(k))
        return int(X)'''
'''n=10#故障
gs=''
for i in range(0,n+1):
    gs=gs+str(combination(n,i))+'x^'+str(i)+'+'
print(gs)'''
'''n=4#故障
gs=''
for i in range(0,n+1):
    if i%2==0:
        gs=gs+'+'+str(combination(n,i))+'x^'+str(i)
    else:
      gs=gs+'-'+str(combination(n,i))+'x^'+str(i)
    print(gs)'''
    
    
    
    

    
