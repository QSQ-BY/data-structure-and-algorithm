""" 题目描述
小 Z 最近捡到了一个 n 行 m 列的棋盘，棋盘上的格子的横纵坐标从 1 开始编号，他想在棋盘上摆放 K 个皇后。他想知道在他摆完这 K 个皇后之后，棋盘上还有多少个格子是不会被攻击到的。

注意：一个皇后会攻击到这个皇后所在的那一行，那一列，以及两条对角线。

输入格式
第一行三个正整数 n,m,K，表示棋盘的行列，以及小 Z 摆放的皇后的个数。

接下来 K 行，每行两个正整数 x,y，表示这个皇后被摆在了第 x 行，第 y 列，数据保证任何两个皇后都不会被摆在同一个格子里。

输出格式
仅一个整数，表示棋盘上还有多少个格子是不会被攻击到的。

输入输出样例
输入 #1复制

12 13 6
10 4
12 10
1 1
2 3
3 2
2 6
输出 #1复制

25
说明/提示
对于 30% 的数据，1≤n,m≤5×10 
3
 ，1≤K≤500；
对于另外 10% 的数据，K=1；
对于 100% 的数据，1≤n,m≤2×10 
4
 ，1≤K≤500。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m,k = read()
row_state = 0
column_state = 0
diagonal_state = 0
back_diagonal_state = 0

for _ in range(k):
    x, y = read()
    row_state |= 1 << (x - 1)
    column_state |= 1 << (y - 1)
    diagonal_state |= 1 << (x + y - 2)
    back_diagonal_state |= 1 << (y - x + n - 1)

full = (1 << m) - 1  # 棋盘内的 m 列
ans = 0

for r in range(1, n + 1):
    if row_state & (1 << (r - 1)):
        continue  # 这一整行都被攻击
    attacked = (
        column_state
        | (diagonal_state >> (r - 1))
        | (back_diagonal_state >> (n - r))
    )
    ans += (full & ~attacked).bit_count()

print(ans)