""" 题目描述
zxh 准备去踏青。

一开始，zxh 不知道任何景点。zxh 总共会搜索 q 次，每次搜索到一个景点。每个景点用一个 n 位的二进制数 a 
i
​
  表示它包含哪些景色，a 
i
​
  可以是 0。（输入时使用十进制）

zxh 会安排若干次踏青，每次踏青是依次访问若干个景点（可以重复访问同一个景点）。

在一次踏青中，如果连续访问的两个景点 u 和 v 满足 a 
u
​
 ora 
v
​
 =2 
n
 −1（即它们按位或的结果包含了所有 n 种景色），那么这次踏青就是“不值得期待”的。

zxh 不会安排不值得期待的踏青。因此，一次踏青中相邻的两个景点必须满足 a 
u
​
 ora 
v
​
 

=2 
n
 −1。

在每一次搜索之后（也就是得到了前 k 个景点之后），zxh 想知道：至少需要安排几次踏青，才能把当前已经搜索到的所有景点都至少访问一次。

注意，不同的踏青之间没有顺序要求，每次踏青可以独立选择景点序列。

你需要对每次搜索后，输出这个最少踏青次数。

输入格式
第一行，两个整数 n,q。

接下来 q 行，每行一个数 a 
i
​
  表示搜索到的景点。

输出格式
共 q 行，每行一个整数，表示插入后的答案。

输入输出样例
输入 #1复制

3 4
3
5
1
6
输出 #1复制

1
2
1
2
说明/提示
对于第四次询问，获得 a 
i
​
 =6 的新景点后，3→1→5，形成一次踏青；6 独自形成一次踏青（注意单独的一个景点也可以是一次踏青），答案为 2。

Subtask 编号	q≤	特殊性质	分值
#1	15	无	2
#2	10 
3
 	7
#3	10 
5
 	23
#4	5×10 
5
 	A	15
#5	无	53
特殊性质 A：n≤2。

对于 100% 的数据，1≤n≤60,0≤a 
i
​
 ≤2 
n
 −1,1≤q≤5×10 
5
 。 """
def test01():
    import sys

    input = sys.stdin.buffer.readline
    class UnionSet:
        def __init__(self, n):
            self.parent = list(range(n))
            self.component_count = n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def merge(self, a, b):
            root_a = self.find(a)
            root_b = self.find(b)

            if root_a == root_b:
                return False

            self.parent[root_a] = root_b
            self.component_count -= 1
            return True


    n, q = map(int, input().split())
    u = UnionSet(q)
    mask = (1 << n) - 1
    spots = []

    for i in range(q):
        spot = int(input())
        for j, old_spot in enumerate(spots):
            # 两个景点可以相邻
            if (spot | old_spot) != mask:
                u.merge(i, j)

        spots.append(spot)

        # q 个节点里面还有 q-(i+1) 个尚未出现
        ans = u.component_count - (q - i - 1)

        print(ans)

def test02():
    import sys
    input = sys.stdin.buffer.readline

    def read():
        return map(int, input().split())


    class UnionSet:
        def __init__(self, n):
            self.parent = list(range(n))

            # 当前 bit 是否出现过
            self.active = [False] * n

            # 当前有效 bit 的连通块数量
            self.component_count = 0

        def find(self, x: int):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])

            return self.parent[x]

        def add(self, x: int):
            if not self.active[x]:
                self.active[x] = True
                self.component_count += 1

        def merge(self, a: int, b: int):
            root_a = self.find(a)
            root_b = self.find(b)

            if root_a == root_b:
                return False

            self.parent[root_a] = root_b
            self.component_count -= 1

            return True


    n, q = read()

    # 并查集维护 n 个 bit
    u = UnionSet(n)

    mask = (1 << n) - 1

    # a == mask 的孤立景点数量
    alone = 0

    for i in range(q):

        spot = int(input())

        # 当前景点缺少哪些景色
        reject = mask ^ spot

        # 111...111
        if reject == 0:
            alone += 1
            print(u.component_count + alone)
            continue

        bits = []

        x = reject

        # 枚举 reject 中的所有 1
        while x:

            lowbit = x & -x

            bit = lowbit.bit_length() - 1

            bits.append(bit)

            # 激活这个 bit
            u.add(bit)

            x -= lowbit

        # 当前景点把这些 bit 全部连起来
        first = bits[0]

        for bit in bits[1:]:
            u.merge(first, bit)

        print(u.component_count + alone)
#test01()
test02()