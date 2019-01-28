f=open("data.txt")
s1=f.readline()
s2=f.readline()
s3=f.readline()
l=[s1,s2,s3]
for x in l:
    print("性名:",x[0:2],"电话:",x[3:],end="")
print("")
d={}
for x in l :
    d={}
    d["name"]=x[0:2]
    d["num"]=x[3:]
    print("姓名:",d["name"],"电话:",d["num"],end="")
print("")
 