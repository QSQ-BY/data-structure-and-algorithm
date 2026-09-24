""" 题目描述
阿里巴巴走进了装满宝藏的藏宝洞。藏宝洞里面有 N(N≤100) 堆金币，第 i 堆金币的总重量和总价值分别是 m 
i
​
 ,v 
i
​
 (1≤m 
i
​
 ,v 
i
​
 ≤100)。阿里巴巴有一个承重量为 T(T≤1000) 的背包，但并不一定有办法将全部的金币都装进去。他想装走尽可能多价值的金币。所有金币都可以随意分割，分割完的金币重量价值比（也就是单位价格）不变。请问阿里巴巴最多可以拿走多少价值的金币？

输入格式
第一行两个整数 N,T。

接下来 N 行，每行两个整数 m 
i
​
 ,v 
i
​
 。

输出格式
一个实数表示答案，输出两位小数。

输入输出样例
输入 #1复制

4 50
10 60
20 100
25 100
15 45
输出 #1复制

240.00 """
import sys
input = sys.stdin.buffer.readline
from functools import cmp_to_key
def read():
    return map(int,input().split())
def cmp(a,b):
    number1 = a[1]/a[0]
    number2 = b[1]/b[0]
    if(number1 > number2):
        return -1
    elif(number1 < number2):
        return 1
    else:
        return 0
n,t = read()#金币的个数和背包的总承重
coin = []
for _ in range(n):
    weight,value = read()#金币的重量和金币的价值
    coin.append((weight,value))

coin.sort(key = cmp_to_key(cmp))
ans = 0
for i in range(n):
    weight = coin[i][0]
    value = coin[i][1]
    if(t >= weight):
        ans += value
        t -= weight
    else:
        ans += value/weight * t
        break
print(f"{ans:.2f}")


