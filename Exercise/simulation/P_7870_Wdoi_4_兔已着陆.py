""" 题目背景
铃瑚和清兰是从月之都到达幻想乡的两只月兔。正因为降落到了幻想乡进行调查，因此她们通过开团子屋制作团子出售的方式，在幻想乡生活。

为了应对越发繁荣的市场，她们向河城荷取购置了一台团子机器，可以高效地生产出五颜六色的团子。不同颜色的团子的售价不尽相同。由于每天顾客数量很多，购买的团子数量也不少，所以清兰总是搞不清楚一大堆团子的售价如何。

清兰找到了你，希望你能告诉她每次售出团子时，这些团子的总价格。

题目描述
清兰使用河童的机器可以生产出各种各样颜色的团子。她发现，对于颜色为 c 的团子，它的售价为 c。同时，团子机器有个特性，那就是生产出来的团子的颜色必然是一段连续的整数。

为了储存已经生产出来的团子，清兰使用了一种类似于「栈」的结构。在一天的开始，这个栈为空栈。现在有 n 次操作，分为两种：

1 l r
​
  ：团子机器生产出来了颜色为 l,l+1,⋯r−1,r 的团子。清兰将这些团子依次入栈。也就是在栈顶依次加入 l,l+1,l+2,⋯r−1,r 。
2 k
​
  ：有一位客人想要购买 k 个团子。此时清兰会依次从栈顶取出 k 个团子并售出。保证 k 不大于当前栈内的团子个数。
你要做的，就是对于每个操作 2 输出这些团子的总价格。

输入格式
第一行有一个整数 n，表示操作的个数。
接下来 n 行描述一组询问。第一个整数 op 表示询问的种类，若为 1 则为操作 1，为 2 则为操作 2。

对于操作 1，接下来有两个整数 l,r，含义如题面所示。
对于操作 2，接下来有一个整数 k，含义如题面所示。
输出格式
若干行。对于每次操作 2，输出这些团子的售价之和。

输入输出样例
输入 #1复制

6
1 1 14
2 5
1 14 19
1 1 9
2 8
2 10
输出 #1复制

60
44
124
说明/提示
样例 2 见下发的附件 stack2.in/stack2.out。

数据范围
对于前 30% 的数据，n,l,r≤100。
对于另外 20% 的数据，l=r。
对于另外 20% 的数据，k≤10。
对于 100% 的数据，1≤n≤5×10 
5
 ，0≤l≤r≤10 
6
 ，1≤k≤10 
12
 。
附件下载
stack.zip
3.87MB """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
stack = deque()
for _ in range(n):
    operation = list(read())
    scode = operation[0]
    match(scode):
        case 1:
            stack.append((operation[1],operation[2]))
        case 2:
            count = operation[1]
            ans = 0
            while(stack and stack[-1][1] - stack[-1][0]+1 <= count):
                count -= stack[-1][1] - stack[-1][0]+1
                ans += (stack[-1][1] - stack[-1][0]+1)*(stack[-1][1] + stack[-1][0])//2
                stack.pop()
            if(count == 0):
                print(ans)
                continue
            if(len(stack)>0):
                l,r = stack.pop()
                new_r = r - count
                stack.append((l,new_r))
                ans += (new_r+1+r)*(r - new_r)//2
                print(ans)

