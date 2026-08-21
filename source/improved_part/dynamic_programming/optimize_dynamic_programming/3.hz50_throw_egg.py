""" 题目描述
定义鸡蛋的硬度为 k，则代表鸡蛋最高从 k 楼扔下来不会碎掉，现在给你 n 个硬度相同的鸡蛋，楼高为 m，问最坏情况下最少测多少次，可以测出鸡蛋的硬度。

2FB2A117A30743DDB39CA46A537BADD2.jpg

输入
输入两个数字 n,m（1≤n≤32,1≤m<231），代表 n 个鸡蛋和 m 层楼。

输出
输出一行整数，代表最坏情况下最少测多少次可以测出鸡蛋的硬度。

样例输入1
2 100
样例输出1
14
样例输入2
1 5
样例输出2
5 """
import sys
input = sys.stdin.buffer.readline

def test01():
    n,m = map(int,input().split())
    """ dp[i][j]表示前i个鸡蛋测j层楼的最多最少次数
    dp[i][j] = min(max(dp[i][j-k],dp[i-1][k-1])) +1 """
    dp = [[0]*(m+2) for _ in range(2)]

    for i in range(1,m+1):
        dp[1][i] = i

    for i in range(2,n+1):#鸡蛋的个数
        index1 = i%2
        index2 = 1-index1
        for j in range(1,m+1):#总楼层
            #枚举第一个鸡蛋所扔的楼层k
            dp[index1][j] = j
            for k in range(1,j):
                dp[index1][j] = min(dp[index1][j],max(dp[index2][k-1],dp[index1][j-k])+1)

    print(dp[n%2][m])


def test02():
    n,m = map(int,input().split())
    """ dp[i][j] = k ->i个鸡蛋测量j层楼最后最最小次数为k
    把j和k的位置进行调换
    dp[i][k] = j->用i个鸡蛋扔k次最多可以测j楼
    dp[i][k] = dp[i-1][k-1] + d[i][k-1] +1 """ 
    dp = [[0]*(1005) for _ in range(n+2)]#i个鸡蛋测j次最多能测多少层
    if(n==1):
        print(m)
        return
    for i in range(1,1002):
        dp[1][i] = i

    ans = 1
    for i in range(2,n+1):
        flag = 0
        for j in range(1,1002):
            dp[i][j] = dp[i][j-1]+dp[i-1][j-1]+1
            if(dp[n][j]>=m):
                ans = j
                flag = 1
                break
        if(flag == 1):
            break

    print(ans)



#test01()
test02()