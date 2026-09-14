import sys
input = sys.stdin.readline
class UnionSet:
    def __init__(self,n:int)->None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.element_count = n
        self.component_count = n

    def find(self,x:int)->int:
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
        self.size[root_a] += self.size[root_b]
        self.component_count -= 1
        return True

#并查集做法
def test01():
    m,n = map(int,sys.stdin.buffer.readline().split())
    g = [[""]*m for _ in range(n)]
    for i in range(n):
        g[i] = str(input().strip())
    dir = [
        (1,0),(0,1)
    ]
    u = UnionSet(n*m + 1)
    start_x = 0
    start_y = 0
    for i in range(n):
        for j in range(m):
            if(g[i][j] == "#"):
                continue
            elif(g[i][j] == "@"):
                start_x = i
                start_y = j
            index1 = j + i*m
            for (dx,dy) in dir:
                x = dx + i
                y = dy + j
                if(x<0 or x>=n or y<0 or y>=m):
                    continue
                index2 = y + x*m
                if(g[x][y] == "#"):
                    continue
                u.merge(index1,index2)

    start_index = start_x*m + start_y
    print(u.size[u.find(start_index)])

#连通块DFS做法
def test02():
    m,n = map(int,input().split())
    g = [list(input().strip()) for _ in range(n)]

    start_x = start_y = 0
    for i in range(n):
        for j in range(m):
            if(g[i][j] == "@"):
                start_x,start_y = i,j

    directions = [
        (-1,0),(1,0),(0,-1),(0,1)
    ]

    def dfs(x:int,y:int)->int:
        if(x<0 or x>=n or y<0 or y>=m or g[x][y] == "#"):
            return 0
        #标记为已经被访问
        g[x][y] = "#"
        count = 1
        for (dx,dy) in directions:
            count += dfs(x+dx,y+dy)
        return count
    print(dfs(start_x,start_y))

#test01()
test02()