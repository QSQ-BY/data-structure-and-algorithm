""" Frank 是一个非常喜爱整洁的人。他有一大堆书和一个书架，想要把书放在书架上。书架可以放下所有的书，所以 Frank 首先将书按高度顺序排列在书架上。但是 Frank 发现，由于很多书的宽度不同，所以书看起来还是非常不整齐。于是他决定从中拿掉 k 本书，使得书架可以看起来整齐一点。

书架的不整齐度是这样定义的：每相邻的两本书宽度的差的绝对值的和。例如有 4 本书：

1×2
5×3
2×4
3×1

那么 Frank 将其排列整齐后是：

1×2
2×4
3×1
5×3

不整齐度就是 2+3+2=7。

已知每本书的高度都不一样，请你求出去掉 k 本书后的最小的不整齐度。

输入格式
第一行两个数字 n 和 k，代表书有几本，从中去掉几本（1<n≤100,1≤k<n）。

下面的 n 行，每行两个数字表示一本书的高度和宽度，均小于等于 200。

保证高度不重复。

输出格式
一行一个整数，表示书架的最小不整齐度。

输入输出样例
输入 #1复制

4 1
1 2
2 4
3 1
5 3
输出 #1复制

3 """
import sys
from functools import cmp_to_key
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#去掉k本数 = 选择n-k本书
#dp[i][k]代表第i本书必须选择的情况下
# 前i本书选择k本数所能得到的最小值
#dp[i][k] = min(dp[j][k-1] + abs(yi-yj))

n,K = read()
K = n-K
datas = [(-1,-1)]
for i in range(n):
    x,y = read()#x为高度,y为宽度
    datas.append((x,y))
def cmp(a,b):
    if(a[0]<b[0]):
        return -1
    elif(a[0] > b[0]):
        return 1
    else:return 0
datas.sort(key = cmp_to_key(cmp))
dp = [[float("inf")]*(n+2)for _ in range(n+2)]
for i in range(1,n+1):
    dp[i][0] = 0
    dp[i][1] = 0
    for k in range(2,i+1):
        for j in range(1,i):
            dp[i][k] = min(dp[i][k],dp[j][k-1]+abs(datas[j][1] - datas[i][1]))

ans = float("inf")
for i in range(1,n+1):
    ans = min(ans,dp[i][K])
print(ans)