""" 题目描述
有一头奶牛冲出了围栏，来到了一处圣地（对于奶牛来说），上面用牛语写着一段文字。

现用汉语翻译为：

有 N 个区间，每个区间 x,y 表示提供的 x∼y 共 y−x+1 堆优质牧草。你可以选择任意区间但不能有重复的部分。

对于奶牛来说，自然是吃的越多越好，然而奶牛智商有限，现在请你帮助他。

输入格式
第一行一个整数 N。

接下来 N 行，每行两个数 x,y，描述一个区间。

输出格式
输出最多能吃到的牧草堆数。

输入输出样例
输入 #1复制

3
1 3
7 8
3 4
输出 #1复制

5
说明/提示
1≤n≤1.5×10 
5
 ，0≤x≤y≤3×10 
6
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
intervals = []
for _ in range(n):
    l,r = read()
    intervals.append((l,r))
from bisect import bisect_left

intervals.sort(key=lambda interval: interval[1])
ends = [r for l, r in intervals]
#dp[i]：前 i 个区间中，
# 选出互不重叠区间所能获得的最大长度。
dp = [0] * (n + 1)

for i, (l, r) in enumerate(intervals, start=1):
    # 前面右端点严格小于 l 的区间数量
    prev = bisect_left(ends, l, 0, i - 1)

    dp[i] = max(
        dp[i - 1],             # 不选当前区间
        dp[prev] + r - l + 1    # 选当前区间
    )

print(dp[n])
