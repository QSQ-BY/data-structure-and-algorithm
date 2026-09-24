""" 题目描述
桃花岛其实也没什么好玩的，黄蓉经常偷偷跑到江湖上与洪七公等人玩。于是，黄药师就经常想一些游戏与女儿玩，为了是把黄蓉留在身边，江湖险恶啊！

这次黄药师又想了一种模拟游戏，游戏是这样的：她把整个桃花岛划分成一个坐标系。游戏开始前，黄蓉站在平面坐标系的一个点上，而她的闺房在坐标系的另一个点上，任何时候，她可以从当前所在点跨一步达到她周围的上、下、左、右四个点，黄药师不断地说四个字“东（E）”、“南（S）”、“西（W）”、“北（N）”，则黄蓉就想象着不断地从一个点走到另一个点，直至到自己的闺房为止。



比如，黄蓉开始时站在 A 点，她的家在 B 点，黄药师连续说了一串：NNNENNWWWSSW，则走了如下一个线路。然后，黄药师会问黄蓉：中间有没有走“弯路”了？即有没有捷径好走？比如，下图中就有多条捷径，可以从 C 走 NN 而到 E，或走 WW 直接到 D。

注意：捷径必须是直线。

黄药师听说你是一个程序设计高手，就想请你编个程序帮他测测这个游戏的难度，以便改进游戏规则后再让黄蓉挑战。

你的任务是：找一条最短的捷径。

输入格式
第一行是一个整数 n（3≤n≤2.5×10 
5
 ）表示黄药师所报出的字符串长度。

第二行是一个由 N,E,S,W 组成的字符串，都是大写字母且中间没有空格。

我们把游戏的起点记为 0，把黄蓉的闺房（即游戏的终点）记为 n，中间的每一个落脚点都依次标记一个自然数。

输出格式
输出只有一行，由 3 个数字和 1 个字符组成，中间用1个空格隔开。

第 1 个数字表示最短捷径的长度。
第 2 个数字表示最短捷径的开始点。
第 3 个数字表示最短捷径的结束点。
最后一个字符表示最短捷径的方向（同样用 N,E,S,W 中的一个表示）。
如果最短捷径存在多个解，那么输出开始点标号最小的那一条。如果仍然有多个解，那么输出结束点标号最大的。数据保证一定存在满足条件的最短捷径。

输入输出样例
输入 #1复制

12
NNNENNWWWSSW
输出 #1复制

2 3 11 W """

import sys
from functools import cmp_to_key
input = sys.stdin.buffer.readline

def cmp_x(a,b):
    if(a[0] != b[0]):
        return a[0] - b[0]
    return a[1] - b[1]

def cmp_y(a,b):
    if(a[1] != b[1]):
        return a[1] - b[1]
    return a[0] - b[0]

#检查两个同行或同列的点能否构成捷径
def check(p,q):
    if(p[2] > q[2]):
        p,q = q,p
    x1,y1,start = p
    x2,y2,end = q
    if(start+1 == end):
        return None

    if(x1 != x2 and y1 != y2):
        return None

    length = abs(x1 - x2) + abs(y1-y2)

    if(length == 0 or length >= end - start):
        return None

    if(x1 == x2):
        direction = "N" if y2 > y1 else "S"
    else:
        direction = "E" if x2 > x1 else "W"

    return (length,start,-end,direction)


n = int(input())
operations = list(input().decode().strip())

points = []
#初始为(0，0)点，点的编号为0
points.append((0,0,0))
for operation in operations:
    cur_x,cur_y,cur_id = points[-1]
    match(operation):
        case "N":
            points.append((cur_x,cur_y+1,cur_id + 1))
        case "S":
            points.append((cur_x,cur_y-1,cur_id + 1))
        case "E":
            points.append((cur_x + 1,cur_y,cur_id + 1))
        case "W":
            points.append((cur_x - 1,cur_y,cur_id + 1))

best = None

points.sort(key = cmp_to_key(cmp_x))

#同一列内检查上下相邻的点
for i in range(n):
    p,q = points[i],points[i+1]
    if(p[0] != q[0]):
        continue
    candidate = check(p,q)
    if candidate is not None:
        if best is None or candidate < best:
            best = candidate

points.sort(key = cmp_to_key(cmp_y))

#同一行内检查上下相邻的点
for i in range(n):
    p,q = points[i],points[i+1]
    if(p[1] != q[1]):
        continue
    candidate = check(p,q)
    if candidate is not None:
        if best is None or candidate < best:
            best = candidate

length, start, negative_end, direction = best
print(length, start, -negative_end, direction)
