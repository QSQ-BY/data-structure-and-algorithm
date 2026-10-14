""" 题目描述
约翰有一架用来称牛的体重的天平。与之配套的是 N (1≤N≤1000) 个已知质量的砝码（所有砝码质量的数值都在 32 位带符号整数范围内）。

每次称牛时，他都把某头奶牛安置在天平的某一边，然后往天平另一边加砝码，直到天平平衡，于是此时砝码的总质量就是牛的质量（约翰不能把砝码放到奶牛的那边，因为奶牛不喜欢称体重，每当约翰把砝码放到她的蹄子底下，她就会尝试把砝码踢到约翰脸上）。

天平能承受的物体的质量不是无限的，当天平某一边物体的质量大于 C (1≤C≤2 
30
 ) 时，天平就会被损坏。砝码按照它们质量的大小被排成一行。并且，这一行中从第 3 个砝码开始，每个砝码的质量至少等于前面两个砝码（也就是质量比它小的砝码中质量最大的两个）的质量的和。

约翰想知道，用他所拥有的这些砝码以及这架天平，能称出的质量最大是多少。由于天平的最大承重能力为 C，他不能把所有砝码都放到天平上。

现在约翰告诉你每个砝码的质量，以及天平能承受的最大质量，你的任务是选出一些砝码，使它们的质量和在不压坏天平的前提下是所有组合中最大的。

输入格式
第 1 行输入两个用空格隔开的正整数 N 和 C。

第 2 到 N+1 行：每一行仅包含一个正整数，即某个砝码的质量。保证这些砝码的质量是一个不下降序列。

输出格式
输出一个正整数，表示用所给的砝码能称出的不压坏天平的最大质量。

输入输出样例
输入 #1复制

3 15
1
10
20
输出 #1复制

11 """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline

n, limit = map(int, input().split())

# 使用 1-based 下标
weights = [0]
for _ in range(n):
    w = int(input())
    if w <= limit:
        weights.append(w)

n = len(weights) - 1

prefix = [*accumulate(weights)]
ans = 0

def dfs(k, total):
    global ans

    if ans == limit:
        return

    upper = total + prefix[k]

    # 全选也无法改进答案
    if upper <= ans:
        return

    # 全选也不超重，直接得到当前分支的最优解
    if upper <= limit:
        ans = max(upper,ans)
        return

    # 优先选当前最大的砝码
    if total + weights[k] <= limit:
        dfs(k - 1, total + weights[k])

    # 不选当前砝码
    dfs(k - 1, total)


dfs(n, 0)
print(ans)