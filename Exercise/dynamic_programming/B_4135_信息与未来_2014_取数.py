""" 题目描述
有 n 个数排成一排，从 n 个数中任取若干个数，取数规则为每次取相邻的 2 个数，不能取 1 个，也不能取多于 2 个连续的数，找一种取法，使取到数的和为最大。

输入格式
第一行一个整数，表示 n； 第二行有 n 个整数，表示 x 
1
​
 ,x 
2
​
 ,⋯,x 
n
​
 。

输出格式
一个整数，即合理取法中最大的和。

输入输出样例
输入 #1复制

6
13 2 17 14 8 16
输出 #1复制

43
说明/提示
2≤n≤10 
5
 ,1≤x 
i
​
 ≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
# dp[i]：必须选择下标 i-1、i 这一对时的最大总和
dp = [float("-inf")] * n

dp[1] = arr[0] + arr[1]
if n >= 3:
    dp[2] = arr[1] + arr[2]
best = 0
for i in range(3, n):
    # 前一对的结束下标最多为 i-3
    best = max(best, dp[i - 3])
    dp[i] = arr[i - 1] + arr[i] + best
print(max(dp))