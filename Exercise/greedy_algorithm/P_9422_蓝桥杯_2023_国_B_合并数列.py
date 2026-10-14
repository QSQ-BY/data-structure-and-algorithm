""" 题目描述
小明发现有很多方案可以把一个很大的正整数拆成若干正整数的和。他采取了其中两种方案，分别将他们列为两个数组 {a 
1
​
 ,a 
2
​
 ,⋯a 
n
​
 } 和 {b 
1
​
 ,b 
2
​
 ,⋯b 
m
​
 }。两个数组的和相同。

定义一次合并操作可以将某数组内相邻的两个数合并为一个新数，新数的值是原来两个数的和。小明想通过若干次合并操作将两个数组变成一模一样，即 n=m 且对于任意下标 i 满足 a 
i
​
 =b 
i
​
 。请计算至少需要多少次合并操作可以完成小明的目标。

输入格式
输入共 3 行。

第一行为两个正整数 n,m。

第二行为 n 个由空格隔开的整数 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 。

第三行为 m 个由空格隔开的整数 b 
1
​
 ,b 
2
​
 ,⋯,b 
m
​
 。

输出格式
输出共 1 行，一个整数。

输入输出样例
输入 #1复制

4 3
1 2 3 4
1 5 4
输出 #1复制

1
说明/提示
样例说明
只需要将 a 
2
​
  和 a 
3
​
  合并，数组 a 变为 {1,5,4}，即和 b 相同。

评测用例规模与约定
对于 20% 的数据，保证 n,m≤10 
3
 。
对于 100% 的数据，保证 n,m≤10 
5
 ，0<a 
i
​
 ,b 
i
​
 ≤10 
5
 。
第十四届蓝桥杯大赛软件赛决赛 C/C++ 大学 B 组 D 题 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())
n,m = read()
arr1 = list(read())
arr2 = list(read())
ans = []
index1 = 0
index2 = 0
while index1<n or index2 < m:
    cur_sum1 = arr1[index1]
    cur_sum2 = arr2[index2]
    while cur_sum1 != cur_sum2:
        if(cur_sum1 < cur_sum2):
            index1 += 1
            cur_sum1 += arr1[index1]
        else:
            index2 += 1
            cur_sum2 += arr2[index2]
    index1 += 1
    index2 += 1
    ans.append(cur_sum1)
ans = m+n-2*len(ans)
print(ans)