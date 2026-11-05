""" 题目描述
阿轩在纸上写了两个字符串，分别记为 A 和 B。利用在数据结构与算法课上学到的知识，他很容易地求出了「字符串 A 从任意位置开始的后缀子串」与字符串 B 匹配的长度。

不过阿轩是一个勤学好问的同学，他向你提出了 Q 个问题：在每个问题中，他给定你一个整数 X，请你告诉他有多少个位置，满足「字符串 A 从该位置开始的后缀子串」与 B 匹配的长度恰好为 X。

例如：A=aabcde，B=ab，则 A 有 aabcde、abcde、bcde、cde、de、e 这 6 个后缀子串，它们与 B=ab 的匹配长度分别是 1,2,0,0,0,0。因此 A 有 4 个位置与 B 的匹配长度恰好为 0，有 1 个位置的匹配长度恰好为 1，有 1 个位置的匹配长度恰好为 2。

输入格式
第一行三个整数 N,M,Q，表示 A 串长度、B 串长度、问题个数。

第二行是字符串 A，第三行是字符串 B。

接下来 Q 行每行 1 个整数 X，表示一个问题。

输出格式
共 Q 行，依次表示每个问题的答案。

输入输出样例
输入 #1复制

6 2 5
aabcde
ab
0
1
2
3
4
输出 #1复制

4
1
1
0
0
说明/提示
数据保证，1≤N,M,Q≤2×10 
5
 ，0≤X≤2×10 
5
 。 """
import sys
input = sys.stdin.buffer.readline

n, m, q = map(int, input().split())
s = input().decode().strip()
t = input().decode().strip()

# next[i]记录最长相同真前后缀的末尾下标
nxt = [-1] * m
j = -1

for i in range(1, m):
    while j != -1 and t[i] != t[j + 1]:
        j = nxt[j]

    if t[i] == t[j + 1]:
        j += 1

    nxt[i] = j

# 第一阶段：统计每个位置结尾的最长匹配长度
# 多留一个位置，保证cnt[m+1]为0
cnt = [0] * (m + 2)
j = -1

for ch in s:
    while j != -1 and ch != t[j + 1]:
        j = nxt[j]

    if ch == t[j + 1]:
        j += 1

    cnt[j + 1] += 1

    # 完整匹配也要先计数，再回退
    if j == m - 1:
        j = nxt[j]

# 第二阶段：沿next链，从长到短累加
for length in range(m, 0, -1):
    parent = nxt[length - 1] + 1
    cnt[parent] += cnt[length]

# 此时cnt[x]表示匹配长度至少为x的位置数量
out = []

for _ in range(q):
    x = int(input())

    if x > m:
        out.append("0")
    else:
        out.append(str(cnt[x] - cnt[x + 1]))

sys.stdout.write("\n".join(out))