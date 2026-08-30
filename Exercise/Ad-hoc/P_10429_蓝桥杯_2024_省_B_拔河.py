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

    # 队头分别是当前窗口中右端点最小、左端点最大的区间下标
    min_right_queue = deque()
    max_left_queue = deque()

    window_left = 0
    answer = float("inf")

    for window_right, (_, left, right) in enumerate(intervals):

        # 右端点递增：队头始终是窗口中的最小右端点
        while (
            min_right_queue
            and intervals[min_right_queue[-1]][2] >= right
        ):
            min_right_queue.pop()
        min_right_queue.append(window_right)

        # 左端点递减：队头始终是窗口中的最大左端点
        while (
            max_left_queue
            and intervals[max_left_queue[-1]][1] <= left
        ):
            max_left_queue.pop()
        max_left_queue.append(window_right)

        # 最小右端点 < 最大左端点
        # 说明窗口中存在两个互不相交的区间
        while (
            intervals[min_right_queue[0]][2]
            < intervals[max_left_queue[0]][1]
        ):
            current_difference = (
                intervals[window_right][0]
                - intervals[window_left][0]
            )

            answer = min(answer, current_difference)

            if answer == 0:
                print(0)
                return

            # 缩小窗口，并删除队头已经过期的区间下标
            window_left += 1

            while min_right_queue[0] < window_left:
                min_right_queue.popleft()

            while max_left_queue[0] < window_left:
                max_left_queue.popleft()

    print(answer)

def solve2():
    n = int(input())
    arr = list(map(int,input().split()))
    intervals = []
    for left_index in range(n):
        total = 0
        for right_index in range(left_index,n):
            total += arr[right_index]
            intervals.append((total,left_index,right_index))
    intervals.sort()#按照区间和大小进行排序

    min_right_index = deque()#最小右边界
    min_left_index = deque()#最大左边界

    answer = float("inf")
    window_left = 0
    for window_right,(total,left,right) in enumerate(intervals):
        #维护最小左边界与最大有边界
        while(len(min_right_index)>0 and intervals[min_right_index[-1]][1] < left):
            min_right_index.pop()
        while(len(min_left_index)>0 and intervals[min_left_index[-1]][2] > right):
            min_left_index.pop()
        min_right_index.append(window_right)
        min_left_index.append(window_right)

        while(intervals[min_right_index[0]][1] > intervals[min_left_index[0]][2]):
            temp_ans = temp_ans = (
                intervals[window_right][0]
                - intervals[window_left][0]
            )
            answer = min(answer,temp_ans)
            if(answer == 0):
                print(0)
                return
            window_left += 1

            while(min_right_index[0] < window_left):
                min_right_index.popleft()
            while(min_left_index[0] < window_left):
                min_left_index.popleft()

    print(answer)


#solve()
solve2()
