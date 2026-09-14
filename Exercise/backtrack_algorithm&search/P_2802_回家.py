""" 题目描述

小 H 在一个划分成了 n×m 个方格的长方形封锁线上。 每次他能向上下左右四个方向移动一格（当然小 H 不可以静止不动）， 但不能离开封锁线，否则就被打死了。 刚开始时他有满血 6 点，每移动一格他要消耗 1 点血量。一旦小 H 的血量降到 0， 他将死去。 他可以沿路通过拾取鼠标（什么鬼。。。）来补满血量。只要他走到有鼠标的格子，他不需要任何时间即可拾取。格子上的鼠标可以瞬间补满，所以每次经过这个格子都有鼠标。就算到了某个有鼠标的格子才死去， 他也不能通过拾取鼠标补满 HP。 即使在家门口死去， 他也不能算完成任务回到家中。

地图上有五种格子：

0：障碍物。

1：空地， 小 H 可以自由行走。

2：小 H 出发点， 也是一片空地。

3：小 H 的家。

4：有鼠标在上面的空地。

小 H 能否安全回家？如果能， 最短需要多长时间呢？

输入格式
第一行两个整数 n,m， 表示地图的大小为 n×m。

下面 n 行， 每行 m 个数字来描述地图。

输出格式
一行， 若小 H 不能回家， 输出 -1，否则输出他回家所需最短时间。

输入输出样例
输入 #1复制

3 3
2 1 1
1 1 0
1 1 3
输出 #1复制

4
说明/提示
对于所有数据，1≤n,m≤9。

2021.9.2 增添一组 hack 数据 by @囧仙 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,m = read()
g = [[0]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    g[i] = [0] + list(read()) + [0]
start_x,start_y,end_x,end_y = 0,0,0,0
for i in range(1,n+1):
    for j in range(1,m+1):
        if(g[i][j] == 2):
            start_x,start_y = i,j
        elif(g[i][j] == 3):
            end_x,end_y = i,j
q = deque()
#visit不光要记录是否到达，还需要记录到达时候的血量状态
visit = [[[False]*7 for _ in range(m+2)] for _ in range(n+2)]
directions = [
    (0,1),(0,-1),(1,0),(-1,0),
]
q.append((start_x,start_y,6,0))
visit[start_x][start_y][6] = True
while q:
    x,y,cur_hp,step = q.popleft()
    for dx,dy in directions:
        nx = x + dx
        ny = y + dy
        next_hp = cur_hp-1
        if(next_hp <= 0):
            continue
        if(g[nx][ny] == 0):
            continue
        if(nx <=0 or nx>n or ny<=0 or ny>m):
            continue
        if(g[nx][ny] == 4):
            next_hp = 6
        if visit[nx][ny][next_hp] == True:
            continue
        visit[nx][ny][next_hp] = True
        if(nx == end_x and ny == end_y):
            print(step+1)
            sys.exit()
        q.append((nx,ny,next_hp,step+1))

print(-1)