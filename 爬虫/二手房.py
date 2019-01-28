from bs4 import BeautifulSoup
import pymongo
import requests
class ERshou:
    def __init__(self):
        self.baseurl = 'https://bj.lianjia.com/ershoufang/pg'
        self.headers={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['Lianjia']
        self.myset=self.db['houseInfo']
    def getpage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding='utf-8'
        html = res.text
        self.parsepage(html)
    def parsepage(self,html):
        #创建解析对象
        soup = BeautifulSoup(html,'lxml')
        #find_all()获取每个房源信息
        rlist = soup.find_all('li',attrs={'class':'clear LOGCLICKDATA'})
        for r in rlist:
            ######################################
            #housrInfo节点
            Info = r.find('div',attrs={"class":'houseInfo'}).get_text().split('/')
            #小区名称
            name = Info[0]
            #户型
            huxing = Info[1]
            #面积
            area = Info[2]
            ######################################
            positionInfo = r.find('div',attrs={'class':'positionInfo'}).get_text().split('/')
            #楼层
            louceng = positionInfo[0]
            #年份
            year = positionInfo[1]
            #地点
            address = positionInfo[2]
            ###########################################################################
            #总价
            totalPrice = r.find('div',attrs={"class":'totalPrice'}).get_text()
            #单价
            unitPrice = r.find('div',attrs={"class":'unitPrice'}).get_text()
            ###########################################################################
            d = {
                "名称":   name,
                "户型":huxing,
                "面积":area,
                "楼层":louceng,
                "年份":year,
                "地点":address,
                "单价":unitPrice,
                "总价":totalPrice
            }
            self.myset.insert_one(d)
    def workon(self):
        num = int(input('请输入要爬取的页数:'))
        for pg in range(1,num+1):
            #拼接ｕｒｌ
            url = self.baseurl + str(pg) + '/'
            self.getpage(url)
            print('第{}页爬取成功'.format(pg))

if __name__ =="__main__":
    spider = ERshou()
    spider.workon()
