""" 题目描述
军团是一个 n 行 m 列的矩阵，每个单元是一个血色先锋军的成员。感染瘟疫的人，每过一个小时，就会向四周扩散瘟疫，直到所有人全部感染上瘟疫。你已经掌握了感染源的位置，任务是算出血色先锋军的领主们感染瘟疫的时间，并且将它报告给巫妖王，以便对血色先锋军进行一轮有针对性的围剿。

输入格式
第 1 行：四个整数 n，m，a，b，表示军团矩阵有 n 行 m 列。有 a 个感染源，b 为血色敢死队中领主的数量。

接下来 a 行：每行有两个整数 x，y，表示感染源在第 x 行第 y 列。

接下来 b 行：每行有两个整数 x，y，表示领主的位置在第 x 行第 y 列。

输出格式
第 1 至 b 行：每行一个整数，表示这个领主感染瘟疫的时间，输出顺序与输入顺序一致。如果某个人的位置在感染源，那么他感染瘟疫的时间为 0。

输入输出样例
输入 #1复制

5 4 2 3
1 1
5 4
3 3
5 3
2 4
输出 #1复制

3
1
3
说明/提示
输入输出样例 1 解释
如下图，标记出了所有人感染瘟疫的时间以及感染源和领主的位置。



数据规模与约定
对于 100% 的数据，保证 1≤n,m≤500，1≤a,b≤10 
5
 。 """

import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m,cnt,q = read()
queue = deque()
g = [[-1]*(m+2)for _ in range(n+2)]#用-1表示还没被访问
for i in range(cnt):
    x,y = read()
    queue.append((x,y))
    g[x][y] = 0

directions = [ 
    (1,0),(0,1),(-1,0),(0,-1)
]
while queue:
    (cur_x,cur_y) = queue.popleft()
    for (dx,dy) in directions:
        nx = cur_x + dx
        ny = cur_y + dy
        if(nx<1 or nx>n or ny<1 or ny>m):
            continue
        if(g[nx][ny] == -1):
            g[nx][ny] = g[cur_x][cur_y] + 1
            queue.append((nx,ny))
ans = []
while q:
    x,y = read()
    ans.append(g[x][y])
    q-=1
for number in ans:
    print(number)
