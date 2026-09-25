""" 题目描述
长江游艇俱乐部在长江上设置了 n 个游艇出租站 1,2,…,n。游客可在这些游艇出租站租用游艇，并在下游的任何一个游艇出租站归还游艇。游艇出租站 i 到游艇出租站 j 之间的租金为 r 
i,j
​
 （1≤i<j≤n）。试设计一个算法，计算出从游艇出租站 1 到游艇出租站 n 所需的最少租金。

输入格式
第一行中有一个正整数 n，表示有 n 个游艇出租站。接下来的 n−1 行是一个半矩阵 r 
i,j
​
 （1≤i<j≤n）。

输出格式
输出计算出的从游艇出租站 1 到游艇出租站 n 所需的最少租金。

输入输出样例
输入 #1复制

3
5 15
7
输出 #1复制

12
说明/提示
1≤n≤200，保证计算过程中任何时刻数值都不超过 10 
6
。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
#g[i][j]表示从i站点到j站点的租金
g = [[0]*(n+2)for _ in range(n+2)]
for i in range(1,n):
    g[i] = [0]*(i+1) + list(read())

#dp[i]表示到达站点i所需要的最小的资金
dp = [float("inf")]*(n+1)
dp[1] = 0
for i in range(2,n+1):
    for j in range(1,i):
        dp[i] = min(dp[i],dp[j] + g[j][i])

print(dp[n])
