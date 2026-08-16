import sys
input = sys.stdin.buffer.readline
def solve():
    n,m,q = map(int,input().split())
    g = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        g[i] = [0] + list(map(int,input().split()))
    for i in range(1,n+1):
        for j in range(1,m+1):
            g[i][j] += g[i-1][j]+g[i][j-1]-g[i-1][j-1]

    ans = 0
    for _ in range(q):
        u,v,x,y = map(int,input().split())
        number = g[x][y] + g[u-1][v-1] - g[x][v-1]-g[u-1][y]
        number %= 1<<64
        ans ^=number
    print(ans)

t = int(input())
while(t!=0):
    solve()
    t -=1