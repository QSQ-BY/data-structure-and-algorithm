""" 题目描述
给定一个长度为 n 的数列 {a}，求 {a} 的子序列 {b} 的最长长度 k，满足 b
i
​
 ∧b
i−1
​


=0，其中 2≤i≤k， ∧ 表示位运算取与。

输入格式
输入文件共 2 行。 第一行包括一个整数 n。 第二行包括 n 个整数，第 i 个整数表示 a
i
​
。

输出格式
输出文件共一行。 包括一个整数，表示子序列 {b} 的最长长度。

输入输出样例
输入 #1复制

3
1 2 3
输出 #1复制

2
说明/提示
对于 100% 的数据，1≤n≤100000，a
i
​
≤10
9
。
"""

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
def test01():
    n = int(input())
    arr = list(read())
    len =[]#len[i]表示以i号数字结尾的最长的满足条件的序列
    for i in range(n):
        len.append(1)

    for i,number1 in enumerate(arr):
        for j in range(i):
            if(number1 & arr[j] != 0):
                len[i] = max(len[i],len[j]+1)
    print(max(len))

def test02():
    n = int(input())
    arr = list(read())

    #best[i]表示
    #前面以“第 0 位为 1”的数字结尾，最长能有多长
    #前面以“第 1 位为 1”的数字结尾，最长能有多长
    #……
    #前面以“第 29 位为 1”的数字结尾，最长能有多长
#best[j] = 目前为止，结尾数字的第 j 位为 1 的最长子序列长度
    best = [0]*30
    for number1 in arr:
        current = 1
        used_bits = []
        for j in range(30):
            #第j位数字为1
            if (number1 & (1<<j) != 0):
                used_bits.append(j)
                current = max(current,best[j]+1)
        for j in used_bits:
            best[j] = max(best[j],current)
    print(max(best))

#test01()
test02()