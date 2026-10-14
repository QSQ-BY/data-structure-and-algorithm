""" 题目背景
NOIP2015 普及组 T3

题目描述
一条狭长的纸带被均匀划分出了 n 个格子，格子编号从 1 到 n。每个格子上都染了一种颜色 color 
i
​
 （用 [1,m] 当中的一个整数表示），并且写了一个数字 number 
i
​
 。

编号	1	2	3	4	5	6
颜色和数字	5	5	3	2	2	2
定义一种特殊的三元组：(x,y,z)，其中 x,y,z 都代表纸带上格子的编号，这里的三元组要求满足以下两个条件：

x,y,z 都是整数，x<y<z,y−x=z−y。

color 
x
​
 =color 
z
​
 。

满足上述条件的三元组的分数规定为 (x+z)×(number 
x
​
 +number 
z
​
 )。整个纸带的分数规定为所有满足条件的三元组的分数的和。这个分数可能会很大，你只要输出整个纸带的分数除以 10007 所得的余数即可。

输入格式
第一行是用一个空格隔开的两个正整数 n 和 m，n 表示纸带上格子的个数，m 表示纸带上颜色的种类数。

第二行有 n 个用空格隔开的正整数，第 i 个数字表示纸带上编号为 i 的格子上面写的数字 number 
i
​
 。

第三行有 n 个用空格隔开的正整数，第 i 个数字表示纸带上编号为 i 的格子染的颜色 color 
i
​
 。

输出格式
一个整数，表示所求的纸带分数除以 10007 所得的余数。

输入输出样例
输入 #1复制

6 2
5 5 3 2 2 2
2 2 1 1 2 1
输出 #1复制

82
输入 #2复制

15 4
5 10 8 2 2 2 9 9 7 7 5 6 4 2 4
2 2 3 3 4 3 3 2 4 4 4 4 1 1 1
输出 #2复制

1388
说明/提示
样例 1 解释

纸带如题目描述中的图所示。

所有满足条件的三元组为：(1,3,5),(4,5,6)。

所以纸带的分数为 (1+5)×(5+2)+(4+6)×(2+2)=42+40=82。

对于第 1 组至第 2 组数据， 1≤n≤100,1≤m≤5；

对于第 3 组至第 4 组数据，1≤n≤3000,1≤m≤100；

对于第 5 组至第 6 组数据，1≤n≤10 
5
 ,1≤m≤10 
5
 ，且不存在出现次数超过 20 的颜色；

对于全部 10 组数据，1≤n≤10 
5
 ,1≤m≤10 
5
 ,1≤color 
i
​
 ≤m,1≤number 
i
​
 ≤10 
5
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,cnt = read()
number = list(read())
color = list(read())
MOD = 10007

def solution1():
    ans = 0
    for mid in range(1, n - 1):
        for length in range(1, min(mid, n - 1 - mid) + 1):
            left = mid - length
            right = mid + length
            if color[left] == color[right]:
                ans += (left + right + 2) * (number[left] + number[right])
    print(ans%MOD)

def solution2():
    groups = {}
    for i,(a,c) in enumerate(zip(number,color),start = 1):
        key = (c,i%2)
        if(key not in groups):
            groups[key] = [0,0,0,0]
        g = groups[key]
        g[0] += 1#k，位置数量
        g[1] += i#si，编号之和
        g[2] += a#sa,数字之和
        g[3] += i*a#sia，编号乘以数字之和
    ans = 0
    for k,si,sa,sia in groups.values():
        ans += (k-2)*sia + si*sa
    print(ans%MOD)
solution2()