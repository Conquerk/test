import re

# s='Hello World'
# pattern=r'hello'

# s='''hello world
# hello kitty
# 你好北京
# '''
# pattern=r'.+'

# s='''hello world
# nihao beijing
# '''
# pattern=r'^nihao'
s='''Hello world
nihao beijing
'''
pattern=r'''hello#匹配hello
\s+#匹配空格
world#匹配world
'''
try:
    regex=re.compile(pattern,re.X|re.I)
    s=regex.search(s).group()
except Exception:
    print("没有匹配到内容")
else:
    print(s)