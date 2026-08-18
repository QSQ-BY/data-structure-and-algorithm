""" You are given a rooted tree∗
 with n
 vertices, numbered from 1
 to n
. The vertex numbered 1
 is the root of the tree. The Beaver, initially located at the root, travels through the tree to one of the beaver dams located at the vertices numbered a1,…,am
.
给定了一棵以 1
 为根的树，该树共有 n
 个顶点，这些顶点的编号分别为 1
 到 n
 。海狸最初位于树的根节点处，它会沿着树的结构移动，最终到达编号为 a1,…,am
 的顶点上所建造的坝坝里。

You need to determine which of these m
 vertices the Beaver went to. To do this, you can place cameras on any edges of the tree. If the Beaver traverses an edge with a camera on it, you will see this. For clarity, we assume that after all the Beaver's movements, you will receive a sequence of edges with cameras in which the Beaver was observed passing through the corresponding edge.
你需要确定海狸究竟经过了这些 m
 顶点中的哪一个。为此，你可以在树的任意边上放置摄像头。如果海狸经过了装有摄像头的边，那么你就能看到这一过程。为便于理解，我们假设在海狸完成所有移动后，你会得到一系列包含装有摄像头的边的序列，这些边正是海狸经过的路径。

Since cameras are expensive, it is necessary to use the minimum number of them sufficient to uniquely determine the Beaver's destination. You are required to state the minimum necessary number of cameras k
 and the edges on which they should be placed.
由于摄像机的成本很高，因此必须使用尽可能少的摄像机数量，只要能确保能够唯一确定海狸的行进路径即可。你需要说明所需的最少摄像机数量 k
 ，以及这些摄像机应放置在哪条边上。

∗
A rooted tree is a tree where one vertex is special and called the root.
∗
 根树是一种特殊的树结构：其中有一个节点被特别指定为“根节点”。

Input  输入
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤2⋅104
). The description of the test cases follows.
每个测试包含多个测试用例。第一行包含测试用例的数量 t
 ( 1≤t≤2⋅104
 )。测试用例的描述随后给出。

In the first line of each test case, there is a single integer n
 (2≤n≤105
).
在每个测试案例的第一行，有一个整数 n
 ( 2≤n≤105
 )。

The second line contains n−1
 integers p2,…,pn
 — the parents of the vertices from the 2
nd to the n
th (1≤pi<i
; 2≤i≤n
).
第二行包含 、 n−1
 个整数 、 p2,…,pn
 ——这些整数分别代表了从第 、 2
 个顶点到第 、 n
 个顶点的父节点的编号（即 、 1≤pi<i
 ； 、 2≤i≤n
 ）。

The third line contains a single integer m
 — the number of vertices containing beaver dams (1≤m≤n
).
第三行包含一个整数 m
 ——即拥有海狸坝的顶点数量（ 1≤m≤n
 ）。

In the fourth line, there are m
 integers a1,…,am
 — the numbers of these vertices (1≤ai≤n
; 1≤i≤m
). All ai
 are distinct.
在第四行中，有 个、 m
 个整数 、 a1,…,am
 ——它们分别代表这些顶点的数量（即 、 1≤ai≤n
 ； 、 1≤i≤m
 ）。所有的 、 ai
 都是互不相同的。

It is guaranteed that the sum of n
 across all test cases does not exceed 105
.
可以保证，在所有测试案例中， n
 的总和都不会超过 105
 。

Output  输出结果
For each test case, output exactly one line. First, output the number k
 — the minimum required number of cameras, and then, in the same line, for each of the k
 edges connecting the vertices u
 and pu
, where cameras need to be installed, output the vertex number u
.
对于每个测试用例，只需输出一行内容。首先输出数字 k
 ——即所需的最少摄像头数量。接着，在同一行中，对于每条连接顶点 u
 与 pu
 的边 k
 ，都需要指出应安装摄像头的顶点编号 u
 。

If there are multiple answers, you can output any one of them.
如果有多个答案，可以选择其中任何一个来输出。

Example  示例
Input  输入Copy  副本
4
2
1
1
1
3
1 1
3
2 3 1
3
1 2
2
2 3
6
1 2 2 1 1
3
5 3 1
Output  输出结果Copy  副本
0
2 2 3
1 3
2 2 5 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int, input().split())
def solve():
    n = int(input())
    father = list(read())
    ans = []
    m = int(input())
    arr = list(read())
    index = min(arr)
    for i in range(m):
        if(arr[i] == index):continue
        ans.append(arr[i])
    ans = [m-1] + ans
    print(*ans)
def main():
    t = int(input())
    while t:
        solve()
        t -= 1
if __name__ == "__main__":
    main()