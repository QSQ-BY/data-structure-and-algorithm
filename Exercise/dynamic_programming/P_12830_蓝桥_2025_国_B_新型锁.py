""" 题目描述
密码学家小蓝受邀参加国际密码学研讨会，为此他设计了一种新型锁，巧妙地融合了数学的严谨性与密码学的安全性。这把锁包含 2025 个连续的数字格，每个格子需填入一个正整数，从而形成一个长度为 2025 的序列 {a 
1
​
 ,a 
2
​
 ,…,a 
2025
​
 }，其中 a 
i
​
  表示第 i 个格子上的数字。

要想解锁，该序列需满足以下条件：任意两个相邻格子中的数字，其最小公倍数（LCM）均为 2025。即对于所有的 i（1≤i≤2024），需满足：

LCM(a 
i
​
 ,a 
i+1
​
 )=2025
现在，请你计算有多少个不同的序列能够解开这把锁。由于答案可能很大，你只需输出其对 10 
9
 +7 取余后的结果即可。

输入格式
无

输出格式
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。

输入输出样例
无 """
n = 2025
limit1 = 4
limit2 = 2
#dp[i][j][k]表示考虑前i位的数字
#且最后一位的数字的3的指数为j 5的指数为k
# 的情况下一共有多少种排列方式
dp = [[[0]*(limit2+1)for _ in range(limit1+1)]for _ in range(n+1)]
for j in range(limit1+1):
    for k in range(limit2+1):
        dp[1][j][k] = 1
mod = 10**9 + 7
for i in range(2,n+1):
    for j in range(limit1+1):
        for k in range(limit2+1):
            for x in range(limit1+1):
                for y in range(limit2+1):
                    if(max(x,j) == limit1 and max(y,k) == limit2):
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][x][y])%mod
ans = sum(sum(row)for row in dp[n])%mod
print(ans)
