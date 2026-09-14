""" 题目描述
在自动化工厂的水线上，依次排列着 3N 个部件。每个部件都标有一个价格 a 
i
​
 ：若执行回收，该标价即为收益；若执行处理，该标价则计为成本。

作为厂区负责人，小蓝的任务是从这 3N 个部件中挑选出两批特定组别：

回收组：挑选出恰好 N 个部件进行回收，总收益记为 R。
处理组：挑选出恰好 N 个部件进行处理，总成本记为 C。
由于水线是不可逆的单向传送，挑选过程必须遵守严格的先后顺序：任何一个被回收的部件，其原始位置都必须早于所有被处理的部件（即若把回收部件的下标记为 p 
1
​
 <p 
2
​
 <⋯<p 
N
​
 ，处理部件的下标记为 q 
1
​
 <q 
2
​
 <⋯<q 
N
​
 ，则必须满足 p 
N
​
 <q 
1
​
 ）。

在满足上述顺序的前提下，水线上剩下的 N 个部件将被直接弃置，不产生任何收益或成本。

现在，小蓝希望通过合理的方案，使得回收的总收益减去处理的总成本（R−C）尽可能大。对此，请你计算出这个差值的最大可能结果。

输入格式
第一行包含一个整数 N，表示每组选取的部件数量。

第二行包含 3N 个整数 a 
1
​
 ,a 
2
​
 ,…,a 
3N
​
 ，表示水线上从左到右每个部件的标价。

给定的网络可能包含重边或自环。

输出格式
输出一个整数，表示在满足所有约束的前提下，R−C 的最大可能值。

输入输出样例
输入 #1复制

2
1 10 5 1 2 1
输出 #1复制

13
说明/提示
【样例说明】
最优的方案为：回收第 2、3 个部件，处理第 4、6 个部件，此时 R=10+5=15，C=1+1=2，R−C=13。

【评测用例规模与约定】
对于 40% 的评测用例，1≤N≤1000。

对于所有评测用例，1≤N≤10 
5
 ，1≤a 
i
​
 ≤10 
9
 。 """
import sys
from itertools import accumulate
import heapq
input = sys.stdin.buffer.readline
sys.setrecursionlimit(50000)
def read():
    return map(int,input().split())

def test01():
    n = int(input())
    arr = [0] + list(read())
    index = []
    ans = ans = float('-inf')
    def calculate():
        nonlocal index
        nonlocal arr
        add = 0
        minus = 0
        for i in range(0,n):
            add += arr[index[i]]
        for i in range(n,2*n):
            minus += arr[index[i]]
        return add - minus

    #排列型枚举
    #即将填入数字的位置，能填数字的最小值
    def dfs(pos,min):
        nonlocal ans
        nonlocal index
        if(pos == 2*n):
            temp_ans = calculate()
            ans = max(ans,temp_ans)
            return
        maximum = 3*n+1
        for number in range(min,maximum):
            if(2*n - pos  > maximum - number):
                break
            index.append(number)
            dfs(pos + 1,number+1)
            index.pop()
        return
    dfs(0,1)
    print(ans)

def test02():
    n = int(input())
    arr = list(read())
    left = [0]*(2*n + 1)
    heap = arr[:n]
    heapq.heapify(heap)
    s = sum(heap)
    left[n] = s
    for i in range(n,2*n):
        removed = heapq.heappushpop(heap,arr[i])
        s += arr[i] - removed
        left[i+1] = s
    right = [0]*(2*n + 1)
    heap = [-x for x in arr[2*n:]]
    heapq.heapify(heap)
    s = -sum(heap)
    right[2*n] = s
    for i in range(2*n - 1,n-1,-1):
        removed = -heapq.heappushpop(heap,-arr[i])
        s+=arr[i] - removed
        right[i] = s
    ans = float("-inf")
    for i in range(n,2*n + 1):
        ans = max(ans,left[i] - right[i])
    print(ans)

#test01()
test02()