from pymongo import MongoClient
import gridfs

#链接数据库，生成数据库对象
conn=MongoClient('localhost',27017)
db=conn.grid

#生成Gridfs对象
fs=gridfs.GridFS(db)

#获取文件集
files=fs.find()

#挑选
for i in files:
    #获取文件名称
    print(i.filename)
    if i.filename == './w.jpg':
        f=open('w.jpg','wb')
        data=i.read()
        f.write(data)

conn.close()