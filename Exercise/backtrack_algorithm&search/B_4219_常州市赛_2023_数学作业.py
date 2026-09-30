""" 题目背景
搬运自 http://czoj.com.cn/p/676。数据为民间数据。

题目描述
今天小 X 的数学老师带领大家学习了斐波那契序列：

斐波那契序列指的是这样一个数列：{1,2,3,5,8,13,21,34}。从第 3 个数开始，每个数都是前两个数的和，比如 8=3+5,34=13+21。数列里的数叫做斐波那契数。

一个数 n 的斐波那契表示是指把 n 写成若干个互不相同的斐波那契数的和。一个数可以有多种不同的斐波那契表示。比如 14 有三种斐波那契表示：14=1+13,14=1+5+8,14=1+2+3+8。数学老师给小 X 留下了一个数学作业，她告诉小 X 一个正整数 n，想让小 X 算出 n 有多少种不同的斐波那契表示。

小 X 请你帮助他完成他的数学作业。

输入格式
第一行为一个正整数 n。

输出格式
输出一行一个整数表示答案。

输入输出样例
输入 #1复制

14
输出 #1复制

3
输入 #2复制

1110
输出 #2复制

21
输入 #3复制

1000000000000
输出 #3复制

283392
说明/提示
测试点编号	n
1∼5	1≤n≤10 
4
 
6∼8	1≤n≤10 
9
 
9∼10	1≤n≤10 
12 """

import sys
input = sys.stdin.buffer.readline
from functools import lru_cache

def test01():
    n = int(input())
    f = [1,2]
    new = 3
    while new <= n:
        f.append(new)
        new = f[-1] + f[-2]
    #子集型枚举
    m = len(f) - 1
    ans = 0
    #当前可枚举的最小下标min,当前可枚举的最大下标max，当前的和s
    def dfs(min,max,s):
        global ans
        if(s==n):
            ans += 1
            return
        elif(s>n):
            return
        if(min > max):
            return
        for index in range(min,max+1):
            number = f[index]
            next_s = s + number
            if(next_s > n):
                break
            dfs(index + 1,max,next_s)

    dfs(0,m,0)
    print(ans)

def test02():
    n = int(input())
    f = [1,2]
    new = 3
    while new <= n:
        f.append(new)
        new = f[-1] + f[-2]

    # prefix[k] 表示 f 的前 k 个数的总和
    prefix = [0]
    for number in f:
        prefix.append(prefix[-1] + number)

    #记忆化搜索
    #只使用 f 的前 k 个数，凑出 rest，有多少种方案？
    @lru_cache(None)
    def dfs(k, rest):
        # 已经凑够：剩下的数全部不选
        if rest == 0:
            return 1

        # 没有数可选，或者全部选上也不够
        if k == 0 or rest > prefix[k]:
            return 0

        # 必须全部选上，恰好一种方案
        if rest == prefix[k]:
            return 1
        number = f[k - 1]
        # 当前最大数太大，只能不选
        if number > rest:
            return dfs(k - 1, rest)
        # 不选当前数的方案数 + 选当前数的方案数
        return dfs(k - 1, rest) + dfs(k - 1, rest - number)
    print(dfs(len(f), n))

test02()
