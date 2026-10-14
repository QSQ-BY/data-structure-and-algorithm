""" 题目描述
熊大和熊二在玩游戏。他们将 n 个正整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
  排成一行，然后各用一个长度为 k 的框在这个数组中各自随机框选出一段长度为 k 的连续子序列（随机框选指在合法的 n−k+1 个连续子序列中均匀随机）。熊大记录了他框出的 k 个数中的最大值 P，熊二记录了他框出的 k 个数的最小值 Q，他们突然有个疑问：P−Q 的期望是多少？

输入格式
输入共 2 行。

第一行为两个正整数 n,k。

第二行为 n 个由空格隔开的正整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 。

输出格式
输出共 1 行，一个浮点数（请保留两位小数）。

输入输出样例
输入 #1复制

3 2
1 2 3
输出 #1复制

1.00
说明/提示
样例说明
一共有四种情况：

熊大框出 [1,2]，P=2；熊二框出 [1,2]，Q=1，P−Q=1。
熊大框出 [1,2]，P=2；熊二框出 [2,3]，Q=2，P−Q=0。
熊大框出 [2,3]，P=3；熊二框出 [1,2]，Q=1，P−Q=2。
熊大框出 [2,3]，P=3；熊二框出 [2,3]，Q=2，P−Q=1。
所以 P−Q 的期望为 (1+0+2+1)/4=1.00。

评测用例规模与约定
对于 20% 的数据，保证 n≤10 
2
 。
对于 40% 的数据，保证 n≤10 
3
 。
对于 100% 的数据，保证 n≤10 
5
 ，0<a 
i
​
 ≤10 
9
 ，0<k≤n。 """
import sys
from collections import deque
from fractions import Fraction
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,length = read()
arr = list(read())
qmax = deque()#单调递减队列，队头是最小值
qmin = deque()#单调递增队列，对头是最小值
p = []
q = []
for right in range(n):
    left = right - length + 1
    while qmin and arr[qmin[-1]]>arr[right]:
        qmin.pop()
    while qmax and arr[qmax[-1]]<arr[right]:
        qmax.pop()
    qmin.append(right)
    qmax.append(right)
    while qmin[0] < left:
        qmin.popleft()
    while qmax[0] < left:
        qmax.popleft()
    if(right >= length-1):
        if(qmax):
            p.append(arr[qmax[0]])
        if(qmin):
            q.append(arr[qmin[0]])
m = n - length +1
ans = (sum(p) - sum(q))/m
print(f"{ans:.2f}")