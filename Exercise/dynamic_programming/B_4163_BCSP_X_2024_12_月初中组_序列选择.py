""" 题目描述
给定两个长度为 n 的序列 a,b，找出一个长为 n 的序列 c，满足对于 i=1,2,⋯,n，有 c 
i
​
 =a 
i
​
  或 c 
i
​
 =b 
i
​
 ，使得 ∑ 
i=2
n
​
 ∣c 
i
​
 −c 
i−1
​
 ∣ 最小，你只需要输出这个最小值。

输入格式
输入的第一行包含一个正整数 n。
接下来一行 n 个整数，表示序列 a 
i
​
 。
接下来一行 n 个整数，表示序列 b 
i
​
 。
输出格式
输出一行一个整数，表示 ∑ 
i=2
n
​
 ∣c 
i
​
 −c 
i−1
​
 ∣ 的最小值。

输入输出样例
输入 #1复制

5
1 3 4 2 5
2 5 4 2 1
输出 #1复制

5
说明/提示
样例 1 解释
令序列 c=[2,3,4,2,1]，此时 ∑ 
i=2
n
​
 ∣c 
i
​
 −c 
i−1
​
 ∣=5，可以证明不存在更小的答案。

样例 2
见附件的 seq/seq2.in 与 seq/seq2.ans。

数据范围
对于 20% 的数据，满足 n≤20。
对于 100% 的数据，满足 1≤n≤2×10 
5
 ，0≤∣a 
i
​
 ∣,∣b 
i
​
 ∣≤10 
9
 。
附件下载
seq.zip
50.62KB """

import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

n = int(input())
a = list(read())
b = list(read())

# dp[i][0]：当前选择a[i]的最小代价
# dp[i][1]：当前选择b[i]的最小代价
dp = [[float("inf")] * 2 for _ in range(2)]

# 初始化
dp[0][0] = 0
dp[0][1] = 0

for i in range(1, n):
    up, down = a[i], b[i]
    cur = i % 2
    pre = 1 - cur

    dp[cur][0] = min(
        dp[pre][0] + abs(a[i-1] - up),
        dp[pre][1] + abs(b[i-1] - up)
    )
    dp[cur][1] = min(
        dp[pre][0] + abs(a[i-1] - down),
        dp[pre][1] + abs(b[i-1] - down)
    )
print(min(dp[(n-1)%2][0], dp[(n-1)%2][1]))
