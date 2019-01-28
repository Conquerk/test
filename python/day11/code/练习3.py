name=["tom","jerry","spike","tyke"]
#"mot","yrrej","ekips","ekyt"   依据

def fk(s):
    r=s[::-1]
    return r
l=sorted(name,key=fk)
print(l)