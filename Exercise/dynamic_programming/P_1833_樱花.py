""" 题目背景
《爱与愁的故事第四弹·plant》第一章。

题目描述
爱与愁大神后院里种了 n 棵樱花树，每棵都有美学值 C 
i
​
 (0<C 
i
​
 ≤200)。爱与愁大神在每天上学前都会来赏花。爱与愁大神可是生物学霸，他懂得如何欣赏樱花：一种樱花树看一遍过，一种樱花树最多看 P 
i
​
 (0≤P 
i
​
 ≤100) 遍，一种樱花树可以看无数遍。但是看每棵樱花树都有一定的时间 T 
i
​
 (0<T 
i
​
 ≤100)。爱与愁大神离去上学的时间只剩下一小会儿了。求解看哪几棵樱花树能使美学值最高且爱与愁大神能准时（或提早）去上学。

输入格式
共 n+1行：

第 1 行：现在时间 T 
s
​
 （几时：几分），去上学的时间 T 
e
​
 （几时：几分），爱与愁大神院子里有几棵樱花树 n。这里的 T 
s
​
 ，T 
e
​
  格式为：hh:mm，其中 0≤hh≤23，0≤mm≤59，且 hh,mm,n 均为非负整数。

第 2 行到第 n+1 行，每行三个非负整数：看完第 i 棵树的耗费时间 T 
i
​
 ，第 i 棵树的美学值 C 
i
​
 ，看第 i 棵树的次数 P 
i
​
 （P 
i
​
 =0 表示无数次，P 
i
​
  是其他数字表示最多可看的次数 P 
i
​
 ）。

输出格式
只有一个整数，表示最大美学值。

输入输出样例
输入 #1复制

6:50 7:00 3
2 1 0
3 3 1
4 5 4
输出 #1复制

11
说明/提示
100% 数据：T 
e
​
 −T 
s
​
 ≤1000（即开始时间距离结束时间不超过 1000 分钟），n≤10000。保证 T 
e
​
 ,T 
s
​
  为同一天内的时间。

样例解释：赏第一棵樱花树一次，赏第三棵樱花树 2 次。 """
import sys
input = sys.stdin.readline

def test01():
    start, end, n = input().split()
    n = int(n)

    # 处理开始时间
    h1, m1 = map(int, start.split(':'))

    # 处理结束时间
    h2, m2 = map(int, end.split(':'))

    # 总共可以赏花的时间
    T = (h2 * 60 + m2) - (h1 * 60 + m1)

    trees = []

    for _ in range(n):
        t, c, p = map(int, input().split())
        if(p == 0):
            p = T//t
        trees.append((t, c, p))
        #消耗的时间，看这棵树能获得的美学值，能够观看的次数(0代表无数次)

    #混合背包问题
    #p == 0：完全背包
    #p == 1：01 背包
    #p > 1：多重背包
    #考虑前 i 种樱花树，在最多花费 j 分钟的情况下，能够得到的最大美学值。
    dp = [[0]*(T+1) for _ in range(2)]

    for i in range(1, n + 1):
        t, c, p = trees[i - 1]
        index1 = i%2
        index2 = 1 - index1
        for j in range(T + 1):
            # 一次都不看第 i 棵树
            dp[index1][j] = dp[index2][j]
            # 看第 i 棵树 k 次
            for k in range(1, p + 1):

                if k * t > j:
                    break

                dp[index1][j] = max(
                    dp[index1][j],
                    dp[index2][j - k * t] + k * c
                )

    print(dp[n%2][T])

def test02():
    def get_time(s):
        h, m = map(int, s.split(':'))
        return h * 60 + m

    start, end, n = input().split()
    n = int(n)

    T = get_time(end) - get_time(start)

    dp = [0] * (T + 1)

    for _ in range(n):
        t, c, p = map(int, input().split())#t为损失的代价，c为获得的奖励
        # 完全背包
        if p == 0:
            for j in range(t, T + 1):
                dp[j] = max(dp[j], dp[j - t] + c)

        else:
            k = 1
            #使用二进制的方式进行优化,对多重背包的k个物品进行打包
            while p > 0:
                cnt = min(k, p)

                cost = t * cnt
                value = c * cnt

                for j in range(T, cost - 1, -1):
                    dp[j] = max(dp[j], dp[j - cost] + value)

                p -= cnt
                k *= 2
    print(dp[T])

def test03():
    def get_time(s):
        h, m = map(int, s.split(':'))
        return h * 60 + m

    start, end, n = input().split()
    n = int(n)

    T = get_time(end) - get_time(start)

    dp = [0] * (T + 1)

    for _ in range(n):
        t, c, p = map(int, input().split())
        # 完全背包
        if p == 0:
            for j in range(t, T + 1):
                dp[j] = max(dp[j], dp[j - t] + c)

        #普通的多重背包转换成01背包问题
        else:
            for _ in range(p):
                for j in range(T, t - 1, -1):
                    dp[j] = max(dp[j], dp[j - t] + c)

    print(dp[T])
test02()
#test03()
