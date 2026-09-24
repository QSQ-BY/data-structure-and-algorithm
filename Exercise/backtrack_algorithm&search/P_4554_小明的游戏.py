""" 题目描述
小明最近喜欢玩一个游戏。给定一个 n×m 的棋盘，上面有两种格子 # 和 @。游戏的规则很简单：给定一个起始位置和一个目标位置，小明每一步能向上，下，左，右四个方向移动一格。如果移动到同一类型的格子，则费用是 0，否则费用是 1。请编程计算从起始位置移动到目标位置的最小花费。

输入格式
输入文件有多组数据。

输入第一行包含两个整数 n，m，分别表示棋盘的行数和列数。
输入接下来的 n 行，每一行有 m 个格子（使用 # 或者 @ 表示）。
输入接下来一行有四个整数 x 
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
 ，分别为起始位置和目标位置。
当输入 n，m 均为 0 时，表示输入结束。

输出格式
对于每组数据，输出从起始位置到目标位置的最小花费。每一组数据独占一行。

输入输出样例
输入 #1复制

2 2
@#
#@
0 0 1 1
2 2
@@
@#
0 1 1 0
0 0
输出 #1复制

2
0
说明/提示
对于 20% 的数据满足：1≤n,m≤10。
对于 40% 的数据满足：1≤n,m≤300。
对于 100% 的数据满足：1≤n,m≤500。 """

import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

while True:
    n,m = read()
    if(n==0 and m==0):
        break
    g = [[""]*(m+1) for _ in range(n+1)]
    for i in range(n):
        g[i] = list(input().decode().strip())
        g[i] = g[i]

    start_x,start_y,end_x,end_y = read()
    dis = [[float("inf")]*(m+1) for _ in range(n+1)]
    dis[start_x][start_y] = 0
    q = deque()
    q.append((start_x,start_y))
    directions = [
        (1,0),(0,1),(-1,0),(0,-1),
    ]
    while q:
        x,y = q.popleft()
        if(x == end_x and y == end_y):
            break
        for (dx,dy) in directions:
            nx = x + dx
            ny = y + dy
            if(nx < 0 or nx >= n or ny <0 or ny >= m):
                continue
            if(g[x][y] == g[nx][ny]):
                w = 0
            else:
                w = 1
            next = dis[x][y] + w
            if(dis[nx][ny] <= next):
                continue
            dis[nx][ny] = next
            if(w == 0):
                q.appendleft((nx,ny))
            else:
                q.append((nx,ny))
    if(dis[end_x][end_y] == float("inf")):
        print(-1)
    else:
        print(dis[end_x][end_y])



