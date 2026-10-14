""" 题目背景
POI 2010 Round III - day 2 Pilots.

题目描述
给定 n,k 和一个长度为 n 的序列，求最长的最大值最小值相差不超过 k 的子段。

输入格式
第一行两个由空格隔开的整数 k,n（0≤k≤2×10 
9
 ，1≤n≤3×10 
6
 ），k 表示设定的极差的最大值，n 表示序列的长度。

第二行 n 个由空格隔开的整数 a 
i
​
 （1≤a 
i
​
 ≤2×10 
9
 ）表示序列。

输出格式
一个整数表示符合条件的子段的长度最大值。

输入输出样例
输入 #1复制

3 9
5 1 3 5 8 6 6 9 10
输出 #1复制

4
说明/提示
样例解释：5,8,6,6 和 8,6,6,9 都是满足条件长度为 4 的子段。

作者：Piotr Chrząstowski """
import sys
from collections import deque

input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solution1():
    k,n = read()
    arr = list(read())
    left = 1
    right = n
    #检查是否存在长度为length的窗口使得最大值和最小值的差值不超过k
    def check(length:int):
        qmax = deque()#单调递减队列，队头为滑动窗口的最大值
        qmin = deque()#单调递增队列，队头为滑动窗口的最小值
        for right in range(n):
            left = max(0,right - length + 1)
            while qmax and arr[qmax[-1]] < arr[right]:
                qmax.pop()
            while qmin and arr[qmin[-1]] > arr[right]:
                qmin.pop()
            qmax.append(right)
            qmin.append(right)
            while qmax and qmax[0] < left:
                qmax.popleft()
            while qmin and qmin[0] < left:
                qmin.popleft()
            cur = arr[qmax[0]] - arr[qmin[0]]
            if right >= length - 1 and cur <= k:
                return True
        return False
    #10二分模型
    while(left < right):
        mid =(left + right + 1)//2
        if(check(mid) == True):
            left = mid
        else:
            right = mid - 1
    print(left)

def solution2():
    k, n = read()
    arr = list(read())
    qmax = deque()  # 单调递减队列，保存下标
    qmin = deque()  # 单调递增队列，保存下标
    left = 0
    ans = 0

    for right in range(n):
        # 加入当前元素，维护窗口的最大值和最小值
        while qmax and arr[qmax[-1]] <= arr[right]:
            qmax.pop()
        while qmin and arr[qmin[-1]] >= arr[right]:
            qmin.pop()
        qmax.append(right)
        qmin.append(right)

        # 极差超过 k 时，移动左端点直到窗口合法
        while arr[qmax[0]] - arr[qmin[0]] > k:
            left += 1
            while qmax and qmax[0] < left:
                qmax.popleft()
            while qmin and qmin[0] < left:
                qmin.popleft()

        ans = max(ans, right - left + 1)

    print(ans)
solution2()