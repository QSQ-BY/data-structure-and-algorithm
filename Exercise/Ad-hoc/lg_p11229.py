""" 小 S 喜欢收集小木棍。在收集了 n 根长度相等的小木棍之后，他闲来无事，便用它们拼起了数字。用小木棍拼每种数字的方法如下图所示。



现在小 S 希望拼出一个正整数，满足如下条件：

拼出这个数恰好使用 n 根小木棍；
拼出的数没有前导 0；
在满足以上两个条件的前提下，这个数尽可能小。
小 S 想知道这个数是多少，可 n 很大，把木棍整理清楚就把小 S 折腾坏了，所以你需要帮他解决这个问题。如果不存在正整数满足以上条件，你需要输出 −1 进行报告。

输入格式
本题有多组测试数据。

输入的第一行包含一个正整数 T，表示数据组数。

接下来包含 T 组数据，每组数据的格式如下：

一行包含一个整数 n，表示木棍数。

输出格式
对于每组数据：输出一行，如果存在满足题意的正整数，输出这个数；否则输出 −1。

输入输出样例
输入 #1复制

5
1
2
3
6
18
输出 #1复制

-1
1
7
6
208 """
import sys

input = sys.stdin.buffer.readline

def solve(n: int) -> str:
    if n == 1:
        return "-1"

    remainder = n%7
    quotient = n//7

    if remainder == 0:
        return "8" * quotient

    if remainder == 1:
        return "10" + "8" * (quotient - 1)

    if remainder == 2:
        return "1" + "8" * quotient

    if remainder == 3:
        if n == 3:
            return "7"
        if n == 10:
            return "22"
        return "200" + "8" * (quotient - 2)

    if remainder == 4:
        if n == 4:
            return "4"
        return "20" + "8" * (quotient - 1)

    if remainder == 5:
        return "2" + "8" * quotient

    # remainder == 6
    return "6" + "8" * quotient


def main() -> None:
    test_count = int(input())
    answers = []

    for _ in range(test_count):
        n = int(input())
        answers.append(solve(n))

    for i,ans in enumerate(answers):
        print(ans)


if __name__ == "__main__":
    main()