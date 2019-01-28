#煎蛋机器人，打开天然气...关闭天然气：
def fry_egg():
    print("打开天然气")
    try:
        count=int(input("请输入鸡蛋个数:"))
        print("完成{}个煎蛋".format(count))
    finally:    
        print("关闭天然气")

try:
    fry_egg()
except :
    print("发生异常，已转为正常")
