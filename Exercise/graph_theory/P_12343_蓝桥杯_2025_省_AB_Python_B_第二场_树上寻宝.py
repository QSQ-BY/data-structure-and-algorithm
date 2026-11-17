""" 题目描述
小蓝正在一棵含有 n 个结点的树的根结点 1 上，他准备在这棵树上寻宝。结点 i 上有一个物品，价值为 w 
i
​
 。然而，小蓝每次寻宝只能从根节点出发走不超过 k 步，每步只能选择走 1 条边或者 2 条边，之后会自动拾取最终停留的结点上的物品并被传送回根结点。请求出小蓝最终能获得的物品的总价值。

输入格式
输入的第一行包含两个正整数 n,k，用一个空格分隔。

第二行包含 n 个正整数 w 
1
​
 ,w 
2
​
 ,⋯,w 
n
​
 ，相邻整数之间使用一个空格分隔。

接下来 n−1 行，每行包含两个正整数 u 
i
​
 ,v 
i
​
 ，用一个空格分隔，表示结点 u 
i
​
  和结点 v 
i
​
  之间有一条边。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

8 2
6 3 3 1 5 4 3 4
1 2
2 3
2 4
4 5
5 6
6 7
7 8
输出 #1复制

22
说明/提示
样例说明
走 0 步能到的结点：1；
走 1 步能到的结点：2,3,4；
走 2 步能到的结点：3,4,5,6；
因此能到的结点为：1,2,3,4,5,6，能获得的总价值为 22。

评测用例规模与约定
对于 20% 的评测用例，1≤n≤15；
对于所有评测用例，0≤k<n≤10 
5
 ，1≤w 
i
​
 ≤10 
6
 ，1≤u 
i
​
 ,v 
i
​
 ≤n。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,k = read()
w = [0]+list(read())
g = [[]for _ in range(n+1)]
step_two = [[]for _ in range(n+1)]
for i in range(n-1):
    u,v = read()
    g[u].append(v)
    g[v].append(u)
ans = 0
stack = [(1,0,0)]#当前节点，父亲节点，步数
while stack:
    u,parent,step = stack.pop()
    ans += w[u]
    if(step >= 2*k):
        continue
    for v in g[u]:
        if(v != parent):
            stack.append((v,u,step+1))
print(ans)