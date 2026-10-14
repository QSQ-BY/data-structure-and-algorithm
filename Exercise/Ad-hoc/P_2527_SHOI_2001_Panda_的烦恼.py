""" 题目描述
Panda 是个数学怪人，他非常喜欢研究跟别人相反的事情。最近他正在研究筛法，众所周知，对一个范围内的整数，经过筛法处理以后，剩下的全部都是质数，不过 Panda 对这些不感兴趣，他只对被筛掉的数感兴趣，他觉得在这些被筛掉的数中一定隐藏着重要的宇宙秘密，只是人们还没有发现罢了。

Panda 还觉得如果只是单纯地从小到大筛的话，还不足够发现其中的奥秘，于是他决定对至多只包含某些质因数的数进行研究（比如说至多只包含质因数 2,3 的数有 2,3,4,6,8,9,…），他需要得到这些数中第 k 小的数（k 是 Panda 认为的宇宙系数），请你编个程序，帮助他找到这个数。

输入格式
第一行有两个整数 n,k，n 代表质因数的个数，k 代表那个宇宙系数。

第二行有 n 个整数，代表这 n 个质因数，设这些质因数组成的序列为 p。

输出格式
仅一行，即至多只包含这 n 个质因数的数中第 k 小的正整数，设这个答案为 ans。

输入输出样例
输入 #1复制

2 7
3 5
输出 #1复制

45

说明/提示
样例解释
前六个数分别是 3,5,9,15,25,27。

数据范围及限制
对于所有数据，有:

1≤n≤100
1≤k≤10 
5
 
∀1≤i<j≤n,p 
i
​
 

=p 
j
​
  且 p 
i
​
 ∈P
1≤ans≤2×10 
9
 。 """

import sys
import heapq
from heapq import heappop, heappush

data = list(map(int, sys.stdin.buffer.read().split()))
n, k = data[:2]
p = sorted(data[2:2 + n])

def solution1():
    heap = [1]
    seen = {1}
    count = 0
    while heap:
        x = heapq.heappop(heap)
        if x != 1:
            count += 1
            if count == k:
                print(x)
                break
        for prime in p:
            y = x * prime

            # 题目保证答案不超过这个范围
            if y <= 2_000_000_000 and y not in seen:
                seen.add(y)
                heapq.heappush(heap, y)

def solution2():
    # (数值，最大质因数的下标)
    heap = [(p[0], 0)]
    limit = 2_000_000_000

    for count in range(1, k + 1):
        x, i = heappop(heap)

        if count == k:
            print(x)
            break

        # ① 再乘一个当前最大质因数
        y = x * p[i]
        if y <= limit:
            heappush(heap, (y, i))

        # ② 把最后一个最大质因数换成下一个质因数
        if i + 1 < n:
            y = (x / p[i]) * p[i + 1]
            if y <= limit:
                heappush(heap, (y, i + 1))

#solution1()
solution2()