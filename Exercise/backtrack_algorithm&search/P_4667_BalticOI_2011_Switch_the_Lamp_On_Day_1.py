""" 题目描述
Casper 在一个 N×M 的电路板上设计电路。有一种正方形的电路元件，在它的两组相对顶点中，有一组会用导线连接起来，另一组则不会。有 N×M 个这样的元件，你想将其排列成 N 行，每行 M 个。 电源连接到板的左上角。灯连接到板的右下角。只有在电源和灯之间有一条电线连接的情况下，灯才会亮着。为了打开灯，任何数量的电路元件都可以转动 90°（两个方向）。





在上面的图片中，灯是关着的。如果从右往左数第二列的任何一个电路元件被旋转 90°，电源和灯都会连接，灯被打开。现在请你编写一个程序，求出最小需要旋转多少电路元件。

输入格式
输入的第一行包含两个整数 N 和 M，表示电路板的尺寸。 在以下 N 行中，每一行有 M 个符号 \ 或 /，表示连接对应电路元件对角线的导线的方向。

输出格式
如果可以打开灯，那么输出只包含一个整数，表示最少转动电路元件的数量。

如果不可能打开灯，输出 NO SOLUTION。

输入输出样例
输入 #1复制

3 5
\\/\\
\\///
/\\\\
输出 #1复制

1
说明/提示
对于 40% 的数据，1≤N≤4，1≤M≤5。

对于所有数据，1≤N,M≤500。 """

import sys
from collections import deque

data = sys.stdin.buffer.read().split()
n, m = map(int, data[:2])
g = [row.decode() for row in data[2:2+n]]

dis = [[float("inf")]*(m+1) for _ in range(n+1)]
q = deque()
dis[0][0]= 0
q.append((0,0))
end_x,end_y = n,m
directions = [
    (1,1),(-1,-1),(1,-1),(-1,1)
]
need = ["\\","\\","/","/"]
while q:
    x,y = q.popleft()
    if(x == end_x and y == end_y):
        break
    for k in range(4):
        (dx,dy) = directions[k]
        nx = x + dx
        ny = y + dy
        if(nx <0 or nx > n or ny < 0 or ny > m):
            continue
        cur = g[min(x,nx)][min(y,ny)]
        if(cur == need[k]):
            w = 0
        else:
            w = 1
        nxt = dis[x][y] + w
        if(nxt >= dis[nx][ny]):
            continue
        dis[nx][ny] = nxt
        if(w == 0):
            q.appendleft((nx,ny))
        else:
            q.append((nx,ny))

if(dis[end_x][end_y] == float("inf")):
    print("NO SOLUTION")
else:
    print(dis[end_x][end_y])

