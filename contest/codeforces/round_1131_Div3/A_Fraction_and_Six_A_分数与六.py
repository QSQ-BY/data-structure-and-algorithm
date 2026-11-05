""" A. Fraction and Six  A. 分数与六
time limit per test1 second
每次测试的时间限制为 1 秒
memory limit per test256 megabytes
每次测试的记忆限制：256 兆字节
You are given two strings p
 and q
, consisting of lowercase English letters.
你得到了两个字符串 p
 和 q
 ，这两个字符串都只包含小写英文字母。

Interpret the string p
 as the product of variables written in the numerator of a fraction, and the string q
 as the product of variables written in the denominator. Each character represents a variable.
将字符串 p
 解释为分数的分子部分中的变量乘积，而将字符串 q
 解释为分数的分母部分中的变量乘积。每个字符都代表一个变量。

Since multiplication is commutative, the variables in both the numerator and the denominator may be reordered arbitrarily. In addition, any variable that appears in both the numerator and the denominator may be cancelled. Note that a single occurrence of a variable in the denominator can only cancel exactly one occurrence of that variable in the numerator and vice versa.
由于乘法是可交换的，因此分子和分母中的变量可以任意重新排列。此外，任何出现在分子和分母中的变量都可以被消除。需要注意的是，分母中某个变量的出现，只能与分子中该变量的一个出现相抵消，反之亦然。

Determine whether it is possible to simplify the fraction so that the resulting expression is exactly equal to the string six
. In other words, after performing any number of cancellations and rearrangements, the remaining variables in the numerator must form the string six
, and no variables may remain in the denominator.
确定是否可以将这个分数简化，使得简化后的表达式完全等于字符串 six
 。换句话说，在进行了任意次数的合并和重新排列之后，分子中剩余的变量必须组成字符串 six
 ，而分母中不得有剩余的变量。

For example, if p=sinx
 and q=n
, then the variable n
 can be cancelled, leaving six
 in the numerator.
例如，如果 p=sinx
 和 q=n
 ，那么变量 n
 可以省略，这样分子就变成了 six
 。


Input  输入
The first line of the input contains a single integer t
 (1≤t≤100
) — the number of test cases. The description of each test case follows.
输入文件的第一行包含一个整数 t
 ( 1≤t≤100
 )，表示测试用例的数量。每个测试用例的描述会在下一行中给出。

The first line of each test case contains two integers n
 and m
 (1≤n,m≤100
) — the lengths of the strings p
 and q
, respectively.
每个测试案例的第一行包含两个整数 n
 和 m
 ( 1≤n,m≤100
 )——分别表示字符串 p
 和 q
 的长度。

The second line of each test case contains a string p
 denoting the numerator of the fraction. It is guaranteed that the length of the string p
 is equal to n
 and that it contains only lowercase English letters.
每个测试案例的第二行包含一个字符串 p
 ，表示分数的分子。保证字符串 p
 的长度等于 n
 ，并且该字符串仅由小写英文字母组成。

The third line of each test case contains a string q
 denoting the denominator of the fraction. It is guaranteed that the length of the string q
 is equal to m
 and that it contains only lowercase English letters.
每个测试案例的第三行包含一个字符串 q
 ，表示分数的分母。保证字符串 q
 的长度等于 m
 ，并且该字符串只包含小写英文字母。

Output  输出结果
For each test case, print "YES" if you can simplify the fraction so that the resulting expression is exactly equal to the string six
 and "NO" otherwise.
对于每个测试案例，如果可以将分数进行简化，使得最终的表达式完全等于字符串 six
 ，则输出“YES”；否则输出“NO”。

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).
你可以在任何情况下都输出“YES”或“NO”作为回应（例如，字符串“yEs”、“yes”或“Yes”将被识别为积极的回应）。

Example  示例
Input  输入Copy  副本
5
4 1
sinx
n
6 7
xixsms
mixsxim
8 5
fixtures
frute
3 3
abc
def
5 10
sixty
codeforces
Output  输出结果Copy  副本
YES
NO
YES
NO
NO
Note  注意/备注
In the first test case, the variable n appears in both the numerator and the denominator, so it can be cancelled. The remaining variables in the numerator are s, i, and x, which can be reordered to obtain six.
在第一个测试案例中，变量 n 同时出现在分子和分母中，因此可以消除它。分子中剩下的变量有 s、i 和 x，这些变量可以重新排序，从而得到六个不同的结果。

In the second test case, after cancelling all possible common variables, the numerator contains only s while the denominator contains only mi. Therefore, the fraction cannot be simplified to six.
在第二个测试案例中，经过取消所有可能的公共变量后，分子只剩下 s，而分母则只剩下 mi。因此，这个分数无法简化为 6。

In the third test case, the variables f, r, u, t, and e can be cancelled from both sides. The remaining variables in the numerator are s, i, and x, which can be reordered to form six.
在第三个测试案例中，变量 f、r、u、t 和 e 可以从等式两边取消。分子中剩下的变量有 s、i 和 x，这些变量可以重新排列组合成六个不同的变量。
 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
t = int(input())
for _ in range(t):
    n,m = read()
    p = input().decode().strip()
    q = input().decode().strip()
    if(n - m != 3):
        print("NO")
        continue
    s = {}
    for ch in p:
        if(ch in s):
            s[ch] += 1
        else:
            s[ch] = 1
    flag = True
    for ch in q:
        if(ch in s):
            s[ch] -= 1
            if(s[ch] == 0):
                s.pop(ch)
        else:
            print("NO")
            flag = False
    if(flag == False):
        continue
    if(len(s) == 3 and ("s" in s and "i" in s and "x" in s) and (s["s"] == 1 and s["i"] == 1 and s["x"] == 1)):
        print("YES")
    else:
        print("NO")