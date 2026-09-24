""" 题目描述
小蓝用黑白棋的 n 个棋子排成了一行，他在脑海里想象出了一个长度为 n 的 01 串 T，他发现如果把黑棋当做 1，白棋当做 0，这一行棋子也是一个长度为 n 的 01 串 S。

小蓝决定，如果在 S 中发现一个棋子和它两边的棋子都不一样，就可以将其翻转变成另一个颜色。也就是说，如果 S 中存在子串 101 或者 010，就可以选择将其分别变为 111 和 000，这样的操作可以无限重复。

小蓝想知道最少翻转多少次可以把 S 变成和 T 一模一样。

输入格式
输入包含多组数据。

输入的第一行包含一个正整数 D 表示数据组数。

后面 2D 行每行包含一个 01 串，每两行为一组数据，第 2i−1 行为第 i 组数据的 T 
i
​
 ，第 2i 行为第 i 组数据的 S 
i
​
 ，S 
i
​
  和 T 
i
​
  长度均为 n 
i
​
 。

输出格式
对于每组数据，输出一行包含一个整数，表示答案，如果答案不存在请输出 −1。

输入输出样例
输入 #1复制

2
1000111
1010101
01000
11000
输出 #1复制

2
-1
说明/提示
【评测用例规模与约定】

对于 20% 的评测用例，1≤ 
i=1
∑
D
​
 n 
i
​
 ≤10；

对于所有评测用例，保证 1≤ 
i=1
∑
D
​
 n 
i
​
 ≤10 
6
 ，n r
i
​
 >0。 """
import sys
input = sys.stdin.buffer.readline
t = int(input())
ans = []

def solve():
    target = list(input().decode().strip())
    string = list(input().decode().strip())
    ret = 0
    length = len(string)
    for i in range(length):
        can_transform = False
        if(i!=0 and i!=length-1):
            if((string[i-1],string[i],string[i+1]) == ("1","0","1") or 
            (string[i-1],string[i],string[i+1]) == ("0","1","0")):
                can_transform = True
        if(can_transform and string[i] != target[i]):
            string[i] = target[i]  # 真正执行翻转
            ret += 1
            continue
        if(string[i] != target[i]):
            return -1
    return ret

for _ in range(t):
    ans.append(solve())
for number in ans:
    print(number)
