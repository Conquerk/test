#创建链接对象
#创建游标对象
#利用游标对象操作数据库
#关闭游标对象
import pymysql
try:
    conn = pymysql.connect(host="localhost",user="root",
                            password='123456',database='t1'
                            ,charset='utf8')
    cur=conn.cursor()

    username = input("请输入用户名:")
    userpwd = input("请输入密码:")
    sql1="select * from user where username='"
    sql1+=username
    sql1+="'"
    sql1+=" and userpwd='"
    sql1+=userpwd
    sql1+="'"
    print(sql1)
    result = cur.execute(sql1)
    print(result)
except:
    print("connect Eroror")