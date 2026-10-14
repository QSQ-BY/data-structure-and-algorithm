""" 题目描述
有 n 个容量无穷大的水壶，它们从 1∼n 编号，初始时 i 号水壶中装有 A 
i
​
  单位的水。

你可以进行不超过 k 次操作，每次操作需要选择一个满足 1≤x≤n−1 的编号 x，然后把 x 号水壶中的水全部倒入 x+1 号水壶中。

最后你可以任意选择恰好一个水壶，并喝掉水壶中所有的水。现在请你求出，你最多能喝到多少单位的水。

输入格式
第一行一个正整数 n，表示水壶的个数。

第二行一个非负整数 k，表示操作次数上限。

第三行 n 个非负整数，相邻两个数用空格隔开，表示水壶的初始装水量 A 
1
​
 , A 
2
​
 , ⋯, A 
n
​
 。

输出格式
一行，仅一个非负整数，表示答案。

输入输出样例
输入 #1复制

10
5
890 965 256 419 296 987 45 676 976 742
输出 #1复制

3813
说明/提示
数据规模与约定
对于 10% 的数据，保证 n≤10。
对于 30% 的数据，保证 n≤100。
对于 50% 的数据，保证 n≤10 
3
 。
对于 70% 的数据，保证 n≤10 
5
 。
对于 100% 的数据，保证 1≤n≤10 
6
 ，0≤k≤n−1，0≤A 
i
​
 ≤10 
3
 。 """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
k = int(input())
arr = list(read())
prefix = [0,*accumulate(arr)]

right = k+1
left = 0
ans =0
while right <= n:
    ans = max(ans,prefix[right] - prefix[left])
    left += 1
    right += 1
print(ans)
