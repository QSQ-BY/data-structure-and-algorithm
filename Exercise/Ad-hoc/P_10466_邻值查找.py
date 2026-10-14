""" 题目描述
给定一个长度为 n 的序列 A，A 中的数各不相同。

对于 A 中的每一个数 A 
i
​
 ，求：

min 
1≤j<i
​
 ∣A 
i
​
 −A 
j
​
 ∣

以及令上式取到最小值的 j（记为 P 
i
​
 ）。若最小值点不唯一，则选择使 A 
j
​
  较小的那个。

输入格式
第一行输入整数 n，代表序列长度。

第二行输入 n 个整数 A 
1
​
 ∼A 
n
​
 ，代表序列的具体数值，数值之间用空格隔开。

输出格式
输出共 n−1 行，每行输出两个整数，数值之间用空格隔开。

分别表示当 i 取 2∼n 时，对应的 min 
1≤j<i
​
 ∣A 
i
​
 −A 
j
​
 ∣ 和 P 
i
​
  的值。

输入输出样例
输入 #1复制

3
1 5 3
输出 #1复制

4 1
2 1
说明/提示
对于 30% 的数据 n≤100。

对于 70% 的数据 n≤10 
4
 。

对于 100% 的数据 n≤10 
5
 ,∣A 
i
​
 ∣≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solution1():
    n = int(input())
    arr = list(read())
    answers = []
    for i in range(1,n):
        cur_ans = float("inf")
        min_index = -1

        for j in range(i):
            diff = abs(arr[i] - arr[j])
            if diff < cur_ans or (diff == cur_ans and arr[j] < arr[min_index]):
                cur_ans = diff
                min_index = j
        answers.append((cur_ans,min_index+1))

    for ans in answers:
        print(*ans)

def solution2():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    arr = data[1:]

    # order[k]：排序后第 k 个元素的原下标
    order = sorted(range(n), key=lambda x:arr[x])

    # pos[i]：原下标 i 对应的排序位置
    pos = [0] * n
    for k, i in enumerate(order):
        pos[i] = k

    # 左右邻居，-1 和 n 表示左边和右边的虚拟空节点
    left = [k - 1 for k in range(n)]
    right = [k + 1 for k in range(n)]

    answers = [None] * n

    for i in range(n - 1, 0, -1):
        k = pos[i]#查找最后一个数字在排序后的顺序的链表的位置
        l, r = left[k], right[k]

        if l == -1:
            j = order[r]
        elif r == n:
            j = order[l]
        elif arr[i] - arr[order[l]] <= arr[order[r]] - arr[i]:
            # 等距离时选左邻居，因为左邻居数值更小
            j = order[l]
        else:
            j = order[r]

        answers[i] = (abs(arr[i] - arr[j]), j + 1)

        # 删除当前元素，让左右邻居直接相连
        if l != -1:
            right[l] = r
        if r != n:
            left[r] = l

    sys.stdout.write(
        "\n".join(f"{diff} {index}" for diff, index in answers[1:])
    )
solution2()