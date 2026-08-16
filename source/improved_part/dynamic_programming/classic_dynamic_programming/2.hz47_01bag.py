""" 题目描述
给一个能承重V的背包，和n件物品，我们用重量和价值的二元组来表示一个物品，第i件物品表示为（Vi，Wi），问：在背包不超重的情况下，得到物品的最大价值是多少？

54E9C51263E1462585A8F6595841EEC0.jpg

输入
第一行输入两个数 V,n，分别代表背包的最大承重和物品数。

接下来n行，每行两个数Vi,Wi，分别代表第i件物品的重量和价值。

(Vi≤V≤10000,n≤100,Wi≤1000000)

输出
输出一个整数，代表在背包不超重情况下所装物品的最大价值。

样例输入1
15 4
4 10
3 7
12 12
9 8
样例输出1
19 """

#dp[i][j]前i件物品在背包承重为j的情况下所能获得的最大价值
#dp[i][j] = max(dp[i-1][j] , dp[i-1][j-weight[i]] + value[i])
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

V,n = read()#背包最大承重和物品数量
dp = [0]*(V+1)

#dp[j]表示已经处理过的商品在背包容量不超过j的时候所能获得的最大价值
#dp[j] = max(dp[j], dp[j-cur_weight] + cur_value)
for i in range(1,n+1):
    cur_weight,cur_value = read()
    for j in range(V,cur_weight-1,-1):
        dp[j] = max(dp[j],dp[j-cur_weight] + cur_value)
print(dp[V])