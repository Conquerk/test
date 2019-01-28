class a:
    # def __bool__(self):
    #     print("bool方法被调用")
    #     return False
    def __len__(self):
        print('len被调用')
        return 5
x=a()
print(bool(x))
if x :
    print("ｘ　为真值")
else:
    print("x　为假值")