""" 题目描述
小明需要在一条 2×n 的河床上铺设水质检测器。在他铺设之前，河床上已经存在一些检测器。如果两个检测器上下或者左右相邻，那么这两个检测器就是互相连通的。连通具有传递性，即如果 A 和 B 连通，B 和 C 连通，那么 A 和 C 也连通。现在他需要在河床上增加铺设一些检测器使得所有的检测器都互相连通。他想知道最少需要增加铺设多少个检测器？

输入格式
输入共两行，表示一个 2×n 的河床。

每行一个长度为 n 的字符串，仅包含 # 和 .，其中 # 表示已经存在的检测器，. 表示空白。

输出格式
输出共 1 行，一个整数表示答案。

输入输出样例
输入 #1复制

.##.....#
.#.#.#...
输出 #1复制

5
说明/提示
样例说明
其中一种方案：

.###....#
.#.######

增加了 5 个检测器。

评测用例规模与约定
对于 100% 的评测用例，保证 n≤1000000。 """

import sys
input = sys.stdin.buffer.readline
l1 = input().decode().strip()
l2 = input().decode().strip()
state = []
n = len(l1)
for i in range(n):
    if(l1[i] == "." and l2[i] == "."):
        state.append(0)
    elif(l1[i] == "#" and l2[i] == "."):
        state.append(1)
    elif(l1[i] == "." and l2[i] == "#"):
        state.append(2)
    elif(l1[i] == "#" and l2[i]== "#"):
        state.append(3)
if(all(s == 0 for s in state)):
    print(0)
    sys.exit()
l = 0
while(state[l] == 0):
    l+=1
r = n-1
while(state[r] == 0):
    r-=1
if(l==r):
    print(0)
    sys.exit()

edge = state[l]
gap = 0
ans = 0
for i in range(l+1,r+1):
    if(state[i] == 0):
        gap+=1
        continue
    cur = state[i]
    if((cur==1 and edge == 2) or (cur==2 and edge == 1)):
        ans += gap+1
        edge = 3
        gap = 0
    else:
        ans += gap
        edge = cur
        gap = 0

print(ans)