""" 题目描述
奶牛想证明它们是聪明而风趣的。为此，贝西筹备了一个奶牛博览会，她已经对 N 头奶牛进行了面试，确定了每头奶牛的智商和情商。

贝西有权选择让哪些奶牛参加展览。由于负的智商或情商会造成负面效果，所以贝西不希望出展奶牛的智商之和小于零，或情商之和小于零。满足这两个条件下，她希望出展奶牛的智商与情商之和越大越好，请帮助贝西求出这个最大值。

输入格式
第一行：单个整数 N，1≤N≤400。

第二行到第 N+1 行：第 i+1 行有两个整数：S 
i
​
  和 F 
i
​
 ，表示第 i 头奶牛的智商和情商，−1000≤S 
i
​
 ,F 
i
​
 ≤1000。

输出格式
输出单个整数：表示情商与智商和的最大值。贝西可以不让任何奶牛参加展览，如果这样做是最好的，输出 0。

输入输出样例
输入 #1复制

5
-5 7
8 -6
6 -3
2 1
-8 -5
输出 #1复制

8
说明/提示
选择第一头，第三头，第四头奶牛，智商和为 −5+6+2=3，情商和为 7−3+1=5。

再加入第二号奶牛可使总和提升到 10，不过由于情商和变成负的了，所以是不允许的。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
#dp[i][iq]表示考虑前i头奶牛，智商和为iq时，情商和的最大值
dp = [{} for _ in range(2)]
dp[0][0] = 0#什么都不选，智商和与情商和均为0
for i in range(1,n+1):
    cur_iq,cur_eq = read()
    cur = i%2
    pre = 1 - cur
    #不选当前奶牛，保留上一轮状态
    dp[cur] = dp[pre].copy()
    for iq,eq in dp[pre].items():
        new_iq = iq + cur_iq
        new_eq = eq + cur_eq
        if(new_eq > dp[cur].get(new_iq,float("-inf"))):
            dp[cur][new_iq] = new_eq#选当前奶牛
ans = 0
for iq,eq in dp[n%2].items():
    if(iq < 0 or eq < 0):
        continue
    ans = max(ans,iq+eq)
print(ans)
