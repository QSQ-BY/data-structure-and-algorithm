""" 题目描述
Alice 有 n 个字符，它们都是英文小写字母，从 1∼n 编号，分别为 c 
1
​
 ,c 
2
​
 ,…,c 
n
​
 。
Bob 准备将这些字符重新排列，组成一个字符串 S。Bob 知道 Alice 有强迫症，所以他打算将 S 组成一个非回文串来折磨 Alice。

现在 Bob 想知道他共有多少种不同的排列字符的方案，能使得 S 是个非回文串。一种排列字符的方案指的是一个 1∼n 的排列 p 
i
​
 ，它所组成的 S=c 
p 
1
​
 
​
 c 
p 
2
​
 
​
 …c 
p 
n
​
 
​
 。

一个字符串是非回文串，当且仅当它的逆序串与原串不同。例如 abcda 的逆序串为 adcba，与原串不同，故 abcda 是非回文串。而 abcba 的逆序串与原串相同，是回文串。

由于最后的结果可能很大，你只需要告诉 Bob 总方案数对 10 
9
 +7 取模后的值。

输入格式
第一行一个正整数 n 表示字符个数。
第二行 n 个英文小写字母 c 
i
​
 。

输出格式
仅一行一个整数表示答案。答案对 10 
9
 +7 取模。

输入输出样例
输入 #1复制

3
aba
输出 #1复制

4
输入 #2复制

8
aabbbbcc
输出 #2复制

39168
说明/提示
【数据范围】
对于 20% 的数据，n≤8；
对于 50% 的数据，n≤20；
另有 30% 的数据，字符只包含 a 和 b；
对于 100% 的数据，3≤n≤2000。 """
import sys
from math import factorial
input = sys.stdin.buffer.readline

MOD = 10**9 + 7
n = int(input())
string = list(input().decode().strip())
cnt = [0]*(26)
for ch in string:
    number = ord(ch) - ord("a")
    cnt[number] += 1
ans = factorial(n)

if(sum(c%2 for c in cnt) <= 1):
    left = factorial(n//2)
    for c in cnt:
        left //= factorial(c//2)
    palindrome = left
    for c in cnt:
        palindrome *= factorial(c)
    ans -= palindrome

print(ans%MOD)
