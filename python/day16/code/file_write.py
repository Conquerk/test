#示意　　写文本文件的方法:
f=open("myfile.txt","w")
print("打开文件成功")
f.write("这是第一行文字")
f.write("\n")
f.write("ABCDEFG\n")
f.writelines(["aaaaaaaa\n","bbbbbbbbb\n","ccccccccc"])
print("写文件成功")
f.close()
print("关闭文件成功")