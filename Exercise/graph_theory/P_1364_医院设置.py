""" 题目描述
设有一棵二叉树，如图：



其中，圈中的数字表示结点中居民的人口。圈边上数字表示结点编号，现在要求在某个结点上建立一个医院，使所有居民所走的路程之和为最小，同时约定，相邻节点之间的距离为 1。如上图中，若医院建在 1 处，则距离和 =4+12+2×20+2×40=136；若医院建在 3 处，则距离和 =4×2+13+20+40=81。

输入格式
第一行一个整数 n，表示树的结点数。

接下来的 n 行每行描述了一个结点的状况，包含三个整数 w,u,v，其中 w 为居民人口数，u 为左链接（为 0 表示无链接），v 为右链接（为 0 表示无链接）。

输出格式
一个整数，表示最小距离和。

输入输出样例
输入 #1复制

5						
13 2 3
4 0 0
12 4 5
20 0 0
40 0 0
输出 #1复制

81
说明/提示
数据规模与约定
对于 100% 的数据，保证 1≤n≤100，0≤u,v≤n，1≤w≤10 
5
 。 """

#直接暴力枚举每一个点，用BFS进行计算
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
w = [0]*(n+1)
g = [[]for _ in range(n+1)]
for i in range(1,n+1):
    wi,u,v = read()
    w[i] = wi
    if(u):
        g[i].append(u)
        g[u].append(i)
    if(v):
        g[i].append(v)
        g[v].append(i)
best = float("inf")
for s in range(1,n+1):
    dist = [-1]*(n+1)
    dist[s] = 0
    q = deque([s])
    total = 0
    while q:
        x = q.popleft()
        total += w[x]*dist[x]
        for y in g[x]:
            if(dist[y]<0):
                dist[y] = dist[x] + 1
                q.append(y)
    best = min(best,total)
print(best)
