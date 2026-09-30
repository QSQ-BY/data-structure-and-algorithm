""" 题目背景
小杉坐在教室里，透过口袋一样的窗户看口袋一样的天空。

有很多云飘在那里，看起来很漂亮，小杉想摘下那样美的几朵云，做成棉花糖。

题目描述
给你云朵的个数 N，再给你 M 个关系，表示哪些云朵可以连在一起。

现在小杉要把所有云朵连成 K 个棉花糖，一个棉花糖最少要用掉一朵云，小杉想知道他怎么连，花费的代价最小。

输入格式
第一行有三个数 N,M,K。

接下来 M 行每行三个数 X,Y,L，表示 X 云和 Y 云可以通过 L 的代价连在一起。

输出格式
对每组数据输出一行，仅有一个整数，表示最小的代价。

如果怎么连都连不出 K 个棉花糖，请输出 No Answer。

输入输出样例
输入 #1复制

3 1 2
1 2 1
输出 #1复制

1
说明/提示
对于 30% 的数据，1≤N≤100，1≤M≤10 
3
 ；

对于 100% 的数据，1≤N≤10 
3
 ，1≤M≤10 
4
 ，1≤K≤10，1≤X,Y≤N，0≤L<10 
4
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m,k = read()#一共有n个点,m条边,要把n个点削弱城k个连通块
if(k>n):
    print("No Answer")
    sys.exit()
if(n==k):
    print(0)
    sys.exit()
class UnionSet:
    def __init__(self,n:int):
        self.parent = list(range(n))
        self.size = [1]*n
        self.collections_count = n
    def find(self,x:int):
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
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.collections_count -= 1

edges = []
for _ in range(m):
    u,v,weight = read()
    edges.append((weight,u,v))
edges.sort()
s =UnionSet(n+1)
ans = 0
cnt = n - k#需要进行cnt次合并的操作
for weight,u,v in edges:
    if(s.find(u) == s.find(v)):
        continue
    ans += weight
    s.merge(u,v)
    cnt -= 1
    if(cnt == 0):
        print(ans)
if(cnt > 0):
    print("No Answer")