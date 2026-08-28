""" 题目描述
Erwin 最近对一种叫 thair 的东西巨感兴趣。。。

在含有 n 个整数的序列 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
  中，三个数被称作thair当且仅当 i<j<k 且 a 
i
​
 <a 
j
​
 <a 
k
​
 。

求一个序列中 thair 的个数。

输入格式
开始一行一个正整数 n,

以后一行 n 个整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 。

输出格式
一行一个整数表示 thair 的个数。

输入输出样例
输入 #1复制

4
2 1 3 4
输出 #1复制

2
输入 #2复制

5
1 2 2 3 4
输出 #2复制

7
说明/提示
样例 2 解释
7 个 thair 分别是：

1 2 3
1 2 4
1 2 3
1 2 4
1 3 4
2 3 4
2 3 4 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#f[i]表示以i为结尾的三元上升序列的数量
#f[i][j]表示以i为结尾的j元上升序列的数量
#递推解法 
def test01():
    n = int(input())
    arr = [0] + list(read())
    f = [[0]*4 for _ in range(n+2)]
    for i in range(1,n+1):
        f[i][1] = 1
    ans = 0
    for i in range(1,n+1):
        for j in range(i):
            if(arr[j] >= arr[i]):
                continue
            f[i][2] += f[j][1]
            f[i][3] += f[j][2]
        ans += f[i][3]
    print(ans)

#树状数组解法
def test02():
    n = int(input())
    arr = [0] + list(read())
    size = max(arr)
    tree1 = [0]*(size+1)
    tree2 = [0]*(size+1)

    def update(tree,index,value):
        while(index <= size):
            tree[index] += value
            index += index & -index

    def query(tree,index):
        ans = 0
        while(index > 0):
            ans += tree[index]
            index -= index & -index
        return ans

    ans = 0
    for i in range(1,n+1):
        number1 = query(tree1,arr[i]-1)
        number2 = query(tree2,arr[i]-1)
        ans += number2
        update(tree1,arr[i],1)
        update(tree2,arr[i],number1)
    print(ans)


#test01()
test02()
