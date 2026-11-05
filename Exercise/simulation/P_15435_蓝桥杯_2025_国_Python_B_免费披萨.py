""" 题目背景
Python 选手可以尝试使用 PyPy3 提交本题。

题目描述
蓝桥小镇披萨店的老板刚刚烤制了他人生中的第 n 个披萨！为了庆祝这一重要时刻，他推出了一项名为“幸运订单”的活动，顾客有机会赢取免费披萨。以下是活动的具体规则：

生成订单编号：每位顾客需要生成一个九位数的订单编号。生成方法如下：首先，将数字 1 到 8 进行任意排列（每个数字正好出现一次），组成一个八位数。然后，在这个八位数的任意位置（可以是开头、结尾或中间）插入一个 1 到 8 的数字，从而得到一个九位数的订单编号。
计算最大公约数，赢取免费披萨：披萨店老板会计算每位顾客生成的订单编号与 n 的最大公约数（GCD）。如果某个订单编号与 n 的最大公约数最大，那么该顾客就有机会赢得免费披萨。注意：订单编号必须严格满足上述生成规则，如果有多个订单编号与 n 的最大公约数相同且达到最大值，则只有生成数值最小的订单编号的顾客能够获奖。
现在，小蓝也想参加这个活动，并希望赢取免费披萨。请你帮助小蓝找出能够让他赢得免费披萨的订单编号。

输入格式
输入一行包含一个八位的正整数 n，表示披萨店老板烤制的第 n 个披萨。

输出格式
输出一行包含一个九位的正整数表示答案，即小蓝能够赢得免费披萨的最小订单编号。

输入输出样例
输入 #1复制

12345678
输出 #1复制

415637826
说明/提示
评测用例规模与约定
对于所有评测用例，10 
7
 ≤n<10 
8
 。 """
from math import gcd
import itertools
import sys
input = sys.stdin.buffer.readline

n_str = input().decode().strip()
n = int(n_str)
digits = []
for i in range(1,9):
    digits.append(str(i))
valid_numbers = set()

for p in itertools.permutations(digits):
    p_str = "".join(p)
    #枚举插入数字的位置
    for i in range(9):
        for d in digits:
            new_str = p_str[:i] + d+ p_str[i:]
            valid_numbers.add(int(new_str))

sorted_numbers = sorted(list(valid_numbers))
max_g = -1
best_ans = -1
for x in sorted_numbers:
    g = gcd(x,n)
    if(g > max_g):
        max_g = g
        best_ans = x
print(best_ans)