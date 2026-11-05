""" 题目描述
题目可能有些许修改，但大意一致。

Polygon 是一个玩家在一个有 n 个顶点的多边形上玩的游戏，如图所示，其中 n=4。每个顶点用整数标记，每个边用符号 +（加）或符号 *（乘积）标记。



第一步，删除其中一条边。随后每一步：

选择一条边连接的两个顶点 V 
1
​
  和 V 
2
​
 ，用边上的运算符计算 V 
1
​
  和 V 
2
​
  得到的结果来替换这两个顶点。

游戏结束时，只有一个顶点，没有多余的边。

如图所示，玩家先移除编号为 3 的边。之后，玩家选择计算编号为 1 的边，然后计算编号为 4 的边，最后，计算编号为 2 的边。结果是 0。

边的编号规则为：第 i 条边连接编号为 i−1 和编号为 i 的点。特别地，第 1 条边连接编号为 1 和编号为 n 的点



（译者注：这里每条边的运算符旁边的数字为边的编号，不拿来计算）

最终剩余的点的数值即为得到的分数。

编写一个程序，给定一个多边形，计算最高可能的分数。

输入格式
输入描述一个有 n 个顶点的多边形，它包含两行。第一行是数字 n，为总边数。

第二行描述这个多边形，一共有 n 组，每组中第一个字符为边 i 的计算符号（t 代表相加，x 代表相乘），第二个代表顶点 i 上的数字。多边形首尾相连。

输出格式
第一行，输出最高的分数。在第二行，对于每一条边，输出这条边当且仅当在删除这条边后，能够通过操作得到所有可能情况中的最高分，以严格升序输出。

输入输出样例
输入 #1复制

4
t -7 t 4 x 2 x 5
输出 #1复制

33
1 2
说明/提示
保证 3≤n≤50。

对于任何一系列的操作，顶点数字都在 [−32768,32767] 的范围内。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#表示一共有n条边
n = int(input())
data = list(input().split())
#mx[l][r]表示把[l,r]闭区间内的所有点合并成一个点之后所能得到的最大值
#mn[l][r]表示把[l,r]闭区间内的所有点合并成一个点之后所能获得的最小值
ops = data[0::2]*2
values = list(map(int,data[1::2]))*2
m = 2*n
#要同时记录最大值和最小值，因为两个负数最小值相乘可能得到一个更大的最大值
mx = [[float("-inf")] * m for _ in range(m)]
mn = [[float("inf")] * m for _ in range(m)]

for i in range(m):
    mx[i][i] = mn[i][i] = values[i]
for length in range(2,n+1):
    for r in range(length-1,m):
        l = r - length + 1
        for k in range(l,r):
            if(ops[k+1] == b"t"):
                high = mx[l][k] + mx[k+1][r]
                low = mn[l][k] + mn[k+1][r]
            else:
                products = (
                    mx[l][k] * mx[k + 1][r],
                    mx[l][k] * mn[k + 1][r],
                    mn[l][k] * mx[k + 1][r],
                    mn[l][k] * mn[k + 1][r],
                )
                high = max(products)
                low = min(products)
            mx[l][r] = max(mx[l][r], high)
            mn[l][r] = min(mn[l][r], low)

best = max(mx[i][i+n-1]for i in range(n))
print(best)
print(*(i+1 for i in range(n)if(mx[i][i+n-1] == best)))
