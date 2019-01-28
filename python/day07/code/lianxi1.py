d=dict([(1,"春季有1，2，3月"),(2,"夏季有4，5，6月"),
(3,"秋季有7，8，9月"),(4,"冬季有10，11，12月")])
print(d)
#遍历
for x in d:
    print(x,d[x])
l=[x for x in d]
print(l)
print(d[1])