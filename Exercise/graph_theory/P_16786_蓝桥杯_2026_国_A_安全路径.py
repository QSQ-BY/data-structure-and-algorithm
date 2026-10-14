""" 题目描述
在一个安全网络中，有 n 个通信基站。它们通过 n−1 条双向光纤连接，并形成一棵树。

本题以基站 1 作为整棵树的根。对于任意基站 x, 若以 x 为根的子树中包含的基站总数为偶数, 则称基站 x 为一个平稳基站。这里的子树包含基站 x 本身。

对于两个不同的基站 x 和 y, 若从 x 到 y 的简单路径上经过的所有基站都是平稳基站, 则称有序路径 x→y 是一条安全路径。

请你计算整棵树中安全路径的总数。

注意, x→y 与 y→x 视为两条不同的安全路径。

输入格式
第一行包含一个正整数 n, 表示基站数量。

接下来 n−1 行, 每行包含两个正整数 u,v, 表示基站 u 和基站 v 之间有一条双向光纤。

输入保证给定的 n 个基站和 n−1 条光纤构成一棵树。

输出格式
输出一行, 包含一个整数, 表示安全路径的总数。

输入输出样例
输入 #1复制

6
1 2
1 3
1 6
2 4
3 5
输出 #1复制

6
说明/提示
【样例说明】
以基站 1 为根时:

基站 2 的子树包含基站 2,4, 大小为 2;
基站 3 的子树包含基站 3,5, 大小为 2;
基站 1 的子树包含全部 6 个基站。
因此平稳基站为 1,2,3。

安全路径共有 6 条: 1→2, 1→3, 2→1, 3→1, 2→3, 3→2。

这些路径经过的所有基站均为平稳基站, 因此满足要求。

【评测用例规模与约定】
对于 40% 的数据, 保证 n≤500。

对于所有数据, 保证 1≤n≤500000。 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

n = int(input())

# 邻接表建树
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = read()
    g[u].append(v)
    g[v].append(u)

# 第一步：记录父节点和遍历顺序
parent = [0] * (n + 1)
order = [1]

for u in order:
    for v in g[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        order.append(v)

# 第二步：计算子树大小
size = [1] * (n + 1)

for u in reversed(order):
    if parent[u] != 0:
        size[parent[u]] += size[u]

# 第三步：树形 DP 统计安全路径
dp = [0] * (n + 1)
ans = 0

for u in reversed(order):
    if size[u] % 2 == 0:
        dp[u] += 1
        p = parent[u]

        if p != 0 and size[p] % 2 == 0:
            dp[p] += dp[u]
        else:
            ans += dp[u] * (dp[u] - 1)

print(ans)