# 用ｗｈｉｌｅ打印10以内的偶数
i=0
while i<10:
    if i%2==1:
        i+=1
        continue
    print(i)
    i+=1