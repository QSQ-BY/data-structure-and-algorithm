""" 题目描述
给定两个长度为 n 的数组 a 和 b。

你可以任选 k∈[0,n]，将 a 的前 k 个元素和 b 的后 n−k 个元素拼接成一个长度为 n 的新数组。

请从新数组中选出恰好 m 个互不相邻的元素。记其中最小的元素为 p ，求 p 的最大值。

输入格式
第一行输入一个整数 T (1≤T≤10 
4
 )，表示测试数据的数量。

每组测试数据第一行输入两个整数 n 和 m (1≤m≤⌈ 
2
n
​
 ⌉≤n≤2×10 
5
 )，分别表示数组长度和需要选择的元素数量。

第二行输入 n 个整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
  (−10 
9
 ≤a 
i
​
 ≤10 
9
 )，表示数组 a。

第三行输入 n 个整数 b 
1
​
 ,b 
2
​
 ,…,b 
n
​
  (−10 
9
 ≤b 
i
​
 ≤10 
9
 )，表示数组 b。

保证所有测试数据的 ∑n≤2×10 
5
 。

输出格式
对于每组测试数据，输出一行一个整数，表示 p 的最大值。

输入输出样例
输入 #1复制

2
5 2
5 4 3 2 1
1 2 3 4 5
9 5
-1 1 -4 -5 -1 4 -1 -9 1
-9 -9 -8 2 4 -4 -3 -5 3
输出 #1复制

5
-4
说明/提示
对于第 1 组测试数据，当 k=4 时，新数组为 [5,4,3,2,5]，选择第 1,5 个元素，最小元素为 5，可以证明这是最大值。
 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
t = int(input())
ans = []

#检查两个数组一分为二之后能不能选出m个不相邻数字都大于等于x
#判断能不能通过某种拼接方式，
# 选出至少 \(m\) 个互不相邻、且数值都不小于 \(x\) 的元素。
def feasible(x,a,b,n,m):
    neg = -10**9
    # b0[i]、b1[i]：后缀 b[i:n] 中，不选、选 b[i] 时的最多选取数
    b0 = [0]*(n+1)
    b1 = [neg]*(n+1)
    for i in range(n-1,-1,-1):
        #如果不选择 b[i]，那么 b[i+1] 选或不选都可以
        b0[i] = max(b0[i + 1], b1[i + 1])
        #如果选 b[i]，则必须满足两个条件：
        #. b[i] >= x，这个元素达到门槛。
        #. 不选相邻的 b[i+1]，所以后面只能接 b0[i+1]。
        if b[i] >= x:
            b1[i] = 1 + b0[i + 1]
    # a0[k]、a1[k]：前缀 a[0:k] 中，不选、选 a[k-1] 时的最多选取数
    # k=0 表示空前缀，此时 a0[0]=0，a1[0]=neg
    a0 = [0]*(n+1)
    a1 = [neg]*(n+1)
    for i in range(n):
        #不选 a[i]，前一个位置选或不选都可以
        a0[i+1] = max(a0[i], a1[i])
        #选 a[i]，要求它达到门槛，且前一个位置不能选
        if a[i] >= x:
            a1[i+1] = 1 + a0[i]

    #枚举拼接位置k
    for k in range(n + 1):
        best = max(
            a0[k] + max(b0[k], b1[k]),
            a1[k] + b0[k],
        )
        if best >= m:
            return True

    return False

def solve():
    n,m = read()
    a = list(read())
    b = list(read())
    #答案一定是a,b原数组中的某一个值
    #所以进行合并去重排序之后对下标做二分就行
    values =sorted(set(a+b))
    left,right = 0,len(values) - 1
    while left < right:
        mid = (left + right + 1)//2
        if(feasible(values[mid],a,b,n,m)):
            left = mid
        else:
            right = mid - 1
    return values[left]

for _ in range(t):
    ans.append(solve())

for number in ans:
    print(number)
