""" 题目描述
在平面中有若干线段 L 
i
​
 （不一定互不相交），组成一个又一个轨道，有一滴液体从上方滴落下来，如果碰到轨道就沿着轨道向下滚，从轨道较低的一端离开轨道，在轨道中不受任何影响，否则就垂直滴落，问最后液滴从什么位置落出整个系统。

相信这个题目一定难不倒你。

输入格式
第一行两个整数 N 和 S，表示有 N 条线段，液滴从横坐标为 S 的地方落下。

以下 N 行，每行四个整数 x 
i1
​
 ，y 
i1
​
 ，x 
i2
​
 ，y 
i2
​
  描述每条线段的端点位置。注意线段不包括两个端点，液体可以从一端点处滴下而不碰到斜面。

输出格式
一行一个整数：表示最终液体落下的位置（横坐标）。

输入输出样例
输入 #1复制

4 2
1 4 3 2
5 4 2 1
-2 -1 0 -2
-1 -3 4 -4
输出 #1复制

4
说明/提示
对于 50% 的数据，1≤n≤100，∣x∣,∣y∣,∣S∣≤500；

对于 100% 的数据，1≤n≤10 
4
 ，∣x∣,∣y∣,∣S∣≤10 
9
 。

 """
import sys
from fractions import Fraction

input = sys.stdin.readline

def read():
    return map(int,input().split())
def test01():
    n, x = map(int, input().split())

    segments = []

    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        segments.append((x1, y1, x2, y2))

    used = [False] * n

    # 初始高度看作无穷大
    current_y = None

    while True:
        best = -1
        best_height = None

        for i in range(n):
            if used[i]:
                continue

            x1, y1, x2, y2 = segments[i]

            # 当前 x 不在线段范围内
            if not (x1 <= x <= x2):
                continue

            # 线段在当前 x 处的高度
            height = Fraction(
                y1 * (x2 - x1) + (y2 - y1) * (x - x1),
                x2 - x1
            )

            # 不在当前水滴下方
            if current_y is not None and height > current_y:
                continue

            # 找当前下面最高的线段
            if best_height is None or height > best_height:
                best_height = height
                best = i

        # 没有线段了，直接落地
        if best == -1:
            break

        x1, y1, x2, y2 = segments[best]

        # 沿线段滑向较低端
        if y1 < y2:
            x = x1
            current_y = Fraction(y1)
        else:
            x = x2
            current_y = Fraction(y2)

        used[best] = True

    print(x)


def test02():
    n,x = read()
    pos = []
    for _ in range(n):
        x1,y1,x2,y2 = read()
        if(x1>x2):
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        pos.append((x1,y1,x2,y2))
    cur_y = float("inf")
    while True:
        best = -1
        best_height = float("-inf")

        for i, (x1,y1,x2,y2) in enumerate(pos):
            if(not (x1<x<x2)):
                continue
            slope = Fraction(y1 - y2,x1-x2)
            height = Fraction(y1 + slope *(x - x1))
            if(height > cur_y):
                continue
            if(height > best_height):
                best_height = height
                best = i

        if(best == -1):
            break

        x1,y1,x2,y2 = pos[best]

        if(y1 < y2):
            cur_y = y1
            x = x1
        else:
            cur_y = y2
            x = x2

    print(x)

test02()
