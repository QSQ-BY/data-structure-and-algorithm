""" 题目描述
小明需要在一条 2×n 的河床上铺设水质检测器。在他铺设之前，河床上已经存在一些检测器。如果两个检测器上下或者左右相邻，那么这两个检测器就是互相连通的。连通具有传递性，即如果 A 和 B 连通，B 和 C 连通，那么 A 和 C 也连通。现在他需要在河床上增加铺设一些检测器使得所有的检测器都互相连通。他想知道最少需要增加铺设多少个检测器？

输入格式
输入共两行，表示一个 2×n 的河床。

每行一个长度为 n 的字符串，仅包含 # 和 .，其中 # 表示已经存在的检测器，. 表示空白。

输出格式
输出共 1 行，一个整数表示答案。

输入输出样例
输入 #1复制

.##.....#
.#.#.#...
输出 #1复制

5
说明/提示
样例说明
其中一种方案：

.###....#
.#.######

增加了 5 个检测器。

评测用例规模与约定
对于 100% 的评测用例，保证 n≤1000000。 """
import sys

input = sys.stdin.readline
def solve():
    top = list(input().strip())
    bottom = list(input().strip())
    n = len(top)
    left = n
    right = -1
    for column in range(n):
        if top[column] == "#" or bottom[column] == "#":
            left = min(left, column)
            right = column

    if right == -1:
        print(0)
        return

    inf = 2 * n + 1
    top = top[left:right+1]
    bottom = bottom[left:right+1]
    n = len(top)
    # 当前列最终只选上格、只选下格、上下都选时的最小新增数量。
    dp_top = 0 if bottom[0] == "." else inf
    dp_bottom = 0 if top[0] == "." else inf
    dp_both = (top[0] == ".") + (bottom[0] == ".")

    for i in range(1, n):
        top_cost = top[i] == "."
        bottom_cost = bottom[i] == "."

        next_top = min(dp_top, dp_both) + top_cost if bottom[i] == "." else inf
        next_bottom = min(dp_bottom, dp_both) + bottom_cost if top[i] == "." else inf
        next_both = min(dp_top, dp_bottom, dp_both) + top_cost + bottom_cost

        dp_top, dp_bottom, dp_both = next_top, next_bottom, next_both

    print(min(dp_top, dp_bottom, dp_both))

solve()
