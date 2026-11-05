""" 题目描述
斐波那契字符串 S 是由 0 和 1 所组成的字符串，其生成规则如下：

S 
1
​
 =0。
S 
2
​
 =1。
对于任意正整数 n(n≥3)，S 
n
​
 =S 
n−2
​
 +S 
n−1
​
 （“+”表示字符串拼接）。
例如：S 
3
​
 =01、S 
4
​
 =101、S 
5
​
 =01101。

在斐波那契字符串 S 中，定义逆序对为满足以下条件的整数对 (i,j):

1≤i<j≤∣S∣（其中 ∣S∣ 表示 S 的长度）。
S[i]=1（第 i 个字符为 1）并且 S[j]=0（第 j 个字符为 0）。
现在，给定一个正整数 N，请你计算出 S 
N
​
  中所有逆序对 (i,j) 的总数。由于结果可能很大，请输出其对 10 
9
 +7 取余后的值。

输入格式
输入的第一行包含一个整数 T，表示测试用例的数量。

接下来的 T 行，每行包含一个整数 N，表示要计算的斐波那契字符串的序号。

输出格式
对于每个测试用例，输出一行，包含一个整数，表示 S 
N
​
  中所有逆序对的总数对 10 
9
 +7 取余后的结果。

输入输出样例
输入 #1复制

2
3
5
输出 #1复制

0
2
说明/提示
【样例说明】

对于 N=3，S 
3
​
 =01，逆序对总数为 0。

对于 N=5，S 
5
​
 =01101，逆序对为 (2,4)、(3,4)，总数为 2。

【评测用例规模与约定】

对于 20% 的评测用例，1≤T≤20，3≤N≤35。

对于 100% 的评测用例，1≤T≤10 
5
 ，3≤N≤10 
5
 。 """
import sys
input = sys.stdin.buffer.readline

MOD = 10**9 + 7
maximum = 3 * 10**5
cnt_zero = [0] * 3
cnt_one = [0] * 3
ans = [0] * (maximum + 1)
cnt_zero[1] = 1
cnt_one[2] = 1
for i in range(3, maximum + 1):
    cur = i % 3
    pre = (i + 2) % 3
    prepre = (i + 1) % 3
    ans[i] = (
        cnt_one[prepre] * cnt_zero[pre]
        + ans[i-2]
        + ans[i-1]
    ) % MOD

    cnt_one[cur] = (cnt_one[prepre] + cnt_one[pre]) % MOD
    cnt_zero[cur] = (cnt_zero[prepre] + cnt_zero[pre]) % MOD

t = int(input())

for _ in range(t):
    n = int(input())
    print(ans[n])