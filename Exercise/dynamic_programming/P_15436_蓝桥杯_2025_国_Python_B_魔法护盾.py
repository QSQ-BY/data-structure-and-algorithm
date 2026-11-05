""" 题目描述
在一个魔法世界里，勇士需要穿越一个危险的迷宫。迷宫中有 n 个房间排成一排，从左至右编号为 1 至 n，勇士需要按照从左至右的顺序从第 1 个房间开始一直到走出第 n 个房间才可以穿越成功，每个房间都存在魔法护盾和魔法攻击。

魔法护盾可以累积，但有最大容量限制。第 i 个房间有 s 
i
​
  个魔法护盾（可能为负，表示护盾被消耗），护盾最大累积容量为 c。

同时，每个房间可能有魔法攻击，a 
i
​
  表示第 i 个房间的攻击力。如果勇士在房间中累积的护盾小于攻击力，则会导致勇士穿越失败。

关键规则：

初始时，勇士拥有 b 个护盾。
进入房间 i 时，先获得 s 
i
​
  护盾（s 
i
​
 <0 表示失去 ∣s 
i
​
 ∣ 护盾），然后面临 a 
i
​
  攻击。
护盾有上限，累积护盾不能超过 c，若获得护盾后护盾大于 c，则护盾立即变为 c。
如果在任何房间中，护盾数量小于攻击力，冒险失败。
可以选择性地从某些房间中获得“护盾增幅”效果，选择增幅的房间，s 
i
​
  的效果会翻倍，该效果不影响 a 
i
​
 。
请计算勇士要成功通过所有房间，最少需要对多少个房间使用护盾增幅？如果无论如何都无法通过迷宫，则输出整数 −1。

输入格式
输入的第一行包含三个整数 n,c,b，相邻整数之间使用一个空格分隔，分别表示房间数量、护盾最大容量和初始护盾。

第二行包含 n 个整数 s 
1
​
 ,s 
2
​
 ,…,s 
n
​
 ，相邻整数之间使用一个空格分隔，s 
i
​
  表示第 i 个房间的护盾变化。

第三行包含 n 个整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 ，相邻整数之间使用一个空格分隔，a 
i
​
  表示第 i 个房间的攻击力。

输出格式
输出一行包含一个整数表示答案，即成功通过迷宫所需的最少护盾增幅房间数量。如果无法通过迷宫，请输出整数 −1。

输入输出样例
输入 #1复制

5 9 2
6 -3 6 -1 -4
9 6 6 7 4
输出 #1复制

1
输入 #2复制

9 9 0
5 3 9 5 -3 7 -1 3 -5
3 4 3 4 2 8 5 1 3
输出 #2复制

0
说明/提示
样例说明 1
对第一个房间使用护盾增幅。

到达第 1 个房间，当前护盾值为 min(2+6×2,9)=9≥9，可以通过第 1 个房间。

到达第 2 个房间，当前护盾值为 9−3=6≥6，可以通过第 2 个房间。

到达第 3 个房间，当前护盾值为 min(6+6,9)=9≥6，可以通过第 3 个房间。

到达第 4 个房间，当前护盾值为 9−1=8≥7，可以通过第 4 个房间。

到达第 5 个房间，当前护盾值为 8−4=4≥4，可以通过第 5 个房间。所以答案为 1。

样例说明 2
不需要使用护盾增幅，就可以通过所有房间。

评测用例规模与约定
对于 25% 的评测用例，1≤n≤10；

对于 50% 的评测用例，1≤n≤20；

对于 60% 的评测用例，1≤n≤50；

对于 70% 的评测用例，1≤n≤100；

对于 80% 的评测用例，1≤n≤1000；

对于所有评测用例，1≤n≤10000，−10000≤s 
i
​
 ≤10000，1≤a 
i
​
 ≤10000，1≤c≤50000，0≤b≤50000。 """
import sys
import heapq
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#使用二分+反悔贪心（错误思路因为这种思路无法考虑到limit）
def solution1():
    #一共有n个房间，护盾的最大值为c，初始的护盾值为b
    n,limit,start = read()
    arr1 = list(read())#获得的护盾值
    arr2 = list(read())#攻击力

    left = 0
    right = n+1
    #检查最多使用k次增强技能能不能通过房间
    def check(k):
        shield = start
        used = 0
        heap = []
        for number,attack in zip(arr1,arr2):
            shield += number
            if(number > 0):
                # 用负数实现最大堆，保存经过且尚未增幅的正收益房间
                heapq.heappush(heap,-number)
            while(shield < attack):
                if(used == k or not heap):
                    return False
                # 反悔选择收益最大的房间增幅，每个房间只能选择一次
                shield -= heapq.heappop(heap)
                used += 1
        return True
    #01二分模型
    while (left < right):
        mid = (left + right)//2
        #check用于检查使用了mid次增强效果能不能使得勇士通过房间
        if(check(mid) == True):
            right = mid
        else:
            left = mid+1
    if(left == n+1):
        print(-1)
    else:
        print(left)

#使用二分+dp
def solution2():
    #一共有n个房间，护盾的最大值为c，初始的护盾值为b
    n,limit,start = read()
    arr1 = list(read())#获得的护盾值
    arr2 = list(read())#攻击力

    left = 0
    right = n+1
    #检查最多使用k次增强技能能不能通过房间
    def check(k):
        # 还没进入房间，最多使用j次增幅时，护盾都是start
        dp = [start] * (k + 1)
        for s, a in zip(arr1, arr2):
            # 倒序更新，避免一个房间被增幅多次
            for j in range(k, -1, -1):
                best = -1
                # 当前房间不使用增幅
                if dp[j] >= 0:
                    best = min(limit, dp[j] + s)

                # 当前房间使用增幅
                if j > 0 and s > 0 and dp[j - 1] >= 0:
                    best = max(
                        best,
                        min(limit, dp[j - 1] + 2 * s)
                    )

                # 攻击只检查是否达标，不扣除护盾
                dp[j] = best if best >= a else -1
            # 最多使用k次都无法到达，直接失败
            if dp[k] == -1:
                return False
        return True
    #01二分模型
    while (left < right):
        mid = (left + right)//2
        #check用于检查使用了mid次增强效果能不能使得勇士通过房间
        if(check(mid) == True):
            right = mid
        else:
            left = mid+1
    if(left == n+1):
        print(-1)
    else:
        print(left)

#直接使用dp
def solution3():
    #一共有n个房间，护盾的最大值为c，初始的护盾值为b
    n,limit,start = read()
    arr1 = list(read())#获得的护盾值
    arr2 = list(read())#攻击力
    #dp[i][j]表示通过前i个房间，恰好使用j次正收益增幅时的最大护盾
    # -1表示该状态无法到达
    dp = [-1] * (n + 1)
    dp[0] = start
    for i, (s, a) in enumerate(zip(arr1, arr2), start=1):
        for j in range(i,-1,-1):
            best = -1
            # 当前房间不增幅，之前已经使用了j次
            if dp[j] >= 0:
                best = min(limit, dp[j] + s)
            # s <= 0 时，增幅没有好处，不需要考虑
            if j > 0 and s > 0 and dp[j - 1] >= 0:
                best = max(best, min(limit, dp[j - 1] + 2 * s))

            dp[j] = best if best >= a else -1

    ans = -1
    for j in range(n + 1):
        if dp[j] >= 0:
            ans = j
            break
    print(ans)
solution3()
