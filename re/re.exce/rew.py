import re
import sys

def get_addres(port):
    f = open('./1.txt')
    while True:
        data=''
        for line in f:
            if line !='\n':
                data+=line
            else:
                break
        #读到文件结尾
        if not data:
            return 'Not found the port'
        #匹配出首个单词
        try:
            PORT = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue

        if port == PORT:
            pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknow)'
            #pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            address = re.search(pattern,data).group(1)
            return address

if __name__ == '__main__':
    while True:
        print('=======================')
        print('|         RE          |')
        print('|       A:查找        |')
        print('|       B:退出        |')
        print('=======================')
        data=input('请输入Ａ或B:')
        if data == 'A':
            port=input('>>')
            print(get_addres(port))
        if data == 'B':
            exit()
        if data != 'A' or 'B':
            print()
            print("输入有误")
            print('请重新输入')