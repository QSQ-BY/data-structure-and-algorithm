""" 题目描述
给出 N 个点的树和 K，问能否把树划分成  
K
N
​
  个连通块，且每个连通块的点数都是 K。

输入格式
第一行，一个整数 T，表示数据组数。接下来 T 组数据，对于每组数据：

第一行，两个整数 N,K。

接下来 N−1 行，每行两个整数 A 
i
​
 ,B 
i
​
 ，表示边 (A 
i
​
 ,B 
i
​
 )。点用 1,2,…,N 编号。

输出格式
对于每组数据，输出 YES 或 NO。

输入输出样例
输入 #1复制

2
4 2
1 2
2 3
3 4
4 2
1 2
1 3
1 4
输出 #1复制

YES
NO
说明/提示
对于 60% 的数据，1≤N,K≤10 
3
 ；
对于 100% 的数据，1≤T≤10，1≤N,K≤10 
5
 。 """


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline

def solve():
    n, k = map(int, input().split())

    #建立邻接表
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 总点数必须能够被 k 整除
    if n % k != 0:
        print("NO")
        return

    #dfs(u, father) 返回以 u 为根的子树中，
    #处理掉完整块以后，
    #剩余的、还必须和父节点连接在一起的节点数量。
    def dfs(u, father):
        size = 1
        for v in graph[u]:
            if v == father:
                continue

            size += dfs(v, u)

        # 正好组成一个大小为 k 的连通块
        if size == k:
            return 0

        return size

    remain = dfs(1, 0)

    if remain == 0:
        print("YES")
    else:
        print("NO")


t = int(input())

for _ in range(t):
    solve()