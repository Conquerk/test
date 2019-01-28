# def get_score():
#     s=int(input("请输入成绩0-100:"))
#     if not (0<=s<=100):
#         return 0
#     return s 
# try:
#     score=get_score()
# except ValueError:
#     score=0
# print("成绩为：",score)    方法一   调用时用ｔｒｙ

# 方法二：　　在ｇｅｔ..函数内部加入语句
def get_score():
    try:
        s=int(input("请输入成绩0-100:"))
    except ValueError:
        return 0
    if not (0<=s<=100):
        return 0
    return s 

score=get_score()
print("成绩为：",score) 
