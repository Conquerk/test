import re

pattern=r'(ab)cd(?P<dog>ef)'

regex= re.compile(pattern)

#获取match对象
obj=regex.search('abcdefgh',pos=0,endpos=6)

#obj属性
print('=============================')
print('目标字符串的开始位置',obj.pos)
print('目标字符串的结束位置',obj.endpos)
print('正则表达式为：',obj.re)
print('目标字符串为:',obj.string)
print('最后一组的组名:',obj.lastgroup)
print('最后一组是第%d组'%obj.lastindex)
print('=============================')
print('匹配内容的起止位置',obj.span())
print('匹配内容的开始位置',obj.start())
print('匹配内容的结束位置',obj.end())
print('=============================')
print('默认获取正则匹配到的内容:',obj.group())
print('通过序列号获取子组的内容:',obj.group(1))
print('通过组名获取子组的内容：',obj.group('dog'))
print('=============================')
print("获取捕获组字典为：",obj.groupdict())
print('获取每个子组匹配到的内容:',obj.groups())
print('=============================')