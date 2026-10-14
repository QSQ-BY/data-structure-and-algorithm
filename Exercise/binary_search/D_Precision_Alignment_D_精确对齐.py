""" D. Precision Alignment  D. 精确对齐
time limit per test2 seconds
每个测试用例的时间限制：2 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
K1o0n volunteered to work as a teaching assistant in the physics department, and he was assigned n
 training laboratories. In the i
-th laboratory, there are three instruments; their readings are ai
, bi
, and ci
. The instruments are distinguishable, and the order in this triple is fixed: the first (ai
), the second (bi
), the third (ci
).
K1o0n 自愿在物理系担任助教工作。他被分配到 n
 号实验室进行培训。在 i
 号实验室里，有三台仪器；它们的读数分别为 ai
 、 bi
 和 ci
 。这三台仪器是可以区分开来的，而且它们的顺序是固定的：第一台是 ai
 ，第二台是 bi
 ，第三台是 ci
 。

One action is to choose the index of a laboratory i
 and perform exactly one of the three adjustments:
其中一个操作是选择某个实验室的索引 i
 ，然后从三种调整方式中选择其中一种来执行。

ci+=sgn(ai−bi)
bi+=sgn(ai−ci)
ai+=sgn(bi−ci)
Here sgn(x)
 equals 1
 if x>0
, equals −1
 if x<0
, and equals 0
 if x=0
.
在这里，当 x>0
 成立时， sgn(x)
 等于 1
 ；当 x<0
 成立时， sgn(x)
 等于 −1
 ；当 x=0
 成立时， sgn(x)
 等于 0
 。

In other words, an adjustment shifts the reading of one instrument by one unit, and the direction of the shift is determined by the difference of the readings of the other two, taken in the order they are written: the earlier one minus the later one.
换句话说，这种调整会使得其中一个仪器的读数发生 1 个单位的变动。而变动的方向则由另外两个仪器的读数之差来决定，具体计算方法是：先取较早的那个仪器的读数，再减去较晚的那个仪器的读数。

The actions are performed one after another, and each adjustment looks at the readings that have been obtained by that moment. The same laboratory may be adjusted any number of times, and some may be left untouched altogether; in total, K1o0n is ready to make at most k
 actions across all laboratories.
这些操作是依次进行的，每次调整都会参考到该时刻所获得的测量数据。同一个实验室可能会被调整多次，也有一些实验室则完全不会被调整。总体而言，K1o0n 最多可以在所有实验室中执行 k
 次操作。

The work will be evaluated by the worst laboratory:
这项工作的评估将由表现最差的实验室来负责：

S=min1≤i≤n(ai+bi+ci),

where the readings are taken after all actions. K1o0n wants to impress his colleagues, so he asks you to find the maximum S
 he can achieve.
所有操作完成后，再记录下相应的数值。K1o0n 想给同事们留下好印象，所以他请你帮他找出能够取得的最大 S
 值。

Input  输入
The first line contains an integer t
 (1≤t≤104
) — the number of testcases.
第一行包含一个整数 t
 ( 1≤t≤104
 )，表示测试用例的数量。

The first line of each testcase contains two integers n
 and k
 (1≤n≤2⋅105
, 0≤k≤1018
) — the number of laboratories and the maximum number of actions.
每个测试用例的第一行包含两个整数 n
 和 k
 （即 1≤n≤2⋅105
 、 0≤k≤1018
 ），分别表示实验室的数量以及允许进行的最大操作次数。

The next n
 lines of each testcase contain three integers ai
, bi
, and ci
 (−109≤ai,bi,ci≤109
).
每个测试用例的接下来 n
 行中，包含三个整数： ai
 、 bi
 和 ci
 （ −109≤ai,bi,ci≤109
 ）。

It is guaranteed that the sum of n
 over all testcases does not exceed 2⋅105
.
可以保证，所有测试用例中 n
 的值之和不会超过 2⋅105
 。

Output  输出
For each testcase, output one integer — the maximum achievable value of S
.
对于每个测试用例，输出一个整数——即 S
 所能达到的最大值。

Note that the answer may not fit into a 32-bit integer type. Use a 64-bit integer type (long long in C++, long in Java).
请注意，该数值可能无法用 32 位整数类型来表示。应使用 64 位整数类型来存储该数值（在 C++中为“long long”，在 Java 中为“long”）。

Example  示例
Input  输入Copy  副本
5
3 4
-3 -1 -2
1 3 5
2 4 6
3 4
6 4 2
6 7 0
7 6 0
3 1000000000000000000
4 4 4
1 5 9
-1000000000 0 1000000000
2 4
1 2 3
0 0 5
4 3
2 1 0
4 4 5
1 5 9
7 -2 1
Output  输出Copy  副本
-2
14
12
6
6
Note  注意/备注
In the first testcase, to obtain a minimum sum of all triples equal to −2
, you need to add sgn(b1−c1)=1
 to a1
 four times. After that, the triplet (a1,b1,c1)
 will become (1,−1,−2)
, and the sum of the remaining triplets was originally greater than −2
. It can be shown that it is impossible to obtain a sum of −1
 or higher with that many operations.
在第一个测试案例中，要想让所有三数之和的最小值等于 −2
 ，需要将 sgn(b1−c1)=1
 加上 a1
 四次。之后，三数 (a1,b1,c1)
 会变成 (1,−1,−2)
 。而剩下的三数之和原本就大于 −2
 。可以证明，通过这么多的操作，不可能让三数之和达到或超过 −1
 。

In the second testcase, to obtain a minimum sum of all triples equal to 14
, it is necessary to add sgn(b1−c1)=1
 to a1
 2
 times, add sgn(a2−c2)=1
 to b2
 once, and add sgn(a3−b3)=1
 to c3
.
在第二个测试案例中，为了使所有三数之和的最小值等于 14
 ，需要将 sgn(b1−c1)=1
 加上 a1
 2
 共 a1
 2
 次；将 sgn(a2−c2)=1
 加上 b2
 共 1 次；最后将 sgn(a3−b3)=1
 加上 c3
 。

In the fourth testcase, it seems that it's impossible to improve the value of the second lab; however, it's not. We can make b2+=sgn(a2−c2)
, and we are out of the "stuck" position.
在第四个测试案例中，似乎无法提升第二个实验室的数值；但实际上并非如此。我们可以将 设置为 b2+=sgn(a2−c2)
 ，这样就能摆脱“僵局”了。


 """
import sys
from bisect import bisect_left#找到第一个大于等于的位置

def main():
    input = sys.stdin.buffer.readline
    t = int(input())
    answers = []

    for _ in range(t):
        n, k = map(int, input().split())

        labs = []
        left = 10**30
        limit = 10**30

        for _ in range(n):
            a, b, c = map(int, input().split())
            s = a + b + c
            left = min(left, s)

            if a == b == c:
                # 无法改变，这个总和限制了最终答案
                limit = min(limit, s)
            else:
                extra = 0
                if a <= b <= c:
                    extra = 2 * (min(b - a, c - b) + 1)

                labs.append((s, extra))

        # 按初始总和排序
        labs.sort()
        sums = [s for s, extra in labs]

        # prefix[i]：前 i 个实验室的 extra - s 之和
        prefix = [0]
        for s, extra in labs:
            prefix.append(prefix[-1] + extra - s)

        right = min(left + k, limit)

        while left < right:
            mid = (left + right + 1) // 2

            # 只有初始总和严格小于 mid 的实验室需要操作
            count = bisect_left(sums, mid)

            # 总费用 = Σ(mid - s + extra)
            cost = count * mid + prefix[count]

            if cost <= k:
                left = mid
            else:
                right = mid - 1

        answers.append(str(left))

    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()