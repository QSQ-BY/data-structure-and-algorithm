""" FJ 和他的奶牛们喜欢玩一个心算游戏。他们将数字从 1 到 N(1≤N≤12) 按某种顺序写下来，然后将相邻的数字相加，得到一个数字更少的新列表。他们重复这个过程，直到只剩下一个数字。例如，游戏的一种情况（当 N=4 时）可能是这样的：

    3   1   2   4
      4   3   6
        7   9
         16

在 FJ 背后，奶牛们开始玩一个更难的游戏，她们试图从最终的总和和数字 N 中确定起始序列。不幸的是，这个游戏有点超出了 FJ 的心算能力。

编写一个程序来帮助 FJ 玩这个游戏，并跟上奶牛们的步伐。

输入格式
共一行两个正整数 n,sum。

输出格式
输出包括一行，为字典序最小的那个答案。

当无解的时候，请什么也不输出。

输入输出样例
输入 #1复制

4 16
输出 #1复制

3 1 2 4 """

import sys
from math import comb#math的计算组合数函数
input = sys.stdin.buffer.readline

n,sum = map(int,input().split())
arr = []
state = (1 << n) - 1


coefficient = [comb(n-1,i) for i in range(n)]

#当前填入的数字的位置，当前可用的数字状态掩码t
def dfs(pos:int,state:int,current_sum:int)->bool:
    global n
    global sum
    global arr
    global coefficient

    if(pos == n+1):
        if(current_sum == sum):
            return True
        else:
            return False

    temp = state

    while(temp!=0):
        bit = -temp&temp
        number = bit.bit_length()
        next_sum = current_sum + number*coefficient[pos-1]
        if(next_sum > sum):
            temp -= (-temp & temp)
            continue
        arr.append(number)
        next_state = bit^state
        ans = dfs(pos+1,next_state,next_sum)
        if(ans == True):
            return True
        arr.pop()
        temp -= (-temp & temp)
    return False

result = dfs(1,state,0)
ans = list(map(str,arr))
if(result == True): print(" ".join(ans))
else:
    pass
