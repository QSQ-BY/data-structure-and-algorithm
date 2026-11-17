import sys
input = sys.stdin.buffer.readline
t = int(input())
for _ in range(t):
    n = int(input())
    if(n == 1):
        print("Fang")
        continue
    #小本先手小方后手，当桌子上没有两个相同的卡牌的时候，游戏结束
    #游戏结束的时候如果桌子上恰好之后又一张牌，则小方获胜否则小本获胜
    if((n-1)&n == 0):
        print("Fang")
    else:

        print("Ben")