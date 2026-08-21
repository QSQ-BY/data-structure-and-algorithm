""" 题目描述
在一个黑白相间的矩形中，问有多少个全白色的子矩形。

18475740.jpg
输入
第一行输入两个数字 n,m（2≤n,m≤1000），代表矩形的长和宽。

接下来 n 行，每行 m 个数字，0 代表黑色格子，1 代表白色格子。

输出
输出一个整数，代表全白色子矩形的数量，
结果可能过大，输出时请对 100007 取余。

样例输入1
6 6
0 1 1 1 1 1
1 1 0 1 1 1
1 1 1 1 1 1
1 1 1 0 1 1
1 1 1 1 0 1
1 0 1 1 1 1
样例输出1
152 """
import sys
input = sys.stdin.buffer.readline
from collections import deque
def read():
    return map(int,input().split())

def test01():
    n,m = read()
    dp = [0]*(m+2)
    f = [[]for _ in range(n+2)]
    for i in range(1,n+1):
        f[i] = [-1] + list(read())+[-1]
    for i in range(n-1,0,-1):
        for j in range(1,m+1):
            if(f[i][j] == 0):continue
            f[i][j] += f[i+1][j]
    ans = 0
    for i in range(n,0,-1):
        q = deque()
        q.append(m+1)
        for j in range(m,0,-1):
            while(f[i][q[-1]] >= f[i][j]):
                q.pop()
            dp[j] = f[i][j]*(q[-1]-j) + dp[q[-1]]
            dp[j]%=100007
            ans += dp[j]
            ans %= 100007
            q.append(j)

    print(ans%100007)
test01()