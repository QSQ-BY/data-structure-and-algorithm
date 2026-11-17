""" Problem Statement  问题陈述
You are playing nine-ball, a billiards game.
你正在玩九球台球游戏。

This game uses a total of 
9 balls, one for each number from 
1 to 
9.
这款游戏总共使用了 
9 个球，从 
1 到 
9 的每个数字对应一个球。
Currently, 
K balls remain on the table, and their numbers are 
A 
1
​
 ,A 
2
​
 ,…,A 
K
​
 .
目前，桌面上还有 
K 个球，其数量为 
A 
1
​
 ,A 
2
​
 ,…,A 
K
​
  。
It is now your turn, and you must aim at the lowest-numbered ball remaining on the table. However, if the ball numbered 
9 is no longer on the table, the game has already ended.
现在轮到你了，你需要瞄准桌子上剩余编号最小的球。不过，如果编号为 
9 的球已经不在桌上，那么游戏就已经结束了。

Print the number of the ball you should aim at on your turn. However, if the ball numbered 
9 is not on the table, the game has already ended, so print -1 instead.
打印出你本轮应该瞄准的球号。不过，如果编号为 
9 的球不在桌面上，那么游戏已经结束，此时应打印 -1 。

Constraints  约束条件
All input values are integers.
所有输入值均为整数。
1≤K≤9
1≤A 
i
​
 ≤9
The values 
A 
i
​
  are distinct.
值 
A 
i
​
  是不同的。
Input  输入
The input is given from Standard Input in the following format:
输入数据从标准输入以如下格式给出：

K
A 
1
​
  
A 
2
​
  
… 
A 
K
​
 
Output  输出
Print the answer.  打印答案。

Sample Input 1  示例输入 1 复制
Copy  复制
5
6 4 2 9 8
Sample Output 1  示例输出 1 复制
Copy  复制
2
The balls numbered 
2,4,6,8,9 remain on the table, and the ball you should aim at next is the one numbered 
2.
编号为 
2,4,6,8,9 的球仍留在桌面上，你接下来应该瞄准的是编号为 
2 的球。

Sample Input 2  示例输入 2 复制
Copy  复制
4
8 2 4 6
Sample Output 2  示例输出 2 复制
Copy  复制
-1
The balls numbered 
2,4,6,8 remain on the table, but the ball numbered 
9 does not.
编号为 
2,4,6,8 的球仍留在桌面上，而编号为 
9 的球则不在了。
In this case, the game has already ended, so the answer is -1.
在这种情况下，游戏已经结束，所以答案是 -1 。

Sample Input 3  示例输入 3 复制
Copy  复制
3
7 9 6
Sample Output 3  示例输出 3 复制
Copy  复制
6 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
s = set(arr)
if(9 not in s):
    print(-1)
else:
    print(min(arr))