""" 题目描述
给定 n，构造一张 n 个点的简单有向无环图，使得距离为 2 的点对的个数不少于  
2
n(n−1)
​
 −n⌈log 
2
​
 n⌉。

点对 (u,v) 之间的距离指 u 到 v 的最短路长度。若 u 无法到达 v，则距离为 100 
100
 。

输入格式
一行一个正整数 n。

输出格式
第一行一个整数 m(0≤m≤ 
2
n(n−1)
​
 )，表示你构造的图的边数。

之后 m 行，每行两个数 u,v，表示你的构造的图中的一条边。你需要保证你构造的图是一张简单有向无环图，即没有重边也没有环。

输入输出样例
输入 #1复制

3
输出 #1复制

2
1 2
2 3
说明/提示
样例解释
样例中唯一距离为 2 的点对是 (1,3)，容易证明不存在满足条件的点对个数比 1 大的方案。

数据范围
1≤n≤2000。

评分方式
若你的程序给出的图不为简单有向无环图，你该测试点的得分将为 0。

否则设你的程序给出的图中距离为 2 的点对数为 x。若 x≥ 
2
n(n−1)
​
 −n⌈log 
2
​
 n⌉，你将获得该测试点的满分；若 ⌊ 
2
n−1
​
 ⌋×⌈ 
2
n−1
​
 ⌉≤x< 
2
n(n−1)
​
 −n⌈log 
2
​
 n⌉，你将获得该测试点 20% 的分数。 """
import sys
input = sys.stdin.buffer.readline
n = int(input())
edges = []
def dfs(center,left,right):
    if(len(left) == 0 and len(right) == 0):
        return
    global edges
    for i in left:
        edges.append((i,center))
    for j in right:
        edges.append((center,j))

    if(left):
        mid = len(left) // 2
        new_center = left[mid]
        new_left = left[:mid]
        new_right = left[mid + 1:]
        dfs(new_center,new_left,new_right)

    if right:
        mid = len(right) // 2
        new_center = right[mid]
        new_left = right[:mid]
        new_right = right[mid + 1:]
        dfs(new_center,new_left,new_right)

initial_center = (n + 1) // 2
initial_left = list(range(1, initial_center))
initial_right = list(range(initial_center + 1, n + 1))
dfs(initial_center,initial_left,initial_right)
print(len(edges))
for (a,b) in edges:
    print(a,b)