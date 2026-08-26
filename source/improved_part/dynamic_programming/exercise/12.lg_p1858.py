""" 题目描述
求 01 背包前 K 优解的价值和。

DD 和好朋友们要去爬山啦！

他们一共有 K 个人，每个人都会背一个包。这些包的容量是相同的，都是 V。可以装进背包里的一共有 N 种物品，每种物品都有给定的体积和价值。

在 DD 看来，合理的背包安排方案是这样的：每个人背包里装的物品的总体积恰等于包的容量。每个包里的每种物品最多只有一件，但两个不同的包中可以存在相同的物品。

任意两个人，他们包里的物品清单不能完全相同。在满足以上要求的前提下，所有包里的所有物品的总价值最大是多少呢？

输入格式
第一行三个数 K,V,N。

接下来 N 行每行两个数，表示体积和价值。

输出格式
共一行，一个整数，表示前 K 优解的价值和。

输入输出样例
输入 #1复制

2 10 5
3 12
7 20
2 4
5 6
1 1
输出 #1复制

57 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#dp[i][j]存储一个数组，存储的是前i个物品在背包容量为j为前提下
#能获得的前k个最大的价值
k,v,n = read()
dp = [[0]*(k+1)for _ in range(v+1)]
dp[0][0] = 1
#让dp[i][j][0]存储该种情况下我们含有的最优解的数量
for i in range(1,n+1):
    weight, value = read()
    dp[0][0] = 1
    dp[0][1] = 0
    for j in range(v,weight-1,-1):
        #把dp[i-1][j]和dp[i-1][j-weight[i]] + value[i]的值整合到一起
        temp = [0]
        index1 = 1
        index2 = 1
        n1 = dp[j][0]
        n2 = dp[j-weight][0]
        temp[0] = min(k,n1+n2)
        while((index1 <= n1 or index2 <= n2) and len(temp) < k+1):
            #数组2为空
            if(index2 > n2 or (index1<=n1 and index2<=n2 and dp[j][index1] >= dp[j - weight][index2] + value)):
                temp.append(dp[j][index1])
                index1 += 1
            else:
                temp.append(dp[j - weight][index2] + value)
                index2 += 1
        dp[j] = temp
count = dp[v][0]
print(sum(dp[v][1:count+1]))


