""" 题目描述
设有 N(N≤300) 堆石子排成一排，其编号为 1,2,3,⋯,N。每堆石子有一定的质量 m 
i
​
  (m 
i
​
 ≤1000)。现在要将这 N 堆石子合并成为一堆。每次只能合并相邻的两堆，合并的代价为这两堆石子的质量之和，合并后与这两堆石子相邻的石子将和新堆相邻。合并时由于选择的顺序不同，合并的总代价也不相同。试找出一种合理的方法，使总的代价最小，并输出最小代价。

输入格式
第一行，一个整数 N。

第二行，N 个整数 m 
i
​
 。

输出格式
输出文件仅一个整数，也就是最小代价。

输入输出样例
输入 #1复制

4
2 5 3 1
输出 #1复制

22 """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#弱化版本序列型石子合并
def solution1():
    n = int(input())
    arr = list(read())
    prefix = [0,*accumulate(arr)]
    #dp[i][j]表示把闭区间[i,j]的石子进行合并所需要的最小代价
    dp = [[float("inf")]*(n)for _ in range(n)]
    #length = 1的时候，所有都是0
    for i in range(n):
        dp[i][i] = 0
    for length in range(2,n+1):
        for right in range(length-1,n):
            left = right - length+1
            for mid in range(left,right):
                dp[left][right] = min(
                    dp[left][mid]+dp[mid+1][right]
                    +prefix[right + 1]-prefix[left]
                    ,dp[left][right]
                )

    print(dp[0][n-1])
""" 题目描述
在一个圆形操场的四周摆放 N 堆石子，现要将石子有次序地合并成一堆，规定每次只能选相邻的 2 堆合并成新的一堆，并将新的一堆的石子数，记为该次合并的得分。

试设计出一个算法，计算出将 N 堆石子合并成 1 堆的最小得分和最大得分。

输入格式
数据的第 1 行是正整数 N，表示有 N 堆石子。

第 2 行有 N 个整数，第 i 个整数 a 
i
​
  表示第 i 堆石子的个数。

输出格式
输出共 2 行，第 1 行为最小得分，第 2 行为最大得分。

输入输出样例
输入 #1复制

4
4 5 9 4
输出 #1复制

43
54
说明/提示
1≤N≤100，0≤a 
i
​
 ≤20。 """
#环形石子合并
def solution2():
    n = int(input())
    arr = list(read())
    arr = arr + arr
    size = 2 * n
    prefix = [0, *accumulate(arr)]
    #dp_min[l][r]：把 [l,r] 合成一堆的最小代价
    #dp_max[l][r]：把 [l,r] 合成一堆的最大代价
    #最小代价 = 左边最小代价 + 右边最小代价 + 整段石子总量
    #最大代价 = 左边最大代价 + 右边最大代价 + 整段石子总量
    dp_min = [[float("inf")] * size for _ in range(size)]
    dp_max = [[0] * size for _ in range(size)]

    for i in range(size):
        dp_min[i][i] = 0

    # 只计算长度不超过 n 的区间就能保证展开后的数组就是一个环形的选择
    for length in range(2, n + 1):
        for left in range(size - length + 1):
            right = left + length - 1
            cost = prefix[right + 1] - prefix[left]

            for mid in range(left, right):
                dp_min[left][right] = min(
                    dp_min[left][right],
                    dp_min[left][mid] + dp_min[mid + 1][right] + cost
                )
                dp_max[left][right] = max(
                    dp_max[left][right],
                    dp_max[left][mid] + dp_max[mid + 1][right] + cost
                )

    print(min(dp_min[i][i + n - 1] for i in range(n)))
    print(max(dp_max[i][i + n - 1] for i in range(n)))
solution2()