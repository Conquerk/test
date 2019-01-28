#在t1中增加记录
#在t1中把李白的成绩改为100
#在t1中删除一条记录
import pymysql
db=pymysql.connect(host="localhost",user="root",password="123456"
,database="db5",charset="utf8")
cur=db.cursor()
cur.execute("insert into t1 values(5,'唐玄宗',90);")
print("添加完成")
cur.execute("update t1 set score=100 where name='李白';")
print("修改完成")
cur.execute("delete from t1 where name='白居易';")
print("删除完成")
db.commit()
cur.close()
db.close()

