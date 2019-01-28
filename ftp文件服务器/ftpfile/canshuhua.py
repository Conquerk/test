import pymysql
db=pymysql.connect(host="localhost",user="root",password="123456"
,database="db5",charset="utf8")
cur=db.cursor()
while True:
    c=input("请输入ｑ退出,空格将继续输入:")
    if c.strip().lower() =="q":
        break
    name=input("请输入姓名:")
    score=input("请输入成绩:")
try:
    insert="insert into t1(name,score) values(%s,%s)"
    #execute（参数，列表）
    cur.execute(insert,[name,score])
    db.commit()
    print("插入完成")
except Exception as e:
    print("failed",e)
    db.rollback()
cur.close()
db.close()