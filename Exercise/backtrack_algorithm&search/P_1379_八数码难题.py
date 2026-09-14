""" 题目描述
在 3×3 的棋盘上，摆有八个棋子，每个棋子上标有 1 至 8 的某一数字。棋盘中留有一个空格，空格用 0 来表示。空格周围的棋子可以移到空格中。要求解的问题是：给出一种初始布局（初始状态）和目标布局（为了使题目简单，设目标状态为 123804765），找到一种最少步骤的移动方法，实现从初始布局到目标布局的转变。

输入格式
输入初始状态，一行九个数字，空格用 0 表示。

输出格式
只有一行，该行只有一个数字，表示从初始状态到目标状态需要的最少移动次数。保证测试数据中无特殊无法到达目标状态数据。

输入输出样例
输入 #1复制

283104765
输出 #1复制

4
说明/提示
样例解释


图中展示了样例当中从初始状态到目标状态的一种方案，共需要 4 步。

并且可以证明，不存在更优的策略。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline

init = input().decode().strip()
target = "123804765"
#棋盘上每一个位置的相邻位置
neighbors = [
    (1, 3),        # 位置 0
    (0, 2, 4),     # 位置 1
    (1, 5),        # 位置 2
    (0, 4, 6),     # 位置 3
    (1, 3, 5, 7),  # 位置 4
    (2, 4, 8),     # 位置 5
    (3, 7),        # 位置 6
    (4, 6, 8),     # 位置 7
    (5, 7),        # 位置 8
]
index = -1
for i in range(9):
    if(init[i] == "0"):
        index = i
q = deque()
q.append((init,index,0))
seen = set()
seen.add(init)
while q:
    (cur_state , pos,step) = q.popleft()
    if cur_state == target:
        print(step)
        sys.exit()
    for next_pos in neighbors[pos]:
        next = []
        for i in range(9):
            if(i == pos):
                next.append(cur_state[next_pos])
            elif(i == next_pos):
                next.append(cur_state[pos])
            else:
                next.append(cur_state[i])
        next = "".join(next)
        if(next in seen):
            continue
        seen.add(next)
        if(next == target):
            print(step+1)
            sys.exit()
        q.append((next,next_pos,step+1))
print(-1)
