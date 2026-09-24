""" 题目背景
高手最近谈恋爱了。不过是单相思。“即使是单相思，也是完整的爱情”，高手从未放弃对它的追求。今天，这个阳光明媚的早晨，太阳从西边缓缓升起。于是它找到高手，希望在晨读开始之前和高手一起在鳌头山上一起散步。高手当然不会放弃这次梦寐以求的机会，他已经准备好了一切。

题目描述
鳌头山上有 n 个观景点，观景点两两之间有游步道共 m 条。高手的那个它，不喜欢太刺激的过程，因此那些没有路的观景点高手是不会选择去的。另外，它也不喜欢去同一个观景点一次以上。而高手想让他们在一起的路程最长（观景时它不会理高手），已知高手的穿梭机可以让他们在任意一个观景点出发，也在任意一个观景点结束。

输入格式
第一行，两个用空格隔开的整数 n,m。 之后 m 行，为每条游步道的信息：两端观景点编号、长度。

输出格式
一个整数，表示他们最长相伴的路程。

输入输出样例
输入 #1复制

4 6
1 2 10
2 3 20
3 4 30
4 1 40
1 3 50
2 4 60
输出 #1复制

150
说明/提示
对于 100% 的数据：n≤20，m≤50，保证观景点两两之间不会有多条游步道连接。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#一共n个景点，有m条边
n,m = read()
g = [[] for _ in range(n+1)]
for _ in range(m):
    data = list(read())
    g[data[0]].append((data[1],data[2]))
    g[data[1]].append((data[0],data[2]))

vis = [False]*(n+1)
vis[0] = True
ans = float("-inf")
#他们现在所在的位置编号以及现在获得的总价值
def dfs(cur,total):
    global vis
    global ans
    ans = max(ans,total)
    if(all(i==True for i in vis)):
        return

    for next_pos,add in g[cur]:
        if(vis[next_pos] ==True):
            continue
        vis[next_pos] = True
        dfs(next_pos,total + add)
        vis[next_pos] = False

for i in range(1,n+1):
    vis[i] = True
    dfs(i,0)
    vis[i] = False

print(ans)