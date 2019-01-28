#二进制文件写操作
# 0x01 0x02 ...... 0xff
try:
    f=open("0-255.bin","wb")
    b=bytes(range(256))
    f.write(b)
    f.close()
    print("输入结束")

except OSError:
    print("文件读写失败")
