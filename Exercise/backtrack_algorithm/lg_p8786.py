""" 题目描述
话说大诗人李白，一生好饮。幸好他从不开车。

一天，他提着酒壶，从家里出来，酒壶中有酒 2 斗。他边走边唱：

无事街上走，提壶去打酒。
逢店加一倍，遇花喝一斗。

这一路上，他一共遇到店 N 次，遇到花 M 次。已知最后一次遇到的是花，他正好把酒喝光了。

请你计算李白这一路遇到店和花的顺序，有多少种不同的可能?

注意：壶里没酒（0 斗）时遇店是合法的，加倍后还是没酒；但是没酒时遇花是不合法的。

输入格式
第一行包含两个整数 N 和 M。

输出格式
输出一个整数表示答案。由于答案可能很大，输出模 1000000007（即 10 
9
+7）的结果。 """
import sys
input = sys.stdin.buffer.readline
from functools import cache
# 现在还剩多少家店、多少朵花，以及当前有多少斗酒
MOD = 1000000007


@cache
def dfs(n: int, m: int, wine: int) -> int:
    # 最后一朵花已经预留，此时必须正好剩 1 斗酒
    if n == 0 and m == 0:
        return int(wine == 1)
    # 剩下的 m 朵花和最后一朵花最多能喝掉 m + 1 斗酒
    if wine == 0 or wine > m + 1:
        return 0
    ans = 0
    # 正向遇店，酒量翻倍
    if n > 0 and wine * 2 <= m + 1:
        ans += dfs(n - 1, m, wine * 2)
    # 正向遇花，喝掉 1 斗酒
    if m > 0 and wine > 0:
        ans += dfs(n, m - 1, wine - 1)
    return ans % MOD
n, m = map(int, input().split())

# 最后一朵花固定在末尾，所以这里只安排前 m - 1 朵花
print(dfs(n, m - 1, 2))
