""" 题目描述
一条工业流水线上排列着 n 个温度传感器。当前各个传感器测得的温度记录在数组 A 中，而各传感器对应的理想标准温度记录在数组 B 中（即 A 
i
​
  为第 i 个传感器的当前温度，B 
i
​
  为第 i 个传感器的理想温度）。

为了让尽可能多的传感器达到理想温度，你可以进行一次区域温度补偿操作：

在流水线上划定一段连续的传感器区间 [l,r]（即第 l 个到第 r 个传感器）。
输入一个温度补偿值 k（k 为任意整数），使得该区间内所有传感器的当前温度都加上 k。
请问在执行完这一次校准操作后，最多能使多少个传感器的温度恰好等于其对应的理想标准温度？

输入格式
第一行包含一个整数 n，表示传感器的数量。

第二行包含 n 个整数 A 
1
​
 ,A 
2
​
 ,…,A 
n
​
 ，表示各传感器的当前温度。

第三行包含 n 个整数 B 
1
​
 ,B 
2
​
 ,…,B 
n
​
 ，表示各传感器对应的理想标准温度。

输出格式
输出一行，包含一个整数，表示补偿操作后处于理想温度的传感器最大数量。

输入输出样例
输入 #1复制

5
1 2 3 4 5
2 3 2 3 2
输出 #1复制

2
说明/提示
【评测用例规模与约定】
对于 30% 的评测用例，保证 1≤n≤2000；

对于所有评测用例，保证 1≤n≤2×10 
5
 , −10 
9
 ≤A 
i
​
 ,B 
i
​
 ≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int, input().split())

def test01():
    n = int(input())
    a = list(read())
    b = list(read())

    diff = []
    for i in range(n):
        diff.append(b[i] - a[i])

    candidates = set()
    for number in diff:
        candidates.add(number)

    def calculate(number):
        temp = diff.copy()
        base = 0
        for i in temp:
            if(i == 0):
                base += 1
        if(number == 0):
            return base
        for i in range(n):
            if(temp[i] == 0):
                temp[i] = -1
                continue
            if(temp[i] == number):
                temp[i] = 1
            else:
                temp[i] = 0

        dp = [0]*(n)#以dp[i]表示以i位置为结尾的最大子段和
        if(temp[0] > 0):
            dp[0] = 1

        for i in range(1,n):
            if(dp[i-1]>=0):
                dp[i] = temp[i]+dp[i-1]
            else:
                dp[i] = temp[i]

        return base + max(dp)

    ans = 0
    for candidate in candidates:
        ans = max(ans,calculate(candidate))

    print(ans)

def test02():
    n = int(input())
    a = list(read())
    b = list(read())

    diff = []
    for i in range(n):
        diff.append(b[i] - a[i])

    zeros = 0       # 已经遇到的零的数量
    gain = 0        # 全局最大净增量
    state = {}      # 差值 -> (最近一次的最优净增量, 当时的零数量)

    for x in diff:
        if x == 0:
            zeros += 1
            continue
        #- prev：补偿值选 x，且区间右端点固定在 x 最近一次出现的位置时，能获得的最大净增量。
        #- seen：处理到那个位置时，已经出现了多少个 0。
        # 首次出现时，默认状态也能让 cur 正确得到 1
        prev, seen = state.get(x, (0, 0))

        # 重新开始，或者接上上一次的最优区间
        #算出两次出现 x 之间有多少个零，也就是延伸区间需要付出的损失
        cur = max(1, prev - (zeros - seen) + 1)

        state[x] = (cur, zeros)
        gain = max(gain, cur)

    # 遍历结束后，zeros 就是原数组中已经达标的总数
    print(zeros + gain)
#test01()
test02()
