""" 题目描述
小蓝有一条环形灯带。灯带上按顺时针方向依次有 N 颗灯珠，第 i 颗灯珠的亮度为 A 
i
​
 。

若两颗相邻灯珠的亮度差的绝对值大于 K，则称这对相邻灯珠是不稳定的。由于灯带是环形的，第 N 颗灯珠和第 1 颗灯珠也相邻。

小蓝可以先在任意两颗相邻灯珠之间选择一个切口，将环形灯带展开成一排。随后，他要在这排中选择一段连续灯珠进行展示。

如果选中的展示段包含 L 颗灯珠，则段内有 L−1 对相邻灯珠需要检查。小蓝最多可以修补其中 M 对不稳定的相邻灯珠。展示段合法当且仅当段内不稳定相邻对的数量不超过 M。

请你计算，在可以自由选择切口和展示段的情况下，小蓝最多能展示多少颗连续灯珠。

输入格式
第一行包含三个整数 N,M,K，分别表示灯珠数量、最多可修补的不稳定相邻对数量、稳定亮度差阈值。

第二行包含 N 个整数 A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ，其中 A 
i
​
  表示第 i 颗灯珠的亮度。

输出格式
输出一行，包含一个整数，表示最多可以选出的连续灯珠数量。

输入输出样例
输入 #1复制

6 1 3
4 6 10 13 30 31
输出 #1复制

4
输入 #2复制

5 0 2
1 10 20 30 40
输出 #2复制

1
输入 #3复制

4 3 0
5 100 5 100
输出 #3复制

4
说明/提示
【样例说明 1】
可以切在第 6 颗和第 1 颗灯珠之间。展开后选择第 1 到第 4 颗灯珠，亮度依次为 4,6,10,13。

这段中共有 3 对相邻灯珠：4 与 6 稳定，6 与 10 不稳定，10 与 13 稳定。修补 6 与 10 这一对后，可以展示 4 颗连续灯珠。

任意展示 5 颗连续灯珠时，段内都会包含至少 2 对不稳定相邻灯珠，超过 M=1，因此答案为 4。

【样例说明 2】
只要展示段长度至少为 2，段内就会出现不稳定相邻对。由于 M=0，不能修补任何不稳定相邻对，所以最多只能展示一颗灯珠。

【样例说明 3】
可以选择合适的切口后展示全部 4 颗灯珠。展开后段内只有 3 对相邻灯珠需要检查，它们都不稳定，但都可以被修补，因此答案为 4。

【评测用例规模与约定】
对于 30% 的评测用例，1≤N≤200。

对于 60% 的评测用例，1≤N≤5000。

对于所有评测用例，1≤N≤2×10 
5
 ，0≤M≤N−1，0≤K≤10 
9
 ，1≤A 
i
​
 ≤10 
9
 。 """
import sys
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m,k = read()#差值大于k则被视为不稳定
#一共有m次机会修复不稳定性
arr = list(read())
arr = arr + arr
stable = [1]*(2*n-1)
for i in range(2*n-1):
    if(abs(arr[i+1] - arr[i]) > k):
        stable[i] = 0
#使用前缀和快速计算这一段内一共有多少对不稳定的灯珠
prefix = [0,*accumulate(stable)]

del arr
del stable
left = 0
right = n
#检查是否能够选出一段长度为length的灯带并保证稳定
def check(length):
    for window_left in range(2*n - length):
        window_right = window_left + length - 1
        s = prefix[window_right] - prefix[window_left]
        if length - 1 - s <= m:
            return True
    return False
#10二分模型
while left < right:
    mid = (left + right + 1)//2
    if(check(mid) == True):
        left = mid
    else:
        right = mid - 1
print(left)
