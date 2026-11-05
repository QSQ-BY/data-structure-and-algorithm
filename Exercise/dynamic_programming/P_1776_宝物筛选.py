""" 题目描述
终于，破解了千年的难题。小 FF 找到了王室的宝物室，里面堆满了无数价值连城的宝物。

这下小 FF 可发财了，嘎嘎。但是这里的宝物实在是太多了，小 FF 的采集车似乎装不下那么多宝物。看来小 FF 只能含泪舍弃其中的一部分宝物了。

小 FF 对洞穴里的宝物进行了整理，他发现每样宝物都有一件或者多件。他粗略估算了下每样宝物的价值，之后开始了宝物筛选工作：小 FF 有一个最大载重为 W 的采集车，洞穴里总共有 n 种宝物，每种宝物的价值为 v 
i
​
 ，重量为 w 
i
​
 ，每种宝物有 m 
i
​
  件。小 FF 希望在采集车不超载的前提下，选择一些宝物装进采集车，使得它们的价值和最大。

输入格式
第一行为两个整数 n 和 W，分别表示宝物种数和采集车的最大载重。

接下来 n 行每行三个整数 v 
i
​
 ,w 
i
​
 ,m 
i
​
 。

输出格式
输出仅一个整数，表示在采集车不超载的情况下收集的宝物的最大价值。

输入输出样例
输入 #1复制

4 20
3 9 3
5 9 1
9 4 2
8 1 3
输出 #1复制

47
说明/提示
对于 30% 的数据，1≤m 
i
​
 ，∑m 
i
​
 ≤10 
4
 ，0≤W≤10 
3
 ，1≤w 
i
​
 ，v 
i
​
 ≤100。

对于 100% 的数据，1≤m 
i
​
 ，∑m 
i
​
 ≤10 
5
 ，0≤W≤4×10 
4
 ，1≤n≤100，1≤w 
i
​
 ，v 
i
​
 ≤1000。 """
#多重背包问题
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solution1():
    n,limit = read()
    dp = [0]*(limit+1)
    for _ in range(n):
        value,weight,cnt = read()
        k = 1
        while(cnt != 0):
            cur_cnt = min(k,cnt)
            cur_value = value*cur_cnt
            cur_weight = weight*cur_cnt
            for j in range(limit,cur_weight-1,-1):
                dp[j] = max(dp[j],dp[j - cur_weight] + cur_value)
            cnt -= cur_cnt
            k *= 2
    print(dp[limit])

#使用单调队列进行优化
def solution2():
    n, limit = read()
    dp = [0] * (limit + 1)
    for _ in range(n):
        value, weight, cnt = read()
        # 保存上一层，所有转移都从尚未考虑当前宝物的状态出发
        old = dp[:]
        # 按容量对 weight 的余数分组
        for r in range(min(weight, limit + 1)):
            q = deque()
            for k, j in enumerate(range(r, limit + 1, weight)):
                # 下标小于 k-cnt，意味着要拿超过 cnt 件，不能使用
                while q and q[0][0] < k - cnt:
                    q.popleft()
                score = old[j] - k * value
                # 新候选更晚过期，且价值不低，可以淘汰队尾
                while q and q[-1][1] <= score:
                    q.pop()
                q.append((k, score))
                # 队首就是当前窗口中的最大值
                dp[j] = q[0][1] + k * value
    print(dp[limit])

solution2()