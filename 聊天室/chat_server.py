#coding=utf-8
"""
chatromm
env:python 3.5
socket and fork
"""

from socket import *
import os,sys

def do_login(s,user,name,addr):
    if (name in user) or name == "管理员":
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto("ok".encode(),addr)

    #通知其他人
    msg="\n欢迎{}进入聊天室".format(name)
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入ｕｓｅｒ
    user[name]=addr
def do_chat(s,user,name,msg):
    msg = "\n%s 说: %s"%(name,msg)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,user,name):
    msg="\n%s 退出了聊天室"%name
    for i in user:
        if i == name:
            s.sendto('EXIT'.encode(),user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name]


def do_request(s):
    #存储结构　　{'张三'：('127.0.0.1'，4444)}
    user={}
    while True:
        msg,addr=s.recvfrom(1024)
        msglist=msg.decode().split(' ')
        #区分请求类型
        if msglist[0] == "l":
           do_login(s,user,msglist[1],addr)
        elif msglist[0] == "c":
            #重新拼接字符串
            msg=" ".join(msglist[2:])
            do_chat(s,user,msglist[1],msg)
        elif msglist[0] == "Q":
            do_quit(s,user,msglist[1])
            
            

#创建网络连接
def main():
    ADDR=("0.0.0.0",4444)
    #创建套接子
    s=socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    
    #用于接收各种客户端请求，调用相应客户端处理
    pid=os.fork()
    if pid < 0:
        print("创建进程失败")
    elif pid == 0:
        while True:
            msg=input("管理员消息:")
            msg="c 管理员 "+msg
            s.sendto(msg.encode(),ADDR)
    else:
        do_request(s)
if __name__ =="__main__":
    main()
