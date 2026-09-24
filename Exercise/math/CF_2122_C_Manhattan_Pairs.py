""" 题目描述
给定二维平面上的 n 个整点 (x 
i
​
 ,y 
i
​
 )，保证 n 是偶数。请选出  
2
n
​
  组不交的点对 (a 
i
​
 ,b 
i
​
 )，使得这些点对之间的曼哈顿距离之和最大。换句话说，需要最大化：

i=1
∑
2
n
​
 
​
 ∣x 
a 
i
​
 
​
 −x 
b 
i
​
 
​
 ∣+∣y 
a 
i
​
 
​
 −y 
b 
i
​
 
​
 ∣
输入格式
第一行输入 t(1≤t≤10 
4
 )，表示测试用例组数。

每组数据第一行包括一个偶数 n(2≤n≤2×10 
5
 )，表示点的数量。

接下来 n 行，第 i 行有两个整数 x 
i
​
 ,y 
i
​
 (−10 
6
 ≤x 
i
​
 ,y 
i
​
 ≤10 
6
 )，表示第 i 个点的坐标。

数据保证所有测试用例的 n 之和不超过 2×10 
5
 。

输出格式
对于第 i 组测试用例，输出  
2
n
​
  行，第 i 行包括两个整数 a 
i
​
 ,b 
i
​
 ，表示第 i 组的两个点的编号。

若有多种解，输出任意一种即可。

输入输出样例
输入 #1复制

2
4
1 1
3 0
4 2
3 4
10
-1 -1
-1 2
-2 -2
-2 0
0 2
2 -3
-4 -4
-4 -2
0 1
-4 -2
输出 #1复制

4 1
2 3
8 1
9 10
7 5
2 3
6 4
说明/提示
【样例解释】

在第一个测试用例中，最优解是选择点对 (1,4) 和 (2,3)，此时距离总和为 5+3=8。

在第二个测试用例中，最优解是选择点对 (1,8)，(9,10)，(5,7)，(2,3)，(4,6)，此时距离总和达到 4+7+10+5+7=33。 """

from functools import cmp_to_key
import sys

input = sys.stdin.buffer.readline

def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    def cmp_x(a, b):
        return points[a][0] - points[b][0]

    def cmp_y(a, b):
        return points[a][1] - points[b][1]

    x_side = [0] * n
    order = sorted(range(n), key=cmp_to_key(cmp_x))
    for i in order[n // 2:]:
        x_side[i] = 1

    y_side = [0] * n
    order = sorted(range(n), key=cmp_to_key(cmp_y))
    for i in order[n // 2:]:
        y_side[i] = 1

    groups = [[[], []], [[], []]]
    for i in range(n):
        groups[x_side[i]][y_side[i]].append(i + 1)

    ans = []
    for a, b in zip(groups[0][0], groups[1][1]):
        ans.append(f"{a} {b}")
    for a, b in zip(groups[0][1], groups[1][0]):
        ans.append(f"{a} {b}")
    return "\n".join(ans)


t = int(input())
print("\n".join(solve() for _ in range(t)))
