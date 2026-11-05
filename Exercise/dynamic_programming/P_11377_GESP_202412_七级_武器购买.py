""" 题目背景
对应的选择、判断题：https://ti.luogu.com.cn/problemset/1171

题目描述
商店里有 n 个武器，第 i 个武器的强度为 p 
i
​
 ，花费为 c 
i
​
 。

小杨想要购买一些武器，满足这些武器的总强度不小于 P，总花费不超过 Q，小杨想知道是否存在满足条件的购买方案，如果有，最少花费又是多少。

输入格式
第一行包含一个正整数 t，代表测试数据组数。

对于每组测试数据，第一行包含三个正整数 n,P,Q，含义如题面所示。

之后 n 行，每行包含两个正整数 p 
i
​
 ,c 
i
​
 ，代表武器的强度和花费。

输出格式
对于每组测试数据，如果存在满足条件的购买方案，输出最少花费，否则输出 -1。

输入输出样例
输入 #1复制

3
3 2 3
1 2
1 2
2 3
3 3 4
1 2
1 2
2 3
3 1000 1000
1 2
1 2
2 3
输出 #1复制

3
-1
-1
说明/提示
子任务编号	数据点占比	n	p 
i
​
 	c 
i
​
 	P	Q
1	20%	≤10	1	1	≤10	≤10
2	20%	≤100	≤5×10 
4
 	1	≤5×10 
4
 	2
3	60%	≤100	≤5×10 
4
 	≤5×10 
4
 	≤5×10 
4
 	≤5×10 
4
 
对于全部数据，保证有 1≤t≤10，1≤n≤100，1≤p 
i
​
 ,c 
i
​
 ,P,Q≤5×10 
4
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
t = int(input())
for _ in range(t):
    #一共有n个武器，所选择的武器总数强度不能小于P，总花费不能超过Q
    #dp[j]表示在目前已经考虑到的所有武器当中，强度至少为j的最小花费
    n,P,Q = read()
    dp = [float("inf")]*(P+1)
    dp[0] = 0
    for _ in range(n):
        p,q = read()
        for j in range(P,-1,-1):
            remain = max(j - p,0)
            if dp[remain]+q<=Q:
                dp[j] = min(dp[j],dp[remain]+q) 
    if(dp[P] == float("inf")):
        print(-1)
    else:
        print(dp[P])
