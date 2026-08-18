""" 题目描述
给出一个字符串S，问对字符串S最少切几刀，使得分成的每一部分都是一个回文串（注意：单一字符是回文串）

87699633.jpg
输入
一个长度为n(1≤n≤500000)​的字符串S，只包含小写字母。

输出
输出一个整数，代表所切的最少刀数。

样例输入
sehuhzzexe
样例输出
4 """
#如果本身就是回文串则且0刀
#否则至少切一刀，枚举这一刀每一个切割的位置
#以区间长度为状态更新方向，区间dp  
""" dp[i][j] = min(dp[i][k] + dp[k+1][j]+1)
dp[i][j] = 0(s[i] = s[j] and d[i+1][j]) """
import sys
input = sys.stdin.readline
def read():
    return map(str,input().split())

string = [" "] + list(input().strip())
n = len(string)-1
dp = [[0]*(n+5) for _ in range(n+5)]
for l in range(1,n+1):
    for i in range(1,n-l+2):
        j = i + l -1
        if(string[i] == string[j] and dp[i+1][j-1] == 0):
            dp[i][j] = 0
        else:
            dp[i][j] = l
            for k in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + 1)
print(dp[1][n])