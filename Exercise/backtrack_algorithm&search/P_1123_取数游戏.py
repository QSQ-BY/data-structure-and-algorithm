""" 题目描述
一个 N×M 的由非负整数构成的数字矩阵，你需要在其中取出若干个数字，使得取出的任意两个数字不相邻（若一个数字在另外一个数字相邻 8 个格子中的一个即认为这两个数字相邻），求取出数字和最大是多少。

输入格式
第一行有一个正整数 T，表示了有 T 组数据。

对于每一组数据，第一行有两个正整数 N 和 M，表示了数字矩阵为 N 行 M 列。

接下来 N 行，每行 M 个非负整数，描述了这个数字矩阵。

输出格式
共 T 行，每行一个非负整数，输出所求得的答案。

输入输出样例
输入 #1复制

3
4 4
67 75 63 10
29 29 92 14
21 68 71 56
8 67 91 25
2 3
87 70 85
10 3 17
3 3
1 1 1
1 99 1
1 1 1
输出 #1复制

271
172
99
说明/提示
样例解释
对于第一组数据，取数方式如下：

[67]
29
[21]
8
​
  
75
29
68
67
​
  
63
[92]
71
[91]
​
  
10
14
56
25
​
 
数据范围及约定
对于20%的数据，1≤N,M≤3；
对于40%的数据，1≤N,M≤4；
对于60%的数据，1≤N,M≤5；
对于100%的数据，1≤N,M≤6，1≤T≤20，a 
i,j
​
 ≤10 
5
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solve()->int:
    n,m = read()
    g = [list(read()) for _ in range(n)]
    ban = [[0]*m for _ in range(n)]
    ans = 0
    values = []
    for i in range(n):
        for j in range(m):
            values.append(g[i][j])
    suffix = [0]*(n*m+1)
    for pos in range(n*m-1,-1,-1):
        suffix[pos] = suffix[pos+1] + values[pos]


    def dfs(pos:int,result:int):
        nonlocal ans
        ans = max(ans,result)
        if(pos == n*m):
            return
        if(suffix[pos] + result <= ans):
            return
        i = pos//m
        j = pos%m
        #分支一，取当前格子
        if(ban[i][j] == 0):
            changed = []
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    nx = i+dx
                    ny = j+dy
                    if(0<=nx<n and 0<=ny<m):
                        ban[nx][ny] += 1
                        changed.append((nx,ny))
            dfs(pos+1,result + g[i][j])
            # 回溯，撤销本次产生的封锁
            for (nx, ny) in changed:
                ban[nx][ny] -= 1
        #分支2，不取当前格子
        dfs(pos+1,result)

    dfs(0,0)
    return ans

def solve2()->int:
    n,m = read()
    g = [list(read()) for _ in range(n)]
    ans = 0
    value = []
    for i in range(n):
        for j in range(m):
            value.append(g[i][j])
    suffix = [0]*(n*m + 1)
    for pos in range(n*m - 1,-1,-1):
        suffix[pos] = value[pos] + suffix[pos+1]
    ban = [[0]*m for _ in range(n)]
    def dfs2(pos:int,result:int):
        nonlocal ans
        ans = max(result,ans)
        if(pos == n*m):
            return
        if(suffix[pos] + result <= ans):
            return
        x = pos//m
        y = pos%m
        if(ban[x][y] == 0):
            changed = []
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    nx = x+dx
                    ny = y + dy
                    if(0<=nx<n and 0<=ny<m):
                        ban[nx][ny] += 1
                        changed.append((nx,ny))
            dfs2(pos + 1,result + g[x][y])
            for (dx,dy) in changed:
                ban[dx][dy] -= 1
        dfs2(pos+1,result)
    dfs2(0,0)
    return ans


def main():
    t = int(input())
    ans = []
    while(t):
        ans.append(solve2())
        t -= 1
    for number in ans:
        print(number)

if (__name__ =="__main__"):
    main()