""" 题目描述
小可可最近在学习平面几何！

给定平面上的 n 个点 (x 
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
 ),⋯,(x 
n
​
 ,y 
n
​
 )。

根据题目要求，输出下列两个值其中一个：

任意两点间欧几里得距离最大值的平方，对于两个点 (x 
i
​
 ,y 
i
​
 ) 和 (x 
j
​
 ,y 
j
​
 )，欧几里得距离定义为  
(x 
i
​
 −x 
j
​
 ) 
2
 +(y 
i
​
 −y 
j
​
 ) 
2
 
​
 。

任意两点间曼哈顿距离最大值，对于两个点 (x 
i
​
 ,y 
i
​
 ) 和 (x 
j
​
 ,y 
j
​
 )，曼哈顿距离定义为 ∣x 
i
​
 −x 
j
​
 ∣+∣y 
i
​
 −y 
j
​
 ∣。

输入格式
第一行，两个整数 n,op，n 为平面内有多少个点，op 为 1 则求欧几里得距离最大值的平方，若 op 为 2 则求曼哈顿距离最大值。

第 2∼n+1 行，每行两个数 x 
i
​
 ,y 
i
​
 ，表示平面上的一个点。

输出格式
一行，一个整数，表示答案。

输入输出样例
输入 #1复制

5 1
3 4
1 2
5 2
3 1
2 3
输出 #1复制

16
输入 #2复制

5 2
3 4
1 2
5 2
3 1
2 3
输出 #2复制

4
说明/提示
数据范围
数据点 1∼2，op=1，1≤n≤10 
3
 ，1≤x 
i
​
 ≤10 
4
 ，y 
i
​
 =1。
数据点 3∼6，op=1，1≤n≤10 
3
 ，1≤x 
i
​
 ≤10 
9
 ，1≤y 
i
​
 ≤10 
9
 。
数据点 7∼10，op=2，1≤n≤10 
3
 ，1≤x 
i
​
 ≤10 
9
 ，1≤y 
i
​
 ≤10 
9
 。
数据点 11∼14，op=2，1≤n≤10 
6
 ，1≤x 
i
​
 ≤10 
9
 ，y 
i
​
 =1。
数据点 15∼20，op=2，1≤n≤10 
6
 ，1≤x 
i
​
 ≤10 
9
 ，1≤y 
i
​
 ≤10 
9
 。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#op为1则求解集合最大距离的平方，op为2则求解曼哈顿最大距离
n,op = read()
if(op == 2):
    x,y = read()
    sum_min = sum_max = x+y
    diff_min = diff_max = x-y
    for _ in range(n-1):
        x,y = read()
        sum_min = min(sum_min,x+y)
        sum_max = max(sum_max,x+y)
        diff_min = min(diff_min,x-y)
        diff_max = max(diff_max,x-y)
    print(max(sum_max-sum_min,diff_max-diff_min))
elif(op == 1):
    pos = []
    for _ in range(n):
        x,y = read()
        pos.append((x,y))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            dx = pos[i][0] - pos[j][0]
            dy = pos[i][1] - pos[j][1]
            ans = max(ans,dx*dx+dy*dy)
    print(ans)
