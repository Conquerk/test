def mycopy(src_file,dst_file):
    """src_file源文件名　　dst_file目标文件名"""
    try:
        fr=open(src_file,"rb")
        try:
            try:
                fw=open(dst_file,"wb")
                try:
                    while True:
                        data=fr.read(4096)
                        if not data:
                            break
                        fw.write(data)
                except:
                    print("可能硬盘损坏")
                finally:
                    fw.close()
            except:
                print("打开写文件失败")
                return False
        finally:
            fr.close()
    except:
        print("打开读文件失败")
        return False
    return True
s=input("请输入源文件名：")
d=input("请输入目标文件名：")
if mycopy(s,d):
    print("复制成功")
else:
    print("复制失败")