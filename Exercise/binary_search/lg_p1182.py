""" 题目描述
对于给定的一个长度为 N 的正整数数列 A 
1∼N
​
 ，现要将其分成 M（M≤N）段，并要求每段连续，且每段和的最大值最小。

关于最大值最小：

例如一数列 4 2 4 5 1 要分成 3 段。

将其如下分段：

[4 2][4 5][1]
第一段和为 6，第 2 段和为 9，第 3 段和为 1，和最大值为 9。

将其如下分段：

[4][2 4][5 1]
第一段和为 4，第 2 段和为 6，第 3 段和为 6，和最大值为 6。

并且无论如何分段，最大值不会小于 6。

所以可以得到要将数列 4 2 4 5 1 要分成 3 段，每段和的最大值最小为 6。

输入格式
第 1 行包含两个正整数 N,M。

第 2 行包含 N 个空格隔开的非负整数 A 
i
​
 ，含义如题目所述。

输出格式
一个正整数，即每段和最大值最小为多少。

输入输出样例
输入 #1复制

5 3
4 2 4 5 1
输出 #1复制

6
说明/提示
对于 20% 的数据，N≤10。

对于 40% 的数据，N≤1000。

对于 100% 的数据，1≤N≤10 
5
 ，M≤N，A 
i
​
 <10 
8
 ， 答案不超过 10 
9
 。 """

#check(i)表示是否能把数列分成m段使得每一段的数值都要小于等于i
#check 0    0    0 ...... 1  1   1   1
#i     1    2    3 ...... 6  7   8   9
#寻找第一个1所在的位置
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int, input().split())

n,m = read()
arr = list(read())
left = max(arr)
right = sum(arr)

def check(limit:int)->int:
    global m
    global arr
    #检查把arr分割成m份可不可以让每一段的值都小于等于limit
    index = 0#index表示即将要检阅的位置
    cur_sum = 0
    temp = m
    while(index <= len(arr)-1):
        if(arr[index] > limit):
            return 0
        next_sum = cur_sum+arr[index]
        if(next_sum <= limit):
            cur_sum = next_sum
        elif(next_sum >limit):
            temp -= 1
            cur_sum = arr[index]
        if(temp<=0):
            return 0
        index += 1
    
    if(temp>0 ): return 1
    else:return 0

while(left < right):
    mid = (left+right)//2
    if(check(mid) == 1):
        right = mid
    else:
        left = mid+1
print(left)
