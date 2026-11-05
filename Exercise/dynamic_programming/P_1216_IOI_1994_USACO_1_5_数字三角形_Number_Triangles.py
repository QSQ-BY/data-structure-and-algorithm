""" 题目描述
观察下面的数字金字塔。

写一个程序来查找从最高点到底部任意处结束的路径，使路径经过数字的和最大。每一步可以走到左下方的点也可以到达右下方的点。



在上面的样例中，从 7→3→8→7→5 的路径产生了最大权值。

输入格式
第一个行一个正整数 r，表示行的数目。

后面每行为这个数字金字塔特定行包含的整数。

输出格式
单独的一行，包含那个可能得到的最大的和。

输入输出样例
输入 #1复制

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5 
输出 #1复制

30
说明/提示
【数据范围】
对于 100% 的数据，1≤r≤1000，其他输入在 [0,100] 范围内。

题目翻译来自 NOCOW。

IOI1994 Day1T1 / USACO Training Section 1.5。 """

import sys
import copy
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())
n = int(input())
arr = [[]for _ in range(n)]
for i in range(n):
    arr[i] = list(read())
#dp[i][j]表示到达第i层的第j个点的时候的时候能获得的最大路径之和
dp = copy.deepcopy(arr) #不管到达那一个点最后一定都会获得自己的价值
#第i 层一共有i+1个点
for i in range(1,n):
    for j in range(i+1):
        if(j-1 >= 0):
            dp[i][j] = max(dp[i][j],dp[i-1][j-1]+arr[i][j])
        if(j< i):
            dp[i][j] = max(dp[i][j],dp[i-1][j] + arr[i][j])
print(max(dp[n-1]))