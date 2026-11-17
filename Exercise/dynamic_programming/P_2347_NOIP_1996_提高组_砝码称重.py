""" 题目描述
设有 1g、2g、3g、5g、10g、20g 的砝码各若干枚（其总重 ≤1000），可以表示成多少种重量？

输入格式
输入方式：a 
1
​
 ,a 
2
​
 ,a 
3
​
 ,a 
4
​
 ,a 
5
​
 ,a 
6
​
 

（表示 1g 砝码有 a 
1
​
  个，2g 砝码有 a 
2
​
  个，…，20g 砝码有 a 
6
​
  个）

输出格式
输出方式：Total=N

（N 表示用这些砝码能称出的不同重量的个数，但不包括一个砝码也不用的情况）

输入输出样例
输入 #1复制

1 1 0 0 0 0
输出 #1复制

Total=3
说明/提示
【题目来源】

NOIP 1996 提高组第四题 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#1 2 3 5 10 20
a1,a2,a3,a4,a5,a6 = read()
arr = [1]*a1 + [2]*a2 + [3]*a3 + [5]*a4 + [10]*a5 +[20]*a6
n = len(arr)
#dp[i]表示考虑前i个发麻，能够称出来的重量的集合
dp = [0]*(n+1)
for i in range(1,n+1):
    weight = arr[i-1]
    dp[i] = dp[i-1]|(dp[i-1]<<weight)|(1<<weight)
ans = dp[n].bit_count()
print(f"Total={ans}")