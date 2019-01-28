import pymongo

#创建数据库连接对象
conn = pymongo.MongoClient('localhost',27017)

#创建库对象
db = conn.spiderdb
#创建集合对象
myset = db.t1

#在集合中插入一条文档
myset.insert_one({'name':'Tom'})

print('success')