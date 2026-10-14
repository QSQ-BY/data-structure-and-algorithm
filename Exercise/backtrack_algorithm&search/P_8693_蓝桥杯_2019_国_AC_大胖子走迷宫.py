""" 题目描述
小明是个大胖子，或者说是个大大胖子，如果说正常人占用 1×1 的面积，小明要占用 5×5 的面积。

由于小明太胖了，所以他行动起来很不方便。当玩一些游戏时，小明相比小伙伴就吃亏很多。小明的朋友们制定了一个计划，帮助小明减肥。计划的主要内容是带小明玩一些游戏，让小明在游戏中运动消耗脂肪。走迷宫是计划中的重要环节。

朋友们设计了一个迷宫，迷宫可以看成是一个由 n×n 个方阵组成的方阵，正常人每次占用方阵中 1×1 的区域，而小明要占用 5×5 的区域。小明的位置定义为小明最正中的一个方格。迷宫四周都有障碍物。为了方便小明，朋友们把迷宫的起点设置在了第 3 行第 3 列，终点设置在了第 n−2 行第 n−2 列。

小明在时刻 0 出发，每单位时间可以向当前位置的上、下、左、右移动单位 1 的距离，也可以停留在原地不动。小明走迷宫走得很辛苦，如果他在迷宫里面待的时间很长，则由于消耗了很多脂肪，他会在时刻 k 变成一个胖子，只占用 3×3 的区域。如果待的时间更长，他会在时刻 2×k 变成一个正常人，只占用 1×1 的区域。注意，当小明变瘦时迷宫的起点和终点不变。

请问，小明最少多长时间能走到迷宫的终点。注意，小明走到终点时可能变瘦了也可能没有变瘦。

输入格式
输入的第一行包含两个整数 n，k。 接下来 n 行，每行一个由 n 个字符组成的字符串，字符为 + 表示为空地， 字符为 * 表示为阻碍物。

输出格式
输出一个整数，表示答案。

输入输出样例
输入 #1复制

9 5
+++++++++
+++++++++
+++++++++
+++++++++
+++++++++
***+*****
+++++++++
+++++++++
+++++++++
输出 #1复制

16
说明/提示
对于 30% 的评测用例, 1≤n≤50。

对于 60% 的评测用例, 1≤n≤100。

对于所有评测用例, 1≤n≤300，1≤k≤1000。

蓝桥杯 2019 年国赛 A 组 F 题（C 组 I 题）。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,k = read()
g = [[]for _ in range(n)]

for i in range(n):
    g[i] = input().decode().strip()
vis1 = [[True] * (n-4) for _ in range(n-4)]
for i in range(n-4):
    for j in range(n-4):
        for a in range(i, i+5):
            for b in range(j, j+5):
                if g[a][b] == "*":
                    vis1[i][j] = False

vis2 = [[True] * (n-2) for _ in range(n-2)]
for i in range(n-2):
    for j in range(n-2):
        for a in range(i, i+3):
            for b in range(j, j+3):
                if g[a][b] == "*":
                    vis2[i][j] = False
from heapq import heappush, heappop,heapify

# s[x][y]：到达该位置的最早时间
s = [[float("inf")] * n for _ in range(n)]
s[2][2] = 0
q = [(0, 2, 2)]
heapify(q)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while q:
    step, x, y = heappop(q)

    # 跳过已经被更早到达时间替代的记录
    if step != s[x][y]:
        continue

    if (x, y) == (n-3, n-3):
        print(step)
        sys.exit()

    for dx, dy in directions:
        nx, ny = x+dx, y+dy

        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if g[nx][ny] == "*":
            continue

        if (2 <= nx < n-2 and 2 <= ny < n-2
                and vis1[nx-2][ny-2]):
            ready = 0
        elif (1 <= nx < n-1 and 1 <= ny < n-1
                and vis2[nx-1][ny-1]):
            ready = k
        else:
            ready = 2*k

        next_step = max(step, ready) + 1

        if next_step < s[nx][ny]:
            s[nx][ny] = next_step
            heappush(q, (next_step, nx, ny))

print(-1)