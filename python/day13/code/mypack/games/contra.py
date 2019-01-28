#mypack/games/contra.py

def play():
    print("正在玩魂斗罗")

print("魂斗罗模块被加载")

def game_over():
    print("游戏结束")
    #绝对导入
    from mypack.menu import show_menu
    show_menu()
    #相对导入
    from ..menu import show_menu
    show_menu()
    #调用　　ｔａｎｋｓ.ｐｌａｙ
    from .tanks import play
    play()
    #另一种方法
    from ..games.tanks import play
    play()
