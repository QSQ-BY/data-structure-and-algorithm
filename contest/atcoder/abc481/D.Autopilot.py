""" Problem Statement  问题描述
There are 
N planets and 
M routes. The planets are numbered 
1 to 
N, and the routes are numbered 
1 to 
M.
共有 
N 颗行星和 
M 条路线。这些行星的编号为 
1 到 
N ，而路线的编号则为 
1 到 
M 。

Route 
i goes from planet 
A 
i
​
  to planet 
B 
i
​
 . Each route is one-way.
路线 
i 从行星 
A 
i
​
  通往行星 
B 
i
​
  。每条路线都是单程的。

A spaceship can perform the following two types of operations.
宇宙飞船可以执行以下两种类型的操作。

Move, without consuming fuel, to the planet with the smallest number among the planets directly reachable by a route from the current planet.
在不消耗燃料的情况下，移动到从当前星球出发、可以通过某条路线直接到达的行星中，编号最小的那个星球上。
Choose any planet directly reachable by a route from the current planet, and move to the chosen planet, consuming 
1 unit of fuel.
选择从当前星球出发、可以通过某条路线直接到达的任意一颗星球，然后前往该星球。此过程会消耗 
1 单位的燃料。
Find the minimum amount of fuel the spaceship consumes to start from planet 
S and arrive at planet 
T. If it is impossible to reach planet 
T, print 
−1 instead.
请计算宇宙飞船从行星 
S 出发、到达行星 
T 所需的最少燃料量。如果无法到达行星 
T ，则输出 
−1 。

Constraints  约束
2≤N≤2×10 
5
 
1≤M≤2×10 
5
 
1≤S,T≤N
S

=T
1≤A 
i
​
 ,B 
i
​
 ≤N
A 
i
​
 

=B 
i
​
 
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

N 
M 
S 
T
A 
1
​
  
B 
1
​
 
⋮
A 
M
​
  
B 
M
​
 
Output  输出结果
Print the answer.  打印出答案。

Sample Input 1  示例输入 1 复制
Copy  副本
7 10 2 1
2 5
2 4
4 2
4 3
3 1
3 5
3 6
5 6
6 1
6 7
Sample Output 1  示例输出 1 复制
Copy  副本
1
By moving in the following order, the spaceship can travel from planet 
2 to planet 
1 with a fuel consumption of 
1.
按照以下顺序移动，宇宙飞船可以以 
1 的燃料消耗量，从 
2 星球到达 
1 星球。

Move from planet 
2 to planet 
4 without consuming fuel.
无需消耗燃料，即可从行星 
2 移动到行星 
4 。
Move from planet 
4 to planet 
3, consuming 
1 unit of fuel.
从行星 
4 移动到行星 
3 ，需要消耗 
1 单位的燃料。
Move from planet 
3 to planet 
1 without consuming fuel.
无需消耗燃料，即可从行星 
3 移动到行星 
1 。
Sample Input 2  示例输入 2 复制
Copy  副本
7 10 2 7
2 5
2 4
4 2
4 3
3 1
3 5
3 6
5 6
6 1
6 7
Sample Output 2  示例输出 2 复制
Copy  副本
2
By moving in the following order, the spaceship can travel from planet 
2 to planet 
7 with a fuel consumption of 
2.
按照以下顺序移动，宇宙飞船可以以 
2 的燃料消耗量，从 
2 星球到达 
7 星球。

Move from planet 
2 to planet 
4 without consuming fuel.
无需消耗燃料，即可从行星 
2 移动到行星 
4 。
Move from planet 
4 to planet 
2 without consuming fuel.
无需消耗燃料，即可从行星 
4 移动到行星 
2 。
Move from planet 
2 to planet 
5, consuming 
1 unit of fuel.
从行星 
2 移动到行星 
5 ，需要消耗 
1 单位的燃料。
Move from planet 
5 to planet 
6 without consuming fuel.
无需消耗燃料，即可从行星 
5 移动到行星 
6 。
Move from planet 
6 to planet 
7, consuming 
1 unit of fuel.
从行星 
6 移动到行星 
7 ，需要消耗 
1 单位的燃料。
Sample Input 3  示例输入 3 复制
Copy  副本
2 1 1 2
2 1
Sample Output 3  示例输出 3 复制
Copy  副本
-1
It is impossible to start from planet 
1 and reach planet 
2.
不可能从行星 
1 开始到达行星 
2 。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int, input().split())
n, m, start, target = read()
g = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = read()
    g[u].append(v)

# 排序后，第一个邻居可以免费到达
for i in range(1, n+1):
    g[i].sort()

# dist[i]表示到达第i颗星球所需的最少燃料
dist = [float("inf")] * (n+1)
dist[start] = 0

q = deque([(0, start)])

while q:
    step, cur = q.popleft()

    # 跳过已经失效的旧状态
    if step > dist[cur]:
        continue

    if cur == target:
        print(step)
        sys.exit()

    for index, nxt in enumerate(g[cur]):
        if index == 0:
            new_dist = step
        else:
            new_dist = step + 1

        if dist[nxt] <= new_dist:
            continue
        dist[nxt] = new_dist
        if index == 0:
            q.appendleft((new_dist, nxt))
        else:
            q.append((new_dist, nxt))

print(-1)
