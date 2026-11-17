""" 题目描述
小苯有一个长度为 n 的排列 {p 
1
​
 ,p 
2
​
 ,…,p 
n
​
 }，但是，他忘记了每一个元素的具体数值，好在他记得排列的每一个前缀的最小值。具体地，我们使用数组 prefix 来表示排列的每一个前缀的最小值，其中，prefix 
i
​
  代表排列中，前 i 个元素的最小值。

现在，根据这 n 个前缀最小值，小苯想知道有多少个符合条件的排列 p，请你帮他数一数吧。特别地，若不存在符合要求的排列，则只需要输出 0 即可。由于答案可能很大，请将答案对 998244353 取模后输出。

长度为 n 的排列是由 1∼n 这 n 个整数、按任意顺序组成的数组，其中每个整数恰好出现一次。例如，{2,3,1,5,4} 是一个长度为 5 的排列，而 {1,2,2} 和 {1,3,4} 都不是排列，因为前者存在重复元素，后者包含了超出范围的数。

输入格式
每个测试文件均包含多组测试数据。第一行输入一个整数 T 代表数据组数，每组测试数据描述如下：

第一行输入一个整数 n 代表排列中的元素数量。

第二行输入 n 个整数 prefix 
1
​
 ,prefix 
2
​
 ,…,prefix 
n
​
  代表排列的每一个前缀的最小值。

输出格式
对于每一组测试数据，新起一行。输出一个整数，代表符合条件的排列的数量。特别地，若不存在符合要求的排列，则只需要输出 0 即可。由于答案可能很大，请将答案对 998244353 取模后输出。

输入输出样例
输入 #1复制

4
3
3 2 1
4
2 2 1 1
2
2 2
7
6 2 2 1 1 1 1
输出 #1复制

1
2
0
24
说明/提示
对于第一组测试数据，符合条件的排列仅为 {3,2,1}。

对于第二组测试数据，需要满足： 
⎩
⎨
⎧
​
  
prefix 
1
​
 
prefix 
2
​
 
prefix 
3
​
 
prefix 
4
​
 
​
  
=
=
=
=
​
  
min{p 
1
​
 }
min{p 
1
​
 ,p 
2
​
 }
min{p 
1
​
 ,p 
2
​
 ,p 
3
​
 }
min{p 
1
​
 ,p 
2
​
 ,p 
3
​
 ,p 
4
​
 }
​
  
=
=
=
=
​
  
2
2
1
1
​
 
有且仅有排列 {2,4,1,3} 和 {2,3,1,4} 满足条件。

对于第三组测试数据，长度为 2 的排列有且仅有 {1,2} 和 {2,1} 两种。而前者的前缀最小值依次为 {1,1}，后者的前缀最小值依次为 {2,1}，均与输入的 prefix 数组不符，因此不存在符合条件的排列。

【数据范围】
对于 10% 的数据有：T=1,1≤n≤10。
对于所有的测试数据有：1≤T≤10 
3
 ,1≤n≤2×10 
5
 ,1≤a 
i
​
 ≤n。除此之外，保证单个测试文件的 n 之和不超过 3×10 
5
 。 """
import sys
from math import factorial
input = sys.stdin.buffer.readline
MOD = 998244353

t = int(input())
def read():
    return map(int,input().split())
for _ in range(t):
    n = int(input())
    prefix = list(read())

    # 前缀最小值不能增加，整个排列的最小值必须为 1
    if prefix[-1] != 1 or any(
        prefix[i] > prefix[i - 1] for i in range(1, n)
    ):
        print(0)
        continue

    intervals = []
    left = 0

    for right in range(1, n):
        if prefix[right] == prefix[right - 1]:
            continue

        intervals.append((prefix[left], left, right - 1))
        left = right
    # 最后一段也要加入
    intervals.append((prefix[left], left, n - 1))
    ans = 1
    for value, left, right in intervals:
        #可选的数字的个数，其中n-value是因为所有的值都必须大于value，减去left是因为left前的值都已经去定下来了
        available = n - value - left
        #当前这一个区间之内即将确定的数字的个数
        slots = right - left

        if available < slots:
            ans = 0
            break

        for j in range(slots):
            ans = ans * (available - j) % MOD

    print(ans)