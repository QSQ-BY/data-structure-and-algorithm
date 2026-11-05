""" 题目描述
2026 年 3 月，全国科学技术名词审定委员会发布公告，优先将人工智能领域术语“Token”的中文译名定为“词元”，并面向全社会试用。从那时起，小蓝所在的平台开始以“词元”作为月度统计的正式单位。

平台上共有 n 个接口，按从左到右的顺序编号为 1 到 n，其中第 i 个接口本月累计消耗的词元数量为 p 
i
​
 。

月末，平台需要根据词元消耗为每个接口安排下月的巡检等级。每个接口都会被分配一个正整数巡检等级，巡检等级越高，表示该接口需要被更重点地观察。不过，平台并不直接根据词元数量的绝对大小来分配巡检等级，而是参考相邻接口之间的相对关系。

对第 i 个接口，定义 c 
i
​
  为与它相邻的接口中，消耗词元数量小于 p 
i
​
  的接口个数。这里的相邻接口指编号相差 1 的接口，即接口 i 只可能与接口 i−1 和接口 i+1 相邻；编号为 1 的接口仅存在右侧相邻接口，编号为 n 的接口仅存在左侧相邻接口，其余接口均有左右两个相邻接口。因此 c 
i
​
 ∈{0,1,2}。

设第 i 个接口的巡检等级为 a 
i
​
 。平台要求任意相邻接口 i 与 i+1 满足：

若 c 
i
​
 <c 
i+1
​
 ，则 a 
i
​
 <a 
i+1
​
 ；
若 c 
i
​
 >c 
i+1
​
 ，则 a 
i
​
 >a 
i+1
​
 ；
若 c 
i
​
 =c 
i+1
​
 ，则 a 
i
​
  与 a 
i+1
​
  的大小关系不作要求。
满足规则的巡检等级分配方案可能有多种。由于巡检资源有限，平台希望巡检等级总和最小（即最小化 ∑ 
i=1
n
​
 a 
i
​
 ）。

现在，请你帮助平台求出这个最小值。

输入格式
输入共两行。

第一行包含一个正整数 n，表示接口的数量。

第二行包含 n 个整数 p 
1
​
 ,p 
2
​
 ,…,p 
n
​
 ，其中 p 
i
​
  表示第 i 个接口本月消耗的词元数量。

输出格式
输出一行，包含一个正整数，表示在满足所有相邻接口巡检等级要求的前提下，所有接口巡检等级之和的最小值。

输入输出样例
输入 #1复制

3
1 2 3
输出 #1复制

4
说明/提示
【评测用例规模与约定】
对于 30% 的评测用例，2≤n≤2×10 
3
 ，1≤p 
i
​
 ≤10 
5
 ；

对于所有评测用例，2≤n≤2×10 
5
 ，1≤p 
i v
​
 ≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
c = []
for i,number in enumerate(arr):
    cur = 0
    if(i == 0 or i == n-1):
        next = arr[1] if i == 0 else arr[n-2]
        if(number > next):
            cur = 1
        else:
            cur = 0
        c.append(cur)
        continue
    pre = arr[i-1]
    nxt = arr[i+1]
    if(number > pre):
        cur += 1
    if(number > nxt):
        cur += 1
    c.append(cur)
a = []
#dp[i][j]表示考虑前i个c，最后一个位置的数字为j的时候所能获得的最小价值
#j只能取到1 2 3
dp = [[float("inf")]*4 for _ in range(n+1)]
for i in range(1,4):
    dp[0][i] = 0
    dp[1][i] = i

for i in range(2,n+1):
    cur = c[i-1]
    pre = c[i-2]
    if(cur > pre):
        dp[i][2] = min(dp[i-1][1] + 2,dp[i][2])
        dp[i][3] = min(dp[i-1][1], dp[i-1][2]) + 3
    elif(cur < pre):
        dp[i][1] = min(dp[i-1][2], dp[i-1][3]) + 1
        dp[i][2] = min(dp[i-1][3] + 2,dp[i][2])
    else:
        for j in range(1,4):
            for k in range(1,4):
                dp[i][j] = min(dp[i-1][k] + j,dp[i][j])
ans = float("inf")
for i in range(1,4):
    ans = min(ans,dp[n][i])

print(ans)

