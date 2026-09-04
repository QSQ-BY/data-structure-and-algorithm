""" 题目背景
oibh 总部突然被水淹没了！现在需要你的救援……

题目描述
oibh 被突来的洪水淹没了，还好 oibh 总部有在某些重要的地方起一些围墙。用 * 号表示，而一个四面被围墙围住的区域洪水是进不去的。

oibh 总部内部也有许多重要区域，每个重要区域在图中用一个 0 表示。

现在给出 oibh 的围墙建设图，问有多少个没被洪水淹到的重要区域。

输入格式
第一行为两个正整数 x,y。

接下来 x 行，每行 y 个字符，由 * 和 0 组成，表示 oibh 总部的建设图。

输出格式
输出没被水淹没的 oibh 总部的 0 的数量。

输入输出样例
输入 #1复制

4 5
00000
00*00
0*0*0
00*00
输出 #1复制

1
输入 #2复制

5 5
*****
*0*0*
**0**
*0*0*
*****
输出 #2复制

5
说明/提示
对于 100% 的数据，1≤x,y≤500。 """
import sys
input = sys.stdin.readline
class UnionSet:
    def __init__(self,n:int):
        self.collection_count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self,x:int):
        if(self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self,a:int,b:int)->bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if(root_a == root_b):
            return False
        if(self.size[root_a] < self.size[root_b]):
            root_a,root_b = root_b,root_a
        self.parent[root_b] = root_a
        self.collection_count -= 1
        self.size[root_a] += self.size[root_b]
        return True

#并查集做法
def test01():
    n,m = map(int,input().split())
    g = [[""]*m for _ in range(n)]
    for i in range(n):
        g[i] = str(input().strip())

    u = UnionSet(n*m+1)
    directions = [
        (0,1),(1,0),(0,-1),(-1,0)
    ]
    for i in range(n):
        for j in range(m):
            if(g[i][j] == "*"):
                continue
            index1 = j + i*m
            if(i==0 or i==n-1 or j==0 or j==m-1):
                u.merge(index1,n*m)
            for (dx,dy) in directions:
                x = i+dx
                y = j+dy
                if(x<0 or x>=n or y<0 or y>=m):
                    continue
                index2 = y+ x*m
                if(g[x][y] == "0"):
                    u.merge(index1,index2)
    s = set()
    ans = 0
    for i in range(n):
        for j in range(m):
            if(g[i][j] == "*"):
                continue
            index = j + i*m
            root = u.find(index)
            if(root == u.find(n*m)):
                continue
            if(root in s):
                continue
            ans += u.size[root]
            s.add(root)
    print(ans)

#DFS做法
def test02():
    n,m = map(int,input().split())
    g = [[""]*m for _ in range(n)]
    for i in range(n):
        g[i] = list(input().strip())
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    def dfs(start_x,start_y):
        stack = [(start_x,start_y)]
        g[start_x][start_y] = "#"
        while(stack):
            x,y = stack.pop()
            for (dx, dy) in directions:
                next_x = x + dx
                next_y = y + dy

                if (
                    0 <= next_x < n
                    and 0 <= next_y < m
                    and g[next_x][next_y] == "0"
                ):
                    # 入栈时就标记，避免重复入栈
                    g[next_x][next_y] = "#"
                    stack.append((next_x, next_y))

    for i in range(n):
        for j in range(m):
            if (
                i == 0
                or i == n - 1
                or j == 0
                or j == m - 1
            ):
                if g[i][j] == "0":
                    dfs(i, j)

    ans = sum(row.count("0") for row in g)
    print(ans)

#test01()
test02()