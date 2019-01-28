poke=["大王","小王"]
kinds=['\u2660','\u2663','\u2665','\u2666']
print(kinds)
numbers=["A"]+[str(x) for x in range(2,11)]+list("JQK")
for k in kinds:
    for n in numbers:
        poke.append(k+n)
poke2=poke.copy()
import random
random.shuffle(poke2)
play1=poke2[0:17]   #给玩家一
play2=poke2[17:34]  #给玩家2
play3=poke2[34:51]  #给玩家3
dipai=poke2[51:]  #底牌
poke2.clear()      # del poke 2
input("请输入回车键发给第1个人")
print(play1)
input("请输入回车键发给第2个人")
print(play2)
input("请输入回车键发给第3个人")
print(play3)
input("请输入回车键底牌")
print(dipai)