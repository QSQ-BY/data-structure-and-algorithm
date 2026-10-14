""" 题目描述
小 K 打下的江山一共有 n 个城市，城市 i 和城市 i+1 有一条双向高速公路连接，走这条路要耗费时间 a 
i
​
 。

小 K 为了关心人民生活，决定定期进行走访。他每一次会从 1 号城市到 n 号城市并在经过的城市进行访问。其中终点必须为城市 n。

不仅如此，他还有一个传送器，传送半径为 k，也就是可以传送到 i−k 和 i+k。如果目标城市编号小于 1 则为 1，大于 n 则为 n。

但是他的传送器电量不足，只能传送一次，况且由于一些原因，他想尽量快的完成访问，于是就想问交通部部长您最快的时间是多少。

注意：他可以不访问所有的城市，使用传送器不耗费时间。

输入格式
两行，第一行两个正整数 n,k。

第二行 n−1 个整数，第 i 个表示 a 
i
​
 。

输出格式
一个整数，表示答案。

输入输出样例
输入 #1复制

4 0
1 2 3
输出 #1复制

6
输入 #2复制

4 1
1 2 3
输出 #2复制

3
说明/提示
样例解释 1：
样例 1,2 的图示均为以下图片：



不使用传送器直接走，答案为 6，可以证明这个是最小值。

样例解释 2：
在 3 处使用，传送到 4，答案为 3，可以证明这个是最小值。

数据范围：
对于所有数据，n≥2，k≥1，a 
i
​
 >0。

测试点编号	n 的范围	k 的范围	a 
i
​
  的范围
1∼10	≤100	≤100	≤10 
5
 
11∼20	≤3×10 
3
 	≤3×10 
3
 	≤10 
9
 
21	≤10 
5
 	≤10 
5
 	≤10 
12
 
22	≤2×10 
5
 	≤2×10 
5
 	≤10 
12
 
23	≤5×10 
5
 	≤5×10 
5
 	≤10 
12
 
24∼25	≤10 
6
 	≤10 
6
 	≤10 
12 """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,k = read()
arr = list(read())
prefix = [0,*accumulate(arr)]
del arr
if(k == 0):
    print(prefix[-1])
    sys.exit()
ans = prefix[-1]
minus = 0
window_left = 0
window_right = k
while window_right < n:
    minus = max(minus,prefix[window_right] - prefix[window_left])
    window_right += 1
    window_left += 1
ans -= minus
print(ans)