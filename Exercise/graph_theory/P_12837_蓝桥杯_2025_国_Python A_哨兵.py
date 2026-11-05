""" 题目背景
建议 Python 用户选择 PyPy3 提交本题。

题目描述
小蓝是一位国王，他的王国里有 n 座城市，通过 n−1 条路来连通。他想在城市中部署三组哨兵 A、B、C，每组哨兵部署在一个城市里面，一个城市可以部署多组哨兵。其中 A 到 B 的距离需要和 A 到 C 的距离相同。小蓝想知道 B 到 C 的距离最大是多少。

输入格式
输入的第一行包含一个正整数 n。

接下来 n−1 行，每行包含两个正整数 u 
i
​
 ,v 
i
​
 ，用一个空格分隔，表示城市 u 
i
​
  和城市 v 
i
​
  之间有一条路。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

8
1 2
1 3
1 4
4 5
4 6
6 7
7 8
输出 #1复制

4
说明/提示
【样例说明】

其中一种方案：A 部署在 5，B 部署在 3，C 部署在 7。

【评测用例规模与约定】

对于 20% 的评测用例，1≤n≤500；

对于所有评测用例，1≤n≤5000，1≤u 
i
​
 ,v 
i
​
 ≤n。

 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
g = [[]for _ in range(n)]
for _ in range(n-1):
    u,v = read()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
#最后的答案就是树的直径，如果直径是奇数那就是树的直径减一
def bfs(start):
    dist = [-1]*(n)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in g[u]:
            if(dist[v] == -1):
                dist[v] = dist[u] + 1
                q.append(v)
    farthest = max(range(n),key = lambda x:dist[x])
    return farthest,dist[farthest]
u,d = bfs(0)
v,ans = bfs(u)
print(ans - ans%2)