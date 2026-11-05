""" 题目背景
你知道食物链吗？Delia 生物考试的时候，数食物链条数的题目全都错了，因为她总是重复数了几条或漏掉了几条。于是她来就来求助你，然而你也不会啊！写一个程序来帮帮她吧。

题目描述
给你一个食物网，你要求出这个食物网中最大食物链的数量。

（这里的“最大食物链”，指的是生物学意义上的食物链，即最左端是不会捕食其他生物的生产者，最右端是不会被其他生物捕食的消费者。）

Delia 非常急，所以你只有 1 秒的时间。

由于这个结果可能过大，你只需要输出总数模上 80112002 的结果。

输入格式
第一行，两个正整数 n、m，表示生物种类 n 和吃与被吃的关系数 m。

接下来 m 行，每行两个正整数，表示被吃的生物 A 和吃 A 的生物 B。

输出格式
一行一个整数，为最大食物链数量模上 80112002 的结果。

输入输出样例
输入 #1复制

5 7
1 2
1 3
2 3
3 5
2 5
4 5
3 4
输出 #1复制

5
说明/提示
各测试点满足以下约定：

测试点编号	n	m
1,2	≤40	≤400
3,4	≤100	≤2×10 
3
 
5,6	≤10 
3
 	≤6×10 
4
 
7,8	≤2×10 
3
 	≤2×10 
5
 
9,10	≤5×10 
3
 	≤5×10 
5
 
对于 100% 的数据，1≤n≤5×10 
3
 ,1≤m≤5×10 
5
 

【补充说明】

数据中不会出现环，满足生物学的要求。（感谢 @AKEE） """
import sys
from collections import deque

input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

MOD = 80112002

n, m = read()
#dp[i]表示从入读为0的节点出发到达当前节点的路径数量
dp = [0] * (n + 1)
indegree = [0] * (n + 1)#记录每一个节点的入读
outdegree = [0] * (n + 1)#记录每一个节点的初读
g = [[] for _ in range(n + 1)]#建图

for _ in range(m):
    u, v = read()
    g[u].append(v)
    indegree[v] += 1
    outdegree[u] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = 1
ans = 0#统计食物链的条数
while q:
    u = q.popleft()
    #每次找到一个初读为0的节点就要加上到达当前节点的路径条数
    if outdegree[u] == 0:
        ans = (ans + dp[u]) % MOD
    for v in g[u]:
        dp[v] += dp[u]
        dp[v] %= MOD
        indegree[v] -= 1

        if indegree[v] == 0:
            q.append(v)

print(ans)