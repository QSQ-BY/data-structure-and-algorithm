""" 题目描述
pigstd 有一堆数，他想在这么多数中选出若干个数排成一列，记为 x 
1
​
 ,x 
2
​
 ,⋯,x 
p
​
 （p 为数的个数）。

这一列数合法当且仅当满足以下条件：

p≥2。
令 y 
i
​
 =x 
i+1
​
 −x 
i
​
 （特别的，y 
p
​
 =x 
1
​
 −x 
p
​
 ），如果把 y 
1
​
  到 y 
p
​
  按 y 
1
​
 ,y 
2
​
 ,⋯,y 
p
​
  的顺序排成一圈，那么每两个相邻的数互为相反数且绝对值都为 k。
pigstd 想知道，在所有合法的数列中，所有在这个数列中的数之和最大是多少。

输入格式
第一行两个整数 n,k。

接下来 n 行，每行两个整数 a 
i
​
 ,b 
i
​
 ，表示 pigstd 有 b 
i
​
  个 a 
i
​
 。

不保证 a 
i
​
  互不相同，若有 a 
i
​
  相同则累加其个数计算。

输出格式
一行一个整数，表示在每一种排列中，所有在这个排列中的数的最大的和。

若没有合法的排列，则只输出 NO。

输入输出样例
输入 #1复制

4 3 
1 5
2 4
3 3
0 2
输出 #1复制

6
说明/提示
【样例 1 说明】

当 pigstd 的排列为：0,3,0,3 或 3,0,3,0 时，总和最大，为 6。

【数据规模与约定】

对于 100% 的数据，1≤n≤10 
6
 ，0≤k,a 
i
​
 ≤10 
6
 ，1≤b 
i
​
 ≤10 
6
 。

本题采用捆绑测试。

Subtask 1（5 points）：保证无合法的数列；
Subtask 2（15 points）：k=0；
Subtask 3（5 points）：n=1；
Subtask 4（5 points）：n=2；
Subtask 5（30 points）：n,k,a 
i
​
 ,b 
i
​
 ≤10 
3
 ；
Subtask 6（40 points）：无特殊限制。 """
import sys
input = sys.stdin.buffer.readline

n, k = map(int, input().split())

cnt = [0] * (10**6 + 1)
maximum = float("-inf")
for _ in range(n):
    a, b = map(int, input().split())
    maximum =max(a,maximum)
    cnt[a] += b

ans = -1

if k == 0:
    for a in range(maximum + 1):
        if cnt[a] >= 2:
            ans = max(ans, a * cnt[a])

else:
    for a in range(maximum - k + 1):
        if cnt[a] > 0 and cnt[a + k] > 0:
            t = min(cnt[a], cnt[a + k])
            ans = max(ans, (2 * a + k) * t)

print(ans if ans != -1 else "NO")
