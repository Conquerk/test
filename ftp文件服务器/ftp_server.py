'''
ftp 文件服务器
fork server　训练
'''
from socket import *
import os,sys
import time

class ftpserver(object):
    def __init__(self,connfd):
        self.connfd=connfd

    def do_list(self):
        print("执行list")
        #获取文件列表
        file_list=os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件为空".encode())
            return
        else:
            self.connfd.send('OK'.encode())
            time.sleep(0.1)
        files=''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files = files + file + '#'
        #将拼接好的文件名发送给客户端
        self.connfd.send(files.encode())

    def do_get(self,filename):
        try:
            fd = open(FILE_PATH+filename,'rb')
        except:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
        #发送文件内容
        while True:
            data=fd.read(2028)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        print("文件发送完毕\n")

    def do_put(self,filename):
        try:
            fd = open(FILE_PATH+filename,'wb')
        except:
            self.connfd.send("上传失败".encode())
            return
        else:
            self.connfd.send(b'OK')
        #接收文件
        while True:
            data=self.connfd.recv(1024)
            if data == "##":
                break
            fd.write(data)
        print("接收完成")
        fd.close()

#全局变量设置
HOST='0.0.0.0'
PORT=8844
ADDR=(HOST,PORT)
FILE_PATH='./ftpfile/'

def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    print("listen to 8844....")

    while True:
        try:
            connfd,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print("服务器异常",e)
            continue
        print("链接服务端",addr)

        #创建子进程
        pid=os.fork()
        if pid ==0 :
            p=os.fork()
            if p==0: #接收客户端请求
                s.close()
                ftp=ftpserver(connfd)
                while True:
                    data=connfd.recv(1024).decode()
                    if not data or data[0] == 'Q':
                        connfd.close()
                        sys.exit("客户端退出")
                    if data[0] == 'L':
                        ftp.do_list()
                    elif data[0] == 'G':
                        filename = data.split(' ')[-1]
                        ftp.do_get(filename)
                    elif data[0] == 'P':
                        filename = data.split(' ')[-1]
                        ftp.do_put(filename)
            else:
                sys.exit(0)
        else:
            connfd.close()
            os.wait()


if __name__ == "__main__":
    main()