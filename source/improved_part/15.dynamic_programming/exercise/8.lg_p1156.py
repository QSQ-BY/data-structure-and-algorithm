""" 题目描述
卡门――农夫约翰极其珍视的一头 Holsteins 奶牛――已经落到了 “垃圾井” 中。“垃圾井” 是农夫们扔垃圾的地方，它的深度为 D（2≤D≤100）英尺。

卡门想把垃圾堆起来，等到堆得与井深同样高或比井深更高（即，垃圾高度总和 ≥D）时，她就能逃出井外了。另外，卡门可以通过吃一些垃圾来维持自己的生命。

每个垃圾都可以用来吃或堆放，并且堆放垃圾不用花费卡门的时间。

假设卡门预先知道了每个垃圾扔下的时间 t（1≤t≤1000），以及每个垃圾堆放的高度 h（1≤h≤25）和吃进该垃圾能增加维持生命的时间 f（1≤f≤30），要求出卡门最早能逃出井外的时间，已知卡门当前体内有足够持续 10 小时的能量，如果卡门 10 小时内（不含 10 小时，维持生命的时间同）没有进食，卡门就将饿死。特别地，若体力值为 0 时吃下垃圾或逃出井外也不会饿死。

输入格式
第一行为两个整数，D 和 G（1≤G≤100），G 为被投入井的垃圾的数量。

第二到第 G+1 行每行包括三个整数：t（1≤t≤1000），表示垃圾被投进井中的时间；f（1≤f≤30），表示该垃圾能维持卡门生命的时间；和 h（1≤h≤25），该垃圾能垫高的高度。

输出格式
如果卡门可以爬出陷阱，输出一个整数，表示最早什么时候可以爬出；否则输出卡门最长可以存活多长时间。

输入输出样例
输入 #1复制

20 4
5 4 9
9 3 2
12 6 10
13 1 1
输出 #1复制

13 """
import sys
input = sys.stdin.buffer.readline
from functools import cmp_to_key
def read():
    return map(int,input().split())
D , n = read()#陷阱的高度和垃圾的数量
datas = []
#dp[i][j]表示前i个垃圾,牛站在j高度的情况下,所能生存的最长时间
#第i个垃圾只能选择吃或者填
#dp[i][j] =  dp[i-1][j] + datas[i][1](吃下垃圾)(dp[i-1][j] >= datas[i][0])
#            dp[i-1][j-datas[i][2]](填入垃圾)(dp[i-1][j-datas[i][2]] >= datas[i][0])

for i in range(n):
    t,f,h = read()
    datas.append((t,f,h))
    #垃圾被投入到井里的时间，维持生命的时间，垃圾能垫的高度

def cmp(a,b)->int:
    if(a[0] < b[0]):
        return -1
    elif(a[0] > b[0]):
        return 1
    else:
        return 0
datas.sort(key = cmp_to_key(cmp))

dp = [[0]*(D+2)for _ in range(n+2)]
dp[0][0] = 10
datas = [(0,0,0)]+datas
longest_life = 10
for i in range(1,n+1):
    t,f,h = datas[i]
    for j in range(D+1):
        if(dp[i-1][j] < t):
            continue

        # 吃下垃圾，高度不变，能够存活的时间增加
        dp[i][j] = max(dp[i][j],dp[i-1][j] + f)
        longest_life = max(longest_life,dp[i][j])

        # 堆放垃圾，存活时间不变，高度增加
        if(j + h >= D):
            print(t)
            sys.exit()
        dp[i][j+h] = max(dp[i][j+h],dp[i-1][j])

print(longest_life)
