""" 题目描述
给定 n 行 m 列共 n×m 个硬币，对于任意一个硬币，我们将其价值视为与其相邻（指上、下、左、右相邻）的硬币中与其正反相同的硬币数的平方。

你可以进行任意次操作，每次可以选择任意一行并将该行的硬币全部翻转。

求所有硬币的价值之和最大可能是多少。

输入格式
输入的第一行包含两个正整数 n,m，用一个空格分隔。

接下来 n 行，每行包含 m 个 0 或 1，表示给定的 n×m 个硬币。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

4 4
1010
1111
1011
1100
输出 #1复制

68
说明/提示
样例说明
如图，实线表示正面，虚线表示反面，翻转最后一行可以得到最大价值和：



评测用例规模与约定
对于 30% 的评测用例，n,m≤20；
对于所有评测用例，1≤n,m≤1000。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,m = read()
g = [input().strip() for _ in range(n)]

#val[i][up][down]表示第i行在上下边界状态分别为up\down时这一行硬币的总价值

val = [[[0]*(2) for _ in range(2)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        horizontal = 0
        if(j>0 and g[i][j] == g[i][j-1]):
            horizontal +=1
        if(j+1 <m and g[i][j] == g[i][j+1]):
            horizontal += 1
        original_up = 0#原来与上方是否相等，相等则为1，不相等则为0
        original_down = 0#原来与下方是否相等，相等则为1，不下跪等则为0
        if(i>0):
            original_up = int(g[i][j] == g[i-1][j])
        if(i+1<n):
            original_down = int(g[i][j] == g[i+1][j])
        for up in range(2):
            for down in range(2):
                same_count = horizontal
                if(i>0):
                    same_count += original_up^up
                if(i+1<n):
                    same_count += original_down^down
                val[i][up][down] += same_count**2

#只有一行的时候。没有任何竖向边界
if n==1:
    print(val[0][0][0])
    sys.exit()

# dp[i][state]：
# 已处理完前 i 行，当前边界状态为 state 时的最大价值
dp = [[0]*2 for _ in range(n+1)]

for i in range(n):
    if i == n-1:
        down_state = (0,)
    else:
        down_state = (0,1)
    for up in range(2):
        for down in down_state:
            dp[i+1][down] = max(dp[i+1][down],dp[i][up] + val[i][up][down]) 

print(dp[n][0])
