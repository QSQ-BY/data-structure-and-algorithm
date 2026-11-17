""" 【问题描述】 
给定一棵包含 n 个点的无向树，点的编号为 1 ∼ n。 
小苯还拿到了一个长度为 n 的排列 p，其中每个点恰好出现一次。 
对于每个前缀长度 k (1 ≤ k ≤ n)，考虑点集 
Sk = {p1, p2, . . . , pk} 
如果在这棵树上存在一条简单路径，使得 Sk 中的所有点都在这条路径上，那么小 
苯称这个前缀是一个“路径前缀”。 
注意，这条路径上可以包含一些不属于 Sk 的点，只要 Sk 中的所有点都落在这条 
路径上即可。 
你的任务就是求出，最大的路径前缀长度是多少。 
【输入格式】 
每个测试文件包含多组测试数据。第一行输入一个整数 T (1 ≤ T ≤ 104 )，表示数 
据组数。 """
import sys

input = sys.stdin.buffer.readline


def solve(g, p):
    n = len(p)
    root = p[0]

    parent = [0] * (n + 1)
    branch = [0] * (n + 1)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)

    timer = 0
    stack = [root]

    while stack:
        u = stack.pop()

        # 负数表示离开这个节点。
        if u < 0:
            tout[-u] = timer
            continue

        tin[u] = timer
        timer += 1
        stack.append(-u)

        for v in g[u]:
            if v == parent[u]:
                continue

            parent[v] = u

            # branch[v] 表示 v 属于根的哪个儿子子树。
            if u == root:
                branch[v] = v
            else:
                branch[v] = branch[u]

            stack.append(v)

    # 子树编号 -> 该子树中最深的已选点。
    ends = {}
    ans = 1

    for x in p[1:]:
        c = branch[x]

        if c not in ends:
            if len(ends) == 2:
                break
            ends[c] = x
        else:
            end = ends[c]

            if tin[end] <= tin[x] < tout[end]:
                # x 在当前端点下方，延长链。
                ends[c] = x
            elif tin[x] <= tin[end] < tout[x]:
                # x 已经在当前链上。
                pass
            else:
                # x 和端点分叉。
                break

        ans += 1

    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    p = list(map(int, input().split()))
    print(solve(g, p))