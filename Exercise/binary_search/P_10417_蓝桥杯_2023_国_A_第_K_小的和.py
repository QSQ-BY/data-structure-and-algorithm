""" 题目描述
给定两个序列 A,B，长度分别为 n,m。

设另有一个序列 C 中包含了 A,B 中的数两两相加的结果 (C 中共有 n×m 个数)。问 C 中第 K 小的数是多少。请注意重复的数需要计算多次。例如 1,1,2,3 中，最小和次小都是 1，而 3 是第 4 小。

输入格式
输入的第一行包含三个整数 n,m,K，相邻两个整数之间使用一个空格分隔。

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

第三行包含 m 个整数，分别表示 B 
1
​
 ,B 
2
​
 ,…,B 
m
​
 ，相邻两个整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

3 4 5
1 3 4
2 3 5 6
输出 #1复制

6
说明/提示
【评测用例规模与约定】

对于 40% 的评测用例，n,m≤5000，A 
i
​
 ,B 
i
​
 ≤1000;
对于所有评测用例，1≤n,m≤10 
5
 ，1≤A 
i
​
 ,B 
i
​
 ≤10 
9
 ，1≤K≤n×m。 """
import sys
from bisect import bisect_right
import heapq
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#使用二分的方法
def solution1():
    n, m, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    #cnt(x)表示有多少对和值小于等于x
    #我们要找的是使得cnt(x)>=k成立的最小正数x
    def check(x):
        j = m-1
        count = 0

        for value in a:
            while j >= 0 and value + b[j] > x:
                j -= 1

            if j < 0:
                break  # 后面的 a 更大，也不会有合法配对

            count += j + 1
            if count >= k:
                return True
        return False

    left = a[0] + b[0]
    right = a[-1] + b[-1]

    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1

    print(left)

#使用序列生成的思路
def solution2():
    n, m, k = read()
    a = sorted(read())
    b = sorted(read())

    if n > m:
        a, b = b, a
        n, m = m, n

    heap = [(a[i] + b[0], i, 0) for i in range(min(n, k))]
    heapq.heapify(heap)
    # 移除前 k-1 小，堆顶就是第 k 小
    for _ in range(k - 1):
        _, i, j = heap[0]

        if j + 1 < m:
            heapq.heapreplace(heap, (a[i] + b[j + 1], i, j + 1))
        else:
            heapq.heappop(heap)

    print(heap[0][0])

solution2()