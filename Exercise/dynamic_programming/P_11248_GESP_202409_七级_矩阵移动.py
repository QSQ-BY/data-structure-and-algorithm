""" 题目描述
小杨有一个 n×m 的矩阵，仅包含 01? 三种字符。矩阵的行从上到下编号依次为 1,2,…,n，列从左到右编号依次为 1,2,…,m。小杨开始在矩阵的左上角 (1,1)，小杨只能向下或者向右移动，最终到达右下角 (n,m) 时停止，在移动的过程中每经过一个字符 1 得分会增加一分（包括起点和终点），经过其它字符则分数不变。小杨的初始分数为 0 分。

小杨可以将矩阵中不超过 x 个字符 ? 变为字符 1。小杨在修改矩阵后，会以最优的策略从左上角移动到右下角。他想知道自己最多能获得多少分。

输入格式
第一行包含一个正整数 t，代表测试用例组数，接下来是 t 组测试用例。对于每组测试用例，一共 n+1 行。

第一行包含三个正整数 n,m,x，含义如题面所示。
之后 n 行，每行一个长度为 m 的仅含 01? 的字符串。

输出格式
对于每组测试用例，输出一行一个整数，代表最优策略下小杨的得分最多是多少。

输入输出样例
输入 #1复制

2
3 3 1
000
111
01?
3 3 1
000
?0?
01?
输出 #1复制

4
2
说明/提示
样例 1 解释
对于第二组测试用例，将 (2,1) 或者 (3,3) 变为 1 均是最优策略。

数据规模与约定
子任务编号	数据点占比	t	n,m	x
1	30%	≤5	≤10	=1
2	30%	≤10	≤500	≤30
3	40%	≤10	≤500	≤300
对全部的测试数据，保证 1≤t≤10，1≤n,m≤500，1≤x≤300，保证所有测试用例 n×m 的总和不超过 2.5×10 
5
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solution1():
    t = int(input())
    for _ in range(t):
        n,m,x = read()
        g = [["*"]for _ in range(n+2)]
        for i in range(1,n+1):
            g[i] = ["*"] + list(input().decode().strip())+ ["*"]
        #dp[cur][j][k]表示到达当前行第j列，最多使用k次技能时能获得的最大价值
        dp = [[[0]*(x+1)for _ in range(m+1)]for _ in range(2)]

        for i in range(1,n+1):
            cur = i%2
            pre = cur^1
            #清空复用的当前行，避免保留两行之前的状态
            dp[cur] = [[0]*(x+1)for _ in range(m+1)]
            for j in range(1,m+1):
                cell = g[i][j]
                for k in range(x+1):
                    if(cell == "1" or cell == "0"):
                        get = int(cell)
                        dp[cur][j][k] = max(dp[pre][j][k],dp[cur][j-1][k])+get
                    elif(cell == "?"):
                        #不使用技能
                        dp[cur][j][k] = max(dp[pre][j][k],dp[cur][j-1][k])
                        #使用技能
                        if(k>=1):
                            dp[cur][j][k] = max(dp[cur][j][k],dp[pre][j][k-1]+1,dp[cur][j-1][k-1]+1)
        ans = 0
        for i in range(x+1):
            ans = max(ans,dp[n%2][m][i])
        print(ans)

#优化了常数开销
def solution2():
    t = int(input())
    for _ in range(t):
        n,m,x = read()
        g = [["*"]for _ in range(n+2)]
        for i in range(1,n+1):
            g[i] = ["*"] + list(input().decode().strip())+ ["*"]
        #最多使用k次技能，只保留当前行和上一行
        dp = [[[0]*(x+1)for _ in range(m+1)]for _ in range(2)]

        for i in range(1,n+1):
            cur = i%2
            pre = 1 - cur
            #每个状态都会被直接覆盖，不需要清空复用行
            for j in range(1,m+1):
                #up[k]	到达上方格子，最多修改k次的最高分
                #left[k]	到达左方格子，最多修改k次的最高分
                #dst[k]	当前格子需要计算的答案
                up = dp[pre][j]
                left = dp[cur][j-1]
                dst = dp[cur][j]
                cell = g[i][j]

                if(cell == "?"):
                    dst[0] = max(up[0],left[0])
                    #有额度时可将一次修改安排在当前格子，不影响最优得分
                    for k in range(1,x+1):
                        dst[k] = max(up[k-1],left[k-1])+1
                else:
                    get = int(cell)
                    for k in range(x+1):
                        dst[k] = max(up[k],left[k])+get
        print(dp[n%2][m][x])


if __name__ == "__main__":
    solution2()
