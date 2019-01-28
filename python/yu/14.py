total_money=100000
def cunqian(money):
    global total_money
    total_money+=money
    print("存钱成功")
    print("剩余存款为：",total_money)
def quqian(money):
    global total_money
    if money > total_money:
        print("取钱失败")
    else:
        total_money-=money
        print("剩余存款为：",total_money)
        print("取钱成功")
quqian(200000)
cunqian(20000)     
quqian(200000)