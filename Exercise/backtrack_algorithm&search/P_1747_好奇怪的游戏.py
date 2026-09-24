""" 题目背景
《爱与愁的故事第三弹·shopping》娱乐章。

调调口味来道水题。

题目描述
爱与愁大神坐在公交车上无聊，于是玩起了手机。一款奇怪的游戏进入了爱与愁大神的眼帘：***（游戏名被打上了马赛克）。这个游戏类似象棋，但是只有黑白马各一匹，在点 x 
1
​
 ,y 
1
​
  和 x 
2
​
 ,y 
2
​
  上。它们得从点 x 
1
​
 ,y 
1
​
  和 x 
2
​
 ,y 
2
​
  走到 (1,1)。这个游戏与普通象棋不同的地方是：马可以走“日”，也可以像象走“田”。现在爱与愁大神想知道两匹马到 (1,1) 的最少步数，你能帮他解决这个问题么？

注意不能走到 x 或 y 坐标 ≤0 的位置。满足此限制的 (x,y) 均可到达。

输入格式
第一行两个整数 x 
1
​
 ,y 
1
​
 。

第二行两个整数 x 
2
​
 ,y 
2
​
 。

输出格式
第一行一个整数，表示黑马到 (1,1) 的步数。

第二行一个整数，表示白马到 (1,1) 的步数。

输入输出样例
输入 #1复制

12 16
18 10
输出 #1复制

8 
9
说明/提示
数据范围及约定
对于 100% 数据，1≤x 
1
​
 ,y 
1
​
 ,x 
2
​
 ,y 
2
​
 ≤20。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

x1,y1 = read()
x2,y2 = read()
n = max(x1,x2)
m = max(y1,y2)

#传入开始的点的坐标
def solve(x,y):
    g = [[float("inf")]*(m+4)for _ in range(n+4)]
    end_x = 1
    end_y = 1
    directions = [
        (1,2),(1,-2),(-1,2),(-1,-2),(2,2),(2,-2),(-2,2),(-2,-2),
        (2,1),(2,-1),(-2,1),(-2,-1)
    ]
    g[x][y] = 0
    q = deque()
    q.append((x,y))
    while q:
        cur_x,cur_y = q.popleft()
        if(cur_x == end_x and cur_y == end_y):
            break
        for dx,dy in directions:
            nx = cur_x + dx
            ny = cur_y + dy
            if(nx<=0 or nx >= n+3 or ny<=0 or ny>=m+3):
                continue
            nxt = g[cur_x][cur_y] + 1
            if(g[nx][ny] <= nxt):
                continue
            g[nx][ny] = nxt
            q.append((nx,ny))
    return g[end_x][end_y]


ans1 = solve(x1,y1)
ans2 = solve(x2,y2)
print(ans1)
print(ans2)
