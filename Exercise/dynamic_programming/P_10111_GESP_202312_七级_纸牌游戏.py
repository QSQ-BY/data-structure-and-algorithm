""" 题目描述
你和小杨在玩一个纸牌游戏。

你和小杨各有 3 张牌，分别是 0、1、2。你们要进行 N 轮游戏，每轮游戏双方都要出一张牌，并按 1 战胜 0，2 战胜 1，0 战胜 2 的规则决出胜负。第 i 轮的胜者可以获得 2×a 
i
​
  分，败者不得分，如果双方出牌相同，则算平局，二人都可获得 a 
i
​
  分 (i=1,2,⋯,N)。

玩了一会后，你们觉得这样太过于单调，于是双方给自己制定了不同的新规则。小杨会在整局游戏开始前确定自己全部 n 轮的出牌，并将他的全部计划告诉你；而你从第 2 轮开始，要么继续出上一轮出的牌，要么记一次“换牌”。游戏结束时，你换了 t 次牌，就要额外扣 b 
1
​
 +⋯+b 
t
​
  分。

请计算出你最多能获得多少分。

输入格式
第一行一个整数 N，表示游戏轮数。

第二行 N 个用单个空格隔开的非负整数 a 
1
​
 ,⋯,a 
N
​
 ，意义见题目描述。

第三行 N−1 个用单个空格隔开的非负整数 b 
1
​
 ,⋯,b 
N−1
​
 ，表示换牌的罚分，具体含义见题目描述。由于游戏进行 N 轮，所以你至多可以换 N−1 次牌。

第四行 N 个用单个空格隔开的整数 c 
1
​
 ,⋯,c 
N
​
 ，依次表示小杨从第 1 轮至第 N 轮出的牌。保证 c 
i
​
 ∈{0,1,2}。

输出格式
一行一个整数，表示你最多获得的分数。

输入输出样例
输入 #1复制

4
1 2 10 100
1 100 1
1 1 2 0
输出 #1复制

219
输入 #2复制

6
3 7 2 8 9 4
1 3 9 27 81
0 1 2 1 2 0
输出 #2复制

56
说明/提示
样例解释 1

你可以第 1 轮出 0，并在第 2,3 轮保持不变，如此输掉第 1,2 轮，但在第 3 轮中取胜，获得 2×10=20 分；

随后，你可以在第 4 轮中以扣 1 分为代价改出 1 ，并在第 4 轮中取得胜利，获得 2×100=200 分。

如此，你可以获得最高的总分 20+200−1=219。

数据范围

对于 30% 的测试点，保证 N≤15。

对于 60% 的测试点，保证 N≤100。

对于所有测试点，保证 N≤1,000；保证 0≤a 
i
​
 ,b 
i
​
 ≤10 
6
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
def compete(a:int,b:int):
    if((a == 1 and b == 0) or (a==2 and b==1) or (a==0 and b==2)):
        return 1
    else:
        return 0
n = int(input())
a = list(read())
b = list(read())
cards = list(read())
#dp[i][j][k]表示进行了i轮比赛，现在的牌是j,且进行了k次换牌之后可以达到的最大分数
NEG = float("-inf")
dp = [[[NEG]*n for _ in range(3)] for _ in range(n+1)]
for j in range(3):
    if j == cards[0]:
        dp[1][j][0] = a[0]
    elif compete(j, cards[0]):
        dp[1][j][0] = 2*a[0]
    else:
        dp[1][j][0] = 0
for i in range(2, n+1):
    for j in range(3):
        if j == cards[i-1]:
            get = a[i-1]
        elif compete(j, cards[i-1]):
            get = 2*a[i-1]
        else:
            get = 0

        #进行了i轮，最多换牌i-1次
        for k in range(i):
            #不换牌
            best = dp[i-1][j][k]

            #本轮进行第k次换牌
            if k >= 1:
                for p in range(3):
                    if p != j:
                        best = max(
                            best,
                            dp[i-1][p][k-1] - b[k-1]
                        )

            dp[i][j][k] = best + get

ans = max(
    dp[n][j][k]
    for j in range(3)
    for k in range(n)
)
print(ans)