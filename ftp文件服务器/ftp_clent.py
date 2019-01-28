from socket import *
import sys
import time
#具体功能放在类中
class ftpclient(object):

    def __init__(self,s):
        self.sockfd=s

    def do_list(self):
        self.sockfd.send(b'L')#发送请求
        data=self.sockfd.recv(128).decode()
        if data == 'OK':
            data=self.sockfd.recv(4096).decode()
            files=data.split('#')
            for x in files:
                print(x)
            print("文件列表展示完毕")
        else:
            #无法执行
            print(data)
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("客户端退出")

    def do_get(self,filename):
        self.sockfd.send(('G '+filename).encode())
        data=self.sockfd.recv(128).decode()
        if data == 'OK':
            fd=open(filename,'wb')
            while True:
                data=self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("下载完闭{}\n".format(filename))
        else:
            print(data)
    
    def do_put(self,filename):
        try:
            f=open(filename,'rb')
        except:
            print("文件不存在")
            return
        self.sockfd.send(('P '+filename).encode())
        data=self.sockfd.recv(128).decode()
        if data == "OK":
            while True:
                data=f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
            print("{}上传完毕\n".format(filename))
        else:
            print(data)
                
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST=sys.argv[1]
    PORT=int(sys.argv[2])
    ADDR=(HOST,PORT)

    s=socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print("链接服务器失败")
        return
    #创建对象下载完闭
    ftp=ftpclient(s)
    while True:
        print("==========命令选项=======")
        print("|----------list---------|")
        print("|--------get file-------|")
        print("|--------put file-------|")
        print("|----------quit---------|")
        print("=========================\n")

        cmd=input("输入命令>>")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip()== 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename=cmd.split(" ")[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename=cmd.split(' ')[-1]
            ftp.do_put(filename)
        else:
            print("请输入正确命令")



if __name__ == "__main__":
    main()