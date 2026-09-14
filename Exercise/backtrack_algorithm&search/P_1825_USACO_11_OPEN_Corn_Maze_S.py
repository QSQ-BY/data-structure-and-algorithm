""" 题目描述
去年秋天，农夫约翰带着奶牛们参观了一个玉米迷宫。但这不是一个普通的玉米迷宫：它有几个重力驱动的传送滑梯，可以让奶牛瞬间从迷宫中的一个点传送到另一个点。滑梯是双向的：奶牛可以瞬间从滑梯的起点滑到终点，或者从终点滑到起点。如果奶牛踩到滑梯的任一端，她必须使用滑梯。

传送操作不能连续使用，即，传送一次之后，必须通过非传送方式移动至少一步才能再次进行传送。

玉米迷宫的外部完全由玉米包围，只有一个出口。

迷宫可以用一个 N×M（2≤N≤300；2≤M≤300）的网格表示。每个网格元素包含以下项目之一：

玉米（玉米网格元素不可通行）
草地（容易通过！）
滑梯端点（会将奶牛传送到另一个端点）
出口
奶牛只能从一个空间移动到相邻的下一个空间，前提是它们相邻且都不包含玉米。每个草地空间有四个潜在的邻居可以让奶牛到达。从一个草地空间移动到相邻空间需要 1 个时间单位；从一个滑梯端点移动到另一个端点需要 0 个时间单位。

填满玉米的空间用井号（#）表示。草地空间用英文句号（.）表示。滑梯端点对用相同的大写字母（A 到 Z）表示，并且没有两个不同的滑梯端点用相同的字母表示。出口用等号（=）表示。

贝茜迷路了。她知道自己在网格中的位置，并用「at」符号（@）标记了她当前的草地空间。她需要的最短时间是多少才能移动到出口空间？

输入格式
第一行：两个用空格隔开的整数 N 和 M。

第 2∼N+1 行：第 i+1 行描述了迷宫中的第 i 行的情况（共有 M 个字符，每个字符之间没有空格）。

输出格式
一个整数，表示起点到出口所需的最短时间。

输入输出样例
输入 #1复制

5 6
###=##
#.W.##
#.####
#.@W##
######
输出 #1复制

3
说明/提示
例如以下矩阵，N=5,M=6。

###=##
#.W.##
#.####
#.@W##
######

唯一的一个装置的结点用大写字母 W 表示。

最优方案为：先向右走到装置的结点，花费一个单位时间，再到装置的另一个结点上，花费 0 个单位时间，然后再向右走一个，再向上走一个，到达出口处，总共花费了 3 个单位时间。

（由 ChatGPT 4o 翻译） """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m = read()
g = [[""]*m for _ in range(n)]
for i in range(n):
    g[i] = list(input().decode().strip())
connect = [[(-1,-1)]*m for _ in range(n)]
start_x,start_y = -1,-1
end_x,end_y = -1,-1
s = {}
for i in range(n):
    for j in range(m):
        if(g[i][j] == "#" or g[i][j] == "."):
            continue
        if(g[i][j] == "@"):
            start_x = i
            start_y = j
            continue
        if(g[i][j] == "="):
            end_x = i
            end_y = j
            continue
        if(g[i][j] in s):
            x,y = s[g[i][j]]
            connect[x][y] = (i,j)
            connect[i][j] = (x,y)
        else:
            s[g[i][j]] = (i,j)

q = deque()
q.append((start_x,start_y,0))
visit = [[False]*m for _ in range(n)]
directions = [
    (-1,0),(1,0),(0,-1),(0,1),
]
while q:
    x, y, step = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 先检查相邻格是否合法，此时不判断 visit
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if g[nx][ny] == "#":
            continue
        # 踩到传送点，必须传送，只保留传送后的坐标，不可以选择不传送
        if connect[nx][ny] != (-1, -1):
            nx, ny = connect[nx][ny]
        # 对最终落点判重
        if visit[nx][ny]:
            continue
        visit[nx][ny] = True
        if nx == end_x and ny == end_y:
            print(step + 1)
            sys.exit()
        q.append((nx, ny, step + 1))
print(-1)