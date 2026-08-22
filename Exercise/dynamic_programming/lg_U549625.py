""" 题目描述
帅气的大白熊这天向小苯提出了一个问题，他给了小苯一个长度为 n 的数组 a 。

他想知道，对于所有 1≤i≤n 的下标 i ，都从数组中选择一段连续的区间 [l,r] 使得 l≤i≤r ，即选择一个包含 i 的区间的话，这段区间和最大是几？

请聪明的你帮帮小苯解答吧。

输入格式
输入包含两行。 第一行一个正整数 n(1≤n≤2×10
5
 )。 第二行 n 个整数 a
i
​
 (−10
9
 ≤a
i
​
 ≤10
9
 )，表示这个数组。

输出格式
输出包含一行 n 个整数。 其中第 i 个整数代表，选择一段包含 a
i
​
  的区间，这段区间的最大和。

输入输出样例
输入 #1复制

4
1 -2 3 -4
输出 #1复制

2 2 3 -1
输入 #2复制

3
-1 -1 -1
输出 #2复制

-1 -1 -1
说明/提示
样例解释1
i=1 ，选择 [1,3]，结果是： 1+(−2)+3=2。是最优解。
i=2 ，选择 [1,3]
i=3 ，选择 [3,3]
i=4 ，选择 [3,4] """


""" left[i]：以 a[i] 结尾的最大连续区间和
right[i]：以 a[i] 开始的最大连续区间和
对于必须包含 i 的最优区间，可以拆成：
[l ... i] + [i ... r]
因此：

ans[i]=left[i]+right[i]-a[i]
减去 a[i]，是因为左右两部分都包含它，加了两遍。 """
import sys
input = sys.stdin.buffer.readline
from itertools import accumulate
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())
arr = [0]+arr+[0]
left = [0]*(n+2)
left[1] = arr[1]
for i in range(2,n+1):
    if(left[i-1] > 0):
        left[i] = arr[i]+left[i-1]
    elif(left[i-1]<=0):
        left[i] = arr[i]

arr.reverse()
right = [0]*(n+2)
right[1] = arr[1]
for i in range(2,n+1):
    if(right[i-1] > 0):
        right[i] = right[i-1]+arr[i]
    elif(right[i-1]<0):
        right[i] = arr[i]
right.reverse()
arr.reverse()
ans = []
for i in range(1,n+1):
    number = left[i] + right[i] - arr[i]
    ans.append(number)
print(*ans)
