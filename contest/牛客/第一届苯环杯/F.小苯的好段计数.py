""" 【问题描述】
小苯有一个长度为 n 的排列 a1, a2, . . . , an。
小苯定义排列的一个“好段”为：这个连续子段的长度，恰好等于该子段内元素的
最大值。
例如，子段 {2, 1, 3} 是一个好段，因为它的长度为 3，子段中的最大值也为 3。
你的任务就是求出排列 a 中有多少个连续子段是“好段”。
【输入格式】
每个测试文件包含多组测试数据。第一行输入一个整数 T (1 ≤ T ≤ 104
)，表示测
试数据组数。
对于每组数据：
• 第一行输入一个整数 n (1 ≤ n ≤ 2 × 105
)，表示排列的长度。
• 第二行输入 n 个整数 a1, a2, . . . , an (1 ≤ ai ≤ n)，表示排列 a。保证输入是一个排
列。
保证所有测试数据中 n 的总和不超过 2 × 105。
【输出格式】
对于每组数据，输出一行一个整数，表示好段的数量。
【样例输入】
2
5
1 2 3 4 5
6
2 1 3 4 5 6
【样例输出】
5
6
试题 F: 好段计数 10
“苯环杯”蓝桥杯大赛软件赛省赛模拟赛 2026 年 3 月 29 日
【样例说明】
对于第一组数据，恰好有 5 个好段，分别是前缀 {1}, {1, 2}, {1, 2, 3}, {1, 2, 3, 4}, {1, 2, 3, 4, 5}。
对于第二组数据，恰好有 6 个好段，分别是 {1}（即位置 2 的单点段）以及前缀
{2, 1}, {2, 1, 3}, {2, 1, 3, 4}, {2, 1, 3, 4, 5}, {2, 1, 3, 4, 5, 6}。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
def solution1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(read())
        ans = 0
        for r in range(n):
            for l in range(r+1):
                if(max(arr[l:r+1]) == r - l + 1):
                    ans += 1
        print(ans)

def solution2():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        pos = [0] * (n + 1)
        for i, x in enumerate(arr):
            pos[x] = i

        left, right = n, -1
        ans = 0

        for k in range(1, n + 1):
            left = min(left, pos[k])
            right = max(right, pos[k])

            if right - left + 1 == k:
                ans += 1

        print(ans)
solution2()