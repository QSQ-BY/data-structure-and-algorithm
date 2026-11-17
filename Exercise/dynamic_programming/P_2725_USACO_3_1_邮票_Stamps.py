""" 题目描述
给一组 n 枚邮票的面值集合和一个上限 k —— 表示信封上能够贴 k 张邮票。请求出最大的正整数 m，满足 1 到 m 的面值都可以用不超过 k 张邮票表示出来。

输入格式
输入的第一行是两个整数，分别代表邮票上限 k 和邮票面值数 n。

自第二行起，除最后一行外，每行有 15 个整数 a 
i
​
  ，最后一行的整数个数不超过 15，共有 n 个整数，第 i 个整数代表第 i 种邮票的面值 a 
i
​
 。

输出格式
输出一行一个整数代表 m。若 m 不存在请输出 0。

输入输出样例
输入 #1复制

5 2
1 3
输出 #1复制

13
说明/提示
样例输入输出 1 解释
有 1 分和 3 分的邮票；你最多可以贴 5 张邮票。很容易贴出 1 到 5 分的邮资（用 1 分邮票贴就行了），接下来的邮资也不难：

6=3+3。
7=3+3+1。
8=3+3+1+1。
9=3+3+3。
10=3+3+3+1。
11=3+3+3+1+1。
12=3+3+3+3。
13=3+3+3+3+1。
然而，使用 5 枚 1 分或者 3 分的邮票根本不可能贴出 14 分的邮资。因此，答案为 13。

数据规模与约定
对于 100% 的数据，保证 1≤k≤200，1≤n≤50，1≤a 
i
​
 ≤10 
4
 。

说明
题目翻译来自 NOCOW。 """
import sys
import heapq
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#使用枚举生成的思路
def solution1():
    k,n = read()
    values = list(map(int, sys.stdin.buffer.read().split()))
    values.sort()
    if(values[0] != 1):
        print(0)
        sys.exit()
    #dp[i]表示i元钱，能否用k张纸币凑出来
    dp = [False]*(k*max(values)+1)
    ans = values[0]
    heap = [(values[0],1,0)]#每次存入当前价值value,所用的钱币数cnt,以及最大的钱的下标index
    while(heap):
        value,cnt,index = heapq.heappop(heap)
        dp[value] = True
        if(value > 1):
            if(dp[value-1] == False):
                print(ans)
                sys.exit()
            else:
                ans = value
        if(index <= n-2):
            new1 = value-values[index]+values[index+1]
            heapq.heappush(heap,(new1,cnt,index+1))
        if(cnt<=k-1):
            new2 = value+values[index]
            heapq.heappush(heap,(new2,cnt+1,index))
    print(ans)

#使用动态规划的思路
def solution2():
    k,n = read()
    values = list(map(int, sys.stdin.buffer.read().split()))
    values.sort()
    if(values[0] != 1):
        print(0)
        sys.exit()
    upper = k*values[-1]
    #对于每一个金额记录他最少需要多少张邮票
    dp = bytearray([k+1])*(upper+1)
    dp[0] = 0
    dp[1] = 1
    ans = upper
    for s in range(2,upper+1):
        best = k+1
        for v in values:
            if(v > s):
                break
            best = min(dp[s-v]+1,best)
            if(best == 1):
                break
        if(best > k):
            ans = s - 1
            break
        dp[s] = best
    print(ans)

solution2()