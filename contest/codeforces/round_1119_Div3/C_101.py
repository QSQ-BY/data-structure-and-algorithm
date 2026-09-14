""" C. 101
time limit per test2 seconds
每个测试用例的时间限制：2 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
The score of an array b
 of length m
 is defined as the maximum length of a subarray of b
 such that the first and last elements of the subarray are equal to 1
 and all other elements in the subarray are equal to 0
. Formally, the score of b
 is equal to the maximum integer k
 for which there exists an index i
 such that:
长度为 m
 的数组 b
 的“得分”是指：在该数组中，存在一个最长的子数组，该子数组的第一个元素和最后一个元素都等于 1
 ，而子数组中的其他所有元素都等于 0
 。换句话说， b
 的得分，就是最大的整数 k
 ，使得存在某个索引 i
 ，使得上述条件成立。

1≤i≤m−k+1
bi=bi+k−1=1
bi+1=bi+2=…=bi+k−2=0
If there is no subarray meeting the requirements, the score of b
 is 0
.
如果没有满足条件的子数组，那么 b
 的得分为 0
 。

You are given an array a1,a2,…,an
, such that each element is equal to one of −1
, 0
, or 1
. Replace each −1
 with either a 0
 or 1
 such that the score of a
 is maximal over all possible ways to replace the −1
s in a
.
给定一个数组 a1,a2,…,an
 ，其中每个元素的值都来自 −1
 、 0
 或 1
 这几种可能。需要将每个 −1
 替换为 0
 或 1
 中的某一种，使得在 a
 中所有可能的替换方式中， a
 的得分尽可能高。

Input  输入
The first line of each input contains t
 (1≤t≤104
) — the number of test cases.
每个输入的第一行包含 t
 ( 1≤t≤104
 )——即测试用例的数量。

The first line of each test case contains n
 (1≤n≤2⋅105
) — the length of a
.
每个测试用例的第一行包含 n
 （ 1≤n≤2⋅105
 ），即 a
 的长度。

The second line of each test case contains a1,a2,…,an
 (ai∈{−1,0,1}
) — the array a
.
每个测试案例的第二行包含 a1,a2,…,an
 ( ai∈{−1,0,1}
 )——即数组 a
 。

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.
保证所有测试用例中 n
 的和不超过 2⋅105
 。

Output  输出结果
For each test case, output n
 space separated integers representing a
 after the −1
s were replaced with 0
s or 1
s. If there are multiple possible solutions, output any.
对于每个测试用例，输出用空格分隔的整数，这些整数分别代表在将所有的 −1
 替换为 0
 或 1
 之后得到的 a
 的值。如果存在多种可能的解决方案，则输出其中任意一种即可。

Example  示例
Input  输入Copy  副本
10
6
1 0 -1 0 0 1
7
0 -1 0 0 1 0 1
5
-1 0 0 -1 0
4
0 0 0 0
1
-1
6
1 0 1 0 0 -1
7
0 1 0 0 0 1 0
6
-1 -1 -1 -1 -1 -1
7
-1 0 1 -1 0 0 1
3
-1 0 0
Output  输出结果Copy  副本
1 0 0 0 0 1
0 1 0 0 1 0 1
1 0 0 1 0
0 0 0 0
1
1 0 1 0 0 1
0 1 0 0 0 1 0
1 0 0 0 0 1
0 0 1 0 0 0 1
1 0 0
Note  注意
In the first test case, we can change the only −1
 to a 0
, making a=[1,0,0,0,0,1]
. Since the first and last elements of a
 are equal to 1
, and all other elements are 0
, the score of a
 is 6
.
在第一个测试案例中，我们可以将唯一的 −1
 替换为 0
 ，这样就变成了 a=[1,0,0,0,0,1]
 。由于 a
 的第一个和最后一个元素都等于 1
 ，而其他所有元素都是 0
 ，因此 a
 的得分就是 6
 。

In the third test case, changing both −1
s to 1
s makes a=[1,0,0,1,0]
, and the largest subarray that satisfies the conditions in the statement is from the 1
-st index to the 4
-th index.
在第三个测试案例中，将 和 −1
 都替换为 和 1
 后，得到的结果是 和 a=[1,0,0,1,0]
 。而满足题目要求的最大子数组，是从第 个索引到第 个索引的这段子数组。

In the fifth test case, we set the only −1
 to 1
, making a=[1]
, meaning the largest subarray that satisfies the conditions in the statement is the full array.
在第五个测试案例中，我们将唯一的 −1
 设置为 1
 ，这样就得到了 a=[1]
 。这意味着，满足该条件条件的最大子数组，其实就是整个数组本身。 """

import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())

def solve():
    n = int(input())
    arr = list(read())
    l = -1
    best_l = best_r = -1
    best_len = 0
    for r in range(n):
        if arr[r] == 0:
            continue
        # 第一次遇到能作为端点的位置
        if l == -1:
            l = r
        # 将当前位置作为右端点
        if r - l + 1 > best_len:
            best_len = r - l + 1
            best_l, best_r = l, r
        # 固定的 1 不能成为后续区间的内部元素
        if arr[r] == 1:
            l = r

    # 先把所有待定位置填成 0
    for i in range(n):
        if arr[i] == -1:
            arr[i] = 0
    # 再设置最佳区间的端点
    if best_len > 0:
        arr[best_l] = arr[best_r] = 1
    print(*arr)

def main():
    t = int(input())
    while t:
        t-=1
        solve()

if __name__ == "__main__":
    main()