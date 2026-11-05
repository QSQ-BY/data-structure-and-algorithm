""" 题目描述
贝西喜欢在手机上下载游戏来玩，尽管她确实觉得对于自己巨大的蹄子来说，小小的触摸屏用起来相当笨拙。

她对当前正在玩的这个游戏特别感兴趣。游戏开始时给定一个包含 N 个正整数的序列（2≤N≤262,144），每个数的范围在 1…40 之间。在一次操作中，贝西可以选择两个相邻且相等的数，将它们替换为一个比原数大 1 的数（例如，她可以将两个相邻的 7 替换为一个 8）。游戏的目标是最大化最终序列中的最大数值。请帮助贝西获得尽可能高的分数！

输入格式
第一行输入包含 N，接下来的 N 行给出游戏开始时序列的 N 个数字。

输出格式
请输出贝西能生成的最大整数。

输入输出样例
输入 #1复制

4
1
1
1
2
输出 #1复制

3
说明/提示
在示例中，贝西首先合并第二个和第三个 1，得到序列 1 2 2，然后将两个 2 合并为 3。注意，合并前两个 1 并不是最优策略。 """



import sys
from array import array

input = sys.stdin.buffer.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 最大可能产生的数字
limit = max(arr) + n.bit_length() - 1

# dp[v][i] 表示从 i 开始合并成 v 后
# 区间右端点的下一个位置
# 0 表示状态不可达
dp = [array('I', [0]) * (n + 1) for _ in range(limit + 1)]

ans = max(arr)

# 初始化：单个数字本身就是一个合法区间
for i in range(n):
    dp[arr[i]][i] = i + 1

# 枚举目标数字
for v in range(2, limit + 1):
    for i in range(n):

        # 如果已经初始化，直接跳过
        if dp[v][i] != 0:
            continue

        # 从位置 i 开始，先合并出一个 v-1
        j = dp[v-1][i]

        if j == 0:
            continue

        # 从位置 j 开始，继续合并出一个 v-1
        if dp[v-1][j] != 0:
            dp[v][i] = dp[v-1][j]
            ans = max(ans, v)

print(ans)
