""" 题目描述
约翰经常给产奶量高的奶牛发特殊津贴，于是很快奶牛们拥有了大笔不知该怎么花的钱。为此，约翰购置了 N（1≤N≤2000）份美味的零食来卖给奶牛们。每天约翰售出一份零食。当然约翰希望这些零食全部售出后能得到最大的收益，这些零食有以下这些有趣的特性：

零食按照 1,…,N 编号，它们被排成一列放在一个很长的盒子里。盒子的两端都有开口，约翰每天可以从盒子的任一端取出最外面的一个。
与美酒与好吃的奶酪相似，这些零食储存得越久就越好吃。当然，这样约翰就可以把它们卖出更高的价钱。
每份零食的初始价值不一定相同。约翰进货时，第 i 份零食的初始价值为 V 
i
​
 （1≤V≤1000）。
第 i 份零食如果在被买进后的第 a 天出售，则它的售价是 V 
i
​
 ×a。
V 
i
​
  表示的是从盒子顶端往下的第 i 份零食的初始价值。约翰告诉了你所有零食的初始价值，并希望你能帮他计算一下，在这些零食全被卖出后，他最多能得到多少钱。

输入格式
第一行一个正整数 N。

接下来 2∼N+1 行，第 i+1 行为一个正整数 V 
i
​
 。

输出格式
一行一个整数表示答案。

输入输出样例
输入 #1复制

5
1
3
1
5
2
输出 #1复制

43
说明/提示
样例的最优解是：按 1→5→2→3→4 的顺序卖零食，得到的钱数是 1×1+2×2+3×3+4×1+5×5=43。 """

import sys
input = sys.stdin.buffer.readline
n = int(input())
arr = []
for _ in range(n):
    number = int(input())
    arr.append(number)

# dp[left][right] 表示：
# 剩余零食为闭区间 [left, right] 时，
# 从当前天开始把它们全部卖完所能获得的最大收益
dp = [[0]*(n)for _ in range(n)]

for i in range(n):
    dp[i][i] = arr[i]*n
    #只有一个零食得时候，他在第i天卖完并获得arr[i]*n得收益
for length in range(2,n+1):
    day = n - length + 1
    for left in range(n - length + 1):
        right = length + left - 1
        dp[left][right] = max(
            arr[left]*day + dp[left+1][right],
            arr[right]*day + dp[left][right - 1]
        )

print(dp[0][n-1])
