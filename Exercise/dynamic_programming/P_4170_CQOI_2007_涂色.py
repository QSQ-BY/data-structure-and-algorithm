""" 题目描述
假设你有一条长度为 n 的木板，初始时没有涂过任何颜色。你希望把它的 n 个单位长度涂上目标颜色，用一个长度为 n 的字符串表示这个目标。

每次你可以把一段连续的木板涂成一个给定的颜色，后涂的颜色覆盖先涂的颜色。

例如，对于目标字符串 RGBGR ，一种涂色方式为：第一次把木板涂成 RRRRR ，第二次涂成 RGGGR ，第三次涂成 RGBGR ，达到目标。

用尽量少的涂色次数达到目标。

输入格式
输入仅一行，包含一个长度为 n 的字符串，即涂色目标。字符串中的每个字符都是一个大写字母，不同的字母代表不同颜色，相同的字母代表相同颜色。

输出格式
仅一行，包含一个数，即最少的涂色次数。

输入输出样例
输入 #1复制

AAAAA
输出 #1复制

1
输入 #2复制

RGBGR
输出 #2复制

3
说明/提示
40% 的数据满足 1≤n≤10。

100% 的数据满足 1≤n≤50。 """
import sys
input = sys.stdin.buffer.readline

string = input().decode().strip()
#dp[l][r]表示在只对闭区间[l,r]区间内进行涂色的情况下，至少需要进行多少次涂色
n = len(string)
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1

        if string[l] == string[r]:
            dp[l][r] = dp[l][r - 1]
        else:
            dp[l][r] = length
            for k in range(l, r):
                dp[l][r] = min(
                    dp[l][r],
                    dp[l][k] + dp[k + 1][r]
                )
print(dp[0][n - 1])
