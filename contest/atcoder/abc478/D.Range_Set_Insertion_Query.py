""" Problem Statement  问题描述
There are 
N sets 
S 
1
​
 ,S 
2
​
 ,…,S 
N
​
 . Initially, 
S 
1
​
 ,S 
2
​
 ,…,S 
N
​
  are all empty sets.
共有 
N 组 
S 
1
​
 ,S 
2
​
 ,…,S 
N
​
  。最初，所有的 
S 
1
​
 ,S 
2
​
 ,…,S 
N
​
  都是空集。

The following operation is performed 
Q times on these sets. In the 
i-th operation 
(1≤i≤Q), a triple of integers 
(L 
i
​
 ,R 
i
​
 ,X 
i
​
 ) is given, and the operation below is performed.
对这些集合，执行以下操作 
Q 次。在第 
i 次操作中，会给出一组三个整数 
(L 
i
​
 ,R 
i
​
 ,X 
i
​
 ) ，然后执行下面的操作。

Add 
X 
i
​
  to 
S 
L 
i
​
 
​
 ,S 
L 
i
​
 +1
​
 ,…,S 
R 
i
​
 
​
 .
将 
X 
i
​
  添加到 
S 
L 
i
​
 
​
 ,S 
L 
i
​
 +1
​
 ,…,S 
R 
i
​
 
​
  中。
For every 
i=1,2,…,N, find the number of elements of 
S 
i
​
  after all operations are finished.
对于每一个 
i=1,2,…,N ，请计算在所有操作完成后， 
S 
i
​
  中包含的元素数量。

Constraints  约束
1≤N≤2×10 
5
 
1≤Q≤2×10 
5
 
1≤L 
i
​
 ≤R 
i
​
 ≤N (1≤i≤Q)
1≤X 
i
​
 ≤Q (1≤i≤Q)
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

N 
Q
L 
1
​
  
R 
1
​
  
X 
1
​
 
L 
2
​
  
R 
2
​
  
X 
2
​
 
⋮
L 
Q
​
  
R 
Q
​
  
X 
Q
​
 
Output  输出
Output the number of elements of 
S 
1
​
 
, the number of elements of 
S 
2
​
 
,…, the number of elements of 
S 
N
​
  after all 
Q operations are finished, in this order, separated by spaces.
输出在所有 
Q 操作完成后， 
S 
1
​
  中的元素数量、 
, 中的元素数量、 
S 
2
​
  中的元素数量、 
,…, 中的元素数量、 
S 
N
​
  中的元素数量。这些数值应按此顺序用空格分隔开来。

Sample Input 1  示例输入 1 复制
Copy  副本
8 5
2 5 1
1 4 2
7 8 1
3 6 3
2 5 2
Sample Output 1  示例输出 1 复制
Copy  副本
1 2 3 3 3 1 1 1
After the five operations, the sets are 
{2},{1,2},{1,2,3},{1,2,3},{1,2,3},{3},{1},{1}, respectively. Thus, output their numbers of elements, 
1,2,3,3,3,1,1,1, in this order, separated by spaces.
经过这五次操作后，各个集合分别变为 
{2},{1,2},{1,2,3},{1,2,3},{1,2,3},{3},{1},{1} 。因此，请按顺序输出这些集合中的元素个数，即 
1,2,3,3,3,1,1,1 ，各数字之间用空格分隔。

Sample Input 2  示例输入 2 复制
Copy  副本
30 20
3 22 11
8 30 10
12 14 7
2 17 4
1 19 12
7 30 15
11 23 2
14 25 17
9 12 7
10 16 7
16 18 19
1 11 14
11 15 4
1 21 6
4 8 10
23 24 11
8 27 10
1 19 12
23 23 16
13 24 12
Sample Output 2  样本输出 2Copy
Copy  副本
3 4 5 6 6 6 7 7 8 8 9 8 8 9 9 10 9 8 7 7 7 6 7 5 3 2 2 2 2 2
"""

import sys
from collections import defaultdict

input = sys.stdin.buffer.readline

n, q = map(int, input().split())

groups = defaultdict(list)
for _ in range(q):
    l, r, x = map(int, input().split())
    groups[x].append((l, r))

# 第一步：分别合并每个 X 对应的区间
merged = []
for intervals in groups.values():
    intervals.sort()
    left, right = intervals[0]
    for l, r in intervals[1:]:
        if l <= right + 1:
            right = max(right, r)
        else:
            merged.append((left, right))
            left, right = l, r
    merged.append((left, right))

# 第二步：对合并后的区间做差分
diff = [0] * (n + 2)

for l, r in merged:
    diff[l] += 1
    diff[r + 1] -= 1

# 第三步：求前缀和，得到答案
ans = []
current = 0

for i in range(1, n + 1):
    current += diff[i]
    ans.append(current)

print(*ans)