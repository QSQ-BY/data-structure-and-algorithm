""" 题目描述
给定一个长度为 n 的序列 A 
i
​
 ，求 L,R 使 (R−L+1)⋅min(A 
L
​
 ,A 
L+1
​
 ,…,A 
R
​
 ) 尽可能大，其中 min 表示最小值。

你只需要输出最大的值即可，不需要输出具体的 L,R。

输入格式
输入的第一行包含一个整数 n。

第二行包含 n 个整数，分别表示 A 
1
​
 ,A 
2
​
 ,…,A 
n
​
 ，相邻两个整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

5
1 1 3 3 1
输出 #1复制

6
说明/提示
评测用例规模与约定
对于 40% 的评测用例，1≤n≤5000，1≤A 
i
​
 ≤5000；

对于所有评测用例，1≤n≤3×10 
5
 ，1≤A 
i
​
 ≤10 
9
 。 """
#本质就是和最大矩形面积一个题
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())
left = [-1] * n
right = [n] * n
stack = []

# 左边最近的、严格更小的元素
for i in range(n):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()

    if stack:
        left[i] = stack[-1]

    stack.append(i)

stack.clear()

# 右边最近的、严格更小的元素
for i in range(n - 1, -1, -1):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()

    if stack:
        right[i] = stack[-1]

    stack.append(i)

ans = 0
for i in range(n):
    length = right[i] - left[i] - 1
    ans = max(ans, length * arr[i])

print(ans)