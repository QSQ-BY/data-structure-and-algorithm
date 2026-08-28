""" 题目描述
Anzu 有一个正整数数列 a 
1
​
 ,…,a 
n
​
  和一个整数 x。她可以进行至多一次操作，选择一对正整数 1≤l≤r≤n，然后对于所有 l≤i≤r 的正整数 i 让 a 
i
​
  变成 x。现在她想要知道，在这之后，数列里所有数的和最大是多少。

输入格式
第一行，两个非负整数 n,x。

第二行，n 个正整数 a 
1
​
 ,…,a 
n
​
 。

输出格式
仅一行，一个正整数，表示答案。

输入输出样例
输入 #1复制

5 2
1 4 1 1 5
输出 #1复制

14
输入 #2复制

7 3
1 1 4 5 1 4 1
输出 #2复制

21
输入 #3复制

1 197
251
输出 #3复制

251
说明/提示
【样例解释 #1】

最优的策略是选择 l=3，r=4 进行一次操作，此时数列变为 [1,4,2,2,5]，总和为 14。

【样例解释 #2】

最优的策略为选择 l=1，r=7 进行一次操作。

【样例解释 #3】

最优的策略为不进行操作。

【数据范围】

对于 30% 的数据，n≤500。

对于另外 20% 的数据，n≤3×10 
3
 。

对于另外 10% 的数据，x=0。

对于所有数据，保证 1≤n≤10 
5
 ，1≤a 
i
​
 ≤10 
9
 ，0≤x≤10 
9
 。 """

import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def test01():
    n,x = read()
    arr = list(read())
    prefix = [0,*accumulate(arr)]
    s = prefix[-1]
    #dp[i]表示以i位置为结尾的区间变换能获得的最大价值
    dp = [0]*(n+1)
    if(prefix[1] >= x):
        dp[1] = s
    else :
        dp[1] = x - prefix[1] + s
    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i] = max(dp[i],(i-j+1)*x + s - prefix[i] + prefix[j-1])
    print(max(max(dp),s))

def test02():
    n,x = read()
    arr= list(read())
    s = sum(arr)
    #ans = s+ sum(x-ai)
    arr = [x - arr[i] for i in range(n)]
    #求解新arr的最大子段和
    dp = [0]*(n+1)
    dp[0] = arr[0]
    
    for i in range(1,n):
        if(dp[i-1] >= 0):
            dp[i] = arr[i] + dp[i-1]
        else:
            dp[i] = arr[i]
    print(s + max(dp))


#test01()
test02()