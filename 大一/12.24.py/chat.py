#coding=cp936
# ���з�����python  chat.py  ������IP ��
import  socket, sys
try:
    server='127.0.0.1'  #Ĭ�����ӱ���
    server=sys.argv[1]  #�������������IP�������ӷ�����
except:
    pass
localIP = socket.gethostbyname(socket.gethostname())  #�õ�����ip
print  ('Ⱥ�Ŀͻ���������  ����IP: ', localIP)
name=input('��������������ǳ�:')
name='('+name+')'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    # TCP
s.connect((server,5000))        #�������������
while  True:
        data=input('��������:')
        if  data!='':
            s.send((name+data).encode('utf-8'))    #����Ϣתbytes���ܷ��͵�������
s.close()
