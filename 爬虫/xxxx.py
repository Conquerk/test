import requests
import pymysql
import re

class NotSpider:
    def __init__(self):
        self.url = "http://code.tarena.com.cn"
        self.headers = {}
        self.auth=('tarenacode','code_2013')
        #库对象
        self.db = pymysql.connect("localhost",'root','123456','spiderdb1',charset='utf8')

        self.cursor= self.db.cursor()

    def getparsePage(self):
        res = requests.get(self.url,auth=self.auth,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        #创建正则
        p = re.compile('<a href="(.*?)/.*?</a>',re.S)
        rlist = p.findall(html)
        print(rlist)
        self.writePage(rlist)

    def writePage(self,rlist):
        ctab = 'create table if not exists tarenanote(name varchar(30))'
        ins= 'insert into tarenanote values(%s)'
        self.cursor.execute(ctab)
        for r in rlist:
            self.cursor.execute(ins,[r])
            self.db.commit()
        #关闭
        self.cursor.close()
        self.db.close()

if __name__ =="__main__":
    spider = NotSpider()
    spider.getparsePage()
    print('成功')
