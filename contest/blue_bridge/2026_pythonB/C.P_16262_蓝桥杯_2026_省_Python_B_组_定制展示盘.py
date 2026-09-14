""" 题目描述
小蓝正在设计一款用于存放纪念币的展示盘。

由于加工设备的限制，展示盘的制作必须满足以下条件：

展示盘是一个矩形，由若干行、若干列的槽位组成。
展示盘的行数和每行的槽位数量都至少为 2。
小蓝手头共有 n 枚纪念币需要安放，他可以根据需要定制不同规格的展示盘，只要展示盘上的总槽位数量（即行数与每行槽位数的乘积）不少于 n 即可。

加工费用是根据展示盘的总面积（即总槽位数量）来计算的，因此，小蓝希望在满足安放需求和设备限制的前提下，使展示盘的总槽位数量尽可能小。现在，请你帮他计算这个最小值。

输入格式
第一行包含一个正整数 T，表示数据的组数。

接下来的 T 行，每行包含一个正整数 n，代表小蓝拥有的纪念币总数。

输出格式
输出共 T 行，每行包含一个整数，表示在符合所有要求的情况下，展示盘最少需要包含的槽位总数。

输入输出样例
输入 #1复制

2
3
5
输出 #1复制

4
6
说明/提示
【样例说明】
当 n=3 时，一种最优方案是定制一个 2×2 的展示盘，此时总槽位数为 4；
当 n=5 时，一种最优方案是定制一个 2×3 的展示盘，此时总槽位数为 6。

【评测用例规模与约定】
对于 20% 的评测用例：1≤T≤10，1≤n≤10 
3
 。
对于所有评测用例，1≤T≤100，1≤n≤10 
9
 。 """
import sys
import math
input = sys.stdin.buffer.readline
t = int(input())
ans = []
def is_prime(n)->bool:
    if(n <= 1):
        return False
    if(n <= 3):
        return True
    if(n%2 == 0 or n%3 == 0):
        return False
    for j in range(5,math.isqrt(n) + 1,6):
        if(n%j == 0 or n%(j+2) == 0):
            return False
    return True

while t:
    n = int(input())
    if(n <= 4):
        ans.append(4)
        t -= 1
        continue
    if(is_prime(n) == True):
        ans.append(n+1)
    else:
        ans.append(n)
    t -= 1

for number in ans:
    print(number)