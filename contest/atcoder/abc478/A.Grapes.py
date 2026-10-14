""" Problem Statement  问题描述
There are 
N people numbered from 
1 to 
N.
共有 
N 个人，他们的编号分别是 
1 到 
N 。

There are 
M grapes. They will be distributed to the 
N people as follows.
共有 
M 颗葡萄。这些葡萄将按以下方式分配给 
N 个人。

Give one grape each to persons 
1,2,…,N in this order. If the grapes run out midway, the distribution ends at that point.
按顺序给 
1,2,…,N 中的每个人一颗葡萄。如果中途葡萄用完了，那么分配就到此为止。
If there are still grapes remaining after giving to person 
N, go back to person 
1 and distribute in order again. Repeat this until the grapes run out.
如果把葡萄分给 
N 之后还有剩余，那就把剩下的葡萄再拿回去，按照顺序重新分给 
1 。如此反复，直到所有的葡萄都被分完为止。
Find how many grapes each person receives.
算一算每个人能得到多少颗葡萄。

Constraints  约束
1≤N≤100
1≤M≤10000
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

N 
M
Output  输出
Output 
N lines. The 
i-th line should contain the number of grapes person 
i receives.
输出 
N 行内容。第 
i 行应包含第 
i 个人所获得的葡萄数量。

Sample Input 1  示例输入 1 复制
Copy  副本
3 5
Sample Output 1  示例输出 1 复制
Copy  副本
2
2
1
The five grapes are given one at a time to persons 
1,2,3,1,2 in this order.
这五颗葡萄会按照这个顺序，一颗一颗地交给 
1,2,3,1,2 号的人。

Sample Input 2  示例输入 2 复制
Copy  副本
4 1
Sample Output 2  样本输出 2Copy
Copy  副本
1
0
0
0
There may be people who receive no grape.
可能会有人根本得不到任何葡萄。

Sample Input 3  示例输入 3 复制
Copy  副本
12 3456
Sample Output 3  示例输出 3 复制
Copy  副本
288
288
288
288
288
288
288
288
288
288
288
288
Everyone may receive the same number of grapes.
每个人得到的葡萄数量可能都是一样的。 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())
#一共n个人，分m个
n,m = read()
number1 = m//n
number2 = m%n
cnt = [number1]*(n)
for i in range(number2):
    cnt[i]+= 1

for number in cnt:
    print(number)