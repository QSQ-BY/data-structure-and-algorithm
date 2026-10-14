""" 题目描述
小明在玩一款迷宫游戏，在游戏中他要控制自己的角色离开一间由 N×N 个格子组成的二维迷宫。

小明的起始位置在左上角，他需要到达右下角的格子才能离开迷宫。

每一步，他可以移动到上下左右相邻的格子中（前提是目标格子可以经过）。

迷宫中有些格子小明可以经过，我们用 . 表示；

有些格子是墙壁，小明不能经过，我们用 # 表示。

此外，有些格子上有陷阱，我们用 X 表示。除非小明处于无敌状态，否则不能经过。

有些格子上有无敌道具，我们用 % 表示。

当小明第一次到达该格子时，自动获得无敌状态，无敌状态会持续 K 步。

之后如果再次到达该格子不会获得无敌状态了。

处于无敌状态时，可以经过有陷阱的格子，但是不会拆除 / 毁坏陷阱，即陷阱仍会阻止没有无敌状态的角色经过。

给定迷宫，请你计算小明最少经过几步可以离开迷宫。

输入格式
第一行包含两个整数 N 和 K。(1≤N≤1000，1≤K≤10)。

以下 N 行包含一个 N×N 的矩阵。

矩阵保证左上角和右下角是 .。

输出格式
一个整数表示答案。如果小明不能离开迷宫，输出 −1。

输入输出样例
输入 #1复制

5 3
...XX
##%#.
...#.
.###.
.....
输出 #1复制

10
输入 #2复制

5 1
...XX
##%#.
...#.
.###.
.....
输出 #2复制

12
说明/提示
时限 3 秒, 256M。蓝桥杯 2018 年第九届国赛 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,k = read()
g = []
s = [[-1]*(n)for _ in range(n)]

for _ in range(n):
    row = input().decode().strip()
    g.append(row)

# . 可以经过 # 不能经过 X 陷阱 % 无敌道具

directions = [
    (1,0),(-1,0),(0,-1),(0,1),
]
end_x,end_y = n-1,n-1
start_x,start_y = 0,0
if(n == 1):
    print(0)
    sys.exit()
s[start_x][start_y] = 0
#现在处在的位置x,y，现在还剩多久的无敌时间t,现在已经走了几步
# s[x][y]：此前到达该位置时，最大的剩余无敌时间
# 初始仍然全部为 -1，表示没有到达过
s[start_x][start_y] = 0

# x, y, 剩余无敌时间, 已走步数
q = deque([(start_x, start_y, 0, 0)])

while q:
    x, y, t, step = q.popleft()
    if x == end_x and y == end_y:
        print(step)
        sys.exit()

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        cell = g[nx][ny]

        if cell == "#":
            continue
#广度优先搜索的顺序天然保证了步数的递增
        # 进入陷阱前必须还有无敌时间
        if cell == "X" and t == 0:
            continue

        # 计算到达新位置后的剩余时间
        if cell == "%":
            nt = k
        else:
            nt = max(t - 1, 0)

        # 以前已经不晚于这次到达，且剩余无敌时间不少
        if nt <= s[nx][ny]:
            continue
        s[nx][ny] = nt
        q.append((nx, ny, nt, step + 1))

print(-1)