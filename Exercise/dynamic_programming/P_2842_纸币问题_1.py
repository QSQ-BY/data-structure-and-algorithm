""" 题目描述
某国有 n 种纸币，每种纸币面额为 a 
i
​
  并且有无限张，现在要凑出 w 的金额，试问最少用多少张纸币可以凑出来？（保证可以凑出对应金额）

输入格式
第一行两个整数 n,w，分别表示纸币的种数和要凑出的金额。
第二行一行 n 个以空格隔开的整数 a 
1
​
 ,a 
2
​
 ,a 
3
​
 ,…a 
n
​
  依次表示这 n 种纸币的面额。

输出格式
一行一个整数，表示最少使用的纸币张数。

输入输出样例
输入 #1复制

6 15
1 5 10 20 50 100
输出 #1复制

2
输入 #2复制

3 15
1 5 11
输出 #2复制

3
说明/提示
对于 40% 的数据，满足 n≤10，w≤100；
对于 100% 的数据，满足 1≤n≤10 
3
 ，1≤a 
i
​
 ,w≤10 
4
 。 """
#dp[i][j]表示使用前i中纸币凑齐元j的最少使用钱币数量
#dp[i][j] = min(dp[i-1][j],dp[i][j-w]+1)
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,target = read()
arr = [0]+list(read())
dp = [[float("inf")]*(target+1)for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0
dp[0][0] = 0
for i in range(1,n+1):
    for j in range(1,target+1):
        dp[i][j] = min(dp[i-1][j],dp[i][j])
        if(arr[i] > j):
            continue
        dp[i][j] = min(dp[i][j],dp[i][j-arr[i]] + 1)

print(dp[n][target])