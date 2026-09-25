""" 题目描述
自 01 背包问世之后，小 A 对此深感兴趣。一天，小 A 去远游，却发现他的背包不同于 01 背包，他的物品大致可分为 k 组，每组中的物品相互冲突，现在，他想知道最大的利用价值是多少。

输入格式
两个数 m,n，表示一共有 n 件物品，背包能承受的最大重量为 m。

接下来 n 行，每行 3 个数 a 
i
​
 ,b 
i
​
 ,c 
i
​
 ，表示物品的重量，利用价值，所属组数。

输出格式
一个数，最大的利用价值。

输入输出样例
输入 #1复制

45 3
10 10 1
10 5 1
50 400 2
输出 #1复制

10
说明/提示
0≤m≤1000，1≤n≤1000，1≤k≤100，a 
i
​
 ,b 
i
​
 ,c 
i
​
  在 int 范围内。 """
import sys
from collections import defaultdict
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
m,n = read()#背包的最大容量m以及物品的数量n
groups = defaultdict(list)

for _ in range(n):
    weight,value,group = read()
    groups[group].append((weight,value))

dp = [0]*(m+1)
#遍历每个组别->遍历容量大小->遍历当前组别的物品
for items in groups.values():
    for capacity in range(m,-1,-1):
        for weight,value in items:
            if(capacity >= weight):
                dp[capacity] = max(
                    dp[capacity],
                    dp[capacity - weight] + value
                )

print(dp[m])