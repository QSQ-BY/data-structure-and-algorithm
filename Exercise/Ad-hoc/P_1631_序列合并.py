""" 题目描述
有两个长度为 N 的单调不降序列 A,B，在 A,B 中各取一个数相加可以得到 N 
2
  个和，求这 N 
2
  个和中最小的 N 个。

输入格式
第一行一个正整数 N；

第二行 N 个整数 A 
1…N
​
 。

第三行 N 个整数 B 
1…N
​
 。

输出格式
一行 N 个整数，从小到大表示这 N 个最小的和。

输入输出样例
输入 #1复制

3
2 6 6
1 4 8
输出 #1复制

3 6 7
说明/提示
对于 50% 的数据，N≤10 
3
 。

对于 100% 的数据，1≤N≤10 
5
 ，1≤A 
i
​
 ,B 
i
​
 ≤10 
9
 。 """
import heapq


n=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))


heap=[]

for i in range(n):
    heapq.heappush(heap,(A[i]+B[0],i,0))

ans=[]
for _ in range(n):
    s,i,j=heapq.heappop(heap)

    ans.append(s)

    if j+1<n:
        heapq.heappush(
            heap,
            (A[i]+B[j+1],i,j+1)
        )


print(*ans)