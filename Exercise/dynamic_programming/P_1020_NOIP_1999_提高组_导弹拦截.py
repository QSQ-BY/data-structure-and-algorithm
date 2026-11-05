""" 题目描述
某国为了防御敌国的导弹袭击，发展出一种导弹拦截系统。但是这种导弹拦截系统有一个缺陷：虽然它的第一发炮弹能够到达任意的高度，但是以后每一发炮弹都不能高于前一发的高度。某天，雷达捕捉到敌国的导弹来袭。由于该系统还在试用阶段，所以只有一套系统，因此有可能不能拦截所有的导弹。

输入导弹依次飞来的高度，计算这套系统最多能拦截多少导弹，如果要拦截所有导弹最少要配备多少套这种导弹拦截系统。

输入格式
一行，若干个整数，中间由空格隔开。

输出格式
两行，每行一个整数，第一个数字表示这套系统最多能拦截多少导弹，第二个数字表示如果要拦截所有导弹最少要配备多少套这种导弹拦截系统。

输入输出样例
输入 #1复制

389 207 155 300 299 170 158 65
输出 #1复制

6
2
说明/提示
对于前 50% 数据，满足导弹的个数不超过 10 
4
  个。该部分数据总分共 100 分。可使用 O(n 
2
 ) 做法通过。
对于后 50% 的数据，满足导弹的个数不超过 10 
5
  个。该部分数据总分也为 100 分。请使用 O(nlogn) 做法通过。

对于全部数据，满足导弹的高度为正整数，且不超过 5×10 
4
 。

此外本题开启 spj，每点两问，按问给分。

NOIP1999 提高组 第一题

upd 2022.8.24：新增加一组 Hack 数据。 """

import sys
from copy import deepcopy
from bisect import bisect_right,bisect_left#查找第一个严格大于当前值的位置
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#第一个就是求解最长下降子序列，
# 第二个就是求解最少能能分成多少组下降子序列
arr = list(read())
n = len(arr)
dp = []
arr.reverse()#把数组翻转过来求解最长上升子序列，方便直接使用bisect
for number in arr:
    pos = bisect_right(dp,number)
    if(pos > len(dp)-1):
        dp.append(number)
    else:
        dp[pos] = number
print(len(dp))

#使用迭代加深进行暴力搜索，时间复杂度过高
def solution1():
    def dfs(index:int,groups:list[list[int]],depth):
        cnt = len(groups)
        if(cnt > depth):
            return False
        if(index == n):
            return True
        number = arr[index]
        new_groups = deepcopy(groups)
        #搜索能接在旧的组后面
        for i in range(cnt):
            group = groups[i]
            if(group[-1] <= number):
                new_groups[i].append(number)
                if dfs(index+1,new_groups,depth):
                    return True
                new_groups[i].pop()
        #开一个新的组
        new_groups.append([number])
        if dfs(index+1,new_groups,depth):
            return True
        return False

    depth = 1
    while(dfs(0,[],depth) == False):
        depth += 1
    print(depth)
#solution1()

arr.reverse()
dp = []
#答案等于原序列的最长严格上升子序列长度
for number in arr:
    pos = bisect_left(dp,number)
    if(pos > len(dp)-1):
        dp.append(number)
    else:
        dp[pos] = number

print(len(dp))