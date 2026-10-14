""" 题目描述
Farmer John 的 N (N≤3×10 
5
 ) 头奶牛的高度为 1,2,…,N。一天，奶牛以某个顺序排成一行玩飞盘；令 h 
1
​
 …h 
N
​
  表示此顺序下奶牛们的高度（因此 h 是 1…N 的一个排列）。

队伍中位于位置 i 和 j 的两头奶牛可以成功地来回扔飞盘当且仅当她们之间的每头奶牛的高度都低于 min(h 
i
​
 ,h 
j
​
 )。

请计算所有可以成功地来回扔飞盘的奶牛所在的位置对 i<j 之间的距离总和。位置 i 和 j 之间的距离为 j−i+1。

输入格式
输入的第一行包含一个整数 N。第二行包含 h 
1
​
 …h 
N
​
 ，用空格分隔。

输出格式
输出可以成功地来回扔飞盘的奶牛所在的位置对 i<j 之间的距离总和。注意这个问题涉及到的整数可能需要使用 64 位整数型（例如，C 或 C++ 中的 "long long"）。

输入输出样例
输入 #1复制

7
4 3 1 2 5 6 7
输出 #1复制

24
说明/提示
【样例解释】

这个例子中可以成功的位置对如下：

(1, 2), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7)

【数据范围】

测试点 1-3 满足 N≤5000。

测试点 4-11 没有额外限制。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())

ans = 0
stack = []

# 找左边最近的、更高的牛
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        stack.pop()

    if stack:
        ans += i - stack[-1] + 1
    stack.append(i)

stack.clear()

# 找右边最近的、更高的牛
for i in range(n - 1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        stack.pop()

    if stack:
        ans += stack[-1] - i + 1

    stack.append(i)
print(ans)
