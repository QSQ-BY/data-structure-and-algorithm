""" D. Lock and Unlock  D. 锁定与解锁
time limit per test2 seconds
每个测试用例的时间限制：2 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
You are given an integer array [a1,a2,…,an]
. Initially, all the elements are unlocked.
你得到一个整数数组 [a1,a2,…,an]
 。最初，数组中的所有元素都是未锁定的。

You may perform the following operation on array a
 any number of times (possibly zero):
您可以多次对数组 a
 执行以下操作（次数可以为 0 次）：

Choose an integer k
 (1≤k≤n
) and choose exactly k
 distinct indices. The elements at these indices are locked for the current operation. This step incurs a cost equal to k
.
请选择一個整數 k
 ( 1≤k≤n
 )，并选择恰好 k
 个不同的索引位置。这些索引位置上的元素将被锁定，用于当前的操作。这一步的成本为 k
 。

Choose one of the following two actions:
选择以下两个操作中的一个：

Increase every unlocked element by 1
;
每个解锁元素的值增加 1
 ；
Decrease every unlocked element by 1
.
每解锁一个元素， 1
 的值就会减少。
This step does not incur any additional cost.
这一步不会产生任何额外的费用。

Unlock all the elements. This step does not incur any additional cost.
解锁所有元素。这一步骤不会产生任何额外成本。
The total cost is equal to the sum of the individual costs over all the operations performed.
总成本等于所有操作中所产生的各个单独成本的总和。

Determine the minimum possible total cost to make all the elements of the array a
 equal. Furthermore, among all the ways to achieve this minimum possible total cost, find the minimum number of operations required.
确定使数组 a
 中所有元素达到相等的最小总成本。此外，在所有能够达到这一最小总成本的方法中，找出所需操作次数最少的方案。

Input  输入
The first line of the input contains a single integer t
 (1≤t≤2⋅104
) — the number of test cases. The description of each test case follows.
输入文件的第一行包含一个整数 t
 ( 1≤t≤2⋅104
 )，表示测试用例的数量。每个测试用例的描述会在下一行中给出。

The first line of each test case contains a single integer n
 (2≤n≤2⋅105
) — the length of the array a
.
每个测试案例的第一行包含一个整数 n
 ( 2≤n≤2⋅105
 )，表示数组的长度 a
 。

The second line of each test case contains n
 integers a1,a2,…,an
 (−109≤ai≤109
) — the elements of the array a
.
每个测试案例的第二行包含 n
 的整数 a1,a2,…,an
 （ −109≤ai≤109
 ）——这些就是数组 a
 中的元素。

It is guaranteed that the sum of n
 over all the test cases does not exceed 2⋅105
.
可以肯定的是，在所有测试用例中， n
 的总和不会超过 2⋅105
 。

Output  输出结果
For each test case, print two space-separated integers on a new line — the minimum possible total cost to make all the elements equal, and the minimum number of operations required to make all the elements equal with the minimum possible total cost.
对于每个测试案例，请在新行中输出两个以空格分隔的整数——第一个表示使所有元素相等时的最小总成本；第二个表示以最小总成本使所有元素相等所需的最小操作次数。

Example  示例
Input  输入Copy  副本
5
3
1 2 3
2
-1 -1
4
18 -2 9 11
9
9 9 8 2 4 4 3 5 3
3
6 67 7
Output  输出结果Copy  副本
2 2
0 0
22 20
19 7
61 61
Note  注意/备注
In the first test case, the following sequence of operations is optimal:
在第一个测试案例中，以下这一系列操作是最优的：

Lock the first element and decrease all unlocked elements by 1
. The array changes from [1,2,3]
 to [1,1,2]
. The cost of this operation is 1
.
锁定第一个元素，并将所有未锁定的元素数量减少 1
 个。数组中的元素数量将从 [1,2,3]
 个变为 [1,1,2]
 个。这个操作的成本为 1
 。

Lock the third element and increase all unlocked elements by 1
. The array changes from [1,1,2]
 to [2,2,2]
. The cost of this operation is 1
.
锁定第三个元素，并将所有未锁定的元素数量增加 1
 。数组中的元素位置将从 [1,1,2]
 变为 [2,2,2]
 。这个操作的成本为 1
 。
The total cost is 1+1=2
, and exactly 2
 operations are performed. It is impossible to make all elements equal with a smaller total cost.
总成本为 1+1=2
 ，实际上共执行了 2
 次操作。以更低的总成本来实现所有元素相等是不可能的。

In the second test case, all elements are already equal, so the minimum total cost and the minimum number of operations are both 0
.
在第二个测试案例中，所有元素的值都是相同的，因此最小总成本和最少的操作次数都是 0
 。 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(read())
    arr.sort()
    ans2 = arr[-1] - arr[0]
    intervals = [[arr[0], 1]]
    for i in range(1, n):
        number = arr[i]
        if intervals[-1][0] == number:
            intervals[-1][1] += 1
        else:
            intervals.append([number, 1])
    ans1 = 0
    index = 0
    m = len(intervals)
    for i in range(m - 1):
        number, cnt = intervals[i]
        diff = intervals[i+1][0] - number
        index += cnt
        ans1 += diff * min(index, n-index)
    print(ans1, ans2)

def solution2():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = sorted(map(int, input().split()))
        ans1 = 0
        for i in range(n - 1):
            ans1 += (arr[i+1] - arr[i]) * min(i+1, n-i-1)
        ans2 = arr[-1] - arr[0]
        print(ans1, ans2)