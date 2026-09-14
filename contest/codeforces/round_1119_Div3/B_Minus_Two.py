""" B. Minus Two  B. 减二
time limit per test2 seconds
每个测试用例的时间限制：2 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
You are given an array a1,a2,…,an
. You may perform the following operation:
给你一个数组 a1,a2,…,an
 。你可以执行以下操作：

For all indices i
 (1≤i≤n
), set ai=|ai−2|
.
对于所有的指标 i
 （ 1≤i≤n
 ），请设置 ai=|ai−2|
 的值。
Find the maximum possible frequency of any integer in a
 after performing the operation an arbitrary number (possibly zero) of times.
在任意次（包括零次）执行该操作之后，找出 a
 中所有整数可能出现的最大频率。

Input  输入
The first line of each input contains an integer t
 (1≤t≤104
) — the number of test cases.
每个输入的第一行包含一个整数 t
 ( 1≤t≤104
 )，表示测试用例的数量。

The first line of each test case contains an integer n
 (1≤n≤2⋅105
) — the length of a
.
每个测试用例的第一行包含一个整数 n
 （ 1≤n≤2⋅105
 ），该整数表示 a
 的长度。

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the array a
.
每个测试案例的第二行包含 、 n
 个整数 、 a1,a2,…,an
 （即 、 1≤ai≤109
 ），这些整数构成了数组 、 a
 。

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.
保证所有测试用例中 n
 的和不超过 2⋅105
 。

Output  输出结果
For each test case, output a single integer denoting the maximum possible frequency of any integer in a
 after performing the operation an arbitrary number of times.
对于每个测试用例，输出一个整数，该整数表示在任意次执行该操作后， a
 中所有整数可能出现的最大频率。

Example  示例
Input  输入Copy  副本
5
2
1 3
4
1 1 1 2
3
6 7 8
4
2 2 2 2
5
1 10 100 1000 100000
Output  输出结果Copy  副本
2
3
1
4
3
Note  注意
In theB. Minus Two  B. 减二
time limit per test2 seconds
每个测试用例的时间限制：2 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
You are given an array a1,a2,…,an
. You may perform the following operation:
给你一个数组 a1,a2,…,an
 。你可以执行以下操作：

For all indices i
 (1≤i≤n
), set ai=|ai−2|
.
对于所有的指标 i
 （ 1≤i≤n
 ），请设置 ai=|ai−2|
 的值。
Find the maximum possible frequency of any integer in a
 after performing the operation an arbitrary number (possibly zero) of times.
在任意次（包括零次）执行该操作之后，找出 a
 中所有整数可能出现的最大频率。

Input  输入
The first line of each input contains an integer t
 (1≤t≤104
) — the number of test cases.
每个输入的第一行包含一个整数 t
 ( 1≤t≤104
 )，表示测试用例的数量。

The first line of each test case contains an integer n
 (1≤n≤2⋅105
) — the length of a
.
每个测试用例的第一行包含一个整数 n
 （ 1≤n≤2⋅105
 ），该整数表示 a
 的长度。

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the array a
.
每个测试案例的第二行包含 、 n
 个整数 、 a1,a2,…,an
 （即 、 1≤ai≤109
 ），这些整数构成了数组 、 a
 。

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.
保证所有测试用例中 n
 的和不超过 2⋅105
 。

Output  输出结果
For each test case, output a single integer denoting the maximum possible frequency of any integer in a
 after performing the operation an arbitrary number of times.
对于每个测试用例，输出一个整数，该整数表示在任意次执行该操作后， a
 中所有整数可能出现的最大频率。

Example  示例
Input  输入Copy  副本
5
2
1 3
4
1 1 1 2
3
6 7 8
4
2 2 2 2
5
1 10 100 1000 100000
Output  输出结果Copy  副本
2
3
1
4
3
Note  注意
In the first test case, we can perform the operation once to have a=[|1−2|,|3−2|]=[1,1]
, which means the maximum possible frequency of any integer in a
 is 2
.
在第一个测试案例中，我们可以执行该操作一次，从而得到 a=[|1−2|,|3−2|]=[1,1]
 的结果。这意味着，在 a
 中，任意整数的最大可能出现频率为 2
 。

In the second test case, the maximum frequency of an integer in a
 is 3
. It can be shown that, no matter how many operations we perform, the maximum possible frequency of an integer in a
 will never exceed 3
.
在第二个测试案例中， a
 中某个整数的最大出现频率为 3
 。可以证明，无论我们进行多少次操作， a
 中某个整数的最大出现频率都不会超过 3
 。 first test case, we can perform the operation once to have a=[|1−2|,|3−2|]=[1,1]
, which means the maximum possible frequency of any integer in a
 is 2
.
在第一个测试案例中，我们可以执行该操作一次，从而得到 a=[|1−2|,|3−2|]=[1,1]
 的结果。这意味着，在 a
 中，任意整数的最大可能出现频率为 2
 。

In the second test case, the maximum frequency of an integer in a
 is 3
. It can be shown that, no matter how many operations we perform, the maximum possible frequency of an integer in a
 will never exceed 3
.
在第二个测试案例中， a
 中某个整数的最大出现频率为 3
 。可以证明，无论我们进行多少次操作， a
 中某个整数的最大出现频率都不会超过 3
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
def solve() -> int:
    n = int(input())
    arr = list(read())
    odd = 0
    even0 = 0
    even2 = 0
    for x in arr:
        if x % 2 == 1:
            odd += 1
        elif x % 4 == 0:
            even0 += 1
        else:
            even2 += 1
    return max(odd, even0, even2)

def main():
    t = int(input())
    ans = []
    while t:
        ans.append(solve())
        t -= 1
    for number in ans:
        print(number)

if __name__ == "__main__":
    main()