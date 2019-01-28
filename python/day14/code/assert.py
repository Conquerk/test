#此示例示意ａｓｓｅｒｔ
def get_score():
    s=int(input("输入学生成绩"))
    assert 0<=s<=100 ,"成绩超出范围"
    return s
try:
    score=get_score()
    print("学生的成绩为",score)
except AssertionError as err:
    print("assertionerror类型的错误被触发",err)