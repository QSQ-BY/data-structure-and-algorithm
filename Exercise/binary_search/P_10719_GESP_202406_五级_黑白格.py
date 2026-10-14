""" 题目背景
对应的选择、判断题：https://ti.luogu.com.cn/problemset/1153

题目描述
小杨有一个 n 行 m 列的网格图，其中每个格子要么是白色，要么是黑色。

小杨想知道至少包含 k 个黑色格子的最小子矩形包含了多少个格子。

输入格式
第一行包含三个正整数 n,m,k，含义如题面所示。

之后 n 行，每行⼀个长度为 m 的 01 串，代表网格图第 i 行格子的颜色，如果为 0，则对应格子为白色，否则为黑色。

输出格式
输出一个整数，代表至少包含 k 个黑色格子的最小子矩形包含格子的数量，如果不存在则输出 0。

输入输出样例
输入 #1复制

4 5 5
00000
01111
00011
00011
输出 #1复制

6
说明/提示
样例解释
对于样例 1，假设 (i,j) 代表第 i 行第 j 列，至少包含 5 个黑色格子的最小子矩形的四个顶点为 (2,4)，(2,5)，(4,4)，(4,5)，共包含 6 个格子。

数据范围
对于全部数据，保证有 1≤n,m≤100，1≤k≤n×m。

子任务编号	得分	n,m
1	20	≤10
2	40	n=1，1≤m≤100
3	40	≤100
Update on 2024/7/9：添加了若干组 hack 数据，感谢 @cff_0102 的贡献。 """
import sys
import math

input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

n, m, target = read()

g = [["0"] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    g[i] = ["0"] + list(input().decode().strip())

for i in range(n + 1):
    for j in range(m + 1):
        g[i][j] = int(g[i][j])

prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = (
            g[i][j]
            - prefix[i - 1][j - 1]
            + prefix[i - 1][j]
            + prefix[i][j - 1]
        )
if prefix[n][m] < target:
    print(0)
    sys.exit()
left = 0
right = n * m
# 计算边长为a,b的矩形所能获得的最大黑格子数量
def calculate(a: int, b: int):
    ret = 0
    for i in range(a, n + 1):
        for j in range(b, m + 1):
            k = i - a + 1
            l = j - b + 1
            cur = (
                prefix[i][j]
                + prefix[k - 1][l - 1]
                - prefix[i][l - 1]
                - prefix[k - 1][j]
            )
            ret = max(cur, ret)
    return ret


# 检查面积不超过s的矩形能不能得到target个黑格
def check(s: int):
    # 枚举矩形的高
    for i in range(1, n + 1):
        # 面积不能超过s，所以宽最多为 s // i
        width = min(m, s // i)
        if width == 0:
            continue
        if calculate(i, width) >= target:
            return True
    return False


while left < right:
    mid = (left + right) // 2

    if check(mid):
        right = mid
    else:
        left = mid + 1

print(left)