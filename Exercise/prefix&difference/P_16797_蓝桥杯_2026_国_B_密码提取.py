""" 题目描述
小蓝在遗迹中发现了一面数字密码墙。密码墙可以看作一个长度为 N 的字符串 S，字符串中只包含数字 0 到 9。

小蓝可以从 S 中截取任意一个非空连续子串，并将这个子串视作一个十进制整数。子串允许包含前导零，任意长度的前导零都不影响最终数值；若子串全部由数字 0 构成，则无论子串长度是多少，其数值均为 0。例如，05 和 005 的数值都为 5，0 和 00 的数值均为 0。

如果两个子串的起止位置不同，即使它们对应的数值相同，也视为两种不同的截取方案。

现在小蓝有 M 次尝试。第 i 次尝试给出一个安全阈值区间 [l 
i
​
 ,r 
i
​
 ]。对于每次尝试，请你计算有多少种截取方案，使得截取得到的十进制数值落在 [l 
i
​
 ,r 
i
​
 ] 内。

输入格式
第一行包含两个正整数 N,M，分别表示数字字符串的长度和询问次数。

第二行包含一个长度为 N 的数字字符串 S。

接下来 M 行，每行包含两个整数 l 
i
​
 ,r 
i
​
 ，表示一次查询的安全阈值区间。

输出格式
输出 M 行。第 i 行输出一个整数，表示第 i 次查询的合法截取方案数。

输入输出样例
输入 #1复制

5 3
00510
0 5
1 10
50 510
输出 #1复制

8
5
6
说明/提示
【样例说明】
字符串为 00510。按数值统计所有非空连续子串，可以得到：

数值 0：子串为 0 的截取方案共 3 种，子串为 00 的截取方案共 1 种，合计 4 种；
数值 1：子串为 1 的截取方案共 1 种；
数值 5：子串分别为 5、05、005 的截取方案各 1 种，合计 3 种；
数值 10：子串为 10 的截取方案共 1 种；
数值 51：子串分别为 51、051、0051 的截取方案各 1 种，合计 3 种；
数值 510：子串分别为 510、0510、00510 的截取方案各 1 种，合计 3 种。
因此，区间 [0,5] 的答案为 4+1+3=8；区间 [1,10] 的答案为 1+3+1=5；区间 [50,510] 的答案为 3+3=6。

【评测用例规模与约定】
对于 30% 的评测用例，1≤N,M≤1000。

对于 80% 的评测用例，1≤N,M≤5000。

对于所有评测用例，1≤N,M≤10 
6
 ，0≤l 
i
​
 ≤r 
i
​
 ≤100000。 """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
def solution1():
    n,m = read()
    number = input().decode().strip()
    s = {}
    for left in range(n):
        for right in range(left,n):
            cur = int(number[left:right+1])
            if(cur in s):
                s[cur] += 1
            else:
                s[cur] = 1

    for _ in range(m):
        ans = 0
        l,r = read()
        for number,cnt in s.items():
            if(l<=number<=r):
                ans += cnt
        print(ans)

def solution2():
    n,m = read()
    number = list(input().decode().strip())
    limit = 100000
    #cnt[x]表示数值恰好为X的子串数量
    cnt = [0] * (limit+1)

    zeros = 0
    for left in range(n):
        if number[left] == "0":
            zeros += 1
            # 以当前零结尾的全零子串共有 zeros 个。
            cnt[0] += zeros
            continue

        # 当前非零数字前的连续零，可以选取 0 到 zeros 个。
        weight = zeros+1
        zeros = 0
        cur = 0
        for right in range(left,min(n,left+6)):
            cur = cur*10+int(number[right])
            if cur > limit:
                break
            cnt[cur] += weight

    #对cnt做前缀和
    # pre[x] 统计数值严格小于 x 的子串数量，方便处理 l=0。
    pre = [0,*accumulate(cnt)]

    ans = []
    for _ in range(m):
        l,r = read()
        ans.append(str(pre[r+1]-pre[l]))
    sys.stdout.write('\n'.join(ans))

#solution1()
solution2()
