""" s题目描述
给定一个 n×m（n 行 m 列）的矩阵。

设一个矩阵的价值为其所有数中的最大值和最小值的乘积。求给定矩阵的所有大小为 a×b（a 行 b 列）的子矩阵的价值的和。

答案可能很大，你只需要输出答案对 998244353 取模后的结果。

输入格式
输入的第一行包含四个整数分别表示 n,m,a,b，相邻整数之间使用一个空格分隔。

接下来 n 行每行包含 m 个整数，相邻整数之间使用一个空格分隔，表示矩阵中的每个数 A 
i,j
​
 。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

2 3 1 2
1 2 3
4 5 6
输出 #1复制

58
说明/提示
【样例说明】

1×2+2×3+4×5+5×6=58。

【评测用例规模与约定】

对于 40% 的评测用例，1≤n,m≤100；

对于 70% 的评测用例，1≤n,m≤500；

对于所有评测用例，1≤a≤n≤1000，1≤b≤m≤1000，1≤A 
i,j
​
 ≤10 
9
 。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())

def test01():
    n,m,a,b = read()

    g = [[]for _ in range(n)]
    for i in range(n):
        g[i] = list(read())

    row_min = []
    row_max = []

    #第一遍，逐行处理长度为b的窗口
    for row in g:
        qmin = deque()#下标对应的值递增，对头是最小值
        qmax = deque()#下标对应的值递减，对头是最大值
        mins = []
        maxs = []

        for j,number in enumerate(row):
            #当前窗口的最左下标是j-b+1
            #因此下标<=j-b的元素已过期
            while qmin and qmin[0] <= j-b:
                qmin.popleft()

            while qmax and qmax[0] <= j - b:
                qmax.popleft()

            while qmin and row[qmin[-1]] >= number:
                qmin.pop()
            while qmax and row[qmax[-1]] <= number:
                qmax.pop()

            qmin.append(j)
            qmax.append(j)

            if(j >= b-1):
                mins.append(row[qmin[0]])
                maxs.append(row[qmax[0]])
        row_min.append(mins)
        row_max.append(maxs)

    MOD = 998244353
    ans = 0
    width = m - b + 1

    for j in range(width):
        qmin = deque()
        qmax = deque()
        for i in range(n):
            while qmin and qmin[0] <= i-a:
                qmin.popleft()
            while qmax and qmax[0] <= i - a:
                qmax.popleft()

            low = row_min[i][j]
            high = row_max[i][j]

            while qmin and row_min[qmin[-1]][j] >= low:
                qmin.pop()
            while qmax and row_max[qmax[-1]][j] <= high:
                qmax.pop()

            qmin.append(i)
            qmax.append(i)

            if(i >= a - 1):
                rectangle_min = row_min[qmin[0]][j]
                rectangle_max = row_max[qmax[0]][j]
                ans = ans = (ans + rectangle_min * rectangle_max) % MOD

    print(ans)

def test02():
    n,m,a,b = read()
    g = [[]for _ in range(n)]
    for i in range(n):
        g[i] = list(read())

    MOD = 998244353
    row_max = []
    row_min = []
    for row in g:
        qmin = deque()
        qmax = deque()
        mins = []
        maxs = []
        for window_right , number in enumerate(row):
            window_left = max(window_right - b + 1,0)
            while(qmin and qmin[0] < window_left):
                qmin.popleft()
            while(qmax and qmax[0] < window_left):
                qmax.popleft()

            while(qmin and row[qmin[-1]] > number):
                qmin.pop()
            while(qmax and row[qmax[-1]] < number):
                qmax.pop()
            qmin.append(window_right)
            qmax.append(window_right)

            if(window_right - b + 1 >= 0):
                mins.append(row[qmin[0]])
                maxs.append(row[qmax[0]])

        row_min.append(mins)
        row_max.append(maxs)

    ans = 0
    for column_index in range(m-b+1):
        qmin = deque()
        qmax = deque()
        mins = []
        maxs = []
        for window_right in range(n):
            window_left = max(window_right - a + 1,0)
            number1 = row_min[window_right][column_index]
            number2 = row_max[window_right][column_index]
            while(qmin and qmin[0] < window_left):
                qmin.popleft()
            while(qmax and qmax[0] < window_left):
                qmax.popleft()

            while(qmin and row_min[qmin[-1]][column_index] > number1):
                qmin.pop()
            while(qmax and row_max[qmax[-1]][column_index] < number2):
                qmax.pop()

            qmin.append(window_right)
            qmax.append(window_right)

            if(window_right - a + 1 >= 0):
                maximum = row_max[qmax[0]][column_index]
                minimum = row_min[qmin[0]][column_index]
                ans += maximum*minimum
                ans %= MOD
    print(ans)

test02()
