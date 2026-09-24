""" 题目描述
键盘输入一个高精度的正整数 n（不超过 250 位），去掉其中任意 k 个数字后剩下的数字按原左右次序将组成一个新的非负整数。编程对给定的 n 和 k，寻找一种方案使得剩下的数字组成的新数最小。

输入格式
输入两行正整数。

第一行输入一个高精度的正整数 n。

第二行输入一个正整数 k，表示需要删除的数字个数。

输出格式
输出一个整数，最后剩下的最小数。

输入输出样例
输入 #1复制

175438 
4
输出 #1复制

13
说明/提示
用 len(n) 表示 n 的位数，保证 1≤k<len(n)≤250。

注意：去掉若干数字后剩下的数可以存在前导零，而输出时不要输出前导零。 """

import sys
input = sys.stdin.buffer.readline

number = input().decode().strip()
k = int(input())

stack = []
for x in number:
    while stack and k > 0 and stack[-1] > x:
        stack.pop()
        k -= 1
    stack.append(x)

# 如果数字本身一直递增，例如 123456
# 那么前面没有机会删除，只需要从后面删除
if k > 0:
    stack = stack[:-k]

ans = ''.join(stack)

# 去掉前导零
ans = ans.lstrip('0')

# 如果全部都是 0
if ans == '':
    ans = '0'

print(ans)