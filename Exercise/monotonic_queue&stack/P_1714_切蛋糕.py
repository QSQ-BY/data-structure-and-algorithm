""" 题目描述
今天是小 Z 的生日，同学们为他带来了一块蛋糕。这块蛋糕是一个长方体，被用不同色彩分成了 n 个相同的小块，每小块都有对应的幸运值。

小 Z 作为寿星，自然希望吃到的蛋糕的幸运值总和最大，但小 Z 最多又只能吃 m(m≤n) 小块的蛋糕。

请你帮他从这 n 小块中找出连续的 k(1≤k≤m) 块蛋糕，使得其上的总幸运值最大。

形式化地，在数列 {p 
n
​
 } 中，找出一个子段 [l,r](r−l+1≤m)，最大化  
i=l
∑
r
​
 p 
i
​
 。

输入格式
第一行两个整数 n,m。分别代表共有 n 小块蛋糕，小 Z 最多只能吃 m 小块。

第二行 n 个整数，第 i 个整数 p 
i
​
  代表第 i 小块蛋糕的幸运值。

输出格式
仅一行一个整数，即小 Z 能够得到的最大幸运值。

输入输出样例
输入 #1复制

5 2
1 2 3 4 5
输出 #1复制

9
输入 #2复制

6 3
1 -2 3 -4 5 -6
输出 #2复制

5
说明/提示
数据规模与约定
对于 20% 的数据，有 1≤n≤100。
对于 100% 的数据，有 1≤n≤5×10 
5
 ，∣p 
i
​
 ∣≤500。
保证答案的绝对值在 [0,2 
31
 −1] 之内。 """
import sys
from collections import deque
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m = read()
arr = list(read())
prefix = [0,*accumulate(arr)]
q = deque([0])
ans = arr[0]
for right in range(1,n+1):
    while q and q[0]< right - m:
        q.popleft()
    ans = max(ans,prefix[right] - prefix[q[0]])
    while q and prefix[q[-1]] >= prefix[right]:
        q.pop()
    q.append(right)

print(ans)