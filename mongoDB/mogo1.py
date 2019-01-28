from pymongo import MongoClient

conn=MongoClient('localhost',27017)
db=conn.stu
myset=db.class0

# index_name=myset.create_index('name')
# print(index_name)

# index_name=myset.create_index([('age',-1)])

#查看索引
# for i in myset.list_indexes():
#     print(i)
#删除索引
# myset.drop_index('name_1')

#删除所有索引
# myset.drop_indexes()

#创建特殊索引
# myset.create_index('name',unique=True,sparse=True)


#聚合操作
# l=[{'$group':{'_id':'$gender','num':{'$sum':1}}}]

# cursor=myset.aggregate(l)
# for x in cursor:
#     print(x)



conn.close()