""" 题目描述
一矩形阵列由数字 0 到 9 组成，数字 1 到 9 代表细胞，细胞的定义为沿细胞数字上下左右若还是细胞数字则为同一细胞，求给定矩形阵列的细胞个数。

输入格式
第一行两个整数代表矩阵大小 n 和 m。

接下来 n 行，每行一个长度为 m 的只含字符 0 到 9 的字符串，代表这个 n×m 的矩阵。

输出格式
一行一个整数代表细胞个数。

输入输出样例
输入 #1复制

4 10
0234500067
1034560500
2045600671
0000000089
输出 #1复制

4
说明/提示
数据规模与约定
对于 100% 的数据，保证 1≤n,m≤100。
 """
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
    (0,1),(1,0),(0,-1),(-1,0),
]
cnt = 0
for i in range(n):
    for j in range(m):
        if(g[i][j] == "0"):
            cnt += 1
            continue
        index1 = j + i*m
        for (dx,dy) in directions:
            x = i+dx
            y = j+dy
            if(x<0 or x>=n or y<0 or y>=m):
                continue
            index2 = y+ x*m
            if(g[x][y] != "0"):
                u.merge(index1,index2)

print(u.collection_count-cnt)
