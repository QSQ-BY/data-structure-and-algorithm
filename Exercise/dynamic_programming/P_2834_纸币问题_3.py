""" 题目背景
你是一个非常有钱的小朋友。

注意： 本题和《进阶篇》的对应题目，输入格式略有差异。

题目描述
你有 n 种面额互不相同的纸币，第 i 种纸币的面额为 a 
i
​
  并且有无限张，现在你需要支付 w 的金额，请问有多少种纸币组合能恰好支付金额 w，答案对 10 
9
 +7 取模。

输入格式
第一行两个正整数 n,w，分别表示纸币的种数和要凑出的金额。
第二行一行 n 个以空格隔开的正整数 a 
1
​
 ,a 
2
​
 ,…a 
n
​
  依次表示这 n 种纸币的面额。

输出格式
一行一个整数，表示能恰好凑齐面额 w 的纸币组合数量。

输入输出样例
输入 #1复制

6 15
1 5 10 20 50 100
输出 #1复制

6
输入 #2复制

3 15
1 5 11
输出 #2复制

5
说明/提示
对于 40% 的数据，满足 n≤10，w≤100；
对于 100% 的数据，满足 1≤n≤10 
3
 ，1≤a 
i
​
 ,w≤10 
4
 。

其实小朋友并不有钱。 """

import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())
MOD = 10**9 + 7
n, target = read()
money = [0] + list(read())

# dp[i][j] 表示使用前 i 种硬币凑出 j 元的方案数
dp = [[0] * (target + 1) for _ in range(n + 1)]

dp[0][0] = 1

for i in range(1, n + 1):
    cur = money[i]
    for j in range(target + 1):
        dp[i][j] = dp[i-1][j]
        if cur <= j:
            dp[i][j] += dp[i][j-cur]

print(dp[n][target]%MOD)