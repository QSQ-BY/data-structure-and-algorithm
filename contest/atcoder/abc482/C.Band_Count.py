""" Problem Statement  问题描述
There is a grid with 
H rows and 
W columns. Let 
(i,j) denote the cell at the 
i-th row from the top and the 
j-th column from the left.
该网格有 
H 行和 
W 列。用 
(i,j) 表示从上往下数第 
i 行、从左往右数第 
j 列的单元格。
There are 
N pieces placed on the grid, and the 
i-th piece is at 
(R 
i
​
 ,C 
i
​
 ).
网格上共有 
N 个棋子，第 
i 个棋子位于 
(R 
i
​
 ,C 
i
​
 ) 位置。
Answer 
Q queries. Each query is of one of the following 
2 types.
回答 
Q 个查询。每个查询都属于以下 
2 种类型中的一种。

1 u d: Print the number of pieces placed in rows 
u through 
d.
1 u d ：打印出从第 
u 行到第 
d 行中，各行所放置的棋子数量。
2 l r: Print the number of pieces placed in columns 
l through 
r.
2 l r ：打印出放置在第 
l 列到第 
r 列中的物品数量。
Constraints  约束
1≤H,W≤10 
9
 
1≤N≤min(H×W,3×10 
5
 )
1≤R 
i
​
 ≤H
1≤C 
i
​
 ≤W
(R 
i
​
 ,C 
i
​
 )

=(R 
j
​
 ,C 
j
​
 ) if 
i

=j.   
(R 
i
​
 ,C 
i
​
 )

=(R 
j
​
 ,C 
j
​
 ) 如果 
i

=j 。
1≤Q≤3×10 
5
 
1≤u≤d≤H
1≤l≤r≤W
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

H 
W 
N 
Q 
R 
1
​
  
C 
1
​
 
R 
2
​
  
C 
2
​
 
⋮
R 
N
​
  
C 
N
​
 
query 
1
​
  
query 
2
​
 
⋮
query 
Q
​
 
Each query 
query 
q
​
  is given in one of the following formats:
每个查询 
query 
q
​
  都采用以下格式之一来表示：

1 
u 
d
2 
l 
r
Output  输出结果
Print 
Q lines. The 
i-th line should contain the answer to the 
i-th query.
打印 
Q 行内容。第 
i 行应包含对第 
i 个查询的回答。

Sample Input 1  示例输入 1 复制
Copy  副本
5 7 5 6
1 1
2 3
2 5
4 3
5 7
1 2 4
2 3 5
1 3 3
2 1 7
1 2 2
2 7 7
Sample Output 1  示例输出 1 复制
Copy  副本
3
3
0
5
2
1
For the 
1-st query, the pieces in rows 
2 through 
4 are the 
2-nd, 
3-rd, and 
4-th pieces, for a total of 
3.
对于第 
1 次查询来说，第 
2 行到第 
4 行中的那些碎片，分别对应第 
2 个、第 
3 个和第 
4 个碎片。总共有 
3 个碎片。

Sample Input 2  示例输入 2 复制
Copy  副本
17 23 12 12
14 8
2 19
17 3
7 11
2 4
10 19
7 8
1 23
14 11
2 23
17 19
7 2
1 2 7
2 9 20
1 3 6
2 8 8
1 11 17
2 1 23
1 1 1
2 20 22
1 7 14
2 3 11
1 15 17
2 19 23
Sample Output 2  示例输出 2 复制
Copy  副本
6
5
0
2
4
12
1
0
6
6
2
5
 """
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.buffer.readline
def read():
    return map(int, input().split())
h, w, n, q = read()
rows = []
cols = []
for _ in range(n):
    x, y = read()
    rows.append(x)
    cols.append(y)
rows.sort()
cols.sort()
ans = []
for _ in range(q):
    op, l, r = read()
    if op == 1:
        #寻找第一个大于等于l的端点下标与第一个严格大于r的端点下标
        cnt = bisect_right(rows, r) - bisect_left(rows, l)
    else:
        cnt = bisect_right(cols, r) - bisect_left(cols, l)

    ans.append(str(cnt))

print('\n'.join(ans))
