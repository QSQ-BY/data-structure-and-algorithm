""" 题目描述
集合是数学中的一个概念，用通俗的话来讲就是：一大堆数在一起就构成了集合。

集合有如下的特性：

无序性：任一个集合中，每个元素的地位都是相同的，元素之间是无序的。

互异性：一个集合中，任何两个元素都认为是不相同的，即每个元素只能出现一次。

确定性：给定一个集合，任给一个元素，该元素或者属于或者不属于该集合，二者必居其一，不允许有模棱两可的情况出现。

例如 A={1,2,3} 就是一个集合。我们可以知道，1 属于 A，即 1∈A；4 不属于 A，即 4∈
/
A。一个集合的大小，就是其中元素的个数。

现在定义一个特殊的 k-集合，要求满足：

集合的所有特性
对任意一个该集合内的元素 x，不存在一个数 y，使得 y=kx 并且 y 属于该集合。即集合中的任意一个数，它乘以 k 之后的数都不在这个集合内。
给你一个由 n 个不同的数组成的集合，请你从这个集合中找出一个最大的 k-集合。

输入格式
第一行：两个整数：n 和 k。

第二行：n 个整数：a 
i
​
  表示给定的集合。

输出格式
第一行：一个整数：ans 表示最大的 k-集合的大小。

输入输出样例
输入 #1复制

6 2	
2 3 6 5 4 10
输出 #1复制

3
说明/提示
提示：在样例所给集合中，找出的最大的 2-集合为 {4,5,6}

对于 30% 的数据：n,k≤100。
对于 40% 的数据：∣a 
i
​
 ∣≤2 
31
 −1。
对于 70% 的数据：n,k≤5000。
对于 100% 的数据：2≤n,k≤10 
5
 ，1≤∣a 
i
​
 ∣≤2 
63
 −1。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,k = read()
arr = list(read())
class UnionSet():
    def __init__(self,n:int):
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.component_count = n
    def find(self,a:int):
        root = a
        while(self.parent[root] != root):
            root = self.parent[root]
        while self.parent[a] != a:
            next = self.parent[a]
            self.parent[a] = root
            a = next
        return root

    def merge(self,a:int,b:int):
        root_a = self.find(a)
        root_b = self.find(b)
        if(root_a == root_b):
            return False
        if(self.size[root_a] < self.size[root_b]):
            root_a,root_b = root_b,root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.component_count -= 1
        return True

union_set = UnionSet(n)
index = {value: i for i, value in enumerate(arr)}

for i, value in enumerate(arr):
    other = index.get(value * k)
    if other is not None:
        union_set.merge(i, other)

# 每个连通分量是一条链，长度为 size 时最多选 (size + 1) // 2 个。
ans = 0
for i in range(n):
    if union_set.parent[i] == i:
        ans += (union_set.size[i] + 1) // 2
print(ans)
