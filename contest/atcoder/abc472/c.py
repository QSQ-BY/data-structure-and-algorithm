""" Problem Statement  问题描述
Takahashi is staying at his parents' house for an
N-day homecoming trip.
高桥正在父母家度过为期
N 天的返乡之旅。

At his parents' house, a snack is prepared every day, and the calorie count of the snack on day
i is
A
i
​
 .
在他父母家里，每天都会准备一些零食。在
i 这一天，所准备的零食的总热量为
A
i
​
  卡路里。

To manage his health, he repeats the following: he eats the snack on a given day if and only if the total calorie count of the snacks he has eaten in the most recent
M days does not exceed
K.
为了保持健康，他遵循以下原则：只有在最近
M 天内所摄入的零食总热量不超过
K 的情况下，他才会在某一天吃零食。

Specifically, in the order
i=1,2,…,N, he decides whether to eat the snack on day
i according to the following rule:
具体来说，在订单
i=1,2,…,N 中，他会根据以下规则来决定在
i 这一天是否要吃零食：

Assuming that he eats the snack on day
i, if the total calorie count of the snacks eaten from day
max(i−M+1,1) through day
i is at most
K, then he actually eats the snack on day
i. Otherwise, he does not eat the snack on day
i.
假设他在第
i 天吃了这份零食，那么如果从第
max(i−M+1,1) 天到第
i 天所吃的零食的总热量不超过
K ，那么他实际上是在第
i 天吃了这份零食。否则，他就在第
i 天不吃这份零食。
For each
i=1,2,…,N, determine whether Takahashi eats the snack on day
i.
对于每一个
i=1,2,…,N ，判断高桥是否在
i 这一天吃了零食。

Constraints  约束
1≤M≤N≤2×10
5

1≤K≤10
15

1≤A
i
​
 ≤10
9

All input values are integers.
所有输入值都是整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

N
M
K
A
1
​

A
2
​

…
A
N
​

Output  输出结果
Output
N lines. The
i-th line should contain Yes if Takahashi eats the snack on day
i, and No otherwise.
输出
N 行内容。如果高桥在
i 那天吃了零食，那么第
i 行应包含 Yes ；否则，该行应包含 No 。

Sample Input 1  示例输入 1 复制
Copy  副本
5 3 83
48 73 59 90 21
Sample Output 1  示例输出 1 复制
Copy  副本
Yes
No
No
No
Yes
For each day, assuming that he eats the snack, the total calorie count of the snacks eaten in the most recent three days is as follows:
假设他每天都会吃零食，那么最近三天所摄入的零食总热量如下：

Day
1:
48  第
1 天：
48
Day
2:
48+73=121  第
2 天：
48+73=121
Day
3:
48+59=107  第
3 天：
48+59=107
Day
4:
90  第
4 天：
90
Day
5:
21  第
5 天：
21
Sample Input 2  示例输入 2 复制
Copy  副本
7 4 728
187 816 349 609 255 308 175
Sample Output 2  示例输出 2 复制
Copy  副本
Yes
No
Yes
No
Yes
No
Yes
Sample Input 3  示例输入 3 复制
Copy  副本
10 3 1368290936
216519459 804733999 297250023 775422599 287963235 999315644 354987425 974810607 653940822 117157941
Sample Output 3  示例输出 3 复制
Copy  副本
Yes
Yes
Yes
No
Yes
Yes
No
No
Yes
Yes
"""
import sys
from itertools import accumulate
input=sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,m,k = read()
arr = [0] + list(read())
ans = []
flag = [0]*(n+1)
current = 0
for i in range(1,n+1):
    next = current + arr[i]
    if(i>m):
        if(flag[i-m] == 1):
            next -= arr[i-m]
    if(next <= k):
        current = next
        ans.append("Yes")
        flag[i] = 1
    elif(next > k):
        current = next - arr[i]
        ans.append("No")
print("\n".join(ans))