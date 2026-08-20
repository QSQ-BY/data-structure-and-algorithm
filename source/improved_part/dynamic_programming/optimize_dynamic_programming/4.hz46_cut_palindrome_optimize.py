#优化转移过程
#dp[i]表示从1到i最少切多少刀
#dp[i] = min(dp[k]+1) s[k+1 -- i]是一个回文串

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
import sys
input = sys.stdin.readline

string = list(input().strip())
n = len(string)
string = [" "] + string
dp=[0]*(n+2)
dp[1] = 0
dp[0] = -1
g = [ [] for _ in range(n+2)]
def extract(i:int,j:int)->None:
    global string
    global g
    if(j>n or i<1 or i>n or i<1): return
    while(string[i] == string[j]):
        if(j>n or i<1 or i>n or i<1): return
        g[j].append(i-1)
        i -= 1
        j +=1
        if(j>n or i<1 or i>n or i<1): return
    return

for i in range(1,n+1):
    extract(i,i)#提取奇数位的回文串
    extract(i,i+1)#提取偶数位的回文串

for i in range(2,n+1):
    dp[i] = i
    for j in range(len(g[i])):
        dp[i] = min(dp[i],dp[g[i][j]]+1)

print(dp[n])