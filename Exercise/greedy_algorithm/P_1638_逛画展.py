""" 题目描述
博览馆正在展出由世上最佳的 m 位画家所画的图画。

游客在购买门票时必须说明两个数字，x 和 y，代表他要看展览中的第 x 幅至第 y 幅画（包含 x,y）之间的所有图画，而门票的价钱就是一张图画一元。

Sept 希望入场后可以看到所有名师的图画。当然，他想最小化购买门票的价格。

请求出他购买门票时应选择的 x,y，数据保证一定有解。

若存在多组解，输出 x 最小的那组。

输入格式
第一行两个整数 n,m，分别表示博览馆内的图画总数及这些图画是由多少位名师所绘画的。

第二行包含 n 个整数 a 
i
​
 ，代表画第 i 幅画的名师的编号。

输出格式
一行两个整数 x,y。

输入输出样例
输入 #1复制

12 5
2 5 3 1 3 2 4 1 1 5 4 3
输出 #1复制

2 7
说明/提示
数据规模与约定
对于 30% 的数据，有 n≤200，m≤20。
对于 60% 的数据，有 n≤10 
5
 ，m≤10 
3
 。
对于 100% 的数据，有 1≤n≤10 
6
 ，1≤a 
i
​
 ≤m≤2×10 
3
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,m = read()
arr = list(read())

#使用二分算法
def test01():
    left = m
    right = n
    #检查长度为length的窗口，返回最靠左的起点（从1开始），无解返回0
    def check(length):
        count = [0] * (m + 1)
        kinds = 0
        for i in range(length):
            painter = arr[i]
            if count[painter] == 0:
                kinds += 1
            count[painter] += 1
        if kinds == m:
            return 1
        for window_right in range(length,n):
            window_left = window_right - length
            painter = arr[window_left]
            count[painter] -= 1
            if count[painter] == 0:
                kinds -= 1
            painter = arr[window_right]
            if count[painter] == 0:
                kinds += 1
            count[painter] += 1
            if kinds == m:
                return window_left + 2
        return 0


    #01二分模型
    while left<right:
        mid = (left + right)//2
        if check(mid):
            right = mid
        else:
            left = mid+1

    x = check(left)
    print(x, x + left - 1)

#使用双指针算法
def test02():
    left = 0
    kinds = 0
    cnt = [0]*(m+1)
    ans_length = float("inf")
    ans = (0,0)
    for right in range(n):
        if(cnt[arr[right]] == 0):
            kinds += 1
        cnt[arr[right]] += 1
        while (left <= right and cnt[arr[left]] >1):
            cnt[arr[left]] -= 1
            left += 1
        if(kinds == m):
            cur_length = right - left + 1
            if(cur_length < ans_length):
                ans_length = cur_length
                ans = (left+1,right+1)
    print(*ans)

test02()
