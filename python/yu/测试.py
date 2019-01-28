1.描述ｐｙｔｈｏｎ的ＧＣ机制，垃圾机制
2.ｇｌｏｂａｌ和nonlocal　
    global 改变全局作用区域变量
    nonlocal　更改嵌套作用区域变量
4.去重
list=[1,2,3,4,55,66,7,7,8,9,9,9]
result=set(list)  (将列表转化为集合)
result=list(result)
print(result)   得到的是顺序打乱的列表　　　　--见测试.ｐｙ

7.有序容器
    ｌｉｓｔ　ｔｕｐｌｅ　　ｓｔｒ
x.isdigit()  判断是否为数字
age.isnumric()  判断是否为数字　　　　日文　繁体　大写
******保持程序健壮性
8.ａ，ｂ＝ｂ，ａ
  python绑定变量　其他语言是赋值

