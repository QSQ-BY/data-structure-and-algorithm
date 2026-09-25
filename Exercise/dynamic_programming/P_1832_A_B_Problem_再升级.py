""" 题目背景
题目名称是吸引你点进来的。

实际上该题还是很水的。

题目描述
1+1=? 显然是 2。
a+b=? P1001 回看不谢。
哥德巴赫猜想 似乎已呈泛滥趋势。
以上纯属个人吐槽

给定一个正整数 n，求将其分解成若干个素数之和的方案总数。

输入格式
一行一个正整数 n。

输出格式
一行一个整数表示方案总数。

输入输出样例
输入 #1复制

7
输出 #1复制

3
输入 #2复制

20
输出 #2复制

26
说明/提示
样例解释
存在如下三种方案：

7=7。
7=2+5。
7=2+2+3。
数据范围及约定
对于 30% 的数据 1≤n≤10。
对于 100% 的数据，1≤n≤10 
3
 。 """
import sys
from math import isqrt

input = sys.stdin.buffer.readline

n = int(input())

# 埃氏筛：求出不超过 n 的所有素数
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False

for number in range(2, isqrt(n) + 1):
    if is_prime[number]:
        for multiple in range(number * number, n + 1, number):
            is_prime[multiple] = False

primes = [
    number
    for number in range(2, n + 1)
    if is_prime[number]
]

prime_count = len(primes)

# dp[i][total]：
# 只使用前 i 个素数，组成 total 的方案数量
dp = [
    [0] * (n + 1)
    for _ in range(prime_count + 1)
]

# 不使用任何素数，组成 0 有一种方案
dp[0][0] = 1

for i in range(1, prime_count + 1):
    prime = primes[i - 1]
    for total in range(n + 1):
        # 不使用当前素数
        dp[i][total] = dp[i - 1][total]

        # 至少使用一个当前素数
        if total >= prime:
            dp[i][total] += dp[i][total - prime]

print(dp[prime_count][n])
