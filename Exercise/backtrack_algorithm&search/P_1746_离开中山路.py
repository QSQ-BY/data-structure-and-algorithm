""" 题目描述
爱与愁大神买完东西后，打算坐车离开中山路。现在爱与愁大神在 
x
1
,
y
1
x 
1
​
 ,y 
1
​
  处，车站在 
x
2
,
y
2
x 
2
​
 ,y 
2
​
  处。现在给出一个 
n
×
n
(
n
≤
1000
)
n×n(n≤1000) 的地图，
0
0 表示马路，
1
1 表示店铺（不能从店铺穿过），爱与愁大神只能垂直或水平着在马路上行进。爱与愁大神为了节省时间，他要求最短到达目的地距离（每两个相邻坐标间距离为 
1
1）。你能帮他解决吗？

输入格式
第 
1
1 行包含一个数 
n
n。

第 
2
2 行到第 
n
+
1
n+1 行：整个地图描述（
0
0 表示马路，
1
1 表示店铺，注意两个数之间没有空格）。

第 
n
+
2
n+2 行：四个数 
x
1
,
y
1
,
x
2
,
y
2
x 
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
 。

输出格式
只有 
1
1 行，即最短到达目的地距离。

输入输出样例
输入#1
3
001
101
100
1 1 3 3
输出#1
4
说明/提示
对于 
20
%
20% 数据，满足 
1
≤
n
≤
100
1≤n≤100。

对于 
100
%
100% 数据，满足 
1
≤
n
≤
1000
1≤n≤1000。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
g = [["1"]*(n+2) for _ in range(n+2)]
vis = [bytearray(n+2) for _ in range(n+2)]
for i in range(1,n+1):
    g[i] = ["1"] + list(input().decode().strip()) + ["1"]
start_x,start_y,end_x,end_y = read()

directions = [
    (0,1),(0,-1),(-1,0),(1,0),
]

# DFS 教学版：穷举所有可行路径，只适合较小的地图
dfs_vis = [["False"] * (n+2) for _ in range(n+2)]
dfs_ans = float("inf")

def dfs(cur_x,cur_y,step):
    global dfs_ans
    if step >= dfs_ans:
        return
    if cur_x == end_x and cur_y == end_y:
        dfs_ans = step
        return

    dfs_vis[cur_x][cur_y] = True
    for dx,dy in directions:
        nx = cur_x + dx
        ny = cur_y + dy
        if g[nx][ny] != "0" or dfs_vis[nx][ny] == True:
            continue
        dfs(nx,ny,step+1)
    dfs_vis[cur_x][cur_y] = False

def bfs():
    queue = deque([(start_x,start_y,0)])
    vis[start_x][start_y] = True

    while queue:
        cur_x,cur_y,step = queue.popleft()
        if cur_x == end_x and cur_y == end_y:
            return step

        for dx,dy in directions:
            nx = cur_x + dx
            ny = cur_y + dy
            if g[nx][ny] != "0" or vis[nx][ny] == True:
                continue
            vis[nx][ny] = True
            queue.append((nx,ny,step+1))
    return -1

print(bfs())
