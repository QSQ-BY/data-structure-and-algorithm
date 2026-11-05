""" There are n
 nuclear cores arranged in a line, numbered from 1
 to n
 from left to right. The i
-th core has an initial mass of ai
.
有一些核核心沿直线排列，从左到右依次编号为 到 再到 n
 。第 和 i
 个核核心的初始质量分别为 到 ai
 。

In one operation, you can choose a core i
 (1≤i≤k
, where k
 is the current number of cores) such that its mass ai≥2
. You then split it into two positive integer parts x
 and y
 such that x≥1
, y≥1
, and x+y=ai
.
在一次操作中，你可以选择一个核心 i
 ( 1≤i≤k
 )，其中 k
 是当前可用的核心数量。然后将其拆分为两个正整数部分 x
 和 y
 ，使得 x≥1
 、 y≥1
 以及 x+y=ai
 分别对应于这两个部分。

After splitting, the i
-th core is removed from the sequence, decreasing the total number of cores by 1
. The mass x
 is added to the left neighbor of the removed core, if it exists. The mass y
 is added to the right neighbor of the removed core, if it exists. If a neighbor does not exist, the corresponding mass is lost to the environment.
在分割之后，序列中的第 i
 个核心会被移除，从而导致总核心数减少 1
 个。如果移除的核心有左邻居，那么质量 x
 会被添加到该邻居节点上；如果移除的核心有右邻居，那么质量 y
 会被添加到该邻居节点上。如果移除的核心没有邻居节点，那么相应的质量就会释放到环境中。

The sequence immediately shifts to close the gap. The process stops when no further operations can be performed.
该序列立即转向关闭间隙的操作。当无法再进行任何操作时，这个过程就会停止。

Determine whether it is possible to end the process with exactly one core remaining. If it is possible, find the maximum possible mass of this single final core.
确定是否有可能在只剩下一个核心的情况下结束该过程。如果可能，请找出这个唯一剩余核心的最大质量。

Input  输入
The first line of the input contains a single integer t
 (1≤t≤104
) — the number of test cases. The description of each test case follows.
输入文件的第一行包含一个整数 t
 ( 1≤t≤104
 )，表示测试用例的数量。每个测试用例的描述会在下一行中给出。

The first line of each test case contains a single integer n
 (2≤n≤2⋅105
) — the initial number of nuclear cores.
每个测试案例的第一行包含一个整数 n
 ( 2≤n≤2⋅105
 )——即初始的核数。

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤1000
) — the initial masses of the cores.
每个测试案例的第二行包含 n
 整数 a1,a2,…,an
 （ 1≤ai≤1000
 ）——这些就是核心的初始质量。

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.
保证所有测试用例中 n
 的和不超过 2⋅105
 。

Output  输出结果
For each test case, print a single integer — the maximum possible mass of the final remaining core. If it is impossible to end up with exactly one core, print −1
 instead.
对于每个测试案例，请输出一个整数——表示最终剩余的核心的最大可能质量。如果无法恰好只剩下一个核心，则输出 −1
 instead。

Example  示例
Input  输入Copy  副本
3
4
1 2 3 4
5
1 1 1 1 1
2
6 7
Output  输出结果Copy  副本
9
-1
12
Note  注意/备注
Consider the first test case. The initial sequence is [1,2,3,4]
. An optimal sequence of operations is:
考虑第一个测试案例。初始序列为 [1,2,3,4]
 。最优的操作序列为：

Split the 2
 into x=1
, y=1
: the sequence becomes [1+1,3+1,4]=[2,4,4]
.
将 2
 分割为 x=1
 以及 y=1
 ：这样之后序列就变成了 [1+1,3+1,4]=[2,4,4]
 。
Split the first 4
 into x=1
, y=3
: the sequence becomes [2+1,4+3]=[3,7]
.
将第一个 4
 拆分为 x=1
 和 y=3
 两部分，这样整个序列就变成了 [2+1,4+3]=[3,7]
 。
Split the 3
 into x=1,y=2
. The 1
 is permanently lost to the left, and the 2
 is added to the right core. The final sequence is [7+2]=[9]
.
将 3
 分割为 x=1,y=2
 。 1
 永久性地丢失到了左侧，而 2
 则被添加到了右侧的核心中。最终的序列为 [7+2]=[9]
 。
Now, exactly one core is left, and it has a mass of 9
. It can be shown that this is the maximum possible.
现在，只剩下恰好一个核心了，其质量为 9
 。可以证明这是所能达到的最大质量了。

For the second test case, no operation can be performed, and thus, it is impossible to end up with a single core remaining. Hence, output −1
.
对于第二个测试案例，无法执行任何操作，因此不可能有单个核心剩余。所以，输出结果为 −1
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int, input().split())
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(read())
    if all(number == 1 for number in arr):
        print(-1)
        continue
    if all(number == 1 for number in arr[1:n-1]):
        print(arr[0] + arr[-1] - 1)
        continue
    print(sum(arr) - 1)
