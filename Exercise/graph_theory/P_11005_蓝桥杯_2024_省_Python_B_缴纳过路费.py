""" 题目描述
在繁华的商业王国中，N 座城市被 M 条商路巧妙地连接在一起，形成了一个错综复杂的无向图网络。每条商路是双向通行的，并且任意两座城市之间最多只有一条直接的商路。每条商路都有它的规则，其中最引人注目的就是穿过商路，需要缴纳过路费。因此，商人们在选择商路时必须格外认真。

有一位名叫小蓝的商人，他对于商路的花费有着自己独到的见解。在小蓝眼中，一条路线包含一条或多条商路，但路线的成本并不是沿途累积的过路费总和，而是这条路线上最贵的那一次收费。这个标准简单而直接，让他能迅速评估出一条路线是否划算。

于是，他设立了一个目标，即找出所有城市对，这些城市之间的最低路线成本介于他心中预设的两个数 L 和 R 之间。他相信，这样的路线既不会太廉价，以至于路况糟糕；也不会过于昂贵，伤害他精打细算的荷包。

作为小蓝的助手，请你帮助小蓝统计出所有满足条件的城市对数量。

输入格式
输入的第一行包含四个整数 N,M,L,R，表示有 N 座城市和 M 条双向通行的商路，以及小蓝心中预设的最高过路费的下限 L 和上限 R。

接下来 M 行，每行包含三个整数 u,v,w，表示城市 u 和城市 v 之间有一条双向通行的商路，过路费为 w。保证每对城市之间最多只有一条直接的商路。

输出格式
输出一行包含一个整数，表示满足条件的城市对数量。

输入输出样例
输入 #1复制

5 5 1 2
1 2 2
1 3 5
1 4 1
2 4 5
2 5 4
输出 #1复制

3
说明/提示
对于 30% 的评测用例，1≤N≤10 
3
 ,1≤M≤min(2×10 
3
 , 
2
N×(N−1)
​
 ),1≤L≤R≤10 
5
 ，1≤u,v≤N,u

=v,1≤w≤10 
5
 。

对于所有评测用例，1≤N≤10 
5
 ,1≤M≤min(2×10 
5
 , 
2
N×(N−1)
​
 ),1≤L≤R≤10 
9
 ,1≤u,v≤N,u

=v，1≤w≤10 
9
 。

样例解释
在样例中，满足条件的城市对有 (1,2),(1,4),(2,4)。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
class UnionSet:
    def __init__(self,n:int):
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.collection_count = n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != x:
            fa = self.parent[x]
            self.parent[x] = root
            x = fa
        return root

    def merge(self,a:int,b:int):
        root_a = self.find(a)
        root_b = self.find(b)
        if(root_a == root_b):
            return False
        if(self.size[root_a] < self.size[root_b]):
            root_a,root_b = root_b,root_a
        self.parent[root_b] =root_a
        self.size[root_a] += self.size[root_b]
        self.collection_count -= 1
        return True

n,m,l,r = read()#n个城市m个通道,范围在l到r
edges = []
for _ in range(m):
    u,v,w = read()
    edges.append((w,u,v))
edges.sort()
ans = 0
s = UnionSet(n+1)
for (w,u,v) in edges:
    if(w > r):
        break
    root_u = s.find(u)
    root_v = s.find(v)
    if(root_u == root_v):
        continue
    if(l<=w<=r):
        ans += s.size[root_u]*s.size[root_v]
    s.merge(root_u,root_v)

print(ans)