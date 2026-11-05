""" 题目描述
在 Mars 星球上，每个 Mars 人都随身佩带着一串能量项链。在项链上有 N 颗能量珠。能量珠是一颗有头标记与尾标记的珠子，这些标记对应着某个正整数。并且，对于相邻的两颗珠子，前一颗珠子的尾标记一定等于后一颗珠子的头标记。因为只有这样，通过吸盘（吸盘是 Mars 人吸收能量的一种器官）的作用，这两颗珠子才能聚合成一颗珠子，同时释放出可以被吸盘吸收的能量。如果前一颗能量珠的头标记为 m，尾标记为 r，后一颗能量珠的头标记为 r，尾标记为 n，则聚合后释放的能量为 m×r×n（Mars 单位），新产生的珠子的头标记为 m，尾标记为 n。

需要时，Mars 人就用吸盘夹住相邻的两颗珠子，通过聚合得到能量，直到项链上只剩下一颗珠子为止。显然，不同的聚合顺序得到的总能量是不同的，请你设计一个聚合顺序，使一串项链释放出的总能量最大。

例如：设 N=4，4 颗珠子的头标记与尾标记依次为 (2,3)(3,5)(5,10)(10,2)。我们用记号 ⊕ 表示两颗珠子的聚合操作，(j⊕k) 表示第 j,k 两颗珠子聚合后所释放的能量。则第 4，1 两颗珠子聚合后释放的能量为：

(4⊕1)=10×2×3=60。

这一串项链可以得到最优值的一个聚合顺序所释放的总能量为：

(((4⊕1)⊕2)⊕3)=10×2×3+10×3×5+10×5×10=710。

输入格式
第一行是一个正整数 N（4≤N≤100），表示项链上珠子的个数。第二行是 N 个用空格隔开的正整数，所有的数均不超过 1000。第 i 个数为第 i 颗珠子的头标记（1≤i≤N），当 i<N 时，第 i 颗珠子的尾标记应该等于第 i+1 颗珠子的头标记。第 N 颗珠子的尾标记应该等于第 1 颗珠子的头标记。

至于珠子的顺序，你可以这样确定：将项链放到桌面上，不要出现交叉，随意指定第一颗珠子，然后按顺时针方向确定其他珠子的顺序。

输出格式
一个正整数 E（E≤2.1×10 
9
 ），为一个最优聚合顺序所释放的总能量。

输入输出样例
输入 #1复制

4
2 3 5 10
输出 #1复制

710
说明/提示
NOIP 2006 提高组 第一题 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
intervals = []
for index,head in enumerate(arr):
    if(index <= len(arr) - 2):
        tail = arr[index+1]
    else:
        tail = arr[0]
    intervals.append((head,tail))
intervals = intervals + intervals
limit = n
n = 2*n
del arr
#dp[i][j]表示合并闭区间[i,j]这一段去区间内的项链所能获得的最大能量
dp = [[float("-inf")]*(n)for _ in range(n)]
for i in range(n):
    dp[i][i] = 0#只有一个珠子不管怎么样也不能合并
for i in range(n-1):
    head = intervals[i][0]
    mid  = intervals[i][1]
    tail = intervals[i+1][1]
    get = head*tail*mid
    dp[i][i+1] = get#区间内只有两个宝珠的时候也只能够直接合并，没有别的选择余地

for length in range(3,limit+1):
    for r in range(length-1,n):
        l = r - length + 1
        for k in range(l,r):
            get = (
                intervals[l][0]*
                intervals[k][1]*
                intervals[r][1]
            )
            dp[l][r] = max(dp[l][r],
                    dp[l][k] + dp[k+1][r] + get)

print(max(dp[i][i+limit-1]for i in range(limit)))
