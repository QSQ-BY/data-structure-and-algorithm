""" 题目描述
给出 N 个整数，要求从中选出若干个数，使得它们的和尽量接近整数 K。

输入格式
第一行两个正整数 N,K。
第二行 N 个数，表示给出的数字。
输出格式
共一行一个整数，表示最接近 K 的和。如果不唯一，输出较小的那个。

输入输出样例
输入 #1复制

4 12
5 6 9 4
输出 #1复制

11
说明/提示
样例解释
{5,6}

数据范围
对于 40% 的数据，1≤N≤10。
对于 100% 的数据，1≤N≤50,1≤K≤10 
6
 ，给出的数字是 [1,1000] 范围内的整数。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,k = read()
arr = list(read())
total = sum(arr)
#dp[i][j]表示能否用前i张钱币凑出j元钱
dp = [[False]*(total+1)for _ in range(n+1)]
dp[0][0] = True

for i in range(1,n+1):
    x = arr[i-1]
    for j in range(total+1):
        dp[i][j] = dp[i-1][j]
        if(j>=x):
            dp[i][j] = dp[i][j] or dp[i-1][j-x]

ans = 0
for j in range(total+1):
    if(dp[n][j] and abs(j-k) < abs(ans - k)):
        ans = j
print(ans)