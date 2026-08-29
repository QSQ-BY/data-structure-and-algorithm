""" 题目描述
小明是学校里的一名老师，他带的班级共有 n 名同学，第 i 名同学力量值为 a 
i
​
 。在闲暇之余，小明决定在班级里组织一场拔河比赛。

为了保证比赛的双方实力尽可能相近，需要在这 n 名同学中挑选出两个队伍，队伍内的同学编号连续 {a 
l 
1
​
 
​
 ,a 
l 
1
​
 +1
​
 ,…,a 
r 
1
​
 −1
​
 ,a 
r 
1
​
 
​
 } 和 {a 
l 
2
​
 
​
 ,a 
l 
2
​
 +1
​
 ,…,a 
r 
2
​
 −1
​
 ,a 
r 
2
​
 
​
 }，其中 l 
1
​
 ≤r 
1
​
 <l 
2
​
 ≤r 
2
​
 。

两个队伍的人数不必相同，但是需要让队伍内的同学们的力量值之和尽可能相近。请计算出力量值之和差距最小的挑选队伍的方式。

输入格式
输入共两行。 第一行为一个正整数 n。
第二行为 n 个正整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 。

输出格式
输出共一行，一个非负整数，表示两个队伍力量值之和的最小差距。

输入输出样例
输入 #1复制

5
10 9 8 12 14
输出 #1复制

1
说明/提示
样例 1 解释
其中一种最优选择方式：

队伍 1：{a 
1
​
 ,a 
2
​
 ,a 
3
​
 }，队伍 2：{a 
4
​
 ,a 
5
​
 }，力量值和分别为 10+9+8=27，12+14=26，差距为 ∣27−26∣=1。

数据规模与约定
对 20% 的数据，n≤50。
对全部的测试数据，保证 2≤n≤10 
3
 ，1≤a 
i
​
 ≤10 
9
 。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # 生成所有连续子数组：(区间和, 左端点, 右端点)
    intervals = []
    for left in range(n):
        total = 0
        for right in range(left, n):
            total += arr[right]
            intervals.append((total, left, right))
    # 按区间和从小到大排序
    intervals.sort()

    # 维护当前窗口中最小的右端点
    min_right = deque()

    # 维护当前窗口中最大的左端点
    max_left = deque()

    window_left = 0
    answer = float("inf")

    for window_right, (_, left, right) in enumerate(intervals):

        # 单调递增：队首是最小右端点
        while min_right and intervals[min_right[-1]][2] >= right:
            min_right.pop()

        min_right.append(window_right)

        # 单调递减：队首是最大左端点
        while max_left and intervals[max_left[-1]][1] <= left:
            max_left.pop()

        max_left.append(window_right)

        # 最小右端点 < 最大左端点
        # 说明窗口中存在两个互不相交的区间
        while intervals[min_right[0]][2] < intervals[max_left[0]][1]:
            current_difference = (
                intervals[window_right][0]
                - intervals[window_left][0]
            )

            answer = min(answer, current_difference)

            if answer == 0:
                print(0)
                return

            # 从窗口中移除 window_left
            if min_right[0] == window_left:
                min_right.popleft()

            if max_left[0] == window_left:
                max_left.popleft()

            window_left += 1

    print(answer)


solve()
