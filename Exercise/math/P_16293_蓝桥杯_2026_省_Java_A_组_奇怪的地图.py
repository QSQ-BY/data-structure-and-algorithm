""" 题目描述
小蓝正在某个国家旅游。这个国家的城市分布在一个六边形网格上，如图所示。图中的每个六边形表示一座城市。



如果两座城市有一条公共边，那么小蓝可以从其中一座城市一步走到另一座城市。

对于任意两座城市，若从一座城市到另一座城市至少需要走 k 步，则称这两座城市之间的距离为 k。也就是说，这里的距离定义为两座城市之间的最少步数。

每座城市都可以用一个唯一的坐标 (x,y) 表示。其含义是：从坐标为 (0,0) 的城市出发，先沿 X 方向走 x 步，再沿 Y 方向走 y 步，就可以到达该城市。

现在给出 n 座城市的坐标。你需要求出这 n 座城市中，距离最远的两座城市之间的距离。

输入格式
第一行包含一个正整数 n，表示给出的城市数量。

接下来 n 行，每行包含两个整数 x 
i
​
 ,y 
i
​
 ，表示第 i 座城市的坐标。

输出格式
输出一行，包含一个整数，表示给出的 n 座城市中距离最远的两座城市之间的距离。

输入输出样例
输入 #1复制

4
0 -1
-1 -1
2 2
4 2
输出 #1复制

5
说明/提示
【样例说明】
这四座城市就是图中标出的四个城市。

其中，距离最远的一对城市是 (−1,−1) 和 (4,2)。从 (−1,−1) 出发，可以先向右上方方向走 3 步，到达 (2,2)；再沿 X 方向的正方向走 2 步，到达 (4,2)。

这两座城市之间的最短距离为 5，所以答案是 5。

【评测用例规模与约定】
对于 50% 的评测用例，n≤3000。

对于所有的评测用例，2≤n≤3×10 
5
 ，∣x 
i
​
 ∣,∣y 
i
​
 ∣≤10 
9
 。 """

#计算曼哈顿距离写比较函数，只需要看移动一个格子，
#会让什么变量的变化量在1以内
#这道题中，移动一个格子会让x+y的值变化2所以不能用它进行比较
import sys
from functools import cmp_to_key
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())
def calculate(a,b)->int:
    x1,y1,x2,y2 = a[0],a[1],b[0],b[1]
    if(x1 == x2):
        return abs(y1 - y2)
    if(y1 == y2):
        return abs(x1 - x2)
    if(x1 > x2 and y1 > y2):
        direction = (-1,-1)
    elif(x1 > x2 and y1 < y2):
        direction = (-1,0)
    elif(x1 < x2 and y1<y2):
        direction = (1,1)
    else:
        direction = (1,0)
    ret = 0
    step = min(abs(x1-x2),abs(y1 - y2))
    x1 += direction[0] * step
    y1 += direction[1] * step
    ret += step
    ret += abs(x1 - x2) + abs(y1 - y2)
    return ret

n = int(input())
dots = []
for _ in range(n):
    x,y = read()
    dots.append((x,y))

dots.sort(key=lambda p: p[0])
ans1 = calculate(dots[0],dots[-1])

dots.sort(key=lambda p: p[0] - p[1])
ans2 = calculate(dots[0],dots[-1])

dots.sort(key=lambda p: p[1])
ans3 = calculate(dots[0],dots[-1])

ans = max(ans1,ans2,ans3)
print(ans)
