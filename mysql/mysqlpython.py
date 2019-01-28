from pymysql import *

class Mysqlpython:
    def __init__(self,database,host='localhost',user='root',password='123456',charset='utf8'):
        self.database=database
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset
    #创建数据库链接和游标对象
    def open(self):
        self.db=connect(host=self.host,user=self.user,password=self.password,database=self.database,charset=self.charset)
        self.cur=self.db.cursor()
    #关闭游标对象和数据库连接对象
    def close(self):
        self.cur.close()
        self.db.close()
    #执行ｓｑｌ命令
    def zhixing(self,sql,l=[]):
        self.open()
        self.cur.execute(sql,l)
        self.db.commit()
        self.close()
    #查询所有的记录
    def all(self,sql,l=[]):
        self.open()
        self.cur.execute(sql,l)
        result=self.cur.fetchall()
        return result
#if __name__ =="__main__":
 #   sqlh=mysqlpython("db5")
 #   sql="update t1 set score=100 where name='小妹妹'"
 #   sqlh.zhixing(sql)
  #  r1=sqlh.all("select * from t1")
  #  print(r1)