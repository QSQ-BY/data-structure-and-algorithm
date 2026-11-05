""" Problem Statement  问题描述
You are given a directed graph with 
N vertices and 
M edges. The vertices are numbered 
1,2,…,N. The 
i-th edge goes from vertex 
A 
i
​
  to vertex 
B 
i
​
 , and a digit 
C 
i
​
  between 
1 and 
9, inclusive, is written on this edge.
给定一个有向图，该图包含 
N 个顶点和 
M 条边。这些顶点被编号为 
1,2,…,N 。第 
i 条边连接顶点 
A 
i
​
  和顶点 
B 
i
​
  ，在这条边上还标有一个数字 
C 
i
​
  ，该数字介于 
1 和 
9 之间（包括 
1 和 
9 ）。

When moving along the edges in their directions, the integer obtained by concatenating the digits written on the traversed edges in the order they are traversed is called the score of the movement. For example, if the digits written on the traversed edges are 
3,1,4 in this order, the score of the movement is 
314. The same vertex or edge may be traversed multiple times.
当沿着边的方向移动时，将所经过的边上所写的数字按顺序连接起来得到的整数，就被称为该次移动的“得分”。例如，如果所经过的边上所写的数字依次为 
3,1,4 ，那么该次移动的得分为 
314 。同一个顶点或边可以被多次经过。

For each 
v=2,3,…,N, find the minimum score of a movement from vertex 
1 to vertex 
v, modulo 
998244353. Here, it is guaranteed that the given directed graph allows moving from vertex 
1 to every other vertex along the edges in their directions.
对于每一个 
v=2,3,…,N ，求出从顶点 
1 到顶点 
v 的路径上的最小得分，结果需要对 
998244353 取模。需要保证的是，给定的有向图允许从顶点 
1 出发，沿着各条边的方向到达其他所有顶点。

Constraints  约束
2≤N≤2×10 
5
 
N−1≤M≤2×10 
5
 
1≤A 
i
​
 ,B 
i
​
 ≤N
1≤C 
i
​
 ≤9
All input values are integers.
所有输入值均为整数。
It is possible to move from vertex 
1 to every other vertex along the edges in their directions.
可以从顶点 
1 出发，沿着各条边的方向，到达该边所连接的其它所有顶点。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

N 
M
A 
1
​
  
B 
1
​
  
C 
1
​
 
A 
2
​
  
B 
2
​
  
C 
2
​
 
⋮
A 
M
​
  
B 
M
​
  
C 
M
​
 
Output  输出结果
Print 
N−1 lines. The 
(v−1)-th line should contain the value found for vertex 
v.
打印 
N−1 行内容。第 
(v−1) 行应包含顶点 
v 对应的数值。

Sample Input 1  示例输入 1 复制
Copy  副本
4 4
1 2 1
1 3 1
2 4 9
3 4 2
Sample Output 1  示例输出 1 复制
Copy  副本
1
1
12
For vertex 
2, 
1 
1
​
 2 gives a score of 
1.
对于顶点 
2 ， 
1 
1
​
 2 给出的评分为 
1 。
For vertex 
3, 
1 
1
​
 3 gives a score of 
1.
对于顶点 
3 ， 
1 
1
​
 3 给出的评分为 
1 。
For vertex 
4, 
1 
1
​
 2 
9
​
 4 gives a score of 
19, and 
1 
1
​
 3 
2
​
 4 gives a score of 
12, so the minimum is 
12.
对于顶点 
4 来说， 
1 
1
​
 2 
9
​
 4 给出的得分为 
19 ， 
1 
1
​
 3 
2
​
 4 给出的得分为 
12 ，因此最小得分为 
12 。
Thus, print 
1,1,12, separated by newlines.
因此，输出 
1,1,12 ，各元素之间用换行符分隔。

Sample Input 2  示例输入 2 复制
Copy  副本
3 5
1 2 9
1 2 2
2 2 1
1 3 9
2 3 1
Sample Output 2  示例输出 2 复制
Copy  副本
2
9
For vertex 
2, 
1 
9
​
 2 gives a score of 
9, and 
1 
2
​
 2 gives a score of 
2, so the minimum is 
2.
对于顶点 
2 来说， 
1 
9
​
 2 给出的得分为 
9 ， 
1 
2
​
 2 给出的得分为 
2 ，因此最小得分为 
2 。
For vertex 
3, 
1 
9
​
 3 gives a score of 
9, and 
1 
2
​
 2 
1
​
 3 gives a score of 
21, so the minimum is 
9.
对于顶点 
3 来说， 
1 
9
​
 3 给出的得分为 
9 ， 
1 
2
​
 2 
1
​
 3 给出的得分为 
21 ，因此最小得分为 
9 。
Note that the given graph may contain multi-edges and self-loops.
请注意，该图可能包含多条边和自环。

Sample Input 3  示例输入 3 复制
Copy  副本
11 11
1 2 9
2 3 9
3 4 8
4 5 2
5 6 4
6 7 4
7 8 3
8 9 5
9 10 3
9 10 2
10 11 9
Sample Output 3  示例输出 3 复制
Copy  副本
9
99
998
9982
99824
998244
9982443
99824435
998244352
998244352
Note that the score should be printed modulo 
998244353.
请注意，乐谱应以 
998244353 的模数打印。 """

import sys
from collections import deque
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

MOD = 998244353

n, m = read()
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = read()
    g[a].append((b, c))

# ans[i] 表示到达节点 i 的最小得分（取模）
ans = [0] * (n+1)

vis = [False] * (n+1)
vis[1] = True

# 队列中的每个元素是一组得分相同的节点
q = deque()
#队列中的每一个成员的表示到达这个点所需要的分数和这个分数的点的集合
q.append(([1], 0))

while q:
    group, score = q.popleft()

    # 按照边上的数字分成9组
    buckets = [[] for _ in range(10)]

    for u in group:
        for v, c in g[u]:
            if not vis[v]:
                buckets[c].append(v)

    # 按数字从小到大扩展
    # 这样就能保证队列取出元素都是按照从小到大进行取数的
    for c in range(1, 10):
        new_group = []
        new_score = (score * 10 + c) % MOD

        for v in buckets[c]:
            if vis[v]:
                continue

            vis[v] = True
            ans[v] = new_score
            new_group.append(v)
        if new_group:
            q.append((new_group, new_score))

for i in range(2, n+1):
    print(ans[i])
