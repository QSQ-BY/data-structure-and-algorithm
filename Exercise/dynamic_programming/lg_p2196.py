""" 在一个地图上有 N (N≤20) 个地窖，每个地窖中埋有一定数量的地雷（每个地窖的地雷均不超过 300 个）。同时，给出地窖之间的连接路径。当地窖及其连接的数据给出之后，某人可以从任一处开始挖地雷，然后每次可以移动到一个编号比当前节点大且联通的节点去挖地雷，当无满足条件的节点时挖地雷工作结束。设计一个挖地雷的方案，使某人能挖到最多的地雷。

输入格式
有若干行。

第 1 行只有一个数字，表示地窖的个数 N。

第 2 行有 N 个数，分别表示每个地窖中的地雷个数。

第 3 行至第 N+1 行表示地窖之间的连接情况：

第 3 行有 n−1 个数（0 或 1），表示第一个地窖至第 2 个、第 3 个 … 第 n 个地窖有否路径连接。如第 3 行为 1 1 0 0 0⋯0，则表示第 1 个地窖至第 2 个地窖有路径，至第 3 个地窖有路径，至第 4 个地窖、第 5 个 … 第 n 个地窖没有路径。

第 4 行有 n−2 个数，表示第二个地窖至第 3 个、第 4 个 … 第 n 个地窖有否路径连接。

……

第 n+1 行有 1 个数，表示第 n−1 个地窖至第 n 个地窖有否路径连接。（为 0 表示没有路径，为 1 表示有路径）。

输出格式
第一行表示挖得最多地雷时的挖地雷的顺序，各地窖序号间以一个空格分隔，不得有多余的空格。

第二行只有一个数，表示能挖到的最多地雷数。

输入输出样例
输入 #1复制

5
10 8 4 7 6
1 1 1 0
0 0 0
1 1
1
输出 #1复制

1 3 4 5
27 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = [0] + list(read())
dp = [0]*(n+2)#dp[i]表示以n节点为结尾的路径的总价值
visit = [[]for _ in range(n+2)]
for i in range(1,n):
    dp[i] = arr[i]
    visit[i] = [0]*(i+1) + list(read()) + [0]
dp[n] = arr[n]
previous = [-1]*(n+2) 
for i in range(1,n+1):
    for j in range(1,i):
        if(visit[j][i] == 1):
            if(dp[j] + arr[i] > dp[i]):
                dp[i] = dp[j] + arr[i]
                previous[i] = j
ans = 0
ans_arr = []
ind = 0
for index,number in enumerate(dp):
    if(number > ans):
        ans = number
        ind = index
while(ind != -1):
    ans_arr.append(ind)
    ind = previous[ind]
ans_arr.reverse()
print(*ans_arr)
print(ans)