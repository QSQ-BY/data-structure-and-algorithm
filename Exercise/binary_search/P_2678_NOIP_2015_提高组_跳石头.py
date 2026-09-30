""" 题目背景
NOIP2015 Day2T1

题目描述
一年一度的“跳石头”比赛又要开始了！

这项比赛将在一条笔直的河道中进行，河道中分布着一些巨大岩石。组委会已经选择好了两块岩石作为比赛起点和终点。在起点和终点之间，有 N 块岩石（不含起点和终点的岩石）。在比赛过程中，选手们将从起点出发，每一步跳向相邻的岩石，直至到达终点。

为了提高比赛难度，组委会计划移走一些岩石，使得选手们在比赛过程中的最短跳跃距离尽可能长。由于预算限制，组委会至多从起点和终点之间移走 M 块岩石（不能移走起点和终点的岩石）。

输入格式
第一行包含三个整数 L,N,M，分别表示起点到终点的距离，起点和终点之间的岩石数，以及组委会至多移走的岩石数。保证 L≥1 且 N≥M≥0。

接下来 N 行，每行一个整数，第 i 行的整数 D 
i
​
 (0<D 
i
​
 <L)， 表示第 i 块岩石与起点的距离。这些岩石按与起点距离从小到大的顺序给出，且不会有两个岩石出现在同一个位置。

输出格式
一个整数，即最短跳跃距离的最大值。

输入输出样例
输入 #1复制

25 5 2 
2
11
14
17 
21
输出 #1复制

4
说明/提示
输入输出样例 1 说明
将与起点距离为 2 和 14 的两个岩石移走后，最短的跳跃距离为 4（从与起点距离 17 的岩石跳到距离 21 的岩石，或者从距离 21 的岩石跳到终点）。

数据规模与约定
对于 20%的数据，0≤M≤N≤10。
对于 50% 的数据，0≤M≤N≤100。
对于 100% 的数据，0≤M≤N≤50000,1≤L≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline

L, n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

diff = []

if n == 0:
    diff.append(L)
else:
    diff.append(arr[0])

    for i in range(1, n):
        diff.append(arr[i] - arr[i - 1])

    diff.append(L - arr[-1])


def check(l):
    cur = 0
    cnt = 0
    for d in diff:
        cur += d
        if cur < l:
            # 目前距离还不够
            # 必须继续和下一段合并
            # 相当于删掉一块石头
            cnt += 1
        else:
            # 已经凑出一个 >= l 的跳跃距离
            cur = 0
        if cnt > m:
            return False

    return True


left = 1
right = L

while left < right:
    mid = (left + right + 1) // 2

    if check(mid):
        left = mid
    else:
        right = mid - 1

print(left)