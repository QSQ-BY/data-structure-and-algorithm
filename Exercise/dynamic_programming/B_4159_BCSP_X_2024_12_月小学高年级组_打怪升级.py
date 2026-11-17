""" 题目描述
Alice 在玩一个游戏，游戏共有 n 个关卡，你需要操作 1 个主角过关，主角有 2 个属性：

血量
等级
每关的 Boss 会对主角造成伤害（血量减小），第 i 关的 Boss 对等级为 j 的主角造成的伤害值为 b[i][j]。

每关打完 Boss 后，在进入下一关前会得到一本经验书，你有 2 个选择：

回血：第 i 关的经验书可以使血量增加 a[i]。
改变等级：若假设主角当前等级为 now，使用经验书可以将等级变为 [1,now+1] 中的任意值。
你需要在 2 个选择中择一执行。

已知主角的初始血量为 m，初始等级为 1，游戏过程中任意时刻血量必须 >0。

现在请问，在通过第 k 个关卡之后（可以使用第 k 关的经验书），主角能达到的最大等级是多少？如果无法通过第 k 关，答案为 0。

请你输出 k=1∼n 的所有答案，注意这 n 个询问是独立的。

例如 n=3,m=2,a=[2,1,1]

b[1][1]=1
b[2][1]=2,b[2][2]=3
b[3][1]=3,b[3][2]=3,b[3][3]=3
当 k=1 时，第一关血量先减为 2−1=1，然后选择升为 2 级，答案为 2。
当 k=2 时，第一关血量先减为 2−1=1，然后选择加血 1+2=3；第二关血量减为 3−2=1，然后选择升为 2 级，答案为 2。
当 k=3 时，无论如何选择都无法通过第 3 关，答案为 0。
输入格式
第一行 2 个整数 n,m，代表关卡数量和初始血量。

第二行 n 个整数 a[1∼n] 代表每关经验书的加血量。

接下来 n 行，第 i 行包含 i 个整数代表第 i 关的 Boss 对等级为 1∼i 的主角造成的伤害值。

输出格式
输出 n 行，第 i 行包含 1 个整数代表通过第 i 个关卡之后，主角能达到的最大等级。

输入输出样例
输入 #1复制

3 2
2 1 1
1
2 3
3 3 3
输出 #1复制

2
2
0
输入 #2复制

10 98
67 100 76 15 44 86 38 95 5 8
43
25 91
14 18 24
79 79 60 85
35 47 59 22 96
53 78 43 95 55 25
74 26 97 30 42 14 6
100 70 79 49 83 74 43 38
64 38 75 79 59 10 54 17 2
34 19 19 4 23 90 99 97 93 10
输出 #2复制

2
2
3
4
4
4
5
5
5
6
说明/提示
样例 3-5
见附件。

数据范围
对于所有数据，1≤n≤1500,0≤a[i],b[i][j]≤100,1≤m≤1500

本题采用捆绑测试，你必须通过子任务中的所有数据点以及其依赖的子任务，才能获得子任务对应的分数。

子任务编号	分值	n	子任务依赖
1	39	≤10	
2	43	≤100	1
3	18	≤1500	1,2 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solution1():
    n,m = read()#关卡个数和初始血量
    arr = list(read())
    g = [[]for _ in range(n)]
    for i in range(n):
        g[i] = list(read())
    #dp[i][j]表示到达第i层等级为j的时候,主角所能获得的最大的血量
    # dp[i][j]：打完第 i 关并使用经验书后，
    # 等级为 j 时的最大血量，0 表示不可达
    dp = [[0] * (n + 2) for _ in range(2)]
    dp[0][1] = m

    for i in range(1, n + 1):
        c = i%2
        p = 1-c
        #当前行即将复用，先清空一次
        dp[c] = [0]*(n+2)
        # 打第 i 关之前，等级最高为 i
        for pre in range(1, i + 1):
            if dp[p][pre] == 0:
                continue

            blood = dp[p][pre] - g[i-1][pre - 1]
            if blood <= 0:
                continue

            # 使用第 i 关经验书后，等级最高为 i + 1
            for j in range(1, i + 2):
                # 选择回血，等级不变
                if j == pre:
                    dp[c][j] = max(
                        dp[c][j],
                        blood + arr[i - 1]
                    )

                # 选择改变等级，血量不变
                if j <= pre + 1:
                    dp[c][j] = max(dp[c][j], blood)

        ans = 0
        for j in range(i + 1, 0, -1):
            if dp[c][j] > 0:
                ans = j
                break
        print(ans)

def solution2():
    n,m = read()#关卡个数和初始血量
    arr = list(read())
    g = [[]for _ in range(n)]
    for i in range(n):
        g[i] = list(read())

    # dp[i][j]：打完第 i 关并使用经验书后，等级为 j 时的最大血量
    # 0 表示不可达；保留全部行，不使用滚动数组
    dp = [[0] * (n + 2) for _ in range(n + 1)]
    dp[0][1] = m

    for i in range(1, n + 1):
        # 改成等级 j，要求原等级 pre >= j - 1
        # 倒序枚举 j，维护这些原等级打完 Boss 后剩余血量的后缀最大值
        best = 0
        for j in range(i + 1, 0, -1):
            if j > 1:
                pre = j - 1
                blood = dp[i - 1][pre] - g[i - 1][pre - 1]
                # best 初始为 0，只有存活状态（blood > 0）能更新它
                best = max(best, blood)

            # 选择改变等级，不回血
            dp[i][j] = best

            # 选择回血，原等级和目标等级都必须为 j
            if j <= i:
                blood = dp[i - 1][j] - g[i - 1][j - 1]
                # 必须先活着打完 Boss，才能使用经验书回血
                if blood > 0:
                    dp[i][j] = max(dp[i][j], blood + arr[i - 1])

        ans = 0
        for j in range(i + 1, 0, -1):
            if dp[i][j] > 0:
                ans = j
                break
        print(ans)


if __name__ == '__main__':
    solution2()
