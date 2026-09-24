""" 题目描述
在一个神奇的小镇上有着一个特别的电车网络，它由一些路口和轨道组成，每个路口都连接着若干个轨道，每个轨道都通向一个路口（不排除有的观光轨道转一圈后返回路口的可能）。在每个路口，都有一个开关决定着出去的轨道，每个开关都有一个默认的状态，每辆电车行驶到路口之后，只能从开关所指向的轨道出去，如果电车司机想走另一个轨道，他就必须下车切换开关的状态。

为了行驶向目标地点，电车司机不得不经常下车来切换开关，于是，他们想请你写一个程序，计算一辆电车从路口 A 到路口 B，司机最少需要下车切换几次开关。

输入格式
第一行有 3 个整数 N,A,B（2≤N≤100,1≤A,B≤N），分别表示路口的数量，和电车的起点，终点。

接下来有 N 行，每行的开头有一个数字 K 
i
​
 （0≤K 
i
​
 ≤N−1），表示这个路口与 K 
i
​
  条轨道相连，接下来有 K 
i
​
  个数字表示每条轨道所通向的路口，开关默认指向第一个数字表示的轨道。

输出格式
输出文件只有一个数字，表示从 A 到 B 所需的最少的切换开关次数，若无法从 A 前往 B，输出 −1。

输入输出样例
输入 #1复制

3 2 1
2 2 3
2 3 1
2 1 2
输出 #1复制

0 """
import sys
from collections import deque
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())

#路口的数量，电车的起点和终点
n,start,target = read()

g = [[] for _ in range(n+2)]
for i in range(n):
    data = list(read())
    if(data[0] == 0):
        g[i+1] = []
        continue
    g[i+1] = data[1:]
    g[i+1] = [g[i+1][0]] + g[i+1]#第一个数字保存当前路口指向的轨道

q = deque()
dis = [float("inf")] * (n+2)
dis[start] = 0
q.append(start)

while q:
    cur = q.popleft()
    if(cur == target):
        break
    if(len(g[cur]) == 0):
        continue
    index = g[cur][0]
    for next in g[cur][1:]:
        if(index == next):
            w = 0
        else:
            w = 1
        next_step = dis[cur] + w
        if(dis[next] <= next_step):
            continue
        dis[next] = next_step
        if(w == 0):
            q.appendleft(next)
        else:
            q.append(next)

if(dis[target] == float("inf")):
    print(-1)
else:
    print(dis[target])

