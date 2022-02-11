# coding=cp936
# 运行方法【python  chatshow.py  】
import  socket,sys
MAX_BYTES=65535     #定义数据包最大字节数
print('准备显示从服务器传来的聊天信息')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp
sock.bind(('', 4900))    #在4900端口等待服务器传来的信息
while  True:
        data, address=sock.recvfrom(MAX_BYTES)  #接收信息
        print(data.decode('utf-8'))   # 收到的是bytes, 解码为字符串再显示 
s.close()
