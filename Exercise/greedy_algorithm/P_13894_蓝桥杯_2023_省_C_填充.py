""" 题目描述
有一个长度为 n 的 01 串，其中有一些位置标记为 ?，这些位置上可以任意填充 0 或者 1，请问如何填充这些位置使得这个 01 串中出现互不重叠的 00 和 11 子串最多，输出子串个数。

输入格式
输入一行包含一个字符串。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

1110?0
输出 #1复制

2
说明/提示
【样例说明】

如果在问号处填 0，则最多出现一个 00 和一个 11：111000。

【评测用例规模与约定】

对于所有评测用例，1≤n≤1000000。 """
import sys
input = sys.stdin.readline
string = list(input().strip())
ans = 0
i = 0
while i < len(string) - 1:
    if string[i] == string[i + 1] or string[i] == "?" or string[i + 1] == "?":
        ans += 1
        i += 2
    else:
        i += 1

print(ans)