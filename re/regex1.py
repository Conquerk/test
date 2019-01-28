import re

pattern = r'\d+'
s = '2008 年事情多,08奥运，512地震'

it=re.finditer(pattern,s)
for x in it:
    #match对象ｇｒｏｕｐ函数获取匹配信息
    print(x.group())
# print(dir(next(it)))
try:
    object=re.fullmatch('\w+','hello1973')
    print(object.group())
except AttributeError as e:
    print(e)
obj= re.match(r'[A-Z]\w+','Hello World')
print(obj.group())

obj=re.search(r'\d+',s)
print(obj.group())

