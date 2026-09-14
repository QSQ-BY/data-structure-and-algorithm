""" 题目描述
贝茜听说一场特别的流星雨即将到来：这些流星会撞向地球，并摧毁它们所撞击的任何东西。她为自己的安全感到焦虑，发誓要找到一个安全的地方（一个永远不会被流星摧毁的地方）。

如果将牧场放入一个直角坐标系中，贝茜现在的位置是原点，并且，贝茜不能踏上一块被流星砸过的土地。

根据预报，一共有 M 颗流星 (1≤M≤50,000) 会坠落在农场上，其中第 i 颗流星会在时刻 T 
i
​
 （0≤T 
i
​
 ≤1000）砸在坐标为 (X 
i
​
 ,Y 
i
​
 )(0≤X 
i
​
 ≤300，0≤Y 
i
​
 ≤300) 的格子里。流星的力量会将它所在的格子，以及周围 4 个相邻的格子都化为焦土，当然贝茜也无法再在这些格子上行走。

贝茜在时刻 0 开始行动，她只能在横纵坐标 X,Y≥0 的区域中，平行于坐标轴行动，每 1 个时刻中，她能移动到相邻的（一般是 4 个）格子中的任意一个，当然目标格子要没有被烧焦才行。如果一个格子在时刻 t 被流星撞击或烧焦，那么贝茜只能在 t 之前的时刻在这个格子里出现。 贝茜一开始在 (0,0)。

请你计算一下，贝茜最少需要多少时间才能到达一个安全的格子。如果不可能到达输出 −1。

输入格式
共 M+1 行，第 1 行输入一个整数 M，接下来的 M 行每行输入三个整数分别为 X 
i
​
 ,Y 
i
​
 ,T 
i
​
 。

输出格式
贝茜到达安全地点所需的最短时间，如果不可能，则为 −1。

输入输出样例
输入 #1复制

4
0 0 2
2 1 2
1 1 2
0 3 5
输出 #1复制

5 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
M = int(input())
pot = []
max_x = 0
max_y = 0
for i in range(M):
    x,y,t = read()
    pot.append((x,y,t))
    max_x = max(x,max_x)
    max_y = max(max_y,y)
#g[i][j]表示坐标为ij的点会在时间为多少的时候被毁掉
g = [[-1]*(max_y + 4)for _ in range(max_x + 4)]
directions1 = [
    (1,0),(-1,0),(0,1),(0,-1)
]
for (x,y,t) in pot:
    if(g[x][y] == -1):
        g[x][y] = t
    else:
        g[x][y] = min(g[x][y] , t)
    for (dx,dy) in directions1:
        nx = x + dx
        ny = y + dy
        if(nx<0 or ny<0):
            continue
        if(g[nx][ny] == -1):
            g[nx][ny] = t
        else:
            if(g[nx][ny] > t):
                g[nx][ny] = t

q = deque()
q.append((0,0,0))#横纵坐标与到达时间
visited = [[False]*(max_y + 4)for _ in range(max_x + 4)]
ans = -1
directions2 = [
    (0,1),(1,0),(0,-1),(-1,0)
]

if(g[0][0] == -1):
    print(0)
    sys.exit()
if(g[0][0] == 0):
    print(-1)
while q:
    (x,y,t) = q.popleft()
    for (dx,dy) in directions2:
        nx = x + dx
        ny = y + dy
        nt = t + 1
        if(nx<0 or ny<0):
            continue
        if(g[nx][ny] == -1):
            ans = nt
            print(ans)
            sys.exit()
        if(g[nx][ny] <= nt):
            continue
        if(visited[nx][ny] == True):
            continue
        visited[nx][ny] = True
        q.append((nx, ny, nt))
print(-1)