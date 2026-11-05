""" 题目描述
数字金字塔由 n 行整数组成，第 i(1≤i≤n) 行有 i 个数字，一个示例如下。

        7
      3   9
    8   1   0
  2   7   4   4 
4   5   2   6   5

现在你在金字塔的顶部（第一行），你希望走到金字塔的底部（第 n 行），每一步你只能走向当前所在位置的左下方的数字或者右下方的数字。同时作为一个强大的小朋友，你可以选择金字塔中的不多于 k 个数字让他们成为原来的 3 倍。

你会收集你路上经过的所有位置上的数字，最后的得分即为收集的数字之和，求最大得分。

输入格式
第一行输入两个整数 n,k，表示数字金字塔的行数和乘 3 的数字个数最大值；
接下来 n 行，其中的第 i 行有 i 个以空格隔开的整数依次表示数字金字塔第 i 行的数字 a 
i,1
​
 ,a 
i,2
​
 ,a 
i,3
​
 ...a 
i,i
​
 。

输出格式
一行一个整数，表示最大得分。

输入输出样例
输入 #1复制

5 3
7
3 9
8 1 0
2 7 4 4
4 5 2 6 5
输出 #1复制

75
说明/提示
对于 30% 的数据，满足 k≤n≤6，并且对于任意 1≤i≤n，1≤j≤i 满足 0≤a 
i,j
​
 ≤100；
对于 100% 的数据，满足 1≤n≤100，0≤k≤ 
2
n(n+1)
​
 ，且对于任意 1≤i≤n，1≤j≤i 满足 ∣a 
i,j
​
 ∣≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m = read()
arr = [[]for _ in range(n)]
for i in range(n):
    arr[i] = list(read())
#dp[i][j][k]表示在第i层第j个位置已经使用了t次三倍时能获得的最大数值
#dp[i][j][t] = max(dp[i-1][j-1][t],dp[i-1][j][t])+value
#dp[i][j][t] = max(dp[i][j][t],max(dp[i-1][j-1][t-1],dp[i - 1][j][t - 1])+3*value)

k = min(n,m)
dp = [[[float("-inf")]*(k+1)for _ in range(n+1)]for _ in range(n+1)]

#还没进入三角形，使用0次三倍技能得分为0
dp[0][0][0] = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        value = arr[i-1][j-1]
        for t in range(min(i,k) + 1):
            # 当前数字不使用三倍
            best = max(
                dp[i - 1][j - 1][t],
                dp[i - 1][j][t]
            )
            dp[i][j][t] = best + value

            # 当前数字使用三倍
            if t > 0:
                best = max(
                    dp[i - 1][j - 1][t - 1],
                    dp[i - 1][j][t - 1]
                )
                dp[i][j][t] = max(
                    dp[i][j][t],
                    best + 3 * value
                )

ans = float("-inf")
for i in range(1,n+1):
    for j in range(k+1):
        ans = max(dp[n][i][j],ans)
print(ans)