""" /*  描述
 提交
 自定义测试
题解视频
题目描述
有一个由数字组成的三角形数塔，站在上一层的某个点，只能到达其下方左右的两个点。现在请找到一条从上到下的路径，使得路径上所有数字相加之和最大

4274F9B8E6E14581A4EC851BCE349029.jpg

输入
第一行输入一个数字 n（1≤n≤1000）代表数塔层数

接下来n行，按数塔图形，每行有一个或多个的整数，表示该层节点的值（节点值≤100000）

输出
输出一个整数，代表从上到下路径上所有数字相加和的最大值。

本题 BUG 已解决！

样例输入1
6
3
9 5
4 2 1
3 4 9 6
3 5 3 7 3
2 1 3 9 3 2
样例输出1
39 */ """

#f[i][j]表示从底边走到i j 点所能获得的最大值
#f[i][j] = max(f[i+1][j],f[i+1][j+1]) + val[i][j]
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#f[i][j]表示从底边走到i j 点所能获得的最大值
#f[i][j] = max(f[i+1][j],f[i+1][j+1]) + val[i][j]
#从下往上走
def test1():
    n = int(input())
    val = [[0]*(n+1) for _ in range(n+1)]
    f = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        val[i] = [0] + list(read())
    for i in range(1,n+1):
        f[n][i] = val[n][i]
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            f[i][j] = max(f[i+1][j ],f[i+1][j+1]) + val[i][j]
    print(f[1][1])


#从上往下走，计算从第一个点到每个点的最大值
#f[i][j] = max(f[i-1][j],f[i-1][j-1]) + val[i][j]
def test2():
    n = int(input())
    val = [[0]*(n+2) for _ in range(n+2)]
    f = [[float("-inf")]*(n+2) for _ in range(n+2)]
    for i in range(1,n+1):
        val[i] = [0] +list(read()) +[0]
    f[1][1] = val[1][1]
    for i in range(2,n+1):
        for j in range(1,i+1):
            f[i][j] = max(f[i-1][j],f[i-1][j-1]) + val[i][j]
    ans = max(f[n][1:n+1])
    print(ans)

#test1()
test2()