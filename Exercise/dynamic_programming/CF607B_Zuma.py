""" 题目描述
Genos 最近在他的手机上下载了祖玛游戏。在祖玛游戏里，存在 n 个一行的宝石，第 i 个宝石的颜色是 C 
i
​
 。这个游戏的目标是尽快的消灭一行中所有的宝石。

在一秒钟，Genos 能很快的挑选出这些有颜色的宝石中的一个回文的、连续的子串，并将这个子串移除。每当一个子串被删除后，剩余的宝石将连接在一起，形成一个新的行列。

你的任务是：求出把整个宝石串都移除的最短时间。

输入格式
第一行包含一个整数 n(1≤n≤500)，表示宝石串的长度。第二行包含 n 个被空格分开的整数，第 i(1≤i≤n) 个表示这行中第 i 个珠子的颜色。

输出格式
输出一个整数，把这行珠子移除的最短时间。

输入输出样例
输入 #1复制

3
1 2 1
输出 #1复制

1
输入 #2复制

3
1 2 3
输出 #2复制

3
输入 #3复制

7
1 4 4 2 3 2 1
输出 #3复制

2
说明/提示
在第一个例子中，Genos 可以在一秒钟就把这行珠子全部移走。在第二个例子中，Genos 一次只能移走一个珠子，所以移走三个珠子花费他三秒。在第三个例子中，为了达到 2 秒的最快时间，先移除回文串 4 4,再移除回文串 1 2 3 2 1。

感谢 @Administrator2004 提供的翻译 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
#dp[i][j]表示删除[i,j]闭区间内的所有回文的最小操作次数
dp = [[float("inf")]*(n)for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for length in range(2,n+1):
    for i in range(n-length+1):
        j = i+length - 1
        dp[i][j] = length#最坏的情况就是所有，都要单个删除
        if(arr[i] == arr[j]):
            if(length == 2):
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i][j],dp[i+1][j-1])
        for k in range(i,j):
            dp[i][j] = min(dp[i][k] + dp[k+1][j],dp[i][j])
print(dp[0][n-1])

