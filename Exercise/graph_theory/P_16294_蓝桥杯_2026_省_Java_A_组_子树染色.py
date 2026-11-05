""" 题目描述
给定一棵有 n 个结点的树，结点编号为 1 到 n，其中结点 1 是树根。现在需要在这棵树上选择一些结点进行染色。

树上有 m 个关键结点。对于每个关键结点 x，设其子树大小为 s（子树包含 x 本身及其所有后代），则以 x 为根的子树中，被染色的结点数必须不少于 ⌈ 
2
s
​
 ⌉。

请你求出，在满足所有关键结点要求的前提下，最少需要染色多少个结点。

输入格式
输入共 n+1 行。

第一行包含两个整数 n,m，分别表示结点总数和关键结点数量；

第二行包含 m 个互不相同的整数，表示所有关键结点的编号；

接下来 n−1 行，每行包含两个整数 a,b，表示结点 a 和结点 b 之间有一条边。

输出格式
输出一个整数，表示最少需要染色的结点总数。

输入输出样例
输入 #1复制

10 5
3 4 5 7 10
1 2
1 3
1 4
3 5
3 6
3 7
5 8
5 9
6 10
输出 #1复制

5
说明/提示
【样例说明】
一种最优方案是将结点 4,5,7,9,10 染色，共 5 个结点。

【评测用例规模与约定】
对于 30% 的评测用例，1≤n≤200；

对于所有的评测用例，1≤m≤n≤100000，1≤a,b≤n。 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())

n,m = read()#总结点数与关键节点数
arr = list(read())#关键节点的编号
g = [[]for _ in range(n+1)]
for _ in range(n-1):
    u,v = read()
    g[u].append(v)
    g[v].append(u)

key = [False] * (n + 1)
for u in arr:
    key[u] = True

# 记录父节点，以及父亲在孩子前面的遍历顺序
parent = [0] * (n + 1)
order = [1]

for u in order:
    for v in g[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        order.append(v)

#size[u]表示以u为根节点的子树大小
#dp[v]表示马修女足这一子树内所有关键节点要求至少需要多少次染色
size = [1] * (n + 1)
dp = [0] * (n + 1)

# 倒序后，孩子一定先于父亲处理
for u in reversed(order):
    if key[u]:
        dp[u] = max(dp[u], (size[u] + 1) // 2)

    p = parent[u]
    if p:
        size[p] += size[u]
        dp[p] += dp[u]

print(dp[1])