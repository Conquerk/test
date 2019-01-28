import re

f=open('./day.txt','r')
data=(f.read())

s1=re.findall(r'\b[A-Z]\S*',data)
print('以大写字母开头的单词:',s1)
s2=re.findall(r'(-?\d+\.?/?\d*%?)',data)
print(s2)
f.close()