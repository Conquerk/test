import pymysql
db=pymysql.connect(host="localhost",user="root",password="123456"
,database="db5",charset="utf8")
cur=db.cursor()
try:
    cur.execute("select * from t1;")
    #取走游标里的第一条记录
    sle=cur.fetchone()
    print(sle)
    print("*"*40)
    #取走剩下的ｎ条
    sle2=cur.fetchmany(2)
    for x in sle2:
        print(x)
    print("*"*40)
    #取走游标中剩下的记录
    sle3=cur.fetchall()
    print(sle3)
except Exception as e :
    print("failed",e)
cur.close()
db.close()
    