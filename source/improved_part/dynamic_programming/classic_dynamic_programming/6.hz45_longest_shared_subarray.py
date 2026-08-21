""" 题目描述
给出两个字符串，求其两个的最长公共子序列长度。



输入
第一行输入一个字符串s1，第二行输入一个字符串s2 (字符串长度≤1000) ，两个字符串长度可以不相同。

输出
输出一个整数，代表两个字符串的最长公共子序列的长度。

样例输入1
sehuaizexi
yhaizeyiux
样例输出1
6 """
""" dp[i][j]表示A字符串取前i位，B字符串取前j位所能形成的最大公共子串
dp[i][j] = max(dp[i][j-1],dp[i][j-1],dp[i][j]+1) """
import sys
input = sys.stdin.readline
def read():
    return map(str,input().split())


def main():
    a = ["0"]+list(input().strip())
    b = ["1"]+list(input().strip())
    n = len(a)-1
    m = len(b)-1
    dp = [[0]*(m+1) for _ in range(2)]
    if(a[1] == b[1]):dp[1][1] = 1
    for i in range(1,n+1):
        index1 = i%2
        index2 = 1-index1
        for j in range(1,m+1):
            dp[index1][j] = max(dp[index2][j],dp[index1][j-1])
            if(a[i] == b[j]):
                dp[index1][j] = max(dp[index1][j],dp[index2][j-1]+1)
    print(dp[n%2][m])


if(__name__ == "__main__"):
    main()