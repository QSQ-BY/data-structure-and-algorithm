""" 题目描述
小蓝在无聊时随机生成了一个长度为 n 的整数数组，数组中的第 i 个数为 a 
i
​
 ，他觉得随机生成的数组不太美观，想把它变成回文数组，也是就对于任意 i∈[1,n] 满足 a 
i
​
 =a 
n−i+1
​
 。小蓝一次操作可以指定相邻的两个数，将它们一起加 1 或减 1；也可以只指定一个数加 1 或减 1，请问他最少需要操作多少次能把这个数组变成回文数组？

输入格式
输入的第一行包含一个正整数 n。

第二行包含 n 个整数 a 
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

4
1 2 3 4
输出 #1复制

3
说明/提示
【样例说明】

第一次操作将 a 
1
​
 ,a 
2
​
  加 1，变为 2,3,3,4；

后面两次操作将 a 
1
​
  加 1，变为 4,3,3,4。

【评测用例规模与约定】

对于 20% 的评测用例，1≤n≤10；
对于所有评测用例，1≤n≤10 
5
 ，−10 
6
 ≤a 
i
​
 ≤10 
6
 。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())


left = 0
right = n - 1
ans = 0
while left + 1 <= right - 1:
    if(arr[left] == arr[right]):
        left += 1
        right -= 1
        continue
    number1,number2,number3,number4 = arr[left],arr[left + 1],arr[right-1],arr[right]
    if(number1 > number4 and number2 > number3):
        gap = min(number1 - number4,number2 - number3)
        ans += gap
        arr[right] += gap
        arr[right - 1] += gap
    elif (number1 < number4 and number2 < number3):
        gap = min(number4 - number1,number3 - number2)
        ans += gap
        arr[left] += gap
        arr[left + 1] += gap
    else:
        ans += abs(arr[left] - arr[right])
        left += 1
        right -= 1

if(right - left == 1):
    ans += abs(arr[right] - arr[left])

print(ans)