""" 题目描述
在一个二维平面内，给定 n 个整数点 (x 
i
​
 ,y 
i
​
 )，此外你还可以自由添加 k 个整数点。

你在自由添加 k 个点后，还需要从 n+k 个点中选出若干个整数点并组成一个序列，使得序列中任意相邻两点间的欧几里得距离恰好为 1 而且横坐标、纵坐标值均单调不减，即 x 
i+1
​
 −x 
i
​
 =1,y 
i+1
​
 =y 
i
​
  或 y 
i+1
​
 −y 
i
​
 =1,x 
i+1
​
 =x 
i
​
 。请给出满足条件的序列的最大长度。

输入格式
第一行两个正整数 n,k 分别表示给定的整点个数、可自由添加的整点个数。

接下来 n 行，第 i 行两个正整数 x 
i
​
 ,y 
i
​
  表示给定的第 i 个点的横纵坐标。

输出格式
输出一个整数表示满足要求的序列的最大长度。

输入输出样例
输入 #1复制

8 2
3 1
3 2
3 3
3 6
1 2
2 2
5 5
5 3
输出 #1复制

8
输入 #2复制

4 100
10 10
15 25
20 20
30 30
输出 #2复制

103
说明/提示
【样例 #3】

见附件中的 point/point3.in 与 point/point3.ans。

第三个样例满足 k=0。

【样例 #4】

见附件中的 point/point4.in 与 point/point4.ans。

【数据范围】

保证对于所有数据满足：1≤n≤500，0≤k≤100。对于所有给定的整点，其横纵坐标 1≤x 
i
​
 ,y 
i
​
 ≤10 
9
 ，且保证所有给定的点互不重合。对于自由添加的整点，其横纵坐标不受限制。

测试点编号	n≤	k≤	x 
i
​
 ,y 
i
​
 ≤
1∼2	10	0	10
3∼4	10	100	100
5∼7	500	0	100
8∼10	500	0	10 
9
 
11∼15	500	100	100
16∼20	500	100	10 
9
 
附件下载
point.zip
1.53KB """

import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

n, k = read()

pos = []
for _ in range(n):
    x, y = read()
    pos.append((x, y))

# 按照横坐标、纵坐标排序
pos.sort()

# dp[i][j]：以第i个点结尾，
# 使用j个新增点，最多经过多少个原有点
dp = [[-1] * (k + 1) for _ in range(n)]

ans = 1

for i in range(n):
    x1, y1 = pos[i]

    # 单独选择当前点
    dp[i][0] = 1

    # 枚举之前的点
    for t in range(i):
        x2, y2 = pos[t]

        # 不能向下走
        if y2 > y1:
            continue

        # 两个原有点之间需要新增的点数
        cost = x1 - x2 + y1 - y2 - 1

        if cost > k:
            continue
        # 枚举此前已经使用的新增点数
        for j in range(k - cost + 1):
            if dp[t][j] == -1:
                continue
            dp[i][j + cost] = max(
                dp[i][j + cost],
                dp[t][j] + 1
            )#只统计在这种花费的情况下能链接多少原点
    ans = max(ans, max(dp[i]))
# 剩余新增点可以全部添加在路径末尾
print(ans + k)
