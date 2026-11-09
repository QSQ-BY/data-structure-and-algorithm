""" 题目描述
小蓝从左到右种了 n 棵小树，第 i 棵树的高度为 h 
i
​
 ，相邻树的间隔相同。小蓝想挪走一些树使得剩下的树等间隔分布，且从左到右高度逐渐上升（相邻两棵树高度满足右边的比左边的高），小蓝想知道最多能留下多少棵树。

输入格式
输入的第一行包含一个正整数 n。

第二行包含 n 个正整数 h 
1
​
 ,h 
2
​
 ,⋯,h 
n
​
 ，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

6
3 5 4 7 6 7
输出 #1复制

3
说明/提示
样例说明
留下第 1、3、5 棵树，它们等间隔且从左到右高度逐渐上升。

评测用例规模与约定
对于 30% 的评测用例，1≤n≤500；
对于 60% 的评测用例，1≤n≤3000；
对于所有评测用例，1≤n≤5000，0<h 
i
​
 <10 
6
 。 """

import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

n = int(input())
arr = list(read())

# dp[i][j] 表示以第i棵树结尾，间隔为j时的最大数量
dp = [[1] * n for _ in range(n+1)]

ans = 1

for i in range(1, n+1):
    for j in range(1, n):
        if i-j >= 1 and arr[i-1] > arr[i-j-1]:
            dp[i][j] = dp[i-j][j] + 1
        ans = max(ans, dp[i][j])
print(ans)
