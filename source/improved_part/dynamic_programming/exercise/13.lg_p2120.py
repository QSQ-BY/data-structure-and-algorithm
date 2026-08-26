""" 题目描述
L 公司有 n 个工厂，由高到低分布在一座山上，工厂 1 在山顶，工厂 n 在山脚。

由于这座山处于高原内陆地区（干燥少雨），L 公司一般把产品直接堆放在露天，以节省费用。突然有一天，L 公司的总裁 L 先生接到气象部门的电话，被告知三天之后将有一场暴雨，于是 L 先生决定紧急在某些工厂建立一些仓库以免产品被淋坏。

由于地形的不同，在不同工厂建立仓库的费用可能是不同的。第 i 个工厂目前已有成品 p 
i
​
  件，在第 i 个工厂位置建立仓库的费用是 c 
i
​
 。

对于没有建立仓库的工厂，其产品应被运往其他的仓库进行储藏，而由于 L 公司产品的对外销售处设置在山脚的工厂 n，故产品只能往山下运（即只能运往编号更大的工厂的仓库），当然运送产品也是需要费用的，一件产品运送一个单位距离的费用是 1。

假设建立的仓库容量都都是足够大的，可以容下所有的产品。你将得到以下数据：

工厂 i 距离工厂 1 的距离 x 
i
​
 （其中 x 
1
​
 =0）。
工厂 i 目前已有成品数量 p 
i
​
 。
在工厂 i 建立仓库的费用 c 
i
​
 。
请你帮助 L 公司寻找一个仓库建设的方案，使得总的费用（建造费用 + 运输费用）最小。

输入格式
输入的第一行是一个整数 n，代表工厂的个数。

第 2 到 (n+1) 行，每行有三个用空格隔开的整数，第 (i+1) 行的整数依次代表 x 
i
​
 , p 
i
​
 , c 
i
​
 。

输出格式
仅输出一行一个整数，代表最优方案的费用。

输入输出样例
输入 #1复制

3
0 5 10
5 3 100
9 6 10
输出 #1复制

32
说明/提示
样例输入输出 1 解释
在工厂 1 和工厂 3 建立仓库，建立费用为 10+10=20 ，运输费用为 (9−5)×3=12，总费用 32。 """

#dp[i]表示前i个位置在i位置建设仓库的最小消耗
import sys
from collections import deque
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
x = []
p = []
c = []
t = []#x*p的前缀和
s = []#p的前缀和
for i in range(n):
    new_x , new_p, new_c = read()
    x.append(new_x)
    p.append(new_p)
    c.append(new_c)
    t.append(new_x * new_p)
s = [0,*accumulate(p)]
t = [0,*accumulate(t)]
dp = [0]*(n+1)
x = [0]+x
p = [0]+p
c = [0]+c

def cmp1(j:int,k:int)->bool:
    if((dp[j]+t[j] - dp[k]-t[k]) > x[i]*(s[j] - s[k])):
        return True
    else: return False

def cmp2(i,j,k,l)->bool:
    if ((dp[i] + t[i] - dp[j]-t[j])*(s[k] - s[l]) < (dp[k] + t[k] - dp[l] - t[l])*(s[i] - s[j])):
        return True
    else:
        return False

#j状态向i状态进行转移
def calculate(i:int,j:int):
    global dp
    global x
    global c
    global p
    dp[i] = dp[j] + x[i]*(s[i] - s[j]) - t[i] + t[j] + c[i]
q = deque()
q.append(0)

for i in range(1,n+1):
    while(len(q) >= 2 and cmp1(q[0],q[1]) == True):
        q.popleft()
    calculate(i,q[0])
    while(len(q)>=2 and cmp2(i,q[-1],q[-1],q[-2]) == True):
        q.pop()
    q.append(i)

last_has_p = n
while last_has_p >= 1 and p[last_has_p] == 0:
    last_has_p -= 1
ans = min(dp[max(1, last_has_p) : n + 1])
print(ans)
