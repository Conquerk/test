kg=float(input("请输入体重："))
m=float(input("请输入身高："))
BMI=kg/(m**2)
if BMI<18.5:
    print("体重过轻")
elif 18.5<=BMI<=24:
    print("正常范围")
else:
    print("体重超标")