""" 题目描述
给定一个长度为 n 的整数序列，要求从中选出两个子段（序列中连续且非空的一段），使得这两个子段中的整数的总和最大，并输出所求的两个子段中的整数的总和。每个子段的最小长度为 1，并且两个子段之间至少间隔一个数。

输入格式
第一行是一个整数，表示 n。

第二行是 n 个整数，表示整数序列。

输出格式
一个整数，表示所求的两个子段中的整数的总和。

输入输出样例
输入 #1复制

5
83 223 -13 1331 -935
输出 #1复制

1637
输入 #2复制

3
83 223 -13
输出 #2复制

70
说明/提示
对于 30% 的数据，有 N≤100。

对于 60% 的数据，有 N≤10 
4
 。

对于 100% 的数据，有 N≤10 
6
 。

数据保证运算过程中的所有数值均在 64 位有符号整型的表示范围内。
 """
import sys
input = sys.stdin.buffer.readline
def read():
    return  map(int,input().split())
n = int(input())
arr = list(read())
limit = 2#直接套用最大k子段和的dp模板，设置limit为2
#end[k][i]表示恰好选择k个不相交的非空区间，且最后一个元素
#恰好在第i个元素结束时能获得的最大收益
end = [[float("-inf")] * (n + 1) for _ in range(limit + 1)]
for i in range(1, n + 1):
    end[1][i] = max(end[1][i - 1], 0) + arr[i - 1]
for k in range(2, limit + 1):
    best = float("-inf")
    for i in range(2 * k - 1, n + 1):
        best = max(best, end[k - 1][i - 2])
        end[k][i] = max(end[k][i - 1], best) + arr[i - 1]

ans = float("-inf")

ans = max(end[2])
print(ans)