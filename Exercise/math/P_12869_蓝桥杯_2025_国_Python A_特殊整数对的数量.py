""" 题目描述
我们称一对正整数 (a,b) 是 “特别互素对”，如果满足以下条件：

1≤a<b≤10 
6
  。
a 与 b 互素，即 a 和 b 的最大公约数为 1 。
a+b 是 2025 的倍数。
请计算一共有多少对 (a,b) 是 “特别互素对”。

输入格式
无

输出格式
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个数字，在提交答案时只填写这个数字，填写多余的内容将无法得分。

输入输出样例
无 """
from math import gcd
#暴力做法，一分钟之内可以解出来
def solution1():
    limit = 2*10**6
    base = 2025
    multi = 1
    ans = 0
    while(base*multi <= limit):
        for i in range(1,base*multi):
            j = base*multi - i
            if(i>j):
                break
            if(i > 10**6 or j>10**6):
                continue
            if(gcd(i,j) == 1):
                ans += 1
        multi += 1
    print(ans)
#最大公约数恒等式gcd(a,b) = gcd(a,a+b)
solution1()
