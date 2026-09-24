""" 题目描述
有一个长度为 n 的数组（n 是 10 的倍数），每个数 a 
i
​
  都是区间 [0,9] 中的整数。小明发现数组里每种数出现的次数不太平均，而更改第 i 个数的代价为 b 
i
​
 ，他想更改若干个数的值使得这 10 种数出现的次数相等（都等于  
10
n
​
 ），请问代价和最少为多少。

输入格式
输入的第一行包含一个正整数 n。

接下来 n 行，第 i 行包含两个整数 a 
i
​
 ,b 
i
​
 ，用一个空格分隔。

输出格式
输出一行包含一个正整数表示答案。

输入输出样例
输入 #1复制

10
1 1
1 2
1 3
2 4
2 5
2 6
3 7
3 8
3 9
4 10
输出 #1复制

27
说明/提示
【样例说明】

只更改第 1,2,4,5,7,8 个数，需要花费代价 1+2+4+5+7+8=27。

【评测用例规模与约定】

对于 20% 的评测用例，n≤1000；

对于所有评测用例，n≤100000,0<b 
i
​
 ≤2×10 
5
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
average = n//10
costs = [[] for _ in range(10)]

for _ in range(n):
    a, b = read()
    costs[a].append(b)

ans = 0
for group in costs:
    excess = len(group) - average
    if excess > 0:
        group.sort()
        ans += sum(group[:excess])

print(ans)