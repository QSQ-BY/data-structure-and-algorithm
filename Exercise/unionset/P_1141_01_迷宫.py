""" 题目描述
有一个仅由数字 
0
0 与 
1
1 组成的 
n
×
n
n×n 格迷宫。若你位于一格 
0
0 上，那么你可以移动到相邻 
4
4 格中的某一格 
1
1 上，同样若你位于一格 
1
1 上，那么你可以移动到相邻 
4
4 格中的某一格 
0
0 上。

你的任务是：对于给定的迷宫，询问从某一格开始能移动到多少个格子（包含自身）。

输入格式
第一行为两个正整数 
n
,
m
n,m。

下面 
n
n 行，每行 
n
n 个字符，字符只可能是 
0
0 或者 
1
1，字符之间没有空格。

接下来 
m
m 行，每行两个用空格分隔的正整数 
i
,
j
i,j，对应了迷宫中第 
i
i 行第 
j
j 列的一个格子，询问从这一格开始能移动到多少格。

输出格式
m
m 行，对于每个询问输出相应答案。

输入输出样例
输入#1
2 2
01
10
1 1
2 2
输出#1
4
4
说明/提示
对于样例，所有格子互相可达。

对于 
20
%
20% 的数据，
n
≤
10
n≤10；
对于 
40
%
40% 的数据，
n
≤
50
n≤50；
对于 
50
%
50% 的数据，
m
≤
5
m≤5；
对于 
60
%
60% 的数据，
n
,
m
≤
100
n,m≤100；
对于 
100
%
100% 的数据，
1
≤
n
≤
1000
1≤n≤1000，
1
≤
m
≤
100000
1≤m≤100000。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
sys.setrecursionlimit(50000)
n,q = read()
g = [["#"] *(n+2) for _ in range(n+2)]
for i in range(1,n+1):
    g[i] = ["#"] + list(input().decode().strip()) + ["#"]
answers = []
directions = [
    (1,0),(0,1),(-1,0),(0,-1)
]
component = [[0]*(n+2) for _ in range(n+2)]
component_size = [0]
def solve1(start_x,start_y)->int:
    ret = 0
    vis = [[False]*(n+2) for _ in range(n+2)]
    def dfs(cur_x,cur_y)->bool:
        nonlocal ret
        nonlocal vis
        if(vis[cur_x][cur_y] == True):
            return False
        vis[cur_x][cur_y] = True
        ret += 1
        cur_state = g[cur_x][cur_y]
        next_state = "0"
        if(cur_state == "0"):
            next_state = "1"
        for (dx,dy) in directions:
            nx = cur_x + dx
            ny = cur_y + dy
            if(g[nx][ny] != next_state):
                continue
            if(vis[nx][ny] == True):
                continue
            if(dfs(nx,ny)):
                return True
        return False
    dfs(start_x,start_y)
    return ret

def solve2(start_x,start_y)->int:
    component_id = component[start_x][start_y]
    if(component_id != 0):
        return component_size[component_id]

    component_id = len(component_size)
    component_size.append(0)
    component[start_x][start_y] = component_id

    queue = deque([(start_x,start_y)])
    ret = 0
    while(queue):
        cur_x,cur_y = queue.popleft()
        ret += 1

        cur_state = g[cur_x][cur_y]
        next_state = "1" if cur_state == "0" else "0"
        for dx,dy in directions:
            nx = cur_x + dx
            ny = cur_y + dy
            if(component[nx][ny] != 0):
                continue
            if(g[nx][ny] != next_state):
                continue
            component[nx][ny] = component_id
            queue.append((nx,ny))

    component_size[component_id] = ret
    return ret

while(q):
    x,y = read()
    answers.append(solve2(x,y))
    q -= 1
for ans in answers:
    print(ans)
