lst=[1,2,3,4,55,66,7,7,8,9,9,9]
result=set(lst)#转化为集合
result=list(result)#转化为列表
result.sort(key=lst.index)#从新排列
print(result)
