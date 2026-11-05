""" 题目描述
设 A 和 B 是两个字符串。我们要用最少的字符操作次数，将字符串 A 转换为字符串 B。这里所说的字符操作共有三种：

删除一个字符；
插入一个字符；
将一个字符改为另一个字符。
A,B 均只包含小写字母。

输入格式
第一行为字符串 A；第二行为字符串 B；字符串 A,B 的长度均小于 2000。

输出格式
只有一个正整数，为最少字符操作次数。

输入输出样例
输入 #1复制

sfdqxbw
gfdgw
输出 #1复制

4
说明/提示
对于 100% 的数据，1≤∣A∣,∣B∣≤2000。 """
import sys
input = sys.stdin.buffer.readline
begin = input().decode().strip()
end = input().decode().strip()
n,m = len(begin),len(end)
#dp[i][j]表示把最初的前i位变为最后的前j位所需要的最小次数
#dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1] + 1)
#如果begin[i] == begin[j] dp[i][j] = min(dp[i][j],dp[i-1][j-1])
dp = [[float("inf")]*(m+1)for _ in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
    dp[i][0] = i#最前面的i个变为最后的前0个字母只能不断的删除
for i in range(1,m+1):
    dp[0][i] = i#最初的前0个字母变为最后的i个只能不断地增加

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = min(dp[i][j],dp[i-1][j] + 1,dp[i][j-1] + 1)
        if(begin[i-1] == end[j-1]):
            dp[i][j] = min(dp[i-1][j-1],dp[i][j])
        else:
            dp[i][j] = min(dp[i][j],dp[i-1][j-1]+1)

print(dp[n][m])
