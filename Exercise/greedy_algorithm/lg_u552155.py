""" 题目描述
给定长度为 n 的序列 a，要求将 a 分割成恰好 k 段，每一段内的所有数字都求和，得到一个长度为 k 的序列 b。

接着，最大化以下式子的和：

i=1
∑
k
​
 i×b 
i
​
 。
即：b 
1
​
 ×1+b 
2
​
 ×2+b 
3
​
 ×3+...+b 
k
​
 ×k。

更通俗的：

请最大化：“第一段的和乘 1，加上第二段的和乘 2，一直加到第 k 段的和乘 k ”。

现在，请你对每一个 k (1≤k≤n)，都求出并回答上述式子的最大值吧。

输入格式
本题有多组测试数据。

输入的第一行包含一个正整数 T，表示数据组数。

接下来包含 T 组数据，每组数据的格式如下：

第一行一个正整数 n，表示序列 a 的长度。

第二行 n 个整数 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 ，表示序列 a。

输出格式
对于每组测试数据：

在单独的一行输出由空格分隔的 n 个整数，其中第 i 个整数表示：把数组分为 i 段时，上述式子的最大值。

输入输出样例
输入 #1复制

2
6
1 3 -4 5 -1 -2
1
100
输出 #1复制

2 4 5 3 1 -2
100
说明/提示
【样例 1 解释】

对于第一组测试数据，我们考虑 k=3 的情况，可以把序列分为：

{{1},{3,−4},{5,−1,−2}}。

此时 b={1,3+(−4),(5+(−1)+(−2))}={1,−1,2}。

而题目所求式子的值为：1×1+(−1)×2+2×3=5。

因此第一组测试数据中，第三个数字的值是 5。

（可以证明，不存在比 5 更优的答案。）

【数据范围】

令 N 表示 T 组数据中 n 的总和。

对于 30% 的数据有：T=1,1≤N≤15。

对于 60% 的数据有：1≤T≤10,1≤N≤200。

对于所有的测试数据有： 1≤T≤100,1≤N≤2×10 
5
  ,−10 
6
 ≤a 
i
​
 ≤10 
6
 。 """
import sys
input = sys.stdin.buffer.readline
from itertools import accumulate
def read():
    return map(int,input().split())

def solve() -> list:
    n = int(input())
    arr = list(read())

    total = sum(arr)

    # 每个切割位置对应的后缀和
    suffixes = []
    suffix_sum = 0

    # i 从 n-1 到 1，不包含 arr[0]
    # 因为不能在第一个元素前面切割
    for i in range(n - 1, 0, -1):
        suffix_sum += arr[i]
        suffixes.append(suffix_sum)

    suffixes.sort(reverse=True)

    # k=1 时没有切割点
    answers = [total]

    # 每多分一段，就多选择一个后缀和
    for value in suffixes:
        answers.append(answers[-1] + value)

    return answers

def main():
    t = int(input())
    answers = []
    while(t != 0):
        t-=1
        answers.append(solve())
    for ans in answers:
        print(*ans)

if( __name__ == "__main__"):
    main()

