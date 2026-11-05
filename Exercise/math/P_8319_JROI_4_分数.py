""" 题目背景
在 QQ 群中，经常会出现这样的接龙：

万人血书 xxx（1/10000）→
万人血书 xxx（1/5000）→
万人血书 xxx（1/2500）→
万人血书 xxx（1/1250）→…
以此类推，在可以约分的情况下，“万人血书”很快就能完成。

题目描述
“x 人血书”的过程可以看成一个函数 f(x)：

有一个  
x
0
​
  的分数。重复以下步骤直到这个分数为 1：

分子 +1。
如果这个分数可以约分，约分到最简形式。
现在小 D 给了你 T 组数据，每组数据都是给定 n，求在 1≤x≤n 的情况下 f(x) 的最大操作次数。

但是他太菜了，不会，你能帮帮他吗？

输入格式
第一行一个正整数 T。

接下来 T 行，每行一个正整数 n。

输出格式
共 T 行，每行一个整数 s 表示在 1≤x≤n 的情况下 f(x) 的最大操作次数。

输入输出样例
输入 #1复制

5
1
2
5
8
114514
输出 #1复制

1
2
5
7
114493
说明/提示
样例解释
f(1)=1,f(2)=2,f(3)=3,f(4)=3,f(5)=5。

我也想把更大的 f(x) 列出来，但是地方不够了。

数据范围
对于全部数据，1≤T≤5×10 
5
 ，1≤n≤2×10 
6
 。

Subtask 中没填的部分表示和全部数据的范围一样。

子任务编号	T 的范围	n 的范围	特殊性质	分值
Subtask 1	T≤3	n≤10		10
Subtask 2	T≤5	n≤10 
3
 		30
Subtask 3			n 为质数	10
Subtask 4		n≤5×10 
5
 		20
Subtask 5				30 """
import sys
from bisect import bisect_right
from math import isqrt

input = sys.stdin.buffer.readline

T = int(input())
queries = [int(input()) for _ in range(T)]
M = max(queries)

# 埃氏筛：只需要筛到所有查询中的最大值。
is_prime = [True] * (M + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, isqrt(M) + 1):
    if is_prime[i]:
        for j in range(i * i, M + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, M + 1) if is_prime[i]]

answers = []
for n in queries:
    if n == 1:
        answers.append('1')
    else:
        # 第一个大于 n 的素数的前一个，就是不超过 n 的最大素数。
        idx = bisect_right(primes, n) - 1
        answers.append(str(primes[idx]))

sys.stdout.write('\n'.join(answers))
