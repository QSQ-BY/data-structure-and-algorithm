""" 题目描述
这是一个简单的动规板子题。

给出一个由 n(n≤5000) 个不超过 10 
6
  的正整数组成的序列。请输出这个序列的最长上升子序列的长度。

最长上升子序列是指，从原序列中按顺序尽可能多取出一些数字排在一起，这些数字是逐渐增大的。

输入格式
第一行，一个整数 n，表示序列长度。

第二行有 n 个整数，表示这个序列。

输出格式
一个整数表示答案。

输入输出样例
输入 #1复制

6
1 2 4 1 3 4
输出 #1复制

4
说明/提示
分别取出 1、2、3、4 即可。 """
#求解最长上升子序列
#dp[i]表示长度为i的上升子序列末尾的值
from bisect import bisect_left
import sys
input = sys.stdin.buffer.readline
n = int(input())
arr = list(map(int, input().split()))
dp = []
for number in arr:
    j = bisect_left(dp, number)

    if j == len(dp):
        dp.append(number)
    else:
        dp[j] = number

print(len(dp))