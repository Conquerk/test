from pymongo import MongoClient
import bson.binary

conn=MongoClient('localhost',27017)
db = conn.image
myset = db.flower

#存储图片
# f = open('test.jpg','rb')
# data=f.read()

#将图片转化为mongodb存储格式
# content=bson.binary.Binary(data)

#插入到集合
# myset.insert({'filename':'flower.jpg','data':content})
img = myset.find_one({'filename':'flower.jpg'})

with open('mm.jpg','wb') as f:
    f.write(img['data'])
conn.close()