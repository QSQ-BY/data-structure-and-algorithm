""" 题目描述
在遥远的未来，星际旅行已经成为常态。宇航员小蓝在一次探险任务中，意外发现了一个古老的太空遗迹。遗迹中存放着一个数据存储器，里面记录着一段加密的信息。经过初步分析，小蓝发现这段信息可以被表示为一个字符串 S，而解密的关键，在于找出 S 中字典序最大的回文子序列。

子序列：指从原字符串中抽取若干个字符（可以不连续），按照它们在原字符串中的相对顺序排列所形成的新序列。例如，对于字符串 abc，其子序列包括 a、b、c、ab、ac、bc 和 abc。
字典序：指字符串按照字典中的排序规则比较大小的方式。对于两个字符串，从左到右逐字符比较，先出现较大字符的字符串字典序更大；若比较到某个字符串结束仍未找到不同的字符，则较短的字符串字典序较小。例如，abc < abd，而 ab < abc。
现在，请你从字符串 S 中，找出字典序最大的回文子序列，帮助小蓝解开这段来自星际文明的信息。

输入格式
输入一行包含一个字符串 S，表示加密的信息。

输出格式
输出一行包含一个字符串，表示 S 中字典序最大的回文子序列。

输入输出样例
输入 #1复制

abcd
输出 #1复制

d
输入 #2复制

abab
输出 #2复制

bb """
import sys
from functools import cmp_to_key
input = sys.stdin.readline

string = str(input().strip())
max = "a"
cnt = 0
for index,ch in enumerate(string):
    if(ch > max):
        cnt = 1
        max = ch
    elif((ch) <max):
        continue
    elif((ch) == max):
        cnt+=1
ans = [str(max)] * (cnt)
print("".join(ans))