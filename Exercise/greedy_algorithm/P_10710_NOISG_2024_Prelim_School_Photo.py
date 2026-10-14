""" 题目描述
Zane 是 NOI 学校的校长。NOI 学校有 n 个班，每个班有 s 名同学。第 i 个班中的第 j 名同学的身高是 a 
i,j
​
 。

现在 Zane 想从每个班上选出一名同学拍照，使得这 n 名同学中最高的同学和最低的同学的身高差最小。

请你输出这个最小值。

输入格式
第一行，两个整数 n,s；

接下来 n 行，每行 s 个整数，表示 a。

输出格式
一行一个整数表示答案。

输入输出样例
输入 #1复制

2 3
2 1 8
5 4 7
输出 #1复制

1
输入 #2复制

3 3
3 1 4
2 7 18
9 8 10
输出 #2复制

4
说明/提示
【样例 #2 解释】
选择 a 
1,3
​
 ,a 
2,2
​
 ,a 
3,2
​
 ，答案为 8−4=4。

【数据范围】
Subtask	分值	特殊性质
0	0	样例
1	11	n=2
2	22	n,s≤100
3	9	n,s≤250
4	33	n,s≤500
5	25	无
对于 100% 的数据，1≤n,s≤1000,1≤a 
i,j
​
 ≤10 
9
 。 """
import sys
from heapq import heapify, heapreplace
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,s = read()
students = [[0]*(s)for _ in range(n)]
for i in range(n):
    students[i] = sorted(list(read()))

from heapq import heapify, heappop, heappush

# 堆中保存：(身高，班级编号，班内下标)
heap = [(students[i][0], i, 0) for i in range(n)]
heapify(heap)

cur_max = max(students[i][0] for i in range(n))
ans = cur_max - heap[0][0]

while heap:
    height, i, j = heap[0]  # 先读取，不弹出

    diff = cur_max - height
    if diff < ans:
        ans = diff
    if ans == 0:
        break

    if j + 1 == s:
        break

    next_height = students[i][j + 1]
    if next_height > cur_max:
        cur_max = next_height
    heapreplace(heap, (next_height, i, j + 1))

print(ans)
