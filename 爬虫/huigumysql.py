import pymysql
#处理警告的模块
import warnings

#过滤警告
warnings.filterwarnings('ignore')
#创建数据库连接对象
db = pymysql.connect('localhost','root','123456',charset='utf8')
#创建油表对象
cursor = db.cursor()
#利用游标对象的exexute()方法执行命令
cdb='create database if not exists spiderdb1 charset utf8'
udb = 'use spiderdb1'
ctab = 'create table if not exists ttt1(id int)'
ins = 'insert into ttt1 values(3)'
cursor.execute(cdb)
cursor.execute(udb)
cursor.execute(ctab)
cursor.execute(ins)
#提交数据库
db.commit()
#关闭游标对象
cursor.close()
#断开数据库连接
db.close()