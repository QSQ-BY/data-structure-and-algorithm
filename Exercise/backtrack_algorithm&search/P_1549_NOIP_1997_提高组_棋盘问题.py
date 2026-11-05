""" 题目描述
在 N×N（1≤N≤10）的棋盘上，填入 1,2,…,N 
2
  共 N 
2
  个数，使得任意两个相邻的数之和为素数。

例如：当 N=2 时，有：

1	2
4	3
其相邻数的和为素数的有：

1+2,1+4,4+3,2+3

当 N=4 时，一种可以填写的方案如下：

1	2	11	12
16	15	8	5
13	4	9	14
6	7	10	3
在这里我们约定：左上角的格子里必须填数字 1。

输入格式
一个数 N。

输出格式
如有多种解，则输出第一行、第一列之和为最小的排列方案；若无解，则输出 NO。

输入输出样例
输入 #1复制

1
输出 #1复制

NO
输入 #2复制

2
输出 #2复制

1 2
4 3 """
import sys
from copy import deepcopy
input = sys.stdin.buffer.readline
n = int(input())

if n == 1:
    print("NO")
    sys.exit()
size = n * n
limit = 2 * size
# 筛素数
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

g = [[0] * (n + 2) for _ in range(n + 2)]
g[1][1] = 1

# 第 k-1 位代表数字 k 是否还可以使用
initial_mask = (1 << size) - 1

best_score = float("inf")
answer = None


# index：即将填写的格子编号，从 1 开始
# mask：未使用数字的掩码
# score：第一行、第一列已填数字之和，左上角只计一次
def dfs(index, mask, score):
    global best_score, answer

    if score >= best_score:
        return

    if index == size + 1:
        best_score = score
        # 保存副本，防止后续回溯修改答案
        answer = deepcopy(g)
        return

    x = (index - 1) // n + 1
    y = (index - 1) % n + 1

    temp = mask
    while temp:
        low_bit = temp & (-temp)
        temp ^= low_bit
        value = low_bit.bit_length()

        # 检查上方和左方
        if x > 1 and not is_prime[g[x - 1][y] + value]:
            continue
        if y > 1 and not is_prime[g[x][y - 1] + value]:
            continue
        g[x][y] = value

        new_score = score
        if x == 1 or y == 1:
            new_score += value
        dfs(index + 1, mask ^ low_bit, new_score)
        g[x][y] = 0

# 数字 1 已放在左上角，从第二个格子开始搜索
dfs(2, initial_mask ^ 1, 1)
if answer is None:
    print("NO")
else:
    for i in range(1, n + 1):
        print(*answer[i][1:n + 1])