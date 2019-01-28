import requests
from lxml import etree
import pymongo

class qiushi:
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/"
        self.headers={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        #连接对象
        self.conn = pymongo.MongoClient('127.0.0.1',27017)
        #库对象
        self.db = self.conn['QiuShidb'] 
        #集合对象
        self.myset = self.db['zhuanye1']
    
    #获取页面
    def getPage(self):
        res = requests.get(self.url,headers = self.headers)
        res.encodeing = "utf-8"
        html = res.text
        self.parsePage(html)

    def parsePage(self,html):
        parseHtml = etree.HTML(html)
        baseList = parseHtml.xpath("//div[contains(@id,'qiushi_tag_')]")
        #for 循环遍历每个段子对象，一个一个提取
        for base in baseList:
            #base :<element at ...>
            #用户昵称
            username = base.xpath("./div/a/h2")
            if username:
                username = username[0].text
            else:
                username = "匿名用户"
            #段子内容
            content = base.xpath("./a/div[@class='content']/span")[0].text
            content = ''.join(content).strip()
            #好笑数量
            laughNum = base.xpath(".//i[@class='number']")[0].text 
            #评论数量
            pingNum = base.xpath(".//i[@class='number']")[1].text

            d = {
                "username":username,
                "content":content,
                "laughNum":laughNum,
                "pingNum":pingNum,
            }
            self.myset.insert_one(d)
    def workOn(self):
        print("正在爬取中......")
        self.getPage()
        print("爬取结束，存入数据库")

if __name__ =="__main__":
    spider = qiushi()
    spider.workOn()


