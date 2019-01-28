class human():
    def set_info(self,name,age,adress="不祥"):
        self.get_name=name
        self.get_age=age
        self.get_adress=adress
    def show_info(self):
        print("{}{}岁，家庭住址{}".format(self.get_name
        ,self.get_age,self.get_adress))

s1=human()
s1.set_info("小张",20,"深圳南山区")
s2=human()
s2.set_info("小李",30)
s1.show_info()
s2.show_info()