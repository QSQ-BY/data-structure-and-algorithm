""" 题目背景
IOI2000 第一题

题目描述
回文词是一种对称的字符串。任意给定一个字符串，通过插入若干字符，都可以变成回文词。此题的任务是，求出将给定字符串变成回文词所需要插入的最少字符数。

比如 Ab3bd 插入 2 个字符后可以变成回文词 dAb3bAd 或 Adb3bdA，但是插入少于 2 个的字符无法变成回文词。

注意：此问题区分大小写。

输入格式
输入共一行，一个字符串。

输出格式
有且只有一个整数，即最少插入字符数。

输入输出样例
输入 #1复制

Ab3bd
输出 #1复制

2
说明/提示
数据范围及约定
记字符串长度为 l。

对于全部数据，0<l≤1000。 """
import sys
input = sys.stdin.buffer.readline

string = input().decode().strip()
n = len(string)

#dp[i][j]表示把[i,j]区间之内的字符串编程回文串所需的最小次数

dp = [[float("inf")]*(n) for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for length in range(2,n+1):
    for left in range(n - length + 1):
        right = left+ length - 1
        if(string[left] == string[right]):
            if(length == 2):
                dp[left][right] = 0
            else:
                dp[left][right] = dp[left+1][right - 1]

        elif(string[left] != string[right]):
            dp[left][right] = min(
                dp[left+1][right],
                dp[left][right-1],
            ) + 1
print(dp[0][n-1])