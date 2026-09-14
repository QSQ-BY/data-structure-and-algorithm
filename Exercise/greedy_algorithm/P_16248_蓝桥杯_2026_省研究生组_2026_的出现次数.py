""" 题目描述
给定一个字符串 S，其只包含数字 0、2、6。

你可以进行任意次以下操作：在字符串中寻找一个连续子串 202，将其替换为 6。

你的目标是：通过执行若干次操作，使得最终得到的字符串中，连续子串 2026 出现的次数最多。

现在，请输出这个最多的出现次数。

输入格式
输入一行，包含一个仅有数字 0、2、6 组成的字符串 S。

输出格式
输出一个整数，表示最终字符串中连续子串 2026 出现的最大次数。

输入输出样例
输入 #1复制

2022026
输出 #1复制

1
输入 #2复制

2026202202
输出 #2复制

2
说明/提示
【评测用例规模与约定】
对于 40% 的评测用例，字符串 S 的长度 ∣S∣ 满足 1≤∣S∣≤500；

对于所有评测用例，字符串 S 的长度 ∣S∣ 满足 1≤∣S∣≤10 
5
 ，所有输入字符均限定在 {0,2,6} 集合内。 """
import sys
input = sys.stdin.readline
string = list(input().strip())
cur_state = []
s1 = list("202202")
s2 = list("2026")
ans = 0
for ch in string:
    cur_state.append(ch)
    if(cur_state == s1 or cur_state==s2):
        ans += 1
        cur_state = []
    else:
        while(s1[:len(cur_state)] != cur_state and s2[:len(cur_state)] != cur_state):
            cur_state.pop(0)
print(ans)
