import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(read())
    #dp[i][j]表示执行完前i个任务且
    #另外一个机器人正在执行完成第j个任务的位置下标的情况下所能获得的最小消耗
    dp = [[float("inf")]*(n+1)for _ in range(2)]
    dp[0][0] = 0
    dp[1][0] = arr[1]
    for i in range(1,n):
        cur = i%2
        nxt = 1 - cur
        dp[nxt] = [float("inf")]*(n+1)
        for j in range(i):
            #把i号机器人移动到i+1号或者把j号机器人移动到i+1号
            #把i号机器人移动到i+1号的同时j号机器人不动
            dp[nxt][j] = min(dp[nxt][j],abs(arr[i] - arr[i+1])+dp[cur][j])
            #把j号机器人移动到i+1号的同时i号机器人不动
            dp[nxt][i] = min(dp[nxt][i],abs(arr[i+1] - arr[j])+dp[cur][j])
    print(min(dp[n%2]))
