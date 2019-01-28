#示例　
# 文件的打开
try:
    f=open("mynote.txt")  #打开文件用ｆ绑定  文件流对象
        #读写文件
    s=f.readline()    # 从文件中读取一行
    print("您读到的是",s)
    print("您读到的字符个数是",len(s))
    print("成功打开文件")
        #关闭文件
    f.close()
    print("成功关闭文件")
except OSError:
    print("文件打开失败")