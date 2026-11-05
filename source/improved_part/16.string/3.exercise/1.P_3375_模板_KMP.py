""" 题目描述
给出两个字符串 s 
1
​
  和 s 
2
​
 ，若 s 
1
​
  的区间 [l,r] 子串与 s 
2
​
  完全相同，则称 s 
2
​
  在 s 
1
​
  中出现了，其出现位置为 l。
现在请你求出 s 
2
​
  在 s 
1
​
  中所有出现的位置。

定义一个字符串 s 的 border 为 s 的一个非 s 本身的子串 t，满足 t 既是 s 的前缀，又是 s 的后缀。
对于 s 
2
​
 ，你还需要求出对于其每个前缀 s 
′
  的最长 border t 
′
  的长度。

输入格式
第一行为一个字符串，即为 s 
1
​
 。
第二行为一个字符串，即为 s 
2
​
 。

输出格式
首先输出若干行，每行一个整数，按从小到大的顺序输出 s 
2
​
  在 s 
1
​
  中出现的位置。
最后一行输出 ∣s 
2
​
 ∣ 个整数，第 i 个整数表示 s 
2
​
  的长度为 i 的前缀的最长 border 长度。

输入输出样例
输入 #1复制

ABABABC
ABA
输出 #1复制

1
3
0 0 1 
说明/提示
样例 1 解释
。

对于 s 
2
​
  长度为 3 的前缀 ABA，字符串 A 既是其后缀也是其前缀，且是最长的，因此最长 border 长度为 1。

数据规模与约定
本题采用多测试点捆绑测试，共有 4 个子任务。

Subtask 0（30 points）：∣s 
1
​
 ∣≤15，∣s 
2
​
 ∣≤5。
Subtask 1（40 points）：∣s 
1
​
 ∣≤10 
4
 ，∣s 
2
​
 ∣≤10 
2
 。
Subtask 2（30 points）：无特殊约定。
Subtask 3（0 points）：Hack。
对于全部的测试点，保证 1≤∣s 
1
​
 ∣,∣s 
2
​
 ∣≤10 
6
 ，s 
1
​
 ,s 
2
​
  中均只含大写英文字母。 """
#KMP模板代码
import sys
input = sys.stdin.buffer.readline
s = input().decode().strip()
t = input().decode().strip()
n,m = len(s),len(t)#n、m分别表示母串和模式串的长度
next = [-1]*(m)
j = -1
for i in range(1,m):
    while(j != -1 and t[i] != t[j+1]):
        j = next[j]
    if(t[i] == t[j+1]):
        j += 1
    next[i] = j
j = -1
ans = []
for i in range(n):
    while(j != -1 and s[i]!= t[j+1]):
        j = next[j]
    if(s[i] == t[j+1]):
        j += 1
    if(j == m-1):
        print(i - j + 1)
        #找到一次匹配之后回退到可复用的前缀
        #如果直接另j=-1就会漏掉重复交叉的方案
        j = next[j]

print(*(x+1 for x in next))
#j = -1
#for i in range(1,m):
#    while(j != -1 and t[i] != t[j+1]):
#        j = next[j]
#    if(t[i] == t[j+1]):
#        j += 1
#    next[i] = j
#j = -1
#for i in range(n):
#    while(j!= -1 and s[i] != t[j+1]):
#        j = next[j]
#    if(s[i] == t[j+1]):
#        j += 1
#    if(j == m-1):
#        ans.append(i - j +1)
#        j = next[j]