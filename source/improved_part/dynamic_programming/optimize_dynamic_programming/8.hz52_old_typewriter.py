""" 题目描述
有一台古老的打字机和一篇待打印的文章，文章中有 n
n
 个字符，每个字符会有一个消耗值 Ci
C
i
, 打字机工作一次会打印若干连续的 k
k
 个字符，同时打字机会有磨损，打字机的单次磨损计算公式为：

(∑i=beginbegin+k−1Ci)2+M
(
∑
i
=
b
e
g
i
n
b
e
g
i
n
+
k
−
1
C
i
)
2
+
M

其中 M
M
 是打字机启动一次的固定磨损值，现在给你 n
n
 个字符的消耗值，问你打字机顺序打印出这 n
n
 个字符的最小磨损值为多少？

输入
第一行输入两个数字，n,M(1≤n≤106,1≤M≤104)
n
,
M
(
1
≤
n
≤
10
6
,
1
≤
M
≤
10
4
)
 代表文章中字符数量和打字机单次启动的固定磨损值。

第二行输入 n
n
 个数字，第 i
i
 个数字代表文章中第 i
i
 个字符的磨损值 Ci(1≤Ci≤100)
C
i
(
1
≤
C
i
≤
100
)
。

输出
输出一个整数，代表打字机顺序打完 n
n
 个字符的最小磨损值

样例输入1
6 40
3 3 6 5 1 2
样例输出1
256 """
#动态规划斜率优化

import sys
from itertools import accumulate
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,M = read()
sum = list(read())
sum = [0,*accumulate(sum)]
dp = [0]*(n+2)
#dp[i]表示打印前i个字符的最小消耗
""" dp[i] = min(dp[j] + prefix[j]**2 - 2prefix[i]prefix[j]+sum[i]**2+M)
查找值，混合值，确定值，用斜率优化 """


dp[1] = sum[1]**2 + M
dp[0] = 0

def slope(i:int,j:int):
    global f
    global sum
    number1 = dp[i] + sum[i]**2
    number2 = dp[j] + sum[j]**2
    return (number1-number2)/(sum[i]-sum[j])
def set(i:int,j:int):
    global dp
    global sum
    global M
    dp[i] = dp[j] + (sum[i]-sum[j])**2 + M
q = deque()
q.append(0)
for i in range(1,n+1):
    while(len(q)>=2 and slope(q[1],q[0]) < 2*sum[i]):
        q.popleft()
    set(i,q[0])
    while(len(q) >=2 and slope(q[-1],q[-2]) > slope(i,q[-1])):
        q.pop()
    q.append(i)
print(dp[n])