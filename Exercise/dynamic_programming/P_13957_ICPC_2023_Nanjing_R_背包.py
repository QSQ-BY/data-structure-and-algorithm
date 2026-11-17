""" 题目描述
小青鱼，一位没有经验的商人，最近开了一家名叫“皇后有机珠宝”（QOJ）的店。这家珠宝店共有 n 枚宝石，其中第 i 枚售价为 w 
i
​
  元，美丽度为 v 
i
​
 。进入商店之前，您准备了 W 元用来买下美丽度总和尽量高的宝石。

有趣的是，小青鱼的店今天正在促销。任何顾客都可以任选 k 枚宝石并免费获得它们。有了这样的机会，您很想知道，如果您使用最佳策略，用 W 元到底能获得美丽度总和多高的宝石。

请注意，每枚宝石独此一份，您不能多次获取同一枚宝石。另外，您无需花完所有的钱。

输入格式
每个测试文件仅有一组测试数据。

第一行输入三个整数 n，W 和 k（1≤n≤5×10 
3
 ，1≤W≤10 
4
 ，0≤k≤n），表示商店中宝石的总数，您拥有的金钱数以及您可以免费获得的宝石数量。

对于接下来 n 行，第 i 行输入两个整数 w 
i
​
  和 v 
i
​
 （1≤w 
i
​
 ≤W，1≤v 
i
​
 ≤10 
9
 ），表示第 i 枚宝石的售价和美丽度。

输出格式
输出一行一个整数表示答案。

输入输出样例
输入 #1复制

4 10 1
9 10
10 1
3 5
5 20
输出 #1复制

35
输入 #2复制

5 13 2
5 16
5 28
7 44
8 15
8 41
输出 #2复制

129
说明/提示
对于第一组样例数据，小青鱼的商店有 4 枚宝石，您可以免费获得其中 1 枚。一种最优策略是免费获取第一枚宝石，并购买第三和第四枚宝石。

宝石
1
2
3
4
​
  
售价w 
i
​
 
9
10
3
5
​
  
美丽度v 
i
​
 
10
1
5
20
​
  
操作
免费获取
/
购买
购买
​
 
​
 
所以答案是 10+5+20=35。 """
import sys
from heapq import heappush, heappop

input = sys.stdin.buffer.readline


def read():
    return map(int, input().split())


def solution1():
    n,limit,m = read()
    #dp[i][j][k]表示考虑前i个物品，在使用k次免费机会且价格总和在j次以内的情况下能获得的最大价值
    dp = [[[float("-inf")]*(m+1)for _ in range(limit+1)]for _ in range(2)]
    for j in range(limit+1):
        for k in range(m+1):
            dp[0][j][k] = 0#一件物品都没有的情况下所能获得的总价值一定都是0
    for i in range(1,n+1):
        cur = i%2
        pre = 1 - cur
        dp[cur] = [[float("-inf")]*(m+1)for _ in range(limit+1)]
        weight,value = read()
        for j in range(limit+1):
            for k in range(m+1):
                dp[cur][j][k] = dp[pre][j][k]#不买第i件商品，直接无视
                #选择买第i件商品
                if(j >= weight):
                    dp[cur][j][k]= max(dp[cur][j][k],dp[pre][j - weight][k] + value)
                #选择使用免费次数购买第i件商品
                if(k>= 1):
                    dp[cur][j][k] = max(dp[cur][j][k],dp[pre][j][k-1] + value)

    print(max(dp[n%2][limit]))

#solution1()


def solution2():
    n, limit, k = read()
    items = [tuple(map(int, input().split())) for _ in range(n)]
    items.sort()

    # suffix[i]：items[i:] 中美丽度最大的至多 k 个宝石的美丽度之和
    suffix = [0] * (n + 1)
    heap = []
    total = 0
    for i in range(n - 1, -1, -1):
        value = items[i][1]
        heappush(heap, value)
        total += value
        if len(heap) > k:
            total -= heappop(heap)
        suffix[i] = total

    # dp[i][j]：前 i 件宝石中，付费预算不超过 j 时的最大美丽度（滚动数组压缩 i 这一维）
    # 一件物品都没有时，任意预算下的价值都是 0
    dp = [[0] * (limit + 1) for _ in range(2)]
    ans = suffix[0]  # 分界点 i=0：没有付费，全部从 items 中免费拿 k 件

    for i in range(1, n + 1):
        cur = i % 2
        pre = 1 - cur
        weight, value = items[i - 1]
        for j in range(limit + 1):
            dp[cur][j] = dp[pre][j]  # 不买第 i 件宝石
            if j >= weight:  # 付费买第 i 件宝石
                dp[cur][j] = max(dp[cur][j], dp[pre][j - weight] + value)

        # 前 i 件允许付费，后缀 items[i:] 选择至多 k 件免费
        ans = max(ans, dp[cur][limit] + suffix[i])

    print(ans)


solution2()
