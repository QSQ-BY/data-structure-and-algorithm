""" 题目背景
有一天，小猫 rainbow 和 freda 来到了湘西张家界的天门山玉蟾宫，玉蟾宫宫主蓝兔盛情地款待了它们，并赐予它们一片土地。

题目描述
这片土地被分成 N×M 个格子，每个格子里写着 R 或者 F，R 代表这块土地被赐予了 rainbow，F 代表这块土地被赐予了 freda。

现在 freda 要在这里卖萌。。。它要找一块矩形土地，要求这片土地都标着 F 并且面积最大。

但是 rainbow 和 freda 的 OI 水平都弱爆了，找不出这块土地，而蓝兔也想看 freda 卖萌（她显然是不会编程的……），所以它们决定，如果你找到的最大的土地面积为 S，它们每人给你 S 两银子。

输入格式
第一行两个整数 N，M，表示矩形土地有 N 行 M 列。

接下来 N 行，每行 M 个用空格隔开的字符 F 或 R，描述了矩形土地。

输出格式
输出一个整数，表示你能得到多少银子，即 3×S 的值。

输入输出样例
输入 #1复制

5 6 
R F F F F F 
F F F F F F 
R R R F F F 
F F F F F F 
F F F F F F
输出 #1复制

45
说明/提示
对于 50% 的数据，1≤N,M≤200。
对于 100% 的数据，1≤N,M≤1000。 """
import sys
input = sys.stdin.buffer.readline
from collections import deque
def read():
    return map(int,input().split())
n,m = read()
g = [[]for _ in range(n)]
for i in range(n):
    g[i] = list(input().decode().split())
#cnt[i][j]表示从(i,j)点网上看有多少连续的F
cnt = [[0]*(m)for _ in range(n)]
for i in range(m):
    if(g[0][i] == "F"):
        cnt[0][i] = 1

for i in range(1,n):
    for j in range(m):
        if(g[i][j] == "F"):
            cnt[i][j] = 1 + cnt[i-1][j]

def calculate_one_row(cnt:list):
    left = [-1]*(m)#left[i]表示第i个柱子左边离他最近的小于他的标号
    right = [m]*(m)#right[i]则是右边
    stack = deque()#单增单调栈
    for i in range(m-1,-1,-1):
        while(stack and cnt[stack[-1]] >= cnt[i]):
            stack.pop()
        if(stack):
            right[i] = stack[-1]
        stack.append(i)
    stack = deque()
    for i in range(m):
        while(stack and cnt[stack[-1]] >= cnt[i]):
            stack.pop()
        if(stack):
            left[i] = stack[-1]
        stack.append(i)
    ret = 0
    for i in range(m):
        ret = max(ret,cnt[i]*(right[i] - left[i] - 1))
    return ret
ans = 0
for i in range(n):
    ans = max(ans,calculate_one_row(cnt[i]))
print(3*ans)