""" 题目描述
金明今天很开心，家里购置的新房就要领钥匙了，新房里有一间金明自己专用的很宽敞的房间。更让他高兴的是，妈妈昨天对他说：“你的房间需要购买哪些物品，怎么布置，你说了算，只要不超过 n 元钱就行”。今天一早，金明就开始做预算了，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：

主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、1 个或 2 个附件。每个附件对应一个主件，附件不再有从属于自己的附件。金明想买的东西很多，肯定会超过妈妈限定的 n 元。于是，他把每件物品规定了一个重要度，分为 5 等：用整数 1∼5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 n 元的前提下，使每件物品的价格与重要度的乘积的总和最大。

设第 j 件物品的价格为 v 
j
​
 ，重要度为 w 
j
​
 ，共选中了 k 件物品，编号依次为 j 
1
​
 ,j 
2
​
 ,…,j 
k
​
 ，则所求的总和为：

v 
j 
1
​
 
​
 ×w 
j 
1
​
 
​
 +v 
j 
2
​
 
​
 ×w 
j 
2
​
 
​
 +⋯+v 
j 
k
​
 
​
 ×w 
j 
k
​
 
​
 
请你帮助金明设计一个满足要求的购物单。

输入格式
第一行有两个整数，分别表示总钱数 n 和希望购买的物品个数 m。

第 2 到第 (m+1) 行，每行三个整数，第 (i+1) 行的整数 v 
i
​
 ，w 
i
​
 ，q 
i
​
  分别表示第 i 件物品的价格、重要度以及它对应的的主件。如果 q 
i
​
 =0，表示该物品本身是主件。

输出格式
输出一行一个整数表示答案。

输入输出样例
输入 #1复制

1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
输出 #1复制

2200
说明/提示
数据规模与约定
对于全部的测试点，保证 1≤n≤3.2×10 
4
 ，1≤m≤60，0≤v 
i
​
 ≤10 
4
 ，1≤w 
i
​
 ≤5，0≤q 
i
​
 ≤m，答案不超过 2×10 
5
 。

NOIP 2006 提高组 第二题 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#最多就是只有60件物品
s,n  = read()
items = []
for _ in range(n):
    weight,value,tag = read()
    value = weight*value
    items.append((weight,value,tag))

#dp[i][j]表示考虑前i个主键在
#总体限制为j的情况下所能获得的最大收益
# 使用原始物品编号，方便通过 tag 找到主件
main = [None] * (n + 1)#主键
attachments = [[] for _ in range(n + 1)]#使用二维数组表示i所有的附件
for i, (weight, value, tag) in enumerate(items, start = 1):
    if tag == 0:
        main[i] = (weight, value)
    else:
        attachments[tag].append((weight, value))

dp = [0] * (s + 1)

for i in range(1, n + 1):
    if main[i] is None:
        continue

    # 最初只有“只买主件”这一种方案
    options = [main[i]]

    #拓展出所有选择，选择主+附件1，主+附件2，主+附件1+附件2
    for aw, av in attachments[i]:
        extra = [(w + aw, v + av) for w, v in options]
        options.extend(extra)

    # 分组背包：当前组至多选一种方案
    for j in range(s, -1, -1):
        for cost, val in options:
            if j >= cost:
                dp[j] = max(dp[j], dp[j - cost] + val)
print(dp[s])
