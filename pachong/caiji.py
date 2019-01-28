from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.runoob.com/python/python-tutorial.html")
bsobj = BeautifulSoup(html.read())
print(bsobj.h1)  


