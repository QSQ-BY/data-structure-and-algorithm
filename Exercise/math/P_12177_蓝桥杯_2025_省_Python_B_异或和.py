""" 题目描述
小蓝有 n 个数 a 
i
​
 ，他想知道这 n 个数中的所有数对下标的差值乘上它们的异或之后，得到的结果的和是多少。

也就是说，小蓝想要得到

i=1
∑
n
​
  
j=i+1
∑
n
​
 (a 
i
​
 ⊕a 
j
​
 )×(j−i)
的值，其中 ⊕ 表示按位异或。

输入格式
输入的第一行包含一个正整数 n。

第二行包含 n 个正整数 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 ，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

3
1 2 3
输出 #1复制

8
输入 #2复制

4
9 8 7 6
输出 #2复制

118
说明/提示
评测用例规模与约定
对于 40% 的评测用例，n≤5000；
对于所有评测用例，1≤n≤10 
5
 ，1≤a 
i
​
 ≤2 
20
 。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())
ans = 0
#cnt[b]：前面这一位为 b 的数有多少个。
#pos[b]：这些数的下标之和。
for k in range(21):#逐位进行处理
    cnt = [0,0]
    sum = [0,0]
    for j,x in enumerate(arr):
        b = (x>>k)&1
        opposite = 1^b

        #当前数字与前面的数字在第k位产生的贡献
        distance_sum = j*cnt[opposite] - sum[opposite]
        ans += distance_sum * (2**k)
        #统计当前数字供后面的数字使用
        cnt[b] += 1
        sum[b] += j

print(ans)

