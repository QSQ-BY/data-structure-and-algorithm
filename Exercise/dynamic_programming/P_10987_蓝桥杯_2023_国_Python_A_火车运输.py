""" 题目描述
钢厂有一辆用于运送废旧钢材的火车，它具有两节车厢，其中车厢 1 的最大载重量为 A，车厢 2 的最大载重量为 B。现在一共有 N 件废旧钢材需要被运输，其中第 i 件钢材的重量为 w 
i
​
 ，为了最大化运输效率，车长想要一次性运输走重量尽可能多的钢材，请你帮助车长计算出一次运输最多可以带走多大重量的钢材。

每件钢材都是独立的不可分割的，只能被放置在某一节车厢中。在装载钢材时只需要考虑重量条件即可。

输入格式
输入的第一行包含三个整数 N,A,B，用一个空格分隔，分别表示钢材的数目以及两节车厢的最大载重。

第二行包含 N 个整数，分别表示 w 
1
​
 ,w 
2
​
 ,⋯,w 
n
​
 ，相邻两个整数之间使用一个空格分隔。

输出格式
输出一个整数表示答案。

输入输出样例
输入 #1复制

3 10 8
8 9 1
输出 #1复制

18
说明/提示
对于 30% 的评测用例，1≤N≤10；

对于所有评测用例，1≤N≤200,1≤w 
i
​
 ,A,B≤1000。

样例解释
车厢 1 装入第 2 件和第 3 件钢材，车厢 2 装入第 1 件钢材。 """

import sys
input = sys.stdin.buffer.readline
from functools import cache
def read():
    return map(int,input().split())

#暴力DFS做法
def solution1():
    #A车的承重位a,B车的承重位b
    n,a,b = read()
    weights = list(read())
    ans = float("-inf")
    suffix = [weights[-1]]#suffix[i]表示从i位置到最后所有的木材的总重量
    for i in range(n-2,-1,-1):
        weight = weights[i]
        suffix = [weight + suffix[0]] + suffix
    #print(*suffix)
    #第一辆车还有多少承重
    #第二辆车还有多少承重
    #现在已经装了多少
    #现在已经处理到了第几个木材
    @cache
    def dfs(limit1,limit2,cur_ans,index):
        nonlocal ans
        ans = max(cur_ans,ans)
        if(index == n):
            return
        if(suffix[index] + cur_ans <= ans):
            return
        weight = weights[index]
        #装进第一辆车
        if(limit1 >= weight):
            dfs(limit1-weight,limit2,cur_ans+weight,index+1)
        #装进第二辆车
        if(limit2 >= weight):
            dfs(limit1,limit2-weight,cur_ans+weight,index+1)
        #什么都不装直接跳过这辆车
        dfs(limit1,limit2,cur_ans,index+1)
    dfs(a,b,0,0)
    print(ans)

#使用动态规划做法
#dp[i][j][k]表示考虑前i个木材，A车的承重至少位j,B车的承重至少位
def solution2():
    n, a, b = read()
    weights = list(read())
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    for w in weights:
        for j in range(a, -1, -1):
            for k in range(b, -1, -1):
                # 不装：保留 dp[j][k]
                # 装进 A 车
                if j >= w:
                    dp[j][k] = max(
                        dp[j][k],
                        dp[j-w][k] + w
                    )
                # 装进 B 车
                if k >= w:
                    dp[j][k] = max(
                        dp[j][k],
                        dp[j][k-w] + w
                    )
    print(dp[a][b])
solution2()