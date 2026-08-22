""" Problem Statement  问题描述
There is a grid with
H rows and
W columns. Each cell is an empty cell or a bomb cell. Let
(i,j) denote the cell at the
i-th row from the top and the
j-th column from the left. The grid is given by
H length-
W strings
S
1
​
 ,S
2
​
 ,…,S
H
​
 : if the
j-th character of
S
i
​
  is .,
(i,j) is an empty cell, and if the
j-th character of
S
i
​
  is #,
(i,j) is a bomb cell.
该网格有
H 行和
W 列。每个单元格要么是空单元格，要么是炸弹单元格。用
(i,j) 表示从上往下数第
i 行、从左往右数第
j 列的单元格。该网格由
H 个长度为
W 的字符串
S
1
​
 ,S
2
​
 ,…,S
H
​
  来描述：如果
S
i
​
  中的第
j 个字符是 . ，则
(i,j) 是空单元格；如果
S
i
​
  中的第
j 个字符是 # ，则
(i,j) 是炸弹单元格。

For an empty cell
(i,j), if there is no bomb cell in the
i-th row nor in the
j-th column, that cell is called a safe empty cell.
对于一个空的单元格
(i,j) 来说，如果第
i 行和第
j 列中都没有炸弹单元格，那么这个单元格就被称为“安全空单元格”。

In one move, you can move from the current cell to an adjacent empty cell in the up, down, left, or right direction (you cannot move to a bomb cell). Find the number of empty cells
(i,j) satisfying the following condition:
只需一步移动，就可以从当前单元格向上、下、左或右方向移动到相邻的空白单元格中（不能移动到有炸弹的单元格上）。请找出满足以下条件的空白单元格的数量：

A safe empty cell can be reached from
(i,j) in at most
K moves.
从
(i,j) 出发，最多只需
K 步即可到达一个为空的安全格子。
Constraints  约束
1≤H,W≤5×10
5

H×W≤5×10
5

0≤K≤H×W−1
S
i
​
  is a string of length
W consisting of . and #.
S
i
​
  是一串长度为
W 的字符串，由 . 和 # 组成。
H,
W, and
K are integers.
H 、
W 和
K 都是整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

H
W
K
S
1
​

S
2
​

⋮
S
H
​

Output  输出结果
Output the number of empty cells satisfying the condition.
输出满足该条件的空单元格的数量。

Sample Input 1  示例输入 1 复制
Copy  副本
3 3 1
#..
...
..#
Sample Output 1  示例输出 1 复制
Copy  副本
5
The only safe empty cell is
(2,2). There are five empty cells from which you can reach
(2,2) in at most one move:
(1,2),(2,1),(2,2),(2,3),(3,2), so the answer is
5.
唯一安全的空格位置是
(2,2) 。有五个空格位置，从这些位置出发，最多只需一步就能到达
(2,2) ：它们分别是
(1,2),(2,1),(2,2),(2,3),(3,2) 。因此，答案是
5 。

Sample Input 2  示例输入 2 复制
Copy  副本
2 3 0
...
...
Sample Output 2  示例输出 2 复制
Copy  副本
6
Since there is no bomb cell, all six cells are safe empty cells. Therefore, every empty cell satisfies the condition with zero moves.
由于没有炸弹单元格，所有六个单元格都是安全的空单元格。因此，每个空单元格都符合“零步移动”的条件。

Sample Input 3  示例输入 3 复制
Copy  副本
5 7 2
..#....
..#....
.......
...#...
...#...
Sample Output 3  示例输出 3 复制
Copy  副本
29 """
import sys
input = sys.stdin.readline
from collections import deque
def read():
    return map(int,sys.stdin.buffer.readline().split())

n,m,k = read()
g = [["*"]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    g[i] = ["*"] + list(input().strip()) + ["*"]

safe_row = [1]*(n+1)
safe_column = [1]*(m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        if(g[i][j] == "."):
            continue
        safe_row[i] = 0
        safe_column[j] = 0

#-1表示这个各自还没有被访问，0表示本身就是安全格，d表示距离最近的安全格子要几步
dist = [[-1] * (m + 2) for _ in range(n + 2)]
q = deque()

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if safe_row[i]==1 and safe_column[j]==1:
            dist[i][j] = 0
            q.append((i, j))
ans = len(q)
directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
)
while q:
    x, y = q.popleft()
    if dist[x][y] >= k:
        continue
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
        if g[next_x][next_y] != ".":
            continue
        if dist[next_x][next_y] != -1:
            continue
        dist[next_x][next_y] = dist[x][y] + 1
        ans += 1
        q.append((next_x, next_y))

print(ans)