""" 题目描述
给定一个正整数 N。你可以对 N 的任意一位数字执行任意次以下 2 种操作:

将该位数字加 1。如果该位数字已经是 9，加 1 之后变成 0。

将该位数字减 1。如果该位数字已经是 0，减 1 之后变成 9。

你现在总共可以执行 1 号操作不超过 A 次，2 号操作不超过 B 次。

请问你最大可以将 N 变成多少?

输入格式
第一行包含 3 个整数：N，A，B 。

输出格式
一个整数代表答案。

输入输出样例
输入 #1复制

123 1 2
输出 #1复制

933
说明/提示
【样例说明】

对百位数字执行 2 次 2 号操作，对十位数字执行 1 次 1 号操作。

【评测用例规模与约定】

对于 30% 的数据，1≤N≤100;0≤A,B≤10

对于 100% 的数据, 1≤N≤10 
17
 ;0≤A,B≤100

蓝桥杯 2022 国赛 B 组 D 题。 """
import sys

s, a, b = sys.stdin.buffer.readline().split()
digits = list(map(int, s.decode()))
a, b = int(a), int(b)
n = len(digits)
def dfs(i, a, b, value):
    if i == n:
        return value
    x = digits[i]
    # 方案一：用加法尽量增大当前位
    k = min(a, 9 - x)
    ans = dfs(i + 1, a - k, b, value * 10 + x + k)

    # 方案二：用减法绕到 9
    # 当前已经是 9 时，不需要花费操作
    if x != 9 and b >= x + 1:
        ans = max(
            ans,
            dfs(i + 1, a, b - x - 1, value * 10 + 9)
        )

    return ans
print(dfs(0, a, b, 0))
