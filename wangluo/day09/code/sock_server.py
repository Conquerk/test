import socketserver import *
#服务器类型
class Server(ForkingMixIn,TCPServer):
    pass
#处理具体请求
class Handler(StreamRequestHandler):
    #具体方法
    def handle(self):
        print('connect from ',self.client_address)
        while True:
            data=self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'receive')

if __name__ == "__main__":
    server_addr = ('0.0.0.0',4444)
    server = Server(server_addr,Handler)
    server.serve_forever() #启动服务端
    #创建服务器对象