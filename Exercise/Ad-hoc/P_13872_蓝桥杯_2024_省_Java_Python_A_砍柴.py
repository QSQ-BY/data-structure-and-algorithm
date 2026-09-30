""" 题目描述
小蓝和小乔正在森林里砍柴，它们有 T 根长度分别为 n 
1
​
 ,n 
2
​
 ,⋯,n 
T
​
  的木头。对于每个初始长度为 n 的木头，小蓝和小乔准备进行交替砍柴，小蓝先出手。每次砍柴时，若当前木头长度为 x，需要砍下一截长度为 p 的木头，然后换另一个人继续砍，其中 2≤p≤x 且 p 必须为质数。当轮到某一方时 x=1 或 x=0，它就没法继续砍柴，它就输了。它们会使用最优策略进行砍柴。请对每根木头判断是小蓝赢还是小乔赢，如果小蓝赢请输出 1（数字 1），如果小乔赢请输出 0（数字 0）。

输入格式
输入的第一行包含一个正整数 T，

接下来 T 行，每行包含一个正整数，其中第 i 的整数为 n 
i
​
 。

输出格式
输出 T 行，每行包含一个整数，依次表示对于每一根木头的答案。

输入输出样例
输入 #1复制

3
1
2
6
输出 #1复制

0
1
1
说明/提示
【样例说明】

对于 n 
1
​
 =1，由于当前长度 x=1，小蓝直接输掉，小乔赢；

对于 n 
2
​
 =2，小蓝选择 p=2，轮到小乔时当前长度 x=2−2=0，小乔输掉，小蓝赢；

对于 n 
3
​
 =6，小蓝选择 p=5，轮到小乔时 x=6−5=1，小乔输掉，小蓝赢。

【评测用例规模与约定】

对于 20% 的评测用例，1≤n 
i
​
 ≤10 
3
 ；

对于所有评测用例，1≤n 
i
​
 ≤10 
5
 ，1≤T≤10 
4
 。 """
import sys
import math

input = sys.stdin.buffer.readline

maximum = 10**5

is_prime = [True] * (maximum + 1)
is_prime[0] = False
is_prime[1] = False

for cur in range(2, math.isqrt(maximum) + 1):
    if is_prime[cur]:
        for j in range(cur * cur, maximum + 1, cur):
            is_prime[j] = False

# 把所有质数保存下来
primes = []

for i in range(2, maximum + 1):
    if is_prime[i]:
        primes.append(i)

# dp[x] = 1 表示当前玩家必胜
# dp[x] = 0 表示当前玩家必败
dp = [0] * (maximum + 1)

# dp[0]、dp[1] 本身就是 0

#博弈论dp，0和1是已知的一定会输掉的必败状态，
#只要可以通过减去一个质数达到这两个必败状态那就是必胜的状态
for x in range(maximum + 1):
    # 只有必败状态才需要向后标记
    if dp[x] == 0:
        for p in primes:
            if x + p > maximum:
                break
            dp[x + p] = 1

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])

