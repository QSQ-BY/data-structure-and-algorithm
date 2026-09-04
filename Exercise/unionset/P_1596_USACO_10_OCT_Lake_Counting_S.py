""" 题目描述
由于最近的降雨，水在农夫约翰的田地里积聚了。田地可以表示为一个 
N
×
M
N×M 的矩形（
1
≤
N
≤
100
1≤N≤100；
1
≤
M
≤
100
1≤M≤100）。每个方格中要么是水（W），要么是干地（.）。农夫约翰想要弄清楚他的田地里形成了多少个水塘。一个水塘是由连通的水方格组成的，其中一个方格被认为与它的八个邻居相邻。给定农夫约翰田地的示意图，确定他有多少个水塘。

输入格式
第 
1
1 行：两个用空格分隔的整数：
N
N 和 
M
M。

第 
2
2 行到第 
N
+
1
N+1 行：每行 
M
M 个字符，表示农夫约翰田地的一行。

每个字符要么是 W，要么是 .。

字符之间没有空格。

输出格式
第 
1
1 行：农夫约翰田地中的水塘数量。

输入输出样例
输入#1
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
输出#1
3
说明/提示
输出详情：共有三个水塘：一个在左上角，一个在左下角，还有一个沿着右侧。 """
import sys
input = sys.stdin.readline

n,m = map(int,sys.stdin.buffer.readline().split())
g = [[""]*m for _ in range(n)]
for i in range(n):
    g[i] = str(input().strip())

class UnionSet:
    def __init__(self,n:int):
        self.collection_count = n
        self.parent = list(range(n))

    def find(self,x:int):
        if(x != self.parent[x]):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self,a:int,b:int)->bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if(root_a == root_b):
            return False
        self.parent[root_b] = root_a
        self.collection_count -= 1
        return True

u = UnionSet(n*m)
directions = [
    (0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)
]
cnt = 0
for i in range(n):
    for j in range(m):
        if(g[i][j] == "."):
            cnt += 1
            continue
        index1 = j + i*m
        for (dx,dy) in directions:
            x = i+dx
            y = j+dy
            if(x<0 or x>=n or y<0 or y>=m):
                continue
            index2 = y+ x*m
            if(g[x][y] == "W"):
                u.merge(index1,index2)

print(u.collection_count-cnt)
