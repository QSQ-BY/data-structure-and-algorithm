""" 题目描述
上课的时候总会有一些同学和前后左右的人交头接耳，这是令小学班主任十分头疼的一件事情。不过，班主任小雪发现了一些有趣的现象，当同学们的座次确定下来之后，只有有限的 D 对同学上课时会交头接耳。

同学们在教室中坐成了 M 行 N 列，坐在第 i 行第 j 列的同学的位置是 (i,j)，为了方便同学们进出，在教室中设置了 K 条横向的通道，L 条纵向的通道。

于是，聪明的小雪想到了一个办法，或许可以减少上课时学生交头接耳的问题：她打算重新摆放桌椅，改变同学们桌椅间通道的位置，因为如果一条通道隔开了 2 个会交头接耳的同学，那么他们就不会交头接耳了。

请你帮忙给小雪编写一个程序，给出最好的通道划分方案。在该方案下，上课时交头接耳的学生的对数最少。

输入格式
第一行，有 5 个用空格隔开的整数，分别是 M,N,K,L,D(2≤N,M≤1000,0≤K<M,0≤L<N,0≤D≤2000)。

接下来的 D 行，每行有 4 个用空格隔开的整数。第 i 行的 4 个整数 X 
i
​
 ,Y 
i
​
 ,P 
i
​
 ,Q 
i
​
 ，表示坐在位置 (X 
i
​
 ,Y 
i
​
 ) 与 (P 
i
​
 ,Q 
i
​
 ) 的两个同学会交头接耳（输入保证他们前后相邻或者左右相邻）。

输入数据保证最优方案的唯一性。

输出格式
共两行。
第一行包含 K 个整数 a 
1
​
 ,a 
2
​
 ,…,a 
K
​
 ，表示第 a 
1
​
  行和 a 
1
​
 +1 行之间、第 a 
2
​
  行和 a 
2
​
 +1 行之间、…、第 a 
K
​
  行和第 a 
K
​
 +1 行之间要开辟通道，其中 a 
i
​
 <a 
i+1
​
 ，每两个整数之间用空格隔开（行尾没有空格）。

第二行包含 L 个整数 b 
1
​
 ,b 
2
​
 ,…,b 
L
​
 ，表示第 b 
1
​
  列和 b 
1
​
 +1 列之间、第 b 
2
​
  列和 b 
2
​
 +1 列之间、…、第 b 
L
​
  列和第 b 
L
​
 +1 列之间要开辟通道，其中b 
i
​
 <b 
i+1
​
 ，每两个整数之间用空格隔开（列尾没有空格）。

输入输出样例
输入 #1复制

4 5 1 2 3
4 2 4 3
2 3 3 3
2 5 2 4
输出 #1复制

2
2 4
说明/提示


上图中用符号*、※、+标出了 3 对会交头接耳的学生的位置，图中 3 条粗线的位置表示通道，图示的通道划分方案是唯一的最佳方案。

2008 年普及组第二题 """
import sys
from functools import cmp_to_key

input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

def test02():
    n, m, k, l, d = read()

    ans1 = [0] * n
    ans2 = [0] * m

    for _ in range(d):
        x, y, p, q = read()

        if x == p:
            # 左右相邻，对应第 min(y,q) 列与下一列之间
            ans2[min(y, q)] += 1
        else:
            # 上下相邻，对应第 min(x,p) 行与下一行之间
            ans1[min(x, p)] += 1


    def cmp_row(a, b):
        # 优先选择能隔开更多同学的通道
        if ans1[a] > ans1[b]:
            return -1
        elif ans1[a] < ans1[b]:
            return 1
        else:
            # 次数相同，编号小的在前
            return a - b


    def cmp_col(a, b):
        if ans2[a] > ans2[b]:
            return -1
        elif ans2[a] < ans2[b]:
            return 1
        else:
            return a - b


    rows = list(range(1, n))
    cols = list(range(1, m))

    rows.sort(key=cmp_to_key(cmp_row))
    cols.sort(key=cmp_to_key(cmp_col))

    top_k_rows = rows[:k]
    top_l_cols = cols[:l]

    # 输出要求编号从小到大
    top_k_rows.sort()
    top_l_cols.sort()

    print(*top_k_rows)
    print(*top_l_cols)


def test01():
    n, m, k, l, d = read()
    
    reject = {}
    
    for _ in range(d):
        x, y, p, q = read()
    
        if (x, y) not in reject:
            reject[(x, y)] = set()
        reject[(x, y)].add((p, q))
    
        if (p, q) not in reject:
            reject[(p, q)] = set()
        reject[(p, q)].add((x, y))
    
    
    directions = [(0, 1), (1, 0)]
    
    # 关键修改：
    # 所有可能的横向/纵向通道都先加入，贡献初始化为 0
    ans1 = {i: 0 for i in range(1, n)}
    ans2 = {i: 0 for i in range(1, m)}
    
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
    
                if nx > n or ny > m:
                    continue
                
                if (x, y) in reject and (nx, ny) in reject[(x, y)]:
                    if dx == 1:
                        # 第 x 行和第 x+1 行之间
                        ans1[x] += 1
                    else:
                        # 第 y 列和第 y+1 列之间
                        ans2[y] += 1
    
    top_k_rows = sorted(ans1, key=ans1.get, reverse=True)[:k]
    top_l_cols = sorted(ans2, key=ans2.get, reverse=True)[:l]
    
    top_k_rows.sort()
    top_l_cols.sort()
    
    print(*top_k_rows)
    print(*top_l_cols)

test02()