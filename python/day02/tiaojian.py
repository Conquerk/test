#商场促销　　满100减20
money=int(input("请输入总金额："))
pay=money-20 if money >=100 else money
print("您要支付",pay,"元")