# coding=cp936
# ���з�����python  chatshow.py  ��
import  socket,sys
MAX_BYTES=65535     #�������ݰ�����ֽ���
print('׼����ʾ�ӷ�����������������Ϣ')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp
sock.bind(('', 4900))    #��4900�˿ڵȴ���������������Ϣ
while  True:
        data, address=sock.recvfrom(MAX_BYTES)  #������Ϣ
        print(data.decode('utf-8'))   # �յ�����bytes, ����Ϊ�ַ�������ʾ 
s.close()
