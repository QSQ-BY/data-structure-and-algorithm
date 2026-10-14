""" C. Unrequited Love  C. 单恋/无果的爱情
time limit per test2 seconds
每个测试用例的时间限制：2 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
K1o0n reached the stage where, for complete happiness, he only lacked a musical instrument, and bought a synthesizer second-hand. The instrument has n
 keys, giving a1,a2,…,an
 units of audience love.
K1o0n 已经达到了这样的境界：要想获得完整的幸福，他只缺一件乐器而已。于是，他买了一台二手合成器。这台乐器有 n
 个键，因此能赢得 a1,a2,…,an
 单位的听众喜爱。

Playing one note at a time is boring, so K1o0n learned a single technique — a triad: three keys with one key between each pair, pressed simultaneously. A triad starting at x
 (1≤x≤n−4
) is the keys x
, x+2
, and x+4
, which brings ax+ax+2−ax+4
 units of audience love.
一次只弹奏一个音符太无聊了，于是 K1o0n 学会了一种新的演奏技巧——三和弦：即同时按下三个键，每两个键之间相隔一个音符。以 x
 （ 1≤x≤n−4
 ）为起点构成的三和弦，对应的键位是 x
 、 x+2
 和 x+4
 。这样的演奏方式能赢得 ax+ax+2−ax+4
 单位的观众喜爱。

The keys are old, and each can withstand exactly one press. Therefore, K1o0n wants to choose exactly two different triads that do not share any keys. In addition, he wants both triads to bring the same amount of audience love.
这些按键都很旧了，每个按键只能被按一次。因此，K1o0n 希望选出两个完全不同的按键组合，这两个组合中的按键互不重复。此外，他还希望这两个按键组合能获得同样多的用户喜爱。

Count the number of ways to choose two such triads.
计算选出这样的三个数对的方法有多少种。

Input  输入
The first line contains an integer t
 (1≤t≤104
) — the number of testcases.
第一行包含一个整数 t
 ( 1≤t≤104
 )，表示测试用例的数量。

The first line of each testcase contains an integer n
 (6≤n≤2⋅105
) — the number of keys.
每个测试用例的第一行包含一个整数 n
 ( 6≤n≤2⋅105
 )，表示键的数量。

The second line of each testcase contains n
 integers ai
 (−104≤ai≤104
) — the units of audience love.
每个测试用例的第二行包含 、 n
 个整数 、 ai
 （即 、 −104≤ai≤104
 ），这些数字代表了观众们所喜爱的单位。

It is guaranteed that the sum of n
 over all testcases does not exceed 2⋅105
.
可以保证，所有测试用例中 n
 的值之和不会超过 2⋅105
 。

Output  输出
For each testcase, output one integer — the number of unordered pairs of disjoint triads with equal audience love values.
对于每个测试用例，输出一个整数——即那些由不相交的三个元素组成的组合中，其成员的“喜爱值”相等的无序组合的数量。

Note that the answer may not fit into a 32-bit type. Use a 64-bit type (long long in C++, long in Java).
请注意，该数值可能无法用 32 位数据类型来表示。请使用 64 位数据类型（C++中为“long long”，Java 中为“long”）。

Example  示例
Input  输入Copy  副本
3
6
5 1 4 2 2 -4
7
0 0 0 0 0 0 0
12
-4 3 0 -4 -4 -1 -4 1 -3 -2 -2 -1
Output  输出Copy  副本
1
2
5
Note  注意/备注
In the first testcase, such a pair is unique: x=1
, y=2
: 5+4−2=1+2−(−4)
.
在第一个测试用例中，这样的配对是唯一的： x=1
 、 y=2
 对应 5+4−2=1+2−(−4)
 。

In the second testcase, there are two such pairs: x=1
, y=2
 and x=3
, y=2
, and each triad brings 0
 units of audience love.
在第二个测试案例中，有这样几对组合： x=1
 、 y=2
 、 x=3
 、 y=2
 。每组这样的组合都能为 0
 带来相应的观众喜爱值。 """
import sys
input = sys.stdin.buffer.readline
t = int(input())
def read():
    return map(int,input().split())
for _ in range(t):
    n = int(input())
    arr = list(read())
    values = [arr[i] + arr[i+2] - arr[i+4] for i in range(n-4)]
    freq = {}
    ans = 0
    for j, value in enumerate(values):
        ans += freq.get(value, 0)
        if j >= 2 and values[j-2] == value:
            ans -= 1
        if j >= 4 and values[j-4] == value:
            ans -= 1
        freq[value] = freq.get(value, 0) + 1
    print(ans)