""" 题目背景
题目名称是吸引你点进来的。
实际上该题还是很水的。

题目描述
给定 l,r，求区间 [l,r] 内质数的个数。

输入格式
第一行有两个整数，分别代表询问次数 n 和给定区间的右端点最大值 m。

接下来 n 行，每行两个整数 l,r，代表一次查询。

输出格式
对于每次查询输出一行，若 l,r∈[1,m]，则输出区间质数个数，否则输出 Crossing the line。

输入输出样例
输入 #1复制

2 5
1 3
2 6
输出 #1复制

2
Crossing the line
说明/提示
数据范围与约定
对于 20% 的数据，保证 n,m≤10。
对于 100% 的数据，保证 1≤n≤1000，1≤m≤10 
6
 ，−10 
9
 ≤l≤r≤10 
9
 。 """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m = read()#进行n次询问，最大的素数是m
is_prime = [True]*(m+1)
is_prime[0] = is_prime[1] = False
for i in range(2,m+1):
    if(is_prime[i] == False):
        continue
    for next in range(i*i,m+1,i):
        is_prime[next] = False
#cnt[m]表示在0到m闭区间范围内的素数个数是多少
cnt = [0]*(m+1)
for i in range(1,m+1):
    if(is_prime[i] == True):
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]

for _ in range(n):
    l,r = read()
    if(l<1 or r>m):
        print("Crossing the line")
        continue
    print(cnt[r] - cnt[l-1])