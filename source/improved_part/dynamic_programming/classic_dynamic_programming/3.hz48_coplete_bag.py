""" 题目描述
有N种物品和一个容量为 V 的背包，每种物品都有无限件可用。

第 i 种物品的体积是Ci，价值是Wi。求解在不超过背包容量的情况下，能够获得的最大价值。

54E9C51263E1462585A8F6595841EEC0.jpg

输入
第一行为两个整数N、V(1≤N,V≤10000)，分别代表题目描述中的物品种类数量N和背包容量V。

后跟N行，第 i 行两个整数Ci、Vi，分别代表每种物品的体积和价值。

输出
输出一个整数，代表可获得的最大价值。

样例输入
5 20
2 3
3 4
10 9
5 2
11 11
样例输出
30 """

#dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i]]+value[i])
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,v = read()#n为物品总数,v为背包容量
dp = [[0]*(v+1) for _ in range(2)]
""" weight = [0]
value = [0]
for i in range(n):
    number1,number2 = read()
    weight.append(number1)
    value.append(number2)
dp[1][weight[1]] = value[1] """

for i in range(1,n+1):
    cur_weight,cur_value = read()
    index = i%2
    rindex = 1-index
    for j in range(0,v+1):
        if(j-cur_weight < 0): 
            dp[index][j] = dp[rindex][j]
        elif(j-cur_weight >= 0):
            dp[index][j] = max(dp[rindex][j], dp[index][j-cur_weight]+cur_value)

print(dp[n%2][v])