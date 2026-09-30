""" 题目描述
我们称一个字符串 S 包含字符串 T 是指 T 是 S 的一个子序列，即可以从字符串 S 中抽出若干个字符，它们按原来的顺序组合成一个新的字符串与 T 完全一样。给定两个字符串 S 和 T，请问 T 中从第一个字符开始最长连续多少个字符被 S 包含？

输入格式
输入两行，每行一个字符串。第一行的字符串为 S，第二行的字符串为 T。两个字符串均非空而且只包含大写英文字母。

输出格式
输出一个整数，表示答案。

输入输出样例
输入 #1复制

ABCDEABCD
AABZ
输出 #1复制

3
说明/提示
对于 20% 的评测用例，1≤∣T∣≤∣S∣≤20；

对于 40% 的评测用例，1≤∣T∣≤∣S∣≤100；

对于所有评测用例，1≤∣T∣≤∣S∣≤1000。

蓝桥杯 2019 年国赛 C 组 F 题。 """
import sys
input = sys.stdin.buffer.readline
string1 = str(input().decode().strip())
string2 = str(input().decode().strip())
ans = 0
for ch in string1:
    if ans == len(string2):
        break
    if ch == string2[ans]:
        ans += 1
print(ans)
