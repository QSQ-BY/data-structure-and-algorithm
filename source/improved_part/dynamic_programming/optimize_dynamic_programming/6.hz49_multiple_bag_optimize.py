#多重背包问题
#优化拆分方式
#例如有14件商品，把14拆分为1，2，4，7，不管我选择多少件商品都有相应的组合
""" 题目描述
给有一个能承重 V 的背包，和n种物品，每种物品的数量有限多，我们用重量、价值和数量的三元组来表示一个物品，第 i 件物品表示为（Vi，Wi，Si），问在背包不超重的情况下，得到物品的最大价值是多少？

54E9C51263E1462585A8F6595841EEC0.jpg

输入
第一行输入两个数V、n，分别代表背包的最大承重和物品种类数。

接下来 n 行，每行三个数 Vi、Wi、Si，分别代表第 i 种物品的重量、价值和数量。

输出
输出一个整数，代表在背包不超重情况下所装物品的最大价值。

样例输入1
15 4
4 10 5
3 7 4
12 12 2
9 8 7
样例输出1
37
"""

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#拆分优化
def test01():
    V,n = read()#最大承重上限和物品数量
    dp = [0]*(V+5)
    for i in range(n):
        v,w,s = read()
        k = 1
        while(s!=0):
            k = min(s,k)
            for j in range(V,k*v-1,-1):
                dp[j] = max(dp[j] , dp[j-k*v]+k*w)
            s -= k
            k*=2
    print(dp[V])

test01()
