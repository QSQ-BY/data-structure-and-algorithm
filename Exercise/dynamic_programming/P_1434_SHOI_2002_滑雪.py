""" 题目描述
Michael 喜欢滑雪。这并不奇怪，因为滑雪的确很刺激。可是为了获得速度，滑的区域必须向下倾斜，而且当你滑到坡底，你不得不再次走上坡或者等待升降机来载你。Michael 想知道在一个区域中最长的滑坡。区域由一个二维数组给出。数组的每个数字代表点的高度。下面是一个例子：

1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9

一个人可以从某个点滑向上下左右相邻四个点之一，当且仅当高度会减小。在上面的例子中，一条可行的滑坡为 24−17−16−1（从 24 开始，在 1 结束）。当然 25−24−23−…−3−2−1 更长。事实上，这是最长的一条。

输入格式
输入的第一行为表示区域的二维数组的行数 R 和列数 C。下面是 R 行，每行有 C 个数，代表高度（两个数字之间用 1 个空格间隔）。

输出格式
输出区域中最长滑坡的长度。

输入输出样例
输入 #1复制

5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
输出 #1复制

25
说明/提示
对于 100% 的数据，1≤R,C≤100。

对于任意输入的高度 h，满足 0≤h≤10000，且 h 是整数。 """

import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

n, m = read()
g = [[] for _ in range(n)]

for i in range(n):
    g[i] = list(read())

# dp[i][j]表示以(i,j)为最高点的最长滑雪路径长度
dp = [[1] * m for _ in range(n)]

pos = []
for i in range(n):
    for j in range(m):
        pos.append((i, j))

# 按高度从小到大排序
pos.sort(key=lambda x: g[x[0]][x[1]])

directions = [(1,0), (-1,0), (0,1), (0,-1)]
ans = 1

for i, j in pos:
    for dx, dy in directions:
        ni = i + dx
        nj = j + dy
        if 0 <= ni < n and 0 <= nj < m:
            if g[ni][nj] < g[i][j]:
                dp[i][j] = max(dp[i][j], dp[ni][nj] + 1)
    ans = max(ans, dp[i][j])
print(ans)
