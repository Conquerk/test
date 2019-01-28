#coding=utf-8

'''
模拟框架程序部分
'''
from socket import *
from views import *

frame_ip = '127.0.0.1'
frame_port = 8080
frameAddr = (frame_ip,frame_port)
#静态网页位置
STATIC_DIR='./static'
#决定我们能处理什么数据
urls = [
    ('/time',show_time()),
    ('/hello',say_hello()),
    ('/bye',say_bye())
]


#写一个应用类将功能封装在类中
class Appliecation(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(frameAddr)

    def start(self):
        self.sockfd.listen(5)
        print('listen to 8080...')
        while True:
            connfd,addr = self.sockfd.accept()
            method= connfd.recv(1024).decode()
            path_info = connfd.recv(1024).decode()
            self.handle(connfd,method,path_info)
    
    def handle(self,connfd,method,path_info):
        if method == 'GET':
            if path_info == "/" or path_info[-5:] == '.html':
                response = self.get_html(path_info)
            else:
                response = self.get_data(path_info)
        elif method == 'PORT':
            pass

        connfd.send(response.encode())
        connfd.close()

    def get_html(self,path_info):
        if path_info == '/':
            get_file = STATIC_DIR + '/index.html' 
        else:
            get_file = STATIC_DIR + path_info
        
        try:
            fd = open(get_file)
        except IOError:
            response = '404'
        else:
            response = fd.read()
        finally:
            return response

    def get_data(self,path_info):
        for url,func in urls:
            if path_info == url:
                return func
        return '404'



if __name__ == '__main__':
    app = Appliecation()
    app.start() #启动应用框架程序