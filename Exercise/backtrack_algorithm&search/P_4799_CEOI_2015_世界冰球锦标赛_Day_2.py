""" 题目描述
译自 CEOI2015 Day2 T1「Ice Hockey World Championship」

今年的世界冰球锦标赛在捷克举行。Bobek 已经抵达布拉格，他不是任何团队的粉丝，也没有时间观念。他只是单纯的想去看几场比赛。如果他有足够的钱，他会去看所有的比赛。不幸的是，他的财产十分有限，他决定把所有财产都用来买门票。

给出 Bobek 的预算和每场比赛的票价，试求：如果总票价不超过预算，他有多少种观赛方案。如果存在以其中一种方案观看某场比赛而另一种方案不观看，则认为这两种方案不同。

输入格式
第一行，两个正整数 N 和 M(1≤N≤40,1≤M≤10 
18
 )，表示比赛的个数和 Bobek 那家徒四壁的财产。

第二行，N 个以空格分隔的正整数，均不超过 10 
16
 ，代表每场比赛门票的价格。

输出格式
输出一行，表示方案的个数。由于 N 十分大，注意：答案 ≤2 
40
 。

输入输出样例
输入 #1复制

5 1000
100 1500 500 500 1000
输出 #1复制

8
说明/提示
样例解释
八种方案分别是：

一场都不看，溜了溜了
价格 100 的比赛
第一场价格 500 的比赛
第二场价格 500 的比赛
价格 100 的比赛和第一场价格 500 的比赛
价格 100 的比赛和第二场价格 500 的比赛
两场价格 500 的比赛
价格 1000 的比赛
有十组数据，每通过一组数据你可以获得 10 分。各组数据的数据范围如下表所示：

数据组号	1−2	3−4	5−7	8−10
N≤	10	20	40	40
M≤	10 
6
 	10 
18
 	10 
6
 	10 
18 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n , m = read()#比赛数量和总预算
price = list(read())

def test01():
    #子集型枚举
    ans = 0
    price.sort()
    ans = 0
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + price[i]
    index = []

    def calculate():
        ret = 0
        for ind in index:
            ret += price[ind]
        return ret

    def dfs(min, max):
        nonlocal ans
        result = calculate()
        if result > m:
            return
        if result + suffix[min] - suffix[max + 1] <= m:
            ans += 2 ** (max - min + 1)
            return
        ans += 1  # 当前方案合法，包含第一次调用时的空集
        for number in range(min, max + 1):
            if result + price[number] > m:
                break
            index.append(number)
            dfs(number + 1, max)
            index.pop()

    dfs(0, n - 1)
    print(ans)

#用 DFS 得到两半的子集总价。
#用排序和二分，快速统计能搭配的方案数。
def test02():
    from bisect import bisect_right
    price.sort()
    index = []
    current_sum = 0
    def dfs(min,max,sums):
        nonlocal current_sum
        result = current_sum
        if(result > m):
            return
        sums.append(result)
        if(min>max):
            return
        for number in range(min,max+1):
            if(result + price[number] > m):
                break
            index.append(number)
            current_sum += price[number]
            dfs(number+1,max,sums)
            current_sum -= price[number]
            index.pop()
        return
    mid = n//2
    left = []
    right = []
    dfs(0,mid-1,left)
    dfs(mid,n-1,right)
    right.sort()
    ans = 0
    for s in left:
        #返回right中第一个值严格大于m-s的下标
        ans += bisect_right(right,m-s)
    print(ans)

#test01()
test02()