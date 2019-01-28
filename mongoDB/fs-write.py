from pymongo import MongoClient
import gridfs

#链接数据库，生成数据库对象
conn=MongoClient('localhost',27017)
db=conn.grid

#生成Gridfs对象
fs=gridfs.GridFS(db)

#将本地文件读取出来写入到数据库中
with open('./send.JPG','rb') as f:
    fs.put(f.read(),filename='mm.jpg')

conn.close()