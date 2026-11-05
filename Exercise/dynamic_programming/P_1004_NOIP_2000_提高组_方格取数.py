""" 题目描述
设有 N×N 的方格图（N≤9），我们将其中的某些方格中填入正整数，而其他的方格中则放入数字 0。如下图所示（见样例）：



某人从图的左上角的 A 点出发，可以向下行走，也可以向右走，直到到达右下角的 B 点。在走过的路上，他可以取走方格中的数（取走后的方格中将变为数字 0）。

此人从 A 点到 B 点共走两次，试找出 2 条这样的路径，使得取得的数之和最大。

输入格式
输入的第一行为一个整数 N，表示 N×N 的方格图。

接下来的若干行，每行有三个整数 x,y,v，表示第 x 行第 y 列的方格中所放的数为 v。

一行单独的 0 表示输入结束。

输出格式
输出一个整数，表示 2 条路径上取得的数的最大总和。

输入输出样例
输入 #1复制

8
2 3 13
2 6 6
3 5 7
4 4 14
5 2 21
5 6 4
6 3 15
7 2 14
0 0 0
输出 #1复制

67 
说明/提示
对于全部测试数据，1≤N≤9，1≤x,y≤N，1≤v≤30。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
g = [[0]*(n+1) for _ in range(n+1)]
while True:
    x,y,v = read()
    if(x == 0 and y==0 and v == 0):
        break
    g[x][y] = v
#两个人都只走一步，所以两个人所在的行号+列号相同
#设这个行号+列号的和为s,则2个人在(row1,s - row1),(row2,s-row2)
#因此只需要三个维度dp[s][row1][row2],避免了使用四个维度dp[x1][y1][x2][y2]来进行状态定义
#表示两个人走到上述位置的时候已经取得到的最大总和
#每个人都可能从上方或者左方走过来
#best = max(
#    dp[s - 1][row1 - 1][row2 - 1],# 两人都从上方来
#    dp[s - 1][row1 - 1][row2],    # 第一人从上方，第二人从左方
#    dp[s - 1][row1][row2 - 1],    # 第一人从左方，第二人从上方
#    dp[s - 1][row1][row2]         # 两人都从左方来
#)

dp = [[[float("-inf")]*(n+1)for _ in range(n+1)]for _ in range(2*n+1)]
dp[2][1][1] = g[1][1]
for s in range(3,2*n+1):
    lower = max(1,s-n)
    upper = min(n,s-1)
    for row1 in range(lower,upper+1):
        col1 = s-row1
        for row2 in range(lower,upper+1):
            col2 = s - row2
            best = max(
                dp[s - 1][row1 - 1][row2 - 1],
                dp[s - 1][row1 - 1][row2],
                dp[s - 1][row1][row2 - 1],
                dp[s - 1][row1][row2]
            )
            gain = g[row1][col1]
            if(row1 != row2):
                gain+= g[row2][col2]
            dp[s][row1][row2] = best + gain

print(dp[2*n][n][n])