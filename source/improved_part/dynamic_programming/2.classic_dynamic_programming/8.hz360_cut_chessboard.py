""" 题目描述
​ 将一个８*８的棋盘进行如下分割：将原棋盘割下一块矩形棋盘并使剩下部分也是矩形，再将剩下的部分继续如此分割，这样割了(n−1)
(
n
−
1
)
次后，连同最后剩下的矩形棋盘共有 n
n
 块矩形棋盘。(每次切割都只能沿着棋盘格子的边进行)



​ 原棋盘上每一格有一个分值，一块矩形棋盘的总分为其所含各格分值之和。现在需要把棋盘按上述规则分割n
n
块矩形棋盘，并使各矩形棋盘总分的平方和最小。

​ 请编程对给出的棋盘及 n
n
，求出平方和的最小值。

输入
​ 第1
1
行为一个整数n(1<n<15)
n
(
1
<
n
<
15
)
。

​ 第2
2
行至第9
9
行每行为8
8
个小于100
100
的非负整数，表示棋盘上相应格子的分值。每行相邻两数之间用一个空格分隔。

输出
​ 仅一个数，为最小的平方和值。

输入样例1
3
1 1 1 1 1 1 1 3
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 0 
1 1 1 1 1 1 0 3
输出样例1
1460 """

#dp[n][i][j][k][l]代表从（i，j)->(k,l)的矩形切分成n块的最小平方和值
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())#n块切n-1刀
g = [[0]*(9) for _ in range(9)]
dp = [[[[[0]*9 for _ in range(9)]for _ in range(9)]for _ in range(9)] for _ in range(n+1)]
for i in range(1,9):
    g[i] = [0]+list(read())

for i in range(1,9):
    for j in range(1,9):
        g[i][j] += -g[i-1][j-1] + g[i-1][j]+ g[i][j-1]

for i in range(1,9):
    for j in range(1,9):
        for k in range(i,9):
            for l in range(j,9):
                dp[1][i][j][k][l] = (g[k][l]+g[i-1][j-1]-g[k][j-1]-g[i-1][l])**2

for t in range(2,n+1):
    for i in range(1,9):
        for j in range(1,9):
            for k in range(i,9):
                for l in range(j,9):
                    ans = (g[k][l]+g[i-1][j-1]-g[k][j-1]-g[i-1][l])**2
                    for c in range(j,l):
                        val1 = dp[1][i][j][k][c] + dp[t-1][i][c+1][k][l]
                        val2 = dp[t-1][i][j][k][c] + dp[1][i][c+1][k][l]
                        ans = min(ans,val1,val2)
                    for c in range(i,k):
                        val1 = dp[1][i][j][c][l] + dp[t-1][c+1][j][k][l]
                        val2 = dp[t-1][i][j][c][l] + dp[1][c+1][j][k][l]
                        ans = min(ans,val1,val2)
                    dp[t][i][j][k][l] = ans 
print(dp[n][1][1][8][8])