""" D - 前缀串接 编辑 / 
Time Limit: 2 sec / Memory Limit: 1024 MiB
时间限制：2 秒 / 内存限制：1024 MiB

Score : 
400 points  得分： 
400 分

Problem Statement  问题描述
You are given an integer sequence 
(A 
1
​
 ,…,A 
N
​
 ) of length 
N.
给定一个整数序列 
(A 
1
​
 ,…,A 
N
​
 ) ，长度为 
N 。

Construct a sequence 
B of length 
2
N(N+1)
​
  by the following procedure.
通过以下程序构造长度为 
2
N(N+1)
​
  的序列 
B 。

Initially, let 
B be an empty sequence.
初始设 
B 为空序列。
For 
i=1,2,…,N in this order, append 
(A 
1
​
 ,…,A 
i
​
 ) to the end of 
B.
对于 
i=1,2,…,N ，按此顺序，将 
(A 
1
​
 ,…,A 
i
​
 ) 附加到 
B 末尾。
You are given 
Q queries of the following form; answer them.
你会得到以下形式的 
Q 查询;回答他们。

Query: You are given 
L and 
R. Find 
B 
L
​
 +B 
L+1
​
 +⋯+B 
R
​
 .
查询：你被赋予 
L 和 
R 。查找 
B 
L
​
 +B 
L+1
​
 +⋯+B 
R
​
  。

Constraints  约束
1≤N≤10 
5
 
1≤Q≤10 
5
 
−10 
8
 ≤A 
i
​
 ≤10 
8
 
For each query, 
1≤L≤R≤ 
2
N(N+1)
​
 .
对于每个查询， 
1≤L≤R≤ 
2
N(N+1)
​
  。
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

N 
Q
A 
1
​
  
A 
2
​
  
… 
A 
N
​
 
query 
1
​
 
query 
2
​
 
⋮
query 
Q
​
 
Here, 
query 
i
​
  represents the 
i-th query and is given in the following format:
这里， 
query 
i
​
  代表第 
i 次查询，格式如下：

L 
R
Output  输出结果
Print 
Q lines.  打印 
Q 行。
The 
i-th line should contain the answer to the 
i-th query.
i 第行应包含对 
i 第个查询的答案。

Sample Input 1  示例输入 1 复制
Copy  副本
4 3
1 10 100 1000
3 6
1 10
8 8
Sample Output 1  示例输出 1 复制
Copy  副本
121
1234
10
B=(1,1,10,1,10,100,1,10,100,1000).

The answer to the 
1-st query is 
10+1+10+100=121.
1 -st 查询的答案是 
10+1+10+100=121 。
The answer to the 
2-nd query is 
1+1+10+1+10+100+1+10+100+1000=1234.
2 -nd 查询的答案是 
1+1+10+1+10+100+1+10+100+1000=1234 。
The answer to the 
3-rd query is 
10.
3 -rd 查询的答案是 
10 。
Sample Input 2  示例输入 2 复制
Copy  副本
7 1
100000000 100000000 100000000 100000000 100000000 100000000 100000000
1 28
Sample Output 2  示例输出 2 复制
Copy  副本
2800000000 """
import sys
from itertools import accumulate
from math import isqrt
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())

#暴力做法
def solution1():
    n,q = read()
    a = list(read())
    b = []
    for i in range(n):
        b = b + a[:i+1]
    del a
    prefix = [0,*accumulate(b)]
    del b
    for _ in range(q):
        l,r = read()
        print(prefix[r] - prefix[l-1])

#使用前缀和思路找到对应的段数
def solution2():
    n, q = read()
    a = list(read())
    # A的前缀和，同时也是各块的元素和
    prefix = [0, *accumulate(a)]
    # 完整前i块的元素和
    prefix2 = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix2[i] = prefix2[i - 1] + prefix[i]
    def calc(x):
        # 前x项包含的完整块数
        k = (isqrt(1 + 8*x) - 1) // 2

        # 下一块中还包含多少个元素
        rest = x - k*(k + 1)//2

        return prefix2[k] + prefix[rest]

    for _ in range(q):
        l, r = read()
        print(calc(r) - calc(l - 1))
solution2()
