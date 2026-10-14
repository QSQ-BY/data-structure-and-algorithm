""" 题目描述
实验室内，小蓝负责维护一个由 N 台计算机组成的局域网络。这些计算机原本通过高速网线互联，但随着设备老化，目前仅剩 M 条网线还能正常工作。正因如此，原本统一的网络分裂成了多个互不相连的通信区域。

为了恢复通信，小蓝计划架设一种特殊的“应急跳线”来重新连接这些区域。在物理逻辑上，只要任意两台计算机之间可以通过残存的网线或新架设的应急跳线建立直接或间接的通路，即视为它们之间恢复了连通。小蓝的任务是选定最优的布线方案，使得实验室内的所有 N 台计算机重新回到全连通的状态。

由于应急跳线的接口会占用计算机宝贵的硬件资源，小蓝在制定方案时设定了两个优先层级：首先，必须确保使用的应急跳线总数达到理论上的最小值；其次，为了减轻单台计算机的负载压力，他要求尽可能平均地分摊这些跳线。具体而言，他需要寻找一种方案，使得在所有计算机中，接入这种应急跳线数量最多的那一台机器，其接入的跳线数降到最低。

现在，请你根据当前网线的残存连接情况，计算出实现全连通所需的最少应急跳线数量，以及在这一最优前提下，单台计算机接入应急跳线数量最大值的最小可能值。

输入格式
第一行包含两个整数 N 和 M，分别表示计算机的总数和目前完好的网线数量。

接下来的 M 行，每行包含两个整数 a 和 b，表示计算机 a 和 b 之间目前仍存在一条完好的网线。

输出格式
输出一行，包含两个由单个空格隔开的整数。第一个整数表示最少需要添加的应急跳线数量，第二个整数表示在确保跳线总数最少的前提下，单台计算机接入跳线数量最大值的最小可能值。

输入输出样例
输入 #1复制

7 2
1 2
2 3
输出 #1复制

4 2
说明/提示
【样例说明】


通过连接 1−4, 4−5, 5−6, 6−7（共计 4 条跳线），可以使节点 4,5,6 各承担两条跳线，而其他节点仅承担一条或不承担，从而使最大值达到最小值为 2。

【评测用例规模与约定】
对于 30% 的评测用例，1≤N≤100, 0≤M≤100;

对于所有评测用例，1≤N≤10 
5
 , 0≤M≤10 
5
 , 1≤a,b≤N, a

=b。保证输入的连接信息中不包含重边。 """
import sys
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
        while(self.parent[root] !=root):
            root = self.parent[root]
        while(self.parent[x] != x):
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
        self.size[root_b] += self.size[root_a]
        self.component_count -= 1
        return True

n,edges =read()
u = UnionSet(n)
for _ in range(edges):
    a,b = read()
    u.merge(a-1,b-1)

k = u.component_count
if k == 1:
    print(0, 0)
else:
    print(k - 1, 1 if n >= 2 * (k - 1) else 2)
