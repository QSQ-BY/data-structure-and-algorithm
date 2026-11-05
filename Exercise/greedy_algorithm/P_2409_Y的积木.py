""" 题目背景
Y 是个大建筑师，他总能用最简单的积木拼出最有创意的造型。

题目描述
Y 手上有 n 盒积木，每个积木有个重量。现在他想从每盒积木中拿一块积木，放在一起，这一堆积木的重量为每块积木的重量和。现在他想知道重量和最小的 k 种取法的重量分别是多少。（只要任意更换一块积木，就视为一种不同的取法。如果多种取法重量总和一样，我们需要输出多次。）

输入格式
第一行输入两个整数，n,k，意义如题目所描述。

每组数据接下来的 n 行，第一个整数为 m 
i
​
 ，表示第 i 盒积木的数量，在同一行有 m 
i
​
  个整数，分别表示每个积木的重量。

输出格式
一行，重量最小的 k 种取法的重量，要求对于每个数据，从小到大输出。

输入输出样例
输入 #1复制

3 10
4 1 3 4 5
3 1 7 9
4 1 2 3 5
输出 #1复制

3 4 5 5 6 6 7 7 7 7
说明/提示
数据规模与约定
对于 30% 的数据，2≤m 
i
​
 ≤10，1≤n≤10。
对于 50% 的数据，2≤m 
i
​
 ≤50，1≤n≤50。
对于 100% 的数据，2≤m 
i
​
 ≤100，1≤n≤100，1≤k≤10 
4
 ，每个积木的重量为不超过 100 的正整数，所有 m 
i
​
  的积大于等于 k。
本题不卡常。 """
import sys
import heapq
input = sys.stdin.buffer.readline
n, k = map(int, input().split())
ans = [0]
for _ in range(n):
    data = list(map(int, input().split()))
    arr = sorted(data[1:])

    heap = []

    # 将每一行的第一个元素加入堆
    for i in range(len(ans)):
        heap.append((ans[i] + arr[0], i, 0))
    heapq.heapify(heap)
    new_ans = []
    while heap and len(new_ans) < k:
        #第i行的第j个元素
        total, i, j = heapq.heappop(heap)
        new_ans.append(total)

        # 将当前行的下一个元素加入堆
        if j + 1 < len(arr):
            heapq.heappush(
                heap,
                (ans[i] + arr[j + 1], i, j + 1)
            )
    ans = new_ans
print(*ans)
