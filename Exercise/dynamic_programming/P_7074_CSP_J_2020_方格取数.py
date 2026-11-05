""" 题目描述
设有 n×m 的方格图，每个方格中都有一个整数。现有一只小熊，想从图的左上角走到右下角，每一步只能向上、向下或向右走一格，并且不能重复经过已经走过的方格，也不能走出边界。小熊会取走所有经过的方格中的整数，求它能取到的整数之和的最大值。

输入格式
第一行有两个整数 n,m。

接下来 n 行每行 m 个整数，依次代表每个方格中的整数。

输出格式
一个整数，表示小熊能取到的整数之和的最大值。

输入输出样例
输入 #1复制

3 4
1 -1 3 2
2 -1 4 -1
-2 2 -3 -1
输出 #1复制

9
输入 #2复制

2 5
-1 -1 -3 -2 -7
-2 -1 -4 -1 -2
输出 #2复制

-10
说明/提示
样例 1 解释

样例 2 解释

数据规模与约定
对于 20% 的数据，n,m≤5。
对于 40% 的数据，n,m≤50。
对于 70% 的数据，n,m≤300。
对于 100% 的数据，1≤n,m≤10 
3
 。方格中整数的绝对值不超过 10 
4
 。
2024/2/4 添加一组 hack 数据。

附件下载
number3.ans
6B
number3.in
23.77KB """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#dp[i][j]表示从起点走到(i,j)点的时候所能获得的最大价值
n,m = read()
g = [[]for _ in range(n)]
for i in range(n):
    g[i] = list(read())

dp = [[float("-inf")]*(m)for _ in range(n)]
#到起始位置就是起始位置本身的价值
dp[0][0] = g[0][0]

#第一列只能从起点开始一直往下走
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + g[i][0]
for j in range(1,m):
    down = [float("-inf")]*n
    up = [float("-inf")]*n
    #向下走
    for i in range(n):
        down[i] = dp[i][j-1]
        if(i>0):
            down[i] = max(down[i],down[i-1])
        down[i] += g[i][j]
    #向上走
    for i in range(n-1,-1,-1):
        up[i] = dp[i][j-1]
        if i + 1 < n:
            up[i] = max(up[i], up[i+1])
        up[i] += g[i][j]

    for i in range(n):
        dp[i][j] = max(down[i],up[i])
print(dp[n-1][m-1])
