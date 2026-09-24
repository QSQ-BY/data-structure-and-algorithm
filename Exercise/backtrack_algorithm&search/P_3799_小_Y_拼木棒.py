""" 题目背景
上道题中，小 Y 斩了一地的木棒，现在她想要将木棒拼起来。

题目描述
有 n 根木棒，现在从中选 4 根，想要组成一个正三角形，问有几种选法？

答案对 10 
9
 +7 取模。

输入格式
第一行一个整数 n。

第二行往下 n 行，每行 1 个整数，第 i 个整数 a 
i
​
  代表第 i 根木棒的长度。

输出格式
一行一个整数代表答案。

输入输出样例
输入 #1复制

4 
1
1
2
2
输出 #1复制

1
说明/提示
数据规模与约定
对于 30% 的数据，保证 n≤5×10 
3
 。
对于 100% 的数据，保证 1≤n≤10 
5
 ，1≤a 
i
​
 ≤5×10 
3
 。
关于标题：因为一些不可抗力的原因，名称进行了更改。深表歉意。 """
import sys
import math
input = sys.stdin.buffer.readline
n = int(input())
s = {}
for _ in range(n):
    number = int(input())
    if(number in s):
        s[number] += 1
    else:
        s[number] = 1
ans = 0

def dfs(edge):
    cnt = s[edge]
    ret = 0
    combination1 = math.comb(cnt,2)
    combination2 = 0
    for length,cnt in s.items():
        if(length == edge):
            continue
        if(length > edge):
            continue
        find = edge - length
        if(find < length):
            continue

        if(find in s):
            if(find == length):
                combination2 += math.comb(cnt,2)
            else:
                combination2 += cnt*s[find]
    ret += combination2 * combination1
    return ret

MOD = 10**9 + 7
for length in s:
    if(s[length] < 2):
        continue
    ans += dfs(length)
print(ans%MOD)