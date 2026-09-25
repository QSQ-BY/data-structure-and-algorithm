""" 题目描述
n 位同学站成一排，音乐老师要请其中的 n−k 位同学出列，使得剩下的 k 位同学排成合唱队形。

合唱队形是指这样的一种队形：设 k 位同学从左到右依次编号为 1,2, … ,k，他们的身高分别为 t 
1
​
 ,t 
2
​
 , … ,t 
k
​
 ，则他们的身高满足 t 
1
​
 <⋯<t 
i
​
 >t 
i+1
​
 > … >t 
k
​
 (1≤i≤k)。

你的任务是，已知所有 n 位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

输入格式
共二行。

第一行是一个整数 n（2≤n≤100），表示同学的总数。

第二行有 n 个整数，用空格分隔，第 i 个整数 t 
i
​
 （130≤t 
i
​
 ≤230）是第 i 位同学的身高（厘米）。

输出格式
一个整数，最少需要几位同学出列。

输入输出样例
输入 #1复制

8
186 186 150 200 160 130 197 220
输出 #1复制

4
说明/提示
对于 50% 的数据，保证有 n≤20。

对于全部的数据，保证有 n≤100。 """
#最长上升子序列,查找两边如果数值一样就相加
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def test01():
    n = int(input())
    arr = list(read())
    #dp[i]表示长度为i的最长上升子序列的末尾数字是多少
    left = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                left[i] = max(left[i], left[j] + 1)

    right = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                right[i] = max(right[i], right[j] + 1)

    print(n - max(left[i] + right[i] - 1 for i in range(n)))


def test02():
    n = int(input())
    arr = list(read())
    left_len = [0]*(n)
    #以第i个同学为结尾的严格上升子序列的长度
    tails = []
    for i,height in enumerate(arr):
        pos = bisect_left(tails,height)
        if(pos == len(tails)):
            tails.append(height)
        else:
            tails[pos] = height

        left_len[i] = pos+1

    #以第i个同学为开头的最长下降子序列的长度
    right_len = [0]*(n)
    tails = []
    for i in range(n-1,-1,-1):
        height = arr[i]
        pos = bisect_left(tails,height)

        if(pos == len(tails)):
            tails.append(height)
        else:
            tails[pos] = height
        right_len[i] = pos+1

    max_students = max(
        left_len[i] + right_len[i] - 1 
        for i in range(n)
    )
    print(n - max_students)

#test01()
test02()