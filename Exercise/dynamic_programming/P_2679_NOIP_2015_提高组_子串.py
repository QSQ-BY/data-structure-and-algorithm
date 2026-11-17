""" 题目背景
NOIP2015 Day2T2

题目描述
有两个仅包含小写英文字母的字符串 A 和 B。

现在要从字符串 A 中取出 k 个互不重叠的非空子串，然后把这 k 个子串按照其在字符串 A 中出现的顺序依次连接起来得到一个新的字符串。请问有多少种方案可以使得这个新串与字符串 B 相等？

注意：子串取出的位置不同也认为是不同的方案。

输入格式
第一行是三个正整数 n,m,k，分别表示字符串 A 的长度，字符串 B 的长度，以及问题描述中所提到的 k，每两个整数之间用一个空格隔开。

第二行包含一个长度为 n 的字符串，表示字符串 A。

第三行包含一个长度为 m 的字符串，表示字符串 B。

输出格式
一个整数，表示所求方案数。

由于答案可能很大，所以这里要求输出答案对 1000000007(10 
9
 +7) 取模的结果。

输入输出样例
输入 #1复制

6 3 1 
aabaab 
aab
输出 #1复制

2
输入 #2复制

6 3 2 
aabaab 
aab
输出 #2复制

7
输入 #3复制

6 3 3 
aabaab 
aab
输出 #3复制

7
说明/提示
样例解释

所有合法方案如下：（加下划线的部分表示取出的子串）

样例 1： 
aab
​
 aab,aab 
aab
​
 。
样例 2： 
a
​
  
ab
​
 aab, 
a
​
 aba 
ab
​
 ,a 
a
​
 ba 
ab
​
 ,aab 
a
​
  
ab
​
 , 
aa
​
  
b
​
 aab, 
aa
​
 baa 
b
​
 ,aab 
aa
​
  
b
​
 。
样例 3： 
a
​
  
a
​
  
b
​
 aab, 
a
​
  
a
​
 baa 
b
​
 , 
a
​
 ab 
a
​
 a 
b
​
 , 
a
​
 aba 
a
​
  
b
​
 ,a 
a
​
 b 
a
​
 a 
b
​
 ,a 
a
​
 ba 
a
​
  
b
​
 ,aab 
a
​
  
a
​
  
b
​
 。

数据范围

对于第 1 组数据：1≤n≤500,1≤m≤50,k=1;
对于第 2 组至第 3 组数据：1≤n≤500,1≤m≤50,k=2;
对于第 4 组至第 5 组数据：1≤n≤500,1≤m≤50,k=m;
对于第 1 组至第 7 组数据：1≤n≤500,1≤m≤50,1≤k≤m;
对于第 1 组至第 9 组数据：1≤n≤1000,1≤m≤100,1≤k≤m;
对于所有 10 组数据：1≤n≤1000,1≤m≤200,1≤k≤m。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
MOD = 10**9 + 7
n,m,k = read()
a = input().decode().strip()
b = input().decode().strip()
#dp[i][j][t]表示考虑a字符串的前i个位置，考虑b字符串的前j个位置用t个子串可以有多少种组合的方法
#end[i][j][t]含义一样，只不过最后一个子串恰好在a[i]结束的时候的方案
dp= [[[0]*(k+1)for _ in range(m+1)]for _ in range(2)]
end= [[[0]*(k+1)for _ in range(m+1)]for _ in range(2)]
dp[0][0][0] = 1
for i in range(1,n+1):
    cur = i%2
    pre = 1 - cur
    dp[cur] = [[0] * (k + 1) for _ in range(m + 1)]
    end[cur] = [[0] * (k + 1) for _ in range(m + 1)]
    dp[cur][0][0] = 1
    for j in range(1,min(m,i)+1):
        for t in range(1,min(j,k) + 1):
            if(a[i-1] == b[j-1]):
                #第一种选择直接延续在上一个的后面，或者是直接新开一个段
                end[cur][j][t] = (end[pre][j-1][t] + dp[pre][j-1][t-1])%MOD

            dp[cur][j][t] = (dp[pre][j][t] + end[cur][j][t])%MOD
print(dp[(n)%2][m][k])