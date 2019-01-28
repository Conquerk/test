l=[2,3,5,7]
it=iter(l)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break
print("----------------------")
for x in l:
    print(x)