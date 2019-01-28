l=[5,-2,-4,0,3,1]
l2=sorted(l)  #   [-4,-2,0,1,3,5]
print(l2)
l3=sorted(l,reverse=True)
print(l3)
l4=sorted(l,key=abs)
print(l)

name=["tom","jerry","spike","tyke"]
l=sorted(name,key=len)
print(l)
l6=sorted(name)
print(l6)