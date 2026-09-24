""" 题目描述
给定 N 个整数 A 
1
​
 ,A 
2
​
 ,⋯,A 
N
​
 。请你从中选出 K 个数，使其乘积最大。

请你求出最大的乘积，由于乘积可能超出整型范围，你只需输出乘积除以 1000000009（即 10 
9
 +9）的余数。

注意，如果 X<0， 我们定义 X 除以 1000000009 的余数是 0−((0−x)mod1000000009)。

输入格式
第一行包含两个整数 N 和 K。

以下 N 行每行一个整数 A 
i
​
 。

输出格式
一个整数，表示答案。

输入输出样例
输入 #1复制

5 3 
-100000   
-10000   
2   
100000  
10000
输出 #1复制

999100009
输入 #2复制

5 3 
-100000   
-100000   
-2   
-100000  
-100000
输出 #2复制

-999999829
说明/提示
对于 40% 的数据，1≤K≤N≤100。

对于 60% 的数据，1≤K≤1000。

对于 100% 的数据，1≤K≤N≤10 
5
 ，−10 
5
 ≤A 
i
​
 ≤10 
5
 。 """

import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())
MOD = 10**9+9
#0代表正数1代表负数
n,k = read()
arr = []
for _ in range(n):
    number = int(input())
    if(number >=0):
        arr.append((abs(number),0))
    else:
        arr.append((abs(number),1))

arr.sort(reverse = True)
ans = []
negative = 0
for i in range(k):
    number,symbol = arr[i]
    if(symbol == 1):
        negative += 1
    ans.append((number,symbol))

is_negative = negative % 2 == 1
if is_negative:
    selected_negative = min((number for number,symbol in ans if symbol == 1), default = None)
    selected_positive = min((number for number,symbol in ans if symbol == 0 and number > 0), default = None)
    remaining_positive = max((number for number,symbol in arr[k:] if symbol == 0 and number > 0), default = None)
    remaining_negative = max((number for number,symbol in arr[k:] if symbol == 1), default = None)

    swap_negative = selected_negative is not None and remaining_positive is not None
    swap_positive = selected_positive is not None and remaining_negative is not None

    if swap_negative and (not swap_positive or remaining_positive * selected_positive >= remaining_negative * selected_negative):
        ans.remove((selected_negative,1))
        ans.append((remaining_positive,0))
        is_negative = False
    elif swap_positive:
        ans.remove((selected_positive,0))
        ans.append((remaining_negative,1))
        is_negative = False
    else:
        if any(number == 0 for number,_ in arr):
            print(0)
            sys.exit()
        # k == n：所有数都必须选，ans 保持不变，即使其中有正数。
        # k < n：此时只能是全负数且 k 为奇数，改选绝对值最小的 k 个。
        if k < n:
            ans = arr[-k:]

result = 1
for number,_ in ans:
    result = result * number % MOD
print(-result if is_negative else result)
