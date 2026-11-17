""" 题目描述
小蓝最近迷上了回文字符串，他有一个只包含小写字母的字符串 S，小蓝可以往字符串 S 的开头处加入任意数目个指定字符：l、q、b（ASCII 码分别为：108、113、98）。小蓝想要知道他是否能通过这种方式把字符串 S 转化为一个回文字符串。

输入格式
输入的第一行包含一个整数 T，表示每次输入包含 T 组数据。

接下来依次描述 T 组数据。

每组数据一行包含一个字符串 S。

输出格式
输出 T 行，每行包含一个字符串，依次表示每组数据的答案。如果可以将 S 转化为一个回文字符串输出 Yes，否则输出 No。

输入输出样例
输入 #1复制

3
gmgqlq
pdlbll
aaa
输出 #1复制

Yes
No
Yes
说明/提示
【样例说明】

对于 gmgqlq，可以在前面加上 qlq => qlqgmgqlq 转化为一个回文字符串；

对于 pdlbll，无法转化为一个回文字符串；

对于 aaa，本身就是一个回文字符串。

【评测用例规模与约定】

对于 50% 的评测用例，1≤∣S∣≤1000，其中 ∣S 
j
​
 ∣ 表示字符串 S 的长度；
对于所有评测用例，1≤T≤10，1≤∑∣S∣≤10 
6
 。 """
import sys
input = sys.stdin.buffer.readline
t = int(input())
allowed = "lqb"
for _ in range(t):
    string = input().decode().strip()
    n = len(string)

    # 统计开头连续属于 l、q、b 的字符数量
    prefix = 0
    while prefix < n and string[prefix] in allowed:
        prefix += 1
    if prefix == n:
        # 全部字符都允许添加，可以在开头补上整个字符串的逆序
        print("Yes")
        continue

    # 串中存在其他字符，因此从末尾扫描一定会停下来
    suffix = 0
    while string[n - 1 - suffix] in allowed:
        suffix += 1
    if prefix > suffix:
        print("No")
        continue

    # 末尾多出的 suffix-prefix 个字符可翻转后补到开头
    # 剩余前缀必须本身就是回文
    left = 0
    right = n - 1 - (suffix - prefix)
    while left < right and string[left] == string[right]:
        left += 1
        right -= 1
    print("Yes" if left >= right else "No")
