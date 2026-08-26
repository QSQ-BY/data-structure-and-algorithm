""" 题目描述
图上有一个矩阵，由 N×M 个格子组成，这些格子由两种颜色构成，黑色和白色。请找到面积最大的且内部是黑白交错（即两个相连的正方形颜色不能相同）的正方形。

输入格式
第一行两个整数 N 和 M，分别表示行数和列数。接下来有 N 行，每行 M 个数，0 或 1 分别表示这个格子是黑色或白色。

输出格式
仅有一行，表示满足条件最大正方形的边长。

输入输出样例
输入 #1复制

3 3
0 1 0
1 0 0
1 1 1
输出 #1复制

2 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#dp[i][j]表示以i,j为右下角的最大正方形的边长
n,m = read()
g = [[-1]*(m+2)for _ in range(n+2)]
for i in range(1,n+1):
    g[i] = [-1] + list(read()) + [-1]
#每个点最小就是1个，即他自己
dp = [[1]*(m+2)for _ in range(n+2)]
ans = 0
for i in range(2,n+1):
    for j in range(2,m+1):
        dp[i][j] = 1
        if (g[i][j] == g[i - 1][j - 1]
                and g[i][j] != g[i - 1][j]
                and g[i][j] != g[i][j - 1]):
            dp[i][j] = min(
                dp[i - 1][j],
                dp[i][j - 1],
                dp[i - 1][j - 1]
            ) + 1
            ans = max(ans,dp[i][j])

print(ans)
