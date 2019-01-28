import re


pattern = r'(\w+):(\d+)'
s='zhang:1994 li:1993'

# #re直接调用
# l=re.findall(pattern,s)
# print(l)


#通过ｃｏｍｐｌｉｅ生成的对象调用
regex = re.compile(pattern)
l=regex.findall(s,pos=0,endpos=12)
print(l)

l=re.split(r'\s+','Hello  world')
print(l)

s=re.subn(r'\s+','##','hello world nihao a')
print(s)