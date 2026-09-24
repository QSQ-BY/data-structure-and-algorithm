""" 题目描述
小蓝设计了一台两栖作战机甲，可以根据地形自动切换形态，以适应陆地和水域作战。

作战区域是一个 N×N 的网格。每个格子用字符表示其地形：

0 表示陆地；
1 表示水域。
小蓝初始位于左上角 (1,1)，目标是到达右下角 (N,N)。

每次行动时，小蓝可以向上、下、左、右四个方向中的一个相邻格子移动，但不能离开网格范围。

如果移动后的格子与当前格子的地形不同，机甲会自动切换一次形态；如果两格地形相同，则不需要切换形态。

现在，请你计算：从 (1,1) 移动到 (N,N)，最少需要切换多少次形态。

输入格式
第一行包含一个正整数 N，表示网格的边长。

接下来 N 行，每行是一个长度为 N 的 01 字符串，表示对应一行的地形。

输出格式
输出一个整数，表示从 (1,1) 到 (N,N) 的最少形态切换次数。

输入输出样例
输入 #1复制

5
01100
10110
10001
01111
11010
输出 #1复制

4
说明/提示
【评测用例规模与约定】
对于 30% 的评测用例，1≤N≤8；

对于所有的评测用例，1≤N≤5000。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
n = int(input())
g = [[]for _ in range(n)]
for i in range(n):
    g[i] = list(input().decode().strip())

q = deque()
q.append((0,0))
dis = [[float("inf")]*n for _ in range(n)]
dis[0][0] = 0

directions = [
    (0,1),(0,-1),(-1,0),(1,0)
]

while q:
    x,y = q.popleft()
    if(x == n-1 and y == n-1):
        break
    cur = dis[x][y]
    for (dx,dy) in directions:
        nx = x+dx
        ny = y+dy
        if(nx<0 or nx>=n or ny<0 or ny>=n):
            continue
        if(g[x][y] == g[nx][ny]):
            w = 0
        else:
            w = 1
        next = cur + w
        if(dis[nx][ny] <= next):
            continue
        else:
            dis[nx][ny] = next
            if(w == 0):
                q.appendleft((nx,ny))
            elif(w == 1):
                q.append((nx,ny))

print(dis[n-1][n-1])
