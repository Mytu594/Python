def square_root_1():  #函数定义，函数名为square_root_1
    c = 10	#所求平方根的输入，即该段程序求根号10
    i = 0		#记录执行循环次数
    g = 0
    for j in range(0,c+1):    #for 循环开始
        if (j * j > c and  g==0): #if 判断，使得g2<c，(g+1)2>c
            g = j - 1        #for 循环结束
            
    while (abs(g * g - c) > 0.0001):#判断g2-c是否在精度范围内
        g += 0.00001	#g每次加步长，以逼近所求解
        i = i+1
        print ("%d:g = %.5f" % (i,g))
    return g  #返回结果
#函数外，执行下面的语句
square_root_1()  #最后输出  16227:g=3.16227
