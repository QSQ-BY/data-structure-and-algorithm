""" 题目描述
经过 11 年的韬光养晦，某国研发出了一种新的导弹拦截系统，凡是与它的距离不超过其工作半径的导弹都能够被它成功拦截。当工作半径为 0 时，则能够拦截与它位置恰好相同的导弹。但该导弹拦截系统也存在这样的缺陷：每套系统每天只能设定一次工作半径。而当天的使用代价，就是所有系统工作半径的平方和。

某天，雷达捕捉到敌国的导弹来袭。由于该系统尚处于试验阶段，所以只有两套系统投入工作。如果现在的要求是拦截所有的导弹，请计算这一天的最小使用代价。

输入格式
第一行包含 4 个整数 x 
1
​
 ,y 
1
​
 ,x 
2
​
 ,y 
2
​
 ，每两个整数之间用一个空格隔开，表示这两套导弹拦截系统的坐标分别为 (x 
1
​
 ,y 
1
​
 ),(x 
2
​
 ,y 
2
​
 )。第二行包含 1 个整数 N，表示有 N 颗导弹。接下来 N 行，每行两个整数 x,y，中间用一个空格隔开，表示一颗导弹的坐标 (x,y)。不同导弹的坐标可能相同。

输出格式
一个整数，即当天的最小使用代价。

输入输出样例
输入 #1复制

0 0 10 0
2
-3 3
10 0
输出 #1复制

18
输入 #2复制

0 0 6 0
5
-4 -2
-2 3
4 0
6 -2
9 1
输出 #2复制

30
说明/提示
两个点 (x 
1
​
 ,y 
1
​
 ),(x 
2
​
 ,y 
2
​
 ) 之间距离的平方是 (x 
1
​
 −x 
2
​
 ) 
2
 +(y 
1
​
 −y 
2
​
 ) 
2
 。

两套系统工作半径 r 
1
​
 ,r 
2
​
  的平方和，是指 r 
1
​
 ,r 
2
​
  分别取平方后再求和，即 r 
1
2
​
 +r 
2
2
​
 。

样例 1 说明
样例 1 中要拦截所有导弹，在满足最小使用代价的前提下，两套系统工作半径的平方分别为 18 和 0。

样例 2 说明
样例 2 中的导弹拦截系统和导弹所在的位置如下图所示。要拦截所有导弹，在满足最小使用代价的前提下，两套系统工作半径的平方分别为 20 和 10。

 """

import sys
input = sys.stdin.buffer.readline
from functools import cmp_to_key
def read():
    return map(int,input().split())
x1,y1,x2,y2 = read()
n = int(input())
pos = []
for i in range(n):
    x,y = read()
    pos.append((x,y))

def cmp(pos1,pos2)->int:
    global x1
    global y1
    d1 = (x1 - pos1[0])**2 + (y1 - pos1[1])**2
    d2 = (x1 - pos2[0])**2 + (y1 - pos2[1])**2
    if(d1 < d2):
        return -1
    elif(d1 > d2):
        return 1
    else:
        return 0
ans = float("inf")
pos.sort(key = cmp_to_key(cmp))
d1 = []
d2 = []
for index,dot in enumerate(pos):
    x,y = dot[0],dot[1]
    number1 = (x1 - x)**2 + (y1 - y)**2
    number2 = (x2 - x)**2 + (y2 - y)**2
    d1.append(number1)
    d2.append(number2)

for i in range(n-2,-1,-1):
    d2[i] = max(d2[i],d2[i+1])

for i in range(n):
    r2 = d2[i]
    r1 = 0
    if(i == 0):
        r1 = 0
    else:
        r1 = d1[i-1]
    ans = min(r1+r2,ans)

ans = min(ans , d1[-1])
print(ans)
