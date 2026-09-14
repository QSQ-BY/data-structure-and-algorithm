""" 哈利•波特作为三强争霸赛的第四名选手，历尽艰险闯到了最后一关——迷宫。

现在，迷宫里只剩下哈利和塞德里克了，哈利只有在塞德里克前面拿到奖杯，才能赢得比赛。哈利只要能看到奖杯，就可以用飞来咒拿到它，所以，现在的问题是哈利如何能尽早地看到奖杯。

题目描述
哈利的视力非常好，他能从迷宫的一端沿直线看到迷宫的另一端（但他只能看八个方向——东北，东，东南，南，西南……），而且他跑得非常快，跑一步（向上、下、左、右移动一格）只需要 1s。但迷宫是不透光的，而且，要烧掉迷宫的墙也不容易，所以哈利决定绕到一个能够看到奖杯的地方。现在，哈利希望你能帮他确定最短需要多长时间才能拿到奖杯。

我们规定，迷宫左上角的坐标为 (1,1)，右下角坐标为 (N,M)。

输入格式
第一行为 2 个数 N,M 表示迷宫的规模（N 为高，M 为宽）。

接下来是 N×M 的迷宫，O 表示空地，X 表示墙。

最后是多对数据，分别是奖杯坐标及哈利的坐标（显然不可能在墙上），每对占一行，0 为结束标志。

输出格式
根据每对数据，计算哈利拿到奖杯的最短时间，每对一行。如果魔法部有意难为选手，用墙将奖杯包围了起来，输出 Poor Harry。

输入输出样例
输入 #1复制

3 4
OXXO
XXOO
XOOO
3 2 2 4
3 3 1 1
0 0 0 0
输出 #1复制

1
Poor Harry
说明/提示
对于 30% 的数据，有 N×M≤100；

对于 60% 的数据，有 N×M≤1600；

对于 100% 的数据，有 N×M≤16384。

询问数据对数不超过 512。 """
import sys
import gc
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n, m = read()
g = ["X" * (m+2)] *(n+2)
for i in range(1,n+1):
    g[i] = "X" + input().decode().strip() + "X"
directions = [
    (1,0),(-1,0),(0,1),(0,-1),
]
directions2 = [
    (1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)
]
query_count = 0
while(1):
    query_count += 1
    if(query_count % 8 == 0):
        gc.collect()
    target_x,target_y,start_x,start_y = read()
    if(start_x == 0 and start_y == 0 and target_x==0 and target_y==0):
        sys.exit()
    can_see = [bytearray(m+2) for _ in range(n+2)]
    visit = [bytearray(m+2) for _ in range(n+2)]
    can_see[target_x][target_y] = True
    for (dx,dy) in directions2:
        for stride in range(1,max(n,m) + 1):
            nx = dx*stride + target_x
            ny = dy*stride + target_y
            if(nx <=0 or nx>n or ny<=0 or ny>m):
                break
            if(g[nx][ny] == "X"):
                break
            can_see[nx][ny] = True
    if can_see[start_x][start_y]:
        print(0)
        continue
    q = deque()
    q.append((start_x ,start_y,0))
    visit[start_x][start_y] = True
    flag = 0
    while q:
        if(flag == 1):
            break
        x,y,step = q.popleft()
        for (dx,dy) in directions:
            nx = x+dx
            ny = y+dy
            if(g[nx][ny] == "X"):
                continue
            if(visit[nx][ny] == True):
                continue
            visit[nx][ny] = True
            if(can_see[nx][ny] == True):
                print(step+1)
                flag = 1
                break
            q.append((nx,ny,step+1))
    if(flag == 0):
        print("Poor Harry")

