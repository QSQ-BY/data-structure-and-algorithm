""" 题目描述
小蓝有 n 个装了水的瓶子，从左到右摆放，第 i 个瓶子里装有 a 
i
​
  单位的水。为了美观，小蓝将水循环染成了 k 种颜色，也就是说，第 i 个瓶子和第 i+k 个瓶子里的水的颜色相同。

小蓝发现有的瓶子里的水太少了，因此他规定如果第 i 个瓶子和第 j 个瓶子中的水颜色相同并且满足 i<j，即可将任意整数单位的水从第 i 个水瓶倒出，倒入第 j 个水瓶中。小蓝想知道任意次操作后所有瓶子中的水的最小值 min{a 
i
​
 } 最大可以是多少？

输入格式
输入的第一行包含两个正整数 n,k，用一个空格分隔。

第二行包含 n 个正整数 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 ，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

7 3
8 5 5 2 2 3 4
输出 #1复制

3
说明/提示
样例说明
其中一种方案：

a 
1
​
  往 a 
4
​
  倒入 3 单位；
a 
2
​
  往 a 
5
​
  倒入 2 单位；
a 
3
​
  往 a 
6
​
  倒入 1 单位； 最终每个瓶子里的水：5,3,4,5,4,4,4，最小值为 3。
评测用例规模与约定
对于 40% 的评测用例，1≤n,a 
i
​
 ≤100；
对于所有评测用例，1≤n,a 
i
​
 ≤100000，1≤k≤n。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,k = read()
arr = list(read())
water = [[]for _ in range(k)]

for i,number in enumerate(arr):
    index = i % k
    water[index].append(number)

group_count = len(water)


def check(x):
    # 判断能否让每个瓶子至少有 x 单位水
    for group in water:
        total = 0

        for count, number in enumerate(group, start=1):
            total += number

            # 当前前缀的水量不够，右边也无法给它补水
            if total < count * x:
                return False
    return True

left = 0
right = sum(arr) // n  # 全部瓶子的平均值是答案的上界

while left < right:
    #10二分模型
    mid = (left + right + 1) // 2

    if check(mid):
        left = mid       # mid 可行，尝试更大的目标
    else:
        right = mid - 1  # mid 不可行，更大的也不行

print(left)