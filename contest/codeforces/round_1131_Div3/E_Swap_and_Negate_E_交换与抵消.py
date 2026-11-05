""" E. Swap and Negate  E. 交换与抵消
time limit per test2 seconds
每个测试用例的时间限制：2 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
You are given an array a
 of length n
.
你得到了一个长度为 n
 的数组 a
 。

You are allowed to perform the following operation on the array a
 any number of times (including zero):
您可以多次对数组 a
 执行以下操作（包括零次）：

Choose an index i
 such that 1≤i<n
;
请选择一个索引 i
 ，使得 1≤i<n
 符合该索引的条件；
Set ai:=−ai+1
 and ai+1:=−ai
 simultaneously.
同时设置 、 ai:=−ai+1
 以及 和 ai+1:=−ai
 。
Determine the maximum possible sum of all elements in the array that can be achieved by performing the operations optimally.
确定通过最优操作能够实现数组中所有元素的最大可能总和。

Input  输入
The first line of the input contains a single integer t
 (1≤t≤104
) — the number of test cases. The description of each test case follows.
输入文件的第一行包含一个整数 t
 ( 1≤t≤104
 )，表示测试用例的数量。每个测试用例的描述会在下一行中给出。

The first line of each test case contains a single integer n
 (1≤n≤2⋅105
) — the length of the array a
.
每个测试案例的第一行包含一个整数 n
 ( 1≤n≤2⋅105
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
 over all test cases does not exceed 2⋅105
.
保证所有测试用例中 n
 的和不超过 2⋅105
 。

Output  输出结果
For each test case, print a single integer — the maximum possible sum of the array elements after performing the operations any number of times.
对于每个测试案例，请输出一个整数——即在不进行任何操作的情况下，数组元素之和所能达到的最大值。

Example  示例
Input  输入Copy  副本
4
1
-3
4
1 -2 -3 4
5
-10 1 0 1 -10
2
6 -7
Output  输出结果Copy  副本
-3
10
18
1
Note  注意/备注
For the first test case, no operation can be performed. Hence, the maximum sum will be equal to −3
.
对于第一个测试案例，无法执行任何操作。因此，最大总和将等于 −3
 。

For the second test case, choosing i=2
 makes the array a=[1,3,2,4]
. Now, the sum of all the elements is equal to 10
. It can be shown that this is the maximum possible.
对于第二个测试案例，选择 i=2
 后，数组变为 a=[1,3,2,4]
 。此时，所有元素的总和等于 10
 。可以证明这是最大可能的总和。
 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int, input().split())
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(read())
    for i in range(n):
        if i % 2 == 1:
            arr[i] = -arr[i]
    arr.sort()
    mid = n // 2
    ans = sum(arr[mid:]) - sum(arr[:mid])
    print(ans)
