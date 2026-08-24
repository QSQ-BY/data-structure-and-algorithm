""" 题目描述
有 n 个任务。完成第 i 个任务需要消耗 rmb 
i
​
  单位预算、rp 
i
​
  单位点数和 time 
i
​
  单位时间。

你共有 m 单位预算和 r 单位点数。请选择若干任务，使所选任务消耗的预算总和不超过 m，点数总和不超过 r。

你需要首先最大化完成的任务数量，并在完成任务数量最多的前提下，最小化完成这些任务所需的总时间。输出这个最小总时间。如果无法完成任何任务，则输出 0。

输入格式
第一行包含一个整数 n，表示任务数量。

接下来 n 行，每行包含三个整数 rmb 
i
​
 ,rp 
i
​
 ,time 
i
​
 ，表示完成第 i 个任务所需的预算、点数和时间。

最后一行包含两个整数 m,r，表示可用的预算和点数。

输出格式
输出一个整数，表示在完成任务数量最多的前提下，所需的最小总时间。

输入输出样例
输入 #1复制

4
1 2 5
2 1 6
2 2 2
2 2 3
5 5
输出 #1复制

13
说明/提示
对于 20% 的数据，1≤n≤10。

对于全部数据，1≤n,m,r≤100，1≤rmb 
i
​
 ,rp 
i
​
 ≤100，1≤time 
i
​
 ≤1000。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
data = [[]for _ in range(n+2)]
for i in range(1,n+1):
    data[i] = list(read())

max_rmb,max_rp = read()

#dp[i][j][k]表示在选择前i件物品，预算上限为j，点数上限为k的情况下，能接到的最大任务数量

count = [
    [[0] * (max_rp + 1) for _ in range(max_rmb + 1)]
    for _ in range(n + 1)
]

total_time = [
    [[0] * (max_rp + 1) for _ in range(max_rmb + 1)]
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    rmb, rp, t = data[i]

    for j in range(max_rmb + 1):
        for k in range(max_rp + 1):
            # 不选择第 i 个任务
            count[i][j][k] = count[i - 1][j][k]
            total_time[i][j][k] = total_time[i - 1][j][k]

            # 选择第 i 个任务
            if j >= rmb and k >= rp:
                new_count = count[i - 1][j - rmb][k - rp] + 1
                new_time = total_time[i - 1][j - rmb][k - rp] + t

                if new_count > count[i][j][k]:
                    count[i][j][k] = new_count
                    total_time[i][j][k] = new_time

                elif (
                    new_count == count[i][j][k]
                    and new_time < total_time[i][j][k]
                ):
                    total_time[i][j][k] = new_time

print(total_time[n][max_rmb][max_rp])
