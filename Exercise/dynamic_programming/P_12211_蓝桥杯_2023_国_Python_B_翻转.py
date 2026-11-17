""" 题目描述
小蓝制作了 n 个工件，每个工件用一个由小写英文字母组成的，长度为 2 的字符串表示，第 i 个工件表示为 s 
i
​
 。小蓝想把 n 个工件拼接到一起，方便转移到另一个地方完成下一道工序，而拼接后的工件用字符串 S=s 
1
​
 +s 
2
​
 +…+s 
n
​
  表示，其中 + 表示一种奇特的拼接方式：对于 c=a+b 来说，如果 a 的第二个字符和 b 的第一个字符相同，则拼接后的结果 c 长度为 3 而不是 4，中间相同的字符可以省略一个，比如 xy+yz=xyz 而 xy+zy=xyzy。小蓝为了让拼接后的字符串 S 的长度尽量小，可以将若干个工件进行左右翻转之后再进行拼接，请问拼接后的字符串 S 的最小长度是多少?

请注意所有工件必须按出现顺序依次拼接，可以翻转任意工件。

输入格式
输入的第一行包含一个正整数 n。

接下来 n 行，每行包含一个长度为 2 的字符串，依次表示 s 
1
​
 ,s 
2
​
 ,⋯,s 
n
​
 。

输出格式
输出一行，包含一个整数表示答案。

输入输出样例
输入 #1复制

3
ab
cb
zz
输出 #1复制

5
说明/提示
样例说明
将 s 
2
​
  翻转后, 拼接结果为 abczz, 长度为 5。

评测用例规模与约定
对于 20% 的评测用例, n≤20；
对于所有评测用例, 1≤n≤10 
5
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = []
for _ in range(n):
    new = input().decode().strip()
    arr.append(new)

#dp[i][0]表示考虑前i个字符且最后一个字符不翻转的时候的最小长度
#dp[i][1]就是最后一个字符翻转
dp = [[float("inf")]*(2)for _ in range(2)]
dp[0][0] = 2
dp[0][1] = 2
for i in range(1,n):
    cur = i%2
    pre = 1 - cur
    head = arr[i][0]
    dp[cur][0] = dp[cur][1] = float("inf")
    if(head == arr[i-1][0]):
        dp[cur][0] = min(dp[cur][0],dp[pre][1] + 1)
    else:
        dp[cur][0] = min(dp[cur][0],dp[pre][1] + 2)
    if(head == arr[i-1][1]):
        dp[cur][0] = min(dp[cur][0],dp[pre][0] + 1)
    else:
        dp[cur][0] = min(dp[cur][0],dp[pre][0] + 2)

    head = arr[i][1]
    if(head == arr[i-1][0]):
        dp[cur][1] = min(dp[cur][1],dp[pre][1] + 1)
    else:
        dp[cur][1] = min(dp[cur][1],dp[pre][1] + 2)
    if(head == arr[i-1][1]):
        dp[cur][1] = min(dp[cur][1],dp[pre][0] + 1)
    else:
        dp[cur][1] = min(dp[cur][1],dp[pre][0] + 2)

print(min(dp[(n-1)%2][0],dp[(n-1)%2][1]))