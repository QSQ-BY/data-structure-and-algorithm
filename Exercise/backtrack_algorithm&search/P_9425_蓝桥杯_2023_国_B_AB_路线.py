""" 题目描述
有一个由 N×M 个方格组成的迷宫，每个方格写有一个字母 A 或者 B。小蓝站在迷宫左上角的方格，目标是走到右下角的方格。他每一步可以移动到上下左右相邻的方格去。

由于特殊的原因，小蓝的路线必须先走 K 个 A 格子、再走 K 个 B 格子、再走 K 个 A 格子、再走 K 个 B 格子……如此反复交替。

请你计算小蓝最少需要走多少步，才能到达右下角方格？

注意路线经过的格子数不必一定是 K 的倍数，即最后一段 A 或 B 的格子可以不满 K 个。起点保证是 A 格子。

例如 K=3 时，以下 3 种路线是合法的：

AA
AAAB
AAABBBAAABBB

以下 3 种路线不合法：

ABABAB
ABBBAAABBB
AAABBBBBBAAA

输入格式
第一行包含三个整数 N、M 和 K。

以下 N 行，每行包含 M 个字符（A 或 B），代表格子类型。

输出格式
一个整数，代表最少步数。如果无法到达右下角，输出 −1。

输入输出样例
输入 #1复制

4 4 2
AAAB
ABAB
BBAB
BAAA
输出 #1复制

8
说明/提示
样例说明
每一步方向如下：下右下右上右下下；路线序列： AABBAABBA。

评测用例规模与约定
对于 20% 的数据，1≤N,M≤4。
对于另 20% 的数据，K=1。
对于 100% 的数据，1≤N,M≤1000，1≤K≤10。
第十四届蓝桥杯大赛软件赛决赛 C/C++ 大学 B 组 G 题 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,m,k = read()
g = []
for _ in range(n):
    row = input().decode().strip()
    g.append(row)

start_x,start_y = 0,0
end_x,end_y = n-1,m-1
q = deque()
vis = [[0] * m for _ in range(n)]
# 起点已经走了本段的第 1 个 A
vis[start_x][start_y] = 1 << 1
#当前的位置坐标，现在已经是是第几个字母，现在的字母是什么
q.append((start_x,start_y,1,g[0][0],0))
directions = [
    (0,1),(1,0),(-1,0),(0,-1)
]

while q:
    x,y,t,state,step = q.popleft()
    if(x==end_x and y == end_y):
        print(step)
        sys.exit()
    for dx , dy in directions:
        nx = x+dx
        ny = y+dy
        if(nx<0 or nx >=n or ny<0 or ny>=m):
            continue
        if(t != k and g[nx][ny] != state):
            continue
        if(t == k and g[nx][ny] == state):
            continue

        next_step = step + 1
        # 到达下一格后，是这一段的第几个字母
        nt = t + 1 if t < k else 1
        bit = 1 << nt
        #当前这一位是1，说明这个状态已经重复了
        if vis[nx][ny] & bit:
            continue
        vis[nx][ny] |= bit
        if(t!= k and g[nx][ny] == state):
            q.append((nx,ny,nt,state,next_step))
        elif(t == k and g[nx][ny] != state):
            if(state == "A"):
                next_state = "B"
            else:
                next_state = "A"
            q.append((nx,ny,nt,next_state,next_step))

print(-1)
