""" 题目描述
给出 1,2,…,n 的两个排列 P 
1
​
  和 P 
2
​
 ，求它们的最长公共子序列。

输入格式
第一行是一个数 n。

接下来两行，每行为 n 个数，为自然数 1,2,…,n 的一个排列。

输出格式
一个数，即最长公共子序列的长度。

输入输出样例
输入 #1复制

5 
3 2 1 4 5
1 2 3 4 5
输出 #1复制

3
说明/提示
对于 50% 的数据， n≤10 
3
 ；
对于 100% 的数据， n≤10 
5
 。 """

import sys
from bisect import bisect_left
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#使用滚动数组进行优化的常规求解最长公共子序列的问题
def solution1():
    n = int(input())
    arr1 = [0]+list(read())
    arr2 = [0]+list(read())
    #dp[i][j]表示第一个序列在i位置以前
    # 第二个序列在j位置以前能有的最长的公共子序列
    #dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    #如果第i个位置和第j个位置相同
    #dp[i][j] =max(dp[i-1][j-1]+1,dp[i][j])

    dp = [[0] * (n + 1) for _ in range(2)]
    for i in range(1, n + 1):
        cur = i % 2          # 当前行
        pre = (i - 1) % 2    # 上一行
        dp[cur][0] = 0
        for j in range(1, n + 1):
            dp[cur][j] = max(dp[pre][j], dp[cur][j - 1])
            if arr1[i] == arr2[j]:
                dp[cur][j] = max(
                    dp[cur][j],
                    dp[pre][j - 1] + 1
                )
    print(dp[n % 2][n])

#利用两个序列都是排列的性质，将最长公共子序列转化为最长上升子序列
#最后的最终公共子序列继续要保证在第一个序列中是从左到右的
#又需要保证在第二个序列中是从左到右的，两个序列中包含的数字又是一定相同
#记录数字number在第一个序列值中出现的位置pos，把第二个序列中的数字全部转换为pos
#最后问题就是求解转换后的第二个序列中最长的上升子序列
def solution2():
    n = int(input())
    arr1 = list(read())

    #pos[number]表示number在第一个排列中的位置
    pos = [0] * (n + 1)
    for i, number in enumerate(arr1):
        pos[number] = i

    #dp[k]表示长度为k+1的上升子序列能取得的最小末尾位置
    dp = []
    for number in read():
        position = pos[number]
        j = bisect_left(dp, position)
        if j == len(dp):
            dp.append(position)
        else:
            dp[j] = position

    print(len(dp))

solution2()
