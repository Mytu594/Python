#coding=cp936
# 运行方法【python  chat.py  服务器IP 】
import  socket, sys
try:
    server='127.0.0.1'  #默认连接本机
    server=sys.argv[1]  #如有输入服务器IP，则连接服务器
except:
    pass
localIP = socket.gethostbyname(socket.gethostname())  #得到本地ip
print  ('群聊客户端已启动  本机IP: ', localIP)
name=input('请输入你的聊天昵称:')
name='('+name+')'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    # TCP
s.connect((server,5000))        #连接聊天服务器
while  True:
        data=input('输入内容:')
        if  data!='':
            s.send((name+data).encode('utf-8'))    #将信息转bytes才能发送到服务器
s.close()
