""" 题目描述
到中午了，机器猫要吃猫粮了。

机器猫掏出 n 份食物，第 i 份食物含有的能量为 w[i]。机器猫可以吃掉其中一些食物，获得这些食物的能量之和。

机器猫又不想变得太胖又不想变得太瘦，所以指定了一个目标区间 [l,r]。显然，可能有很多种选择食物的方式可以达成这个目标，因此机器猫想知道方案总数。

输入格式
第一行，三个正整数 n,l,r。

第二行，n 个正整数，表示每一份食物含有的能量 w[i]。

输出格式
仅一行，一个整数，表示方案数。

输入输出样例
输入 #1复制

4 70 85
10 10 20 50
输出 #1复制

4
说明/提示
样例解释
所有方案如下：

选择食物 1,2,4，能量 10+10+50=70；
选择食物 1,3,4，能量 10+20+50=80；
选择食物 2,3,4，能量 10+20+50=80；
选择食物 3,4，能量 50+20=70。

共 4 种方案。

数据规模与约定
对于 50% 的数据，满足 n≤20。

对于 100% 的数据，满足 n≤40,20≤w[i]≤100,l≤r≤300。

提示：w[i] 在范围内均匀随机生成。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,l,r = read()
arr = list(read())
#使用子集型枚举

ans = 0
#当前可枚举的最小下标，下标的最大值,现在的总和sum
def dfs(min,max,sum):
    global ans
    if(l<= sum <=r):
        ans += 1
    elif(sum > r):
        return
    if(min > max):
        return
    for index in range(min,max+1):
        number = arr[index]
        next_sum = sum + number
        if(next_sum > r):
            continue
        dfs(index + 1,max,next_sum)

dfs(0,n-1,0)
print(ans)