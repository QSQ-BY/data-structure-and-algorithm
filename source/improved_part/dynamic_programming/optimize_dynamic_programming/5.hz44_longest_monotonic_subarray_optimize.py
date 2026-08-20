""" 题目描述
有一个数字序列，求其中最长严格上升子序列的长度

B28E0055CAC24D4D8F260936BD6F358F.jpg
输入
输入一个数字n (1≤n≤1000000)，代表数字序列的长度。

后跟 n​ 个整数，第 i​ 个整数 ai(1≤ai≤10000)​，代表数字序列中的第 i​ 个值。

输出
输出一个整数，代表所求的最长严格上升子序列的长度。

样例输入
10
3 2 5 7 4 5 7 9 6 8
样例输出
5
"""
""" dp[i]为以i位置作为结尾的最长上升子序列
dp[i] = max(dp[j]) + 1(j属于1到i-1，且j要小于i) """
import sys
from bisect import bisect_left
input = sys.stdin.buffer.readline

n = int(input())
arr = list(map(int,input().split()))
tails = []
""" dp[i]还是以i位置为结尾的最长上升子序列长度
tails[i]为长度为i的上升子序列中结尾的最小值 """
#使用二分法找到最长的结尾小于当前值的序列的长度
""" dp[i] = binarysearch(val[i]) + 1  
tails[dp[i]] = val[i] """
for i,number in enumerate(arr):
    pos = bisect_left(tails,number)
    if pos == len(tails):
        tails.append(number)
    else:
        tails[pos] = number
print(len(tails))
