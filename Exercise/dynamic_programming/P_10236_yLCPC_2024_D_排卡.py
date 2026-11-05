""" 题目背景
经过千辛万苦，扶苏终于到达了机厅。但是她很快发现机厅排起了大 b 队 （不是省选的 B 队）。

舞萌玩家们在人多的时候经常采取排卡的方式决定谁下一个上机。因为人实在是太多了，他们在排卡的时候，便注意到了卡上的编号。

他们向扶苏提了一个问题，你能解决吗？

题目描述
扶苏有一个双端队列 a。这个队列与计算机科学中队列的概念类似，不同的是，这个队列既可以从队列头读取和弹出元素，也可以在队列尾部读取和弹出元素，因此被称为『双端队列』。

这个队列中有 n 个数。扶苏将通过 n 次操作构造一个长度为 n 的序列 b，第 i（1≤i≤n）次操作会可以进行如下两个过程之一：

令 b 
i
​
  为 a 的队列头，并在 a 的头部弹出一个元素。
令 b 
i
​
  为 a 的队列尾，并在 a 的尾部弹出一个元素。
我们定义一个数对 (i,j) 的得分为：

score(i,j)=i 
j
 mod998244353
即 i 的 j 次幂对 998244353 取余数的结果。特别的，在本题中我们规定 0 
0
 =0。

现在，扶苏想用最优的策略构造 b 序列，最大化如下式子的值：

i=1
∑
n−1
​
 score(b 
i
​
 ,b 
i+1
​
 )
即 b 所有相邻两项按原顺序计算的得分之和。

注意，我们仅在计算一个数对的时候将得分对 998,244,353 取模，在计算求和时不再将这个和取余。

输入格式
本题单个测试点内有多组测试数据。第一行是一个正整数，表示数据组数 T。对每组数据：

第一行是一个整数 n（2≤n≤10 
3
 ），表示序列的长度。
第二行有 n 个整数 a 
1
​
 ,a 
2
​
 ,…a 
n
​
 （0≤a 
i
​
 <998,244,353），按从头到尾的顺序表示队列 a 里每个数字的值。

数据保证单个测试点内 n 的和不超过 10 
3
 。

输出格式
对每组测试数据，输出一行一个整数表示答案。

输入输出样例
输入 #1复制

2
5
5 3 1 4 2
6
6 5 1 4 2 3
输出 #1复制

1168
15655 """
import sys
input = sys.stdin.buffer.readline
MOD = 998244353
def read():
    return map(int,input().split())
t = int(input())
def score(x,y):
    if(x == 0 and y == 0):
        return 0
    return pow(x,y,MOD)
for _ in range(t):
    n = int(input())
    arr = list(read())
    # 提前计算出所有相邻位置的得分
    forward = [score(arr[i],arr[i+1]) for i in range(n-1)]
    backward = [score(arr[i+1],arr[i]) for i in range(n-1)]

    #dp[l][r][i]：
    #目前只剩下 [l,r] 还没有取，
    #上一次取出的数字是从左边还是右边，
    #从现在开始把剩余数字取完，最多还能增加多少得分。
    # [l,r] 表示还没取出的区间，dp 记录接下来最多能增加的得分
    # dp[l][r][0]：上一次从左边取走了 arr[l-1]，仅 l > 0 时有效
    # dp[l][r][1]：上一次从右边取走了 arr[r+1]，仅 r < n-1 时有效
    dp = [[[0]*(2) for _ in range(n)] for _ in range(n)]

    # 只剩一个数时，增加的得分就是上一个数到这个数的得分
    for p in range(n):
        if p > 0:
            dp[p][p][0] = forward[p - 1]
        if p < n - 1:
            dp[p][p][1] = backward[p]

    # 第一个数取出后，剩余区间最多长 n-1，因此不用计算长度 n
    for length in range(2,n):
        for l in range(n-length + 1):
            r = l+length-1

            if l > 0:
                # 上一个数是 arr[l-1]，现在选择取 arr[l] 或 arr[r]
                dp[l][r][0] = max(
                    forward[l - 1] + dp[l + 1][r][0],
                    score(arr[l - 1], arr[r]) + dp[l][r - 1][1]
                )

            if r < n - 1:
                # 上一个数是 arr[r+1]，现在选择取 arr[l] 或 arr[r]
                dp[l][r][1] = max(
                    score(arr[r + 1], arr[l]) + dp[l + 1][r][0],
                    backward[r] + dp[l][r - 1][1]
                )
    ans = float("-inf")
    #直接无脑遍历所有状态取最大的状态就一定是答案，整个序列保持绝对的递增性
    #最后的精确ans应该是max(dp[l+1][r][0],dp[l][r-1][1])
    #第一个取得数应该是从左边取或者从右边取
    #dp[l][r][0]和dp[l][r][1]都是没有意义的
    for i in range(n):
        for j in range(n):
            for k in range(2):
                ans = max(ans,dp[i][j][k])
    print(ans)

