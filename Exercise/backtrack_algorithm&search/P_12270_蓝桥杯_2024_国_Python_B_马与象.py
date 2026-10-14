""" 题目描述
小蓝有一个大小为 N×N 的棋盘（棋子可以走的位置有 (N+1)×(N+1) 个），棋盘上只有两个棋子：一个马和一个象，他们的行动规则是：马走日，马可以走到一个日字形状的对角；象飞田，象可以走到一个田字形状的对角，即斜着走两格（注意无需遵守象棋中的蹩马腿、塞象眼的规则）。在下图所示的大小为 4×4 的棋盘上，展示了两种棋子具体的行进方式：



在任意一方先手、每一方都可以连续走任意步的情况下，请问有没有可能出现一方吃掉另一方的局面，如果有，请输出最少需要经过几步可以达到这个局面，否则输出 −1。注意：棋子不能走出棋盘。

输入格式
输入一行包括五个整数 N,x 
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
  ，相邻整数之间使用一个空格分隔，表示棋盘大小、马的初始位置 (x 
1
​
 ,y 
1
​
 ) 以及象的初始位置 (x 
2
​
 ,y 
2
​
 )。

输出格式
输出一行包含一个整数表示答案。如果答案不存在输出 −1。

输入输出样例
输入 #1复制

4 0 2 1 2
输出 #1复制

3
输入 #2复制

4 2 2 2 3
输出 #2复制

2
说明/提示
样例说明 1


样例说明 2
各走一步可能出现一方吃掉另一方的局面。

评测用例规模与约定
对于 50% 的评测用例，1≤N≤10；
对于所有评测用例，1≤N≤50，0≤x 
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
 ≤N。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,x1,y1,x2,y2 = read()#棋盘大小，马的初始位置，象的初始位置
#马的步数棋盘
g1 = [[-1]*(n+1)for _ in range(n+1)]
#象的步数棋盘
g2 = [[-1]*(n+1)for _ in range(n+1)]
g1[x1][y1] = 0
directions = [
    (1,2),(-1,2),(1,-2),(-1,-2),
    (2,1),(2,-1),(-2,1),(-2,-1),
]

q = deque()
q.append((x1,y1))
while q:
    x,y = q.popleft()
    step = g1[x][y]
    for dx,dy in directions:
        nx = x+dx
        ny = y+dy
        if(nx <0 or nx > n or ny < 0 or ny>n):
            continue
        if(g1[nx][ny] != -1 and g1[nx][ny] <= step+1):
            continue
        g1[nx][ny] = step+1
        q.append((nx,ny))

q = deque()
g2[x2][y2] = 0
directions = [
    (2,2),(-2,-2),(-2,2),(2,-2),
]
q.append((x2,y2))
while q:
    x,y = q.popleft()
    step = g2[x][y]
    for dx,dy in directions:
        nx = x+dx
        ny = y+dy
        if(nx <0 or nx > n or ny < 0 or ny>n):
            continue
        if(g2[nx][ny] != -1 and g2[nx][ny] <= step+1):
            continue
        g2[nx][ny] = step+1
        q.append((nx,ny))

ans = float("inf")
for i in range(n+1):
    for j in range(n+1):
        horse = g1[i][j]
        elephent = g2[i][j]
        if(horse == -1 or elephent == -1):
            continue
        ans = min(ans,horse+elephent)
if(ans == float("inf")):
    print(-1)
else:
    print(ans)

