""" 题目描述
小明喜欢在一个围棋网站上找别人在线对弈。这个网站上所有注册用户都有一个积分，代表他的围棋水平。

小明发现网站的自动对局系统在匹配对手时，只会将积分差恰好是 K 的两名用户匹配在一起。如果两人分差小于或大于 K，系统都不会将他们匹配。

现在小明知道这个网站总共有 N 名用户，以及他们的积分分别是 A 
1
​
 ,A 
2
​
 ,⋯A 
N
​
 。

小明想了解最多可能有多少名用户同时在线寻找对手，但是系统却一场对局都匹配不起来（任意两名用户积分差不等于 K）？

输入格式
第一行包含两个个整数 N 和 K。

第二行包含 N 个整数 A 
1
​
 ,A 
2
​
 ,⋯,A 
N
​
 。

输出格式
一个整数，代表答案。

输入输出样例
输入 #1复制

10 0
1 4 2 8 5 7 1 4 2 8
输出 #1复制

6
输入 #2复制

10 1
2 1 1 1 1 4 4 3 4 4
输出 #2复制

8
说明/提示
对于 30% 的数据，1≤N≤10。

对于 100% 的数据，1≤N≤10 
5
 ，0≤K,A 
i
​
 ≤10 
5
  。

时限 1 秒, 256M。蓝桥杯 2017 年第八届国赛 """
import sys
from collections import Counter

input = sys.stdin.buffer.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = Counter(arr)

if k == 0:
    print(len(cnt))
else:
    g = []
    vis = set()

    # 构造每一条链
    for x in sorted(cnt):
        if x in vis:
            continue

        row = []

        while x in cnt and x not in vis:
            row.append(x)
            vis.add(x)
            x += k

        g.append(row)

    # 每条链分别进行 DP
    ans = 0

    for row in g:
        dp = [0] * (len(row) + 1)

        for i in range(1, len(row) + 1):
            dp[i] = max(
                dp[i-1],
                dp[i-2] + cnt[row[i-1]] if i >= 2 else cnt[row[i-1]]
            )

        ans += dp[-1]
    print(ans)