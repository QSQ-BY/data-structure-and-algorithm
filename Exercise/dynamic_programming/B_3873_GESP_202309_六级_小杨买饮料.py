""" 题目背景
对应的选择、判断题：https://ti.luogu.com.cn/problemset/1132

题目描述
小杨来到了一家商店，打算购买一些饮料。这家商店总共出售 N 种饮料，编号从 0 至 N−1，其中编号为 i 的饮料售价 c 
i
​
  元，容量 l 
i
​
  毫升。

小杨的需求有如下几点：

小杨想要尽可能尝试不同种类的饮料，因此他希望每种饮料至多购买 1 瓶；

小杨很渴，所以他想要购买总容量不低于 L 的饮料；

小杨勤俭节约，所以在 1 和 2 的前提下，他希望使用尽可能少的费用。

方便起见，你只需要输出最少花费的费用即可。特别地，如果不能满足小杨的要求，则输出 no solution。

输入格式
第一行两个整数 N,L。

接下来 N行，依次描述第 i=0,1,⋯,N−1 种饮料：每行两个整数 c 
i
​
 ,l 
i
​
 。

输出格式
输出一行一个整数，表示最少需要花费多少钱，才能满足小杨的要求。特别地，如果不能满足要求，则输出 no solution。

输入输出样例
输入 #1复制

5 100
100 2000
2 50
4 40
5 30
3 20
输出 #1复制

9
输入 #2复制

5 141
100 2000
2 50
4 40
5 30
3 20
输出 #2复制

100
输入 #3复制

4 141
2 50
4 40
5 30
3 20
输出 #3复制

no solution
说明/提示
样例 1 解释

小杨可以购买 1,2,4 号饮料，总计获得 50+40+20=110 毫升饮料，花费 2+4+3=9 元。

如果只考虑前两项需求，小杨也可以购买 1,3,4 号饮料，它们的容量总和为 50+30+20=100 毫升，恰好可以满足需求。但遗憾的是，这个方案需要花费 2+5+3=10 元。

样例 2 解释

1,2,3,4 号饮料总计 140 毫升，如每种饮料至多购买 1 瓶，则恰好无法满足需求，因此只能花费 100 元购买 0 号饮料。

数据规模

对于 40% 的测试点，保证 N≤20;1≤L≤100;l 
i
​
 ≤100。

对于 70% 的测试点，保证 l 
i
​
 ≤100。

对于 100% 的测试点，保证 1≤N≤500;1≤L≤2000;1≤c 
i
​
 ,l 
i
​
 ≤10 
6
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solution1():
    #总容量不能低于L升的情况下最后的花费最小
    n,limit = read()
    #dp[j]表示在已经考虑的饮料中，买到至少j毫升所需要的最小费用
    dp = [float("inf")]*(limit+1)
    #需求为0的时候直接什么都不买
    dp[0] = 0
    #考虑第 i 种饮料，有两种选择：
    #- 不买：保持原来的 dp[j]。
    #- 买：花费 c[i]，剩余需求变成 max(0, j - l[i])。
    for i in range(n):
        c,l = read()
        for j in range(limit,0,-1):
            remain = max(0,j - l)
            dp[j] = min(dp[j],dp[remain] + c)
    if(dp[limit] == float("inf")):
        print("no solution")
    else:
        print(dp[limit])


def solution2():
    n,limit = read()
    #dp[i][j]表示只考虑前i种饮料，买到至少j毫升所需要的最小费用
    dp = [[float("inf")]*(limit+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0

    for i in range(1,n+1):
        c,l = read()
        for j in range(1,limit+1):
            remain = max(0,j-l)
            #不买当前饮料，或者买一瓶后由前i-1种饮料满足剩余需求
            dp[i][j] = min(dp[i-1][j],dp[i-1][remain]+c)

    if(dp[n][limit] == float("inf")):
        print("no solution")
    else:
        print(dp[n][limit])

solution1()
