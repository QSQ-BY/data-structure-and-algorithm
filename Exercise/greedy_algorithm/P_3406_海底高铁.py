""" 题目描述
该铁路经过 N 个城市，每个城市都有一个站。不过，由于各个城市之间不能协调好，于是乘车每经过两个相邻的城市之间（方向不限），必须单独购买这一小段的车票。第 i 段铁路连接了城市 i 和城市 i+1(1≤i<N)。如果搭乘的比较远，需要购买多张车票。第 i 段铁路购买纸质单程票需要 A 
i
​
  博艾元。

虽然一些事情没有协调好，各段铁路公司也为了方便乘客，推出了 IC 卡。对于第 i 段铁路，需要花 C 
i
​
  博艾元的工本费购买一张 IC 卡，然后乘坐这段铁路一次就只要扣 B 
i
​
 (B 
i
​
 <A 
i
​
 ) 元。IC 卡可以提前购买，有钱就可以从网上买得到，而不需要亲自去对应的城市购买。工本费不能退，也不能购买车票。每张卡都可以充值任意数额。对于第 i 段铁路的 IC 卡，无法乘坐别的铁路的车。

Uim 现在需要出差，要去 M 个城市，从城市 P 
1
​
  出发分别按照 P 
1
​
 ,P 
2
​
 ,P 
3
​
 ,⋯,P 
M
​
  的顺序访问各个城市，可能会多次访问一个城市，且相邻访问的城市位置不一定相邻，而且不会是同一个城市。

现在他希望知道，出差结束后，至少会花掉多少的钱，包括购买纸质车票、买卡和充值的总费用。

输入格式
第一行两个整数，N,M。

接下来一行，M 个数字，表示 P 
i
​
 。

接下来 N−1 行，表示第 i 段铁路的 A 
i
​
 ,B 
i
​
 ,C 
i
​
 。

输出格式
一个整数，表示最少花费。

输入输出样例
输入 #1复制

9 10
3 1 4 1 5 9 2 6 5 3
200 100 50
300 299 100
500 200 500
345 234 123
100 50 100
600 100 1
450 400 80
2 1 10
输出 #1复制

6394
说明/提示
2 到 3 以及 8 到 9 买票，其余买卡。

对于 30% 数据 M=2。

对于另外 30% 数据 N≤1000，M≤1000。

对于 100% 的数据 M,N≤10 
5
 ，A 
i
​
 ,B 
i
​
 ,C 
i
​
 ≤10 
5
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m = read()
#一共有n个城市，需要经过m个城市
order = list(read())#游览城市的顺序
price = []
for _ in range(n-1):
    a,b,c = read()
    price.append((a,b,c))
price = [(0,0,0)]+price+[(0,0,0)]
cnt = [0]*(n+1)#记录一共做了几次i号铁路从
ans = 0

for i in range(1,m):
    start = min(order[i-1],order[i])
    end = max(order[i-1],order[i])
    cnt[start] += 1
    cnt[end] -= 1

for i in range(1,n+1):
    cnt[i] += cnt[i-1]

for index,count in enumerate(cnt):
    (a,b,c) = price[index]
    if(a*count >= b*count + c):
        ans += b*count + c
    else:
        ans += a*count
print(ans)
