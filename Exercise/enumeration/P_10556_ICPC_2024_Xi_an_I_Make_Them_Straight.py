""" 题目描述
有一个长度为 n 的非负整数序列 a，其中第 i 个元素为 a 
i
​
 (1≤i≤n)。

如果存在一个非负整数 k(0≤k≤10 
6
 ) 满足以下条件，则该序列被定义为「好」序列：

对于所有 1≤i≤n，都有 a 
i
​
 =a 
1
​
 +(i−1)k。

为了使这个序列成为「好」序列，对于每个 i(1≤i≤n)，你可以选择不做任何操作，或者支付 b 
i
​
  个硬币将 a 
i
​
  替换为任意非负整数。

问题是，使这个序列成为「好」序列的最小代价是多少。

输入格式
第一行包含一个整数 n(1≤n≤2×10 
5
 )，如题述。

第二行包含 n 个整数 a 
1
​
 ,...,a 
n
​
 (0≤a 
i
​
 ≤10 
6
 )。

第三行包含 n 个整数 b 
1
​
 ,...,b 
n
​
 (0≤b 
i
​
 ≤10 
6
 )。

输出格式
一个整数，表示答案。

输入输出样例
输入 #1复制

5
1 4 3 2 5
1 1 1 1 1
输出 #1复制

2
输入 #2复制

5
1 4 3 2 5
1 9 1 1 1
输出 #2复制

3
说明/提示
（由 ChatGPT 4o 翻译） """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n=int(input())
a = list(read())
b = list(read())
prefix = [0,*accumulate(b)]
M = max(a)
best = 0

# k = 0：目标序列所有数相同
saved = {}
for value, cost in zip(a, b):
    current = saved.get(value, 0) + cost
    saved[value] = current
    best = max(best, current)

# k > 0 枚举公差k
for k in range(1, M + 1):
    # 下标 0 对应的首项始终是 a[0]
    saved = {a[0]: b[0]}

    limit = min(n - 1, M // k)
    for i in range(1, limit + 1):
        first = a[i] - i * k#查找第i个数字对应的对开头的数字，第i个数字所在的序列在公差为k的情况下最开头的数字一定是a[i] - i*k

        if first < 0:
            continue

        current = saved.get(first, 0) + b[i]
        saved[first] = current
        best = max(best, current)

print(prefix[-1] - best)
