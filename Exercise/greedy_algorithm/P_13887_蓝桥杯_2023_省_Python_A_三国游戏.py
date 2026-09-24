""" 题目描述
小蓝正在玩一款游戏。游戏中魏蜀吴三个国家各自拥有一定数量的士兵 X,Y,Z（一开始可以认为都为 0）。游戏有 n 个可能会发生的事件，每个事件之间相互独立且最多只会发生一次，当第 i 个事件发生时会分别让 X,Y,Z 增加 A 
i
​
 ,B 
i
​
 ,C 
i
​
 。

当游戏结束时（所有事件的发生与否已经确定），如果 X,Y,Z 的其中一个大于另外两个之和，我们认为其获胜。例如，当 X>Y+Z 时，我们认为魏国获胜。小蓝想知道游戏结束时如果有其中一个国家获胜，最多发生了多少个事件？

如果不存在任何能让某国获胜的情况，请输出 −1。

输入格式
输入的第一行包含一个整数 n。

第二行包含 n 个整数表示 A 
i
​
 ，相邻整数之间使用一个空格分隔。

第三行包含 n 个整数表示 B 
i
​
 ，相邻整数之间使用一个空格分隔。

第四行包含 n 个整数表示 C 
i
​
 ，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

3
1 2 2
2 3 2
1 0 7
输出 #1复制

2
说明/提示
【样例说明】

发生两个事件时，有两种不同的情况会出现获胜方。

发生 1,2 事件时蜀国获胜。

发生 1,3 事件时吴国获胜。

【评测用例规模与约定】

对于 40% 的评测用例，n≤500；

对于 70% 的评测用例，n≤5000；

对于所有评测用例，1≤n≤10 
5
 ，1≤A 
i
​
 ,B 
i
​
 ,C 
i
​
 ≤10 
9
 。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr_a = list(read())
arr_b = list(read())
arr_c = list(read())


def max_events(winner, other1, other2):
    contributions = sorted(
        (x - y - z for x, y, z in zip(winner, other1, other2)),
        reverse=True,
    )
    total = 0
    count = 0
    for value in contributions:
        if total + value <= 0:
            break
        total += value
        count += 1
    return count


ans = max(
    max_events(arr_a, arr_b, arr_c),
    max_events(arr_b, arr_a, arr_c),
    max_events(arr_c, arr_a, arr_b),
)

print(ans if ans else -1)
