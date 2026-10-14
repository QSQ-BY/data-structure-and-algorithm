""" 题目背景
在植树节那天，小 L，小 H，小 X 却要面对繁忙的考试。

考完后，按照惯例，他们讨论起了成绩。小 L 非常八卦，他向全班 N 个同学问了他们的成绩情况。当然，就如你想象的那样，每个人也不愿意透露太多信息，每个人只说了他的分数比哪一个同学低，也有些人没说任何信息。

勤奋的小 H 和爱偷懒的小 X 对于班上所有同学的成绩排名都有一个“心理期望”，也就是说，小 H 可能认为 XX 会排第 1，YY 会排第 2……但小 X 却会认为 XX 应该排最后 1 名，YY 会排倒数第 2 名。

不过理想和现实总是有差距的，通过小 L 打探到的情报， XX 不能排在第 1 了，但是，小 H 仍然觉得 XX 应该排在尽可能前。

小 L 由此想到了一个问题，他想知道小 H 和小 X 知道他打探到的情报之后，对班上同学的心里排名是什么样的。

每个同学的编号即为小 H 的心理排名，也就是说，小 H 希望编号越靠前的同学排名也尽量靠前，而小 X 希望希望编号越靠前的同学排名尽量靠后。（注意不是越后面的同学排名越靠前）

题目描述
给定一个长度为 N 的数列 A，其中 A 
i
​
  表示第 i 个同学的分数比第 A 
i
​
  个同学的分数低（或者说，第 i 个同学的排名在第 A 
i
​
  个同学之后）。当然，A 
i
​
  有可能等于 0，则表明没有关于第 i 个同学的信息。

你需要得到一个长度为 N 的数列 H，表示班上同学的排名。这个排名要求是满足所有 A 
i
​
  构成的约束的排名中字典序最小的哪一个。

同时，你还需要得到一个数列 X，表示班上同学的排名。这个排名要求是满足所有 A 
i
​
  构成的约束的排名中字典序最大的哪一个。

输入格式
第 1 行一个正整数 N，表示班上同学的个数。

第 2 行包含 N 个用空格隔开的非负整数，第 i 个数表示 A 
i
​
 。

输出格式
两行，每行 N 个正整数，用空格隔开。其中，第 1 行为小 L 的心理排名，第 2 行为小 X 的心理排名。

输入输出样例
输入 #1复制

4
3 0 2 2
输出 #1复制

3 1 2 4
4 1 3 2
说明/提示
样例解释
共有 3 种排名满足大小关系：

4 1 3 2
4 1 2 3
3 1 2 4

其中，3 1 2 4 字典序最小，4 1 3 2 字典序最大。

数据范围
对于 10% 的数据，N≤10。

对于 20% 的数据，N≤20。

对于 40% 的数据，N≤2×10 
3
 。

对于 100% 的数据，1≤N≤2×10 
5
 ,A 
i
​
 ≤N。其中，第 5 组数据保证 N=1.2×10 
4
 。 """
#拓扑排序
import sys
import heapq
input = sys.stdin.buffer.readline                                  
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
g = [[]for _ in range(n+1)]
indegree = [0]*(n+1)
for index,j in enumerate(arr):
    if(j == 0):
        continue
    i = index + 1
    #第i位同学的分比第j位同学的分要低
    g[i].append(j)#g[i]存储的是比i分数要高的下标
    indegree[j] += 1


q = [-i for i in range(1,n+1) if indegree[i] == 0]
heapq.heapify(q)

ans = [0]*(n+1)
#第一种是把大的排名分配给大的编号的同学，从分数较低的开始进行拓扑排序
for rank in range(n, 0, -1):
    cur = -heapq.heappop(q)
    ans[cur] = rank
    for nxt in g[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(q, -nxt)

print(*ans[1:])

del g
del indegree

# 重新建图、统计入度，第一次排序已经消耗了原来的入度
g2 = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)

for i, j in enumerate(arr, 1):
    if j:
        g2[j].append(i)  # j 的名次必须在 i 前面
        degree[i] += 1

q = [-i for i in range(1, n + 1) if degree[i] == 0]
heapq.heapify(q)
ans = [0] * (n + 1)
#第二种是把小的排名分配给大的编号的同学，从分数较小的开始拓扑序
for rank in range(1, n + 1):
    cur = -heapq.heappop(q)
    ans[cur] = rank
    for nxt in g2[cur]:
        degree[nxt] -= 1
        if degree[nxt] == 0:
            heapq.heappush(q, -nxt)

print(*ans[1:])