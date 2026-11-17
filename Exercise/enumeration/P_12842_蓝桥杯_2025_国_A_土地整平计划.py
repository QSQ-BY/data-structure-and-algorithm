""" 题目描述
小蓝作为一个二维生物快乐地生活在二维坐标系中，他最近得到了一块土地，他想把这块土地整平用于修建花园。具体来说，这块土地从左到右长度为 n 格，第 i 格的高度为 h 
i
​
 (i∈[1,n])。小蓝每次可以花费代价 w 将一段连续的区间 [l,r] 中的土地高度都变为 w，其中 l≤r，这段区间需要满足以下三组条件之一：

l=1, r<n，且对于 i∈[l,r] 有 h 
i
​
 

=h 
r+1
​
 ，此时代价 w=h 
r+1
​
 ；
l>1, r=n，且对于 i∈[l,r] 有 h 
i
​
 

=h 
l−1
​
 ，此时代价 w=h 
l−1
​
 ；
1<l≤r<n，h 
l−1
​
 =h 
r+1
​
 ，且对于 i∈[l,r] 有 h 
i
​
 

=h 
l−1
​
 ，此时代价 w=h 
l−1
​
 =h 
r+1
​
 。
每一个土地至多只能操作一次。小蓝希望在若干次操作之后将这块土地整平，即所有格子的高度都相等，并且花费的代价总和最小。请你帮助他计算一下最小花费。

输入格式
输入的第一行包含一个正整数 n。

第二行包含 n 个正整数 h 
1
​
 ,h 
2
​
 ,…,h 
n
​
 ，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

8
5 4 10 4 20 5 4 5
输出 #1复制

10
说明/提示
【样例说明】

选择将土地高度都变为 5，只需操作两次：将 [2,5] 和 [7,7] 的高度都变为 5，代价总和为 10。

【评测用例规模与约定】

对于 50% 的评测用例，1≤n≤5000；

对于所有评测用例，1≤n≤10 
6
 ，1≤h 
i
​
 ≤10 
6
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
if( n == 1):
    print(0)
    sys.exit()
if(n == 2):
    if(arr[0] != arr[1]):
        print(min(arr[0],arr[1]))
    else:
        print(0)
    sys.exit()
new_arr = [arr[0]]
for i in range(1,n):
    number = arr[i]
    if(number == new_arr[-1]):
        continue
    new_arr.append(number)
arr = new_arr[:]
n = len(arr)
del new_arr
if(n==1):
    print(0)
    sys.exit()
s = {}
for i in range(n):
    number = arr[i]
    if(number in s):
        if(i == n-1):
            continue
        s[number] += 1
    else:
        if(i == 0 or i == n-1):
            s[number] = 0
        else:
            s[number] = 1
ans = float("inf")
for number,cnt in s.items():
    ans = min(ans,number*(cnt+1))
print(ans)