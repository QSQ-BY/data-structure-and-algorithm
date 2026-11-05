""" 题目描述
kkk 做了一个人体感觉分析器。每一天，人都有一个感受值 A 
i
​
 ，A 
i
​
  越大，表示人感觉越舒适。在一段时间 [i,j] 内，人的舒适程度定义为 [i,j] 中最不舒服的那一天的感受值 × [i,j]中每一天感受值的和。现在给出 kkk 在连续 N 天中的感受值，请问，在哪一段时间，kkk 感觉最舒适？

输入格式
第一行为 N，代表数据记录的天数。

第二行 N 个整数，代表每一天的感受值。

输出格式
一行，表示在最舒适的一段时间中的舒适程度。

输入输出样例
输入 #1复制

6
3 1 6 4 5 2
输出 #1复制

60
说明/提示
kkk 最舒适的一段时间是第 3 天到第 5 天，舒适程度：(6+4+5)×4=60。

对于 30% 的数据，1≤N≤100。

对于 70% 的数据，1≤N≤2000。

对于 100% 的数据，1≤N≤10 
5
 ，1≤A 
i
​
 ≤10 
6
 。 """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())
stack = []
#left表示距离i号左边位置最近的小于他的元素
#right表示距离i号右边位置最近的小于它的元素
left = [-1]*(n)
right = [n]*(n)
ans = 0
prefix = [0,*accumulate(arr)]
for i in range(n):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if(stack):
        left[i] = stack[-1]
    stack.append(i)
stack.clear()
for i in range(n-1,-1,-1):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if(stack):
        right[i] = stack[-1]
    stack.append(i)
for i in range(n):
    ans = max(ans,arr[i]*(prefix[right[i]] - prefix[left[i]+1]))
print(ans)