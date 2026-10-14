""" 题目描述
程序员小蓝要在今晚重构一个复杂的项目。由于工作强度极高，他需要通过摄入糖分来补充能量，以维持大脑的高速运转。

然而，根据年初体检的报告，小蓝身体的糖分耐受极限为 N 克。一旦体内的糖分超过这个界限，他就会因为血糖过高瞬间昏睡。

起初，小蓝体内的糖分为 0 克。

公司有两种无限供应的甜品：

甜甜圈：每吃一个，体内的糖分增加 a 克。
冰可乐：每喝一罐，体内的糖分增加 b 克。
为了能够安全地摄入更多能量，小蓝在整个重构过程中，可以进行一次开合跳来消耗糖分（最多进行一次），这会立即使他当前体内的糖分减少一半。如果减半后的值不是整数，则直接舍弃小数部分（即向下取整，例如 5 克减半后变为 2 克）。

整个操作过程中，任意时刻小蓝体内的糖分都不得超过耐受极限 N 克。

现在请你帮小蓝计算，在满足上述安全限制的前提下，他最多能让自己体内的糖分达到多少克？

输入格式
输入一行，包含三个用空格隔开的正整数 N、a 和 b，分别表示小蓝身体的糖分耐受极限、食用一个甜甜圈所增加的糖分以及饮用一罐冰可乐所增加的糖分（单位：克）。

输出格式
输出一个整数，表示小蓝在安全范围内能够达到的最大糖分含量（单位：克）。

输入输出样例
输入 #1复制

8 5 6
输出 #1复制

8
说明/提示
【样例说明】
小蓝可以进行如下操作：

吃一个甜甜圈，体内糖分达到 5 克。
做一次开合跳，体内糖分瞬间减半，变为 2 克。
喝一罐冰可乐，体内糖分增加 6 克，达到 8 克。
此时正好达到耐受极限 8，无法再进一步提高，因此输出 8。

【评测用例规模与约定】
对于 30% 的评测用例，1≤N≤500；

对于所有评测用例，1≤N≤10 
6
 , 1≤a,b≤N。 """
import sys
from collections import deque

input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

#使用BFS的做法
def solution1():
    n, a, b = read()

    dp = [[False] * 2 for _ in range(n + 1)]
    dp[0][0] = True

    q = deque([(0, 0)])

    while q:
        i, used = q.popleft()

        for nxt in (i + a, i + b):
            if nxt > n:
                continue

            if dp[nxt][used]:
                continue

            dp[nxt][used] = True
            q.append((nxt, used))

        if used == 0:
            nxt = i // 2

            if not dp[nxt][1]:
                dp[nxt][1] = True
                q.append((nxt, 1))

    for i in range(n, -1, -1):
        if dp[i][0] or dp[i][1]:
            print(i)
            break

def solution2():
    n, a, b = map(int, input().split())

    dp = [False] * (n + 1)
    dp[0] = True

    # 第一阶段：开合跳之前
    for i in range(n + 1):
        if not dp[i]:
            continue

        if i + a <= n:
            dp[i + a] = True

        if i + b <= n:
            dp[i + b] = True

    # 第二阶段：使用开合跳
    for i in range(n + 1):
        if dp[i]:
            dp[i // 2] = True

    # 开合跳之后继续吃甜品
    for i in range(n + 1):
        if not dp[i]:
            continue

        if i + a <= n:
            dp[i + a] = True

        if i + b <= n:
            dp[i + b] = True

    for i in range(n, -1, -1):
        if dp[i]:
            print(i)
            break
solution2()
