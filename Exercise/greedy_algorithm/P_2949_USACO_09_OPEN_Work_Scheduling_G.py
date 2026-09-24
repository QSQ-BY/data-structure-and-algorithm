""" 题目描述
农夫约翰有很多工作要做！为了高效地经营农场，他必须从他所做的每一项工作中赚取利润，每项工作只需要一个时间单位。

他的工作日从时间 0 开始，总共有 10 
9
  个时间单位。他目前可以从 N (1≤N≤10 
5
 ) 项工作中选择要做的工作，这些工作被方便地编号为 1 到 N。

虽然理论上他有可能完成所有 N 项工作，但实际上这是极不可能的，因为他在任何一个时间单位内只能完成一项工作，而截止日期通常会导致他无法完成所有任务。

第 i 项工作的截止时间为 D 
i
​
  (1≤D 
i
​
 ≤10 
9
 )。如果他在截止时间前完成第 i 项工作（如果当前时间为 t，那么仅当 D 
i
​
 >t 的时候他能做这个任务，完成后 t→t+1，他将获得 P 
i
​
  (1≤P 
i
​
 ≤10 
9
 ) 的利润。

给定一系列工作和截止日期，FJ 能够获得的最大总利润是多少？答案可能无法用 32 位整数存储。

输入格式
第一行输入一个整数 N，意义见题目描述。

第二行到第 N+1 行：第 i+1 行包含两个用空格分隔的整数：D 
i
​
  和 P 
i
​
 。

输出格式
只有一个数字，表示 FJ 能够获得的最大利润。

输入输出样例
输入 #1复制

3 
2 10 
1 5 
1 7 
输出 #1复制

17 
说明/提示
在时间 1 完成工作 3 (1,7)，在时间 2 完成工作 1 (2,10) 以最大化收益，最后收益为 7+10=17。

由 ChatGPT 4o 翻译。 """
import sys
import heapq

input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

n = int(input())
jobs = []
for _ in range(n):
    time,value = read()
    jobs.append((time,value))

jobs.sort()
heap = []
heapq.heapify(heap)
for (time,value) in jobs:
    heapq.heappush(heap,value)
    while(len(heap) > time):
        heapq.heappop(heap)

print(sum(heap))