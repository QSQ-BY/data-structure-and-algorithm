""" 题目描述
小蓝正在玩一个叫“一维消消乐”的游戏。游戏初始时给出一个长度为 n 的字符串 S=S 
0
​
 S 
1
​
 …S 
n−1
​
 ，字符串只包含字符 A 和 B。小蓝可以对这个字符串进行若干次操作，每次操作可以选择两个下标 i,j∈[0,n−1]，如果 i<j 且 S 
i
​
 =A 且 S 
j
​
 =B，小蓝就可以把它们同时消掉。小蓝想知道在经过若干次操作后，直到无法对字符串继续进行操作时，字符串最多剩下多少个字符。

输入格式
输入一行包含一个长度为 n 的字符串 S。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

BABAABBA
输出 #1复制

4
说明/提示
样例说明
先消掉 (S 
1
​
 ,S 
6
​
 )，再消掉 (S 
4
​
 ,S 
5
​
 )，此时剩下 BBAA，无法继续进行操作。

评测用例规模与约定
对于 10% 的评测用例，1≤n≤20；
对于 20% 的评测用例，1≤n≤100；
对于 50% 的评测用例，1≤n≤10000；
对于所有评测用例，1≤n≤10 
6
 。 """
import sys
input = sys.stdin.buffer.readline
string = input().decode().strip()
n = len(string)
left = 0
right = n-1
ans = n
while(left < right):
    while(left <= n-1 and string[left] != "A"):
        left += 1
        if(left >= right):
            break
    while(right >= 0 and string[right] != "B"):
        right -= 1
        if(left >= right):
            break
    if(left >= right):
        break
    left += 1
    right -= 1
    ans -= 2
print(ans)
