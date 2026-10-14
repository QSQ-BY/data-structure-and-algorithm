""" 题目背景
NOIP2017 提高组 D2T1

题目描述
现有一块大奶酪，它的高度为 h，它的长度和宽度我们可以认为是无限大的，奶酪中间有许多半径相同的球形空洞。我们可以在这块奶酪中建立空间坐标系，在坐标系中，奶酪的下表面为 z=0，奶酪的上表面为 z=h。

现在，奶酪的下表面有一只小老鼠 Jerry，它知道奶酪中所有空洞的球心所在的坐标。如果两个空洞相切或是相交，则 Jerry 可以从其中一个空洞跑到另一个空洞，特别地，如果一个空洞与下表面相切或是相交，Jerry 则可以从奶酪下表面跑进空洞；如果一个空洞与上表面相切或是相交，Jerry 则可以从空洞跑到奶酪上表面。

位于奶酪下表面的 Jerry 想知道，在不破坏奶酪的情况下，能否利用已有的空洞跑到奶酪的上表面去?

空间内两点 P 
1
​
 (x 
1
​
 ,y 
1
​
 ,z 
1
​
 )、P 
2
​
 (x 
2
​
 ,y 
2
​
 ,z 
2
​
 ) 的距离公式如下：

dist(P 
1
​
 ,P 
2
​
 )= 
(x 
1
​
 −x 
2
​
 ) 
2
 +(y 
1
​
 −y 
2
​
 ) 
2
 +(z 
1
​
 −z 
2
​
 ) 
2
 
​
 
输入格式
每个输入文件包含多组数据。

第一行，包含一个正整数 T，代表该输入文件中所含的数据组数。

接下来是 T 组数据，每组数据的格式如下： 第一行包含三个正整数 n,h,r，两个数之间以一个空格分开，分别代表奶酪中空洞的数量，奶酪的高度和空洞的半径。

接下来的 n 行，每行包含三个整数 x,y,z，两个数之间以一个空格分开，表示空洞球心坐标为 (x,y,z)。

输出格式
T 行，分别对应 T 组数据的答案，如果在第 i 组数据中，Jerry 能从下表面跑到上表面，则输出 Yes，如果不能，则输出 No。

输入输出样例
输入 #1复制

3 
2 4 1 
0 0 1 
0 0 3 
2 5 1 
0 0 1 
0 0 4 
2 5 2 
0 0 2 
2 0 4
输出 #1复制

Yes
No
Yes
说明/提示
【输入输出样例 1 说明】



第一组数据，由奶酪的剖面图可见：

第一个空洞在 (0,0,0) 与下表面相切；

第二个空洞在 (0,0,4) 与上表面相切；

两个空洞在 (0,0,2) 相切。

输出 Yes。

第二组数据，由奶酪的剖面图可见：

两个空洞既不相交也不相切。

输出 No。

第三组数据，由奶酪的剖面图可见：

两个空洞相交，且与上下表面相切或相交。

输出 Yes。

【数据规模与约定】

对于 20% 的数据，n=1，1≤h，r≤10 
4
 ，坐标的绝对值不超过 10 
4
 。

对于 40% 的数据，1≤n≤8，1≤h，r≤10 
4
 ，坐标的绝对值不超过 10 
4
 。

对于 80% 的数据，1≤n≤10 
3
 ，1≤h,r≤10 
4
 ，坐标的绝对值不超过 10 
4
 。

对于 100% 的数据，1≤n≤1×10 
3
 ，1≤h,r≤10 
9
 ，1≤T≤20，坐标的绝对值不超过 10 
9
 。 """
import sys
from math import dist
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

class UnionSet():
    def __init__(self,n:int):
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.component_count = n

    def find(self,x:int):
        root = x
        while(self.parent[root] != root):
            root = self.parent[root]
        while x!= root:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x
        return root

    def merge(self,a:int,b:int):
        root_a = self.find(a)
        root_b = self.find(b)
        if(root_a == root_b):
            return False
        if(self.size[root_a] > self.size[root_b]):
            root_a,root_b = root_b,root_a
        self.parent[root_a] = root_b
        self.size[root_b] +=self.size[root_a]
        self.component_count -= 1
        return True

t = int(input())
for _ in range(t):
    n,h,r = read()
    items = []
    u = UnionSet(n+2)#n号下标和n+1号下标对应的分别是底和顶
    for i in range(n):
        x,y,z = read()
        items.append((x,y,z))
        if(z+r >= h):
            u.merge(i,n+1)
        if(z-r<=0):
            u.merge(i,n)

    #并查集优化
    #按 z 排序。若两点的高度差超过 2*r，后面的点也不可能相交，直接 break。
    #两个节点已经在同一个集合时，跳过距离计算和合并。
    #上下表面连通后，立即停止。
    # 排序下标，保留 items 与并查集编号的对应关系
    order = sorted(range(n), key=lambda i: items[i][2])
    diameter = 2 * r
    find = u.find
    merge = u.merge

    connected = find(n) == find(n + 1)

    for p in range(n):
        if connected:
            break
        i = order[p]
        x, y, z = items[i]
        root_i = find(i)

        for q in range(p + 1, n):
            j = order[q]
            xx, yy, zz = items[j]

            if zz - z > diameter:
                break

            root_j = find(j)
            if root_i == root_j:
                continue

            # 任意一个方向距离过大，都不可能相交
            if abs(xx - x) > diameter or abs(yy - y) > diameter:
                continue

            if dist(items[i], items[j]) <= diameter:
                merge(root_i, root_j)
                root_i = find(i)  # 合并后根可能改变，必须更新

                if find(n) == find(n + 1):
                    connected = True
                    break

    if connected:
        print("Yes")
    else:
        print("No")
