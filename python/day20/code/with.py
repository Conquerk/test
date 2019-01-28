# f=open("text.txt",'w')
try:
    with open("text.txt","w")as f:
        s=int(input("请输入整数"))  # 制造异常
        f.write("hello")
except OSError:
    print("文件打开失败")
except:
    print("写入数据失败")