""" 题目背景
蒟蒻 HansBug 在英语考场上，挠了无数次的头，可脑子里还是一片空白。

题目描述
眼下出现在 HansBug 蒟蒻面前的是一篇英语作文，然而智商捉急的 HansBug 已经草草写完了，此时他发现离考试结束还有 40 分钟，于是他打算估计一下这篇共有 M 个单词的英语作文的含金量如何。众所周知的是，在中高考英语作文中使用高级词汇可以有效提高文章的含金量，从而获得更好的分数。已知蒟蒻 HansBug 知道 N 个高级词汇，该词汇为 A 
i
​
 （词汇长度为 L 
i
​
 ，包含数字、大小写字母），该高级词汇的含金量为 B 
i
​
 ，则该高级词汇每出现一次便可增加 B 
i
​
  的含金量。可是他脑细胞和 RP 已经消耗殆尽，所以这个伟大的任务就交给你啦！

输入格式
第一行包含两个正整数 N 和 P，N 表示 HansBug 共知道的高级词汇个数，P 为模数。

接下来 N 行，每行包含一个单词 A 
i
​
 （长度为 L 
i
​
 ）和一个整数 B 
i
​
 ，其中 B 
i
​
 (0<B 
i
​
 ≤10 
5
 ) 表示该单词的含金量。

接下来直到输入结束的若干行为一篇英语作文，其中包含共计 M 个单词，以及若干的分隔符（分隔符包含且仅包含 ,、.、!、?）。

输出格式
一行，包含一个整数，为该文章的总含金量对 P 的模。

输入输出样例
输入 #1复制

5 99
hansbug 1
kkksc03 2
yyy 3
absi2011 4
lzn 100
hansbug is a juruo!but absi2011 not.!?!
one day absi2011 laughed at yyy and hansbug.
then kkksc03 and lzn blamed him for that.
输出 #1复制

16
输入 #2复制

5 99
yyyy 1
kkksc03 2
yyy 3
absi2011 4
lzn 100
yyyy is a juruo!but absi2011 not.!?!
one day absi2011 laughed at yyy and yyyy.
then kkksc03 and lzn blamed him for that.
输出 #2复制

16
说明/提示
样例 1 中，共计出现了 2 次 hansbug、2 次 absi2011、1 次 yyy、1 次 kkksc03、1 次 lzn，所以总含金量为 1×2+2×4+3×1+4×1+100×1=115，对 99 取模就是 16。

样例 2 中，和样例 1 基本一样，值得注意的是整体的 yyyy 不可以被认为是 yyy 出现 2 次，请注意这是一篇英语作文，一切以单词为最小单位。

此题目中大小写敏感。

数据范围（设所有单词的最大长度为 Lmax）：

测试点编号	N	M	Lmax
1∼3	≤10	≤100	≤4
4∼5	≤10 
5
 	≤3×10 
4
 
6∼7	≤5×10 
4
 	≤10 
4
 	≤50
8∼10	≤10 
5
 	≤3×10 
4
 
对于所有数据，1≤N≤10 
5
 ，1≤M≤3×10 
4
 ，1≤P≤10 
9
 。 """
import sys
inputr = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,MOD = read()
s = {}
for _ in range(n):
    data = input().split()
    s[data[0]] = int(data[1])
ans = 0
import re
from re import findall
words = findall(r'[A-Za-z0-9]+', sys.stdin.read())
for word in words:
    if(word in s):
        ans += s[word]
        ans %= MOD
print(ans%MOD)