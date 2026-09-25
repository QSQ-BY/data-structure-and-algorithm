""" 题目描述
你有一条由 n 个红色的，白色的，或蓝色的珠子组成的项链，珠子是随意安排的。这里是 n=29 的两个例子:



第一和第二个珠子在图片中已经被作记号。

图片 A 中的项链可以用下面的字符串表示：brbrrrbbbrrrrrbrrbbrbbbbrrrrb

假如你要在一些点打破项链，展开成一条直线，然后从一端开始收集同颜色的珠子直到你遇到一个不同的颜色珠子，在另一端做同样的事（颜色可能与在这之前收集的不同）。确定应该在哪里打破项链来收集到最大数目的珠子。

例如，在图片 A 中的项链中，在珠子 9 和珠子 10 或珠子 24 和珠子 25 之间打断项链可以收集到 8 个珠子。

表现含有白珠项链的字符串将会包括三个符号 r，b，w。

写一个程序来确定从一条被给出的项链可以收集到的珠子最大数目。

输入格式
第一行一个正整数 n，表示珠子数目。

第二行一串长度为 n 的字符串，每个字符是 r，b 或 w。

输出格式
输出一行一个整数，表示从给出的项链中可以收集到的珠子的最大数量。

输入输出样例
输入 #1复制

29 
wwwbbrwrbrbrrbrbrwrwwrbwrwrrb
输出 #1复制

11
说明/提示
【数据范围】

对于 100% 的数据，3≤n≤350。

题目翻译来自 NOCOW。

USACO Training Section 1.1 """
import sys

input = sys.stdin.buffer.readline

n = int(input())
original = input().decode().strip()

# 复制三遍，使中间一段的每个断点左右都有足够空间
beads = original * 3
size = len(beads)

# 下标 0 表示红色，下标 1 表示蓝色
left = [[0, 0] for _ in range(size)]
right = [[0, 0] for _ in range(size)]

# 从左向右 DP
for i in range(size):
    bead = beads[i]

    if bead == 'r' or bead == 'w':
        left[i][0] = 1
        if i > 0:
            left[i][0] += left[i - 1][0]

    if bead == 'b' or bead == 'w':
        left[i][1] = 1
        if i > 0:
            left[i][1] += left[i - 1][1]

# 从右向左 DP
for i in range(size - 1, -1, -1):
    bead = beads[i]

    if bead == 'r' or bead == 'w':
        right[i][0] = 1
        if i + 1 < size:
            right[i][0] += right[i + 1][0]

    if bead == 'b' or bead == 'w':
        right[i][1] = 1
        if i + 1 < size:
            right[i][1] += right[i + 1][1]

answer = 0

# 只枚举三倍字符串中间那一段的断点
for cut in range(n, 2 * n):
    # 断点在 cut-1 与 cut 之间
    left_count = max(left[cut - 1])
    right_count = max(right[cut])

    # 不能超过原项链的珠子总数
    collected = min(n, left_count + right_count)
    answer = max(answer, collected)

print(answer)