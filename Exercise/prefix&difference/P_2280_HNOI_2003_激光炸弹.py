""" 题目描述
一种新型的激光炸弹，可以摧毁一个边长为 m 的正方形内的所有目标。现在地图上有 n 个目标，用整数 x 
i
​
  , y 
i
​
  表示目标在地图上的位置，每个目标都有一个价值 v 
i
​
 。激光炸弹的投放是通过卫星定位的，但其有一个缺点，就是其爆破范围，即那个边长为 m 的边必须与 x 轴，y 轴平行。若目标位于爆破正方形的边上，该目标不会被摧毁。

现在你的任务是计算一颗炸弹最多能炸掉地图上总价值为多少的目标。

可能存在多个目标在同一位置上的情况。

输入格式
输入的第一行为整数 n 和整数 m；

接下来的 n 行，每行有 3 个整数 x,y,v，表示一个目标的坐标与价值。

输出格式
输出仅有一个正整数，表示一颗炸弹最多能炸掉地图上总价值为多少的目标（结果不会超过 32767 ）。

输入输出样例
输入 #1复制

2 1
0 0 1
1 1 1
输出 #1复制

1
说明/提示
数据规模与约定

对于 100% 的数据，保证 1≤n≤10 
4
 ，0≤x 
i
​
 ,y 
i
​
 ≤5×10 
3
 ，1≤m≤5×10 
3
 ，1≤v 
i
​
 <100。 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

n, m = read()

pos = []
maximum_x = 0
maximum_y = 0

for _ in range(n):
    x, y, value = read()
    # 坐标整体 +1
    x += 1
    y += 1
    pos.append((x, y, value))
    maximum_x = max(maximum_x, x)
    maximum_y = max(maximum_y, y)

# 至少要保证能放下一个 m × m 的窗口
maximum_x = max(maximum_x, m)
maximum_y = max(maximum_y, m)

g = [[0] * (maximum_y + 1) for _ in range(maximum_x + 1)]

for x, y, value in pos:
    g[x][y] += value

prefix = [[0] * (maximum_y + 1) for _ in range(maximum_x + 1)]

for i in range(1, maximum_x + 1):
    for j in range(1, maximum_y + 1):
        prefix[i][j] = (
            g[i][j]
            + prefix[i - 1][j]
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]
        )

ans = 0

# 枚举右下角
for i in range(m, maximum_x + 1):
    for j in range(m, maximum_y + 1):
        cur = (
            prefix[i][j]
            - prefix[i - m][j]
            - prefix[i][j - m]
            + prefix[i - m][j - m]
        )
        ans = max(ans, cur)

print(ans)