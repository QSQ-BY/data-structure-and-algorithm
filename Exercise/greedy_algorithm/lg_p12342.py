""" 题目描述
小蓝有两个长度均为 n 的数列 A={a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 } 和 B={b 
1
​
 ,b 
2
​
 ,⋯,b 
n
​
 }，将两个数列作差定义为 C=A−B={c 
1
​
 =a 
1
​
 −b 
1
​
 ,c 
2
​
 =a 
2
​
 −b 
2
​
 ,⋯,c 
n
​
 =a 
n
​
 −b 
n
​
 }。小蓝将对数列 B 进行若干次操作，每次操作可以将数列 B 中的任意一个数更改为任意一个整数。在进行完所有操作后，小蓝可以按任意顺序将数列 B 重排，之后再计算数列 C。小蓝想知道，最少操作多少次可以使得数列 C 中的所有数都为正整数。

输入格式
输入的第一行包含一个正整数 n；

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

第三行包含 n 个整数 b 
1
​
 ,b 
2
​
 ,⋯,b 
n
​
 ，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

4
22 31 12 14
3 19 27 44
输出 #1复制

1
说明/提示
样例说明
其中一种方案：将 44 改为 0，重新排列 B 为 {19,27,3,0}，使得数列 C={3,4,9,14} 均为正整数。

评测用例规模与约定
对于 30% 的评测用例，n≤10；
对于所有评测用例，1≤n≤10 
5
 ，−10 
9
 ≤a 
i
​
 ≤10 
9
 ，−10 
9
 ≤b 
i
​
 ≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr1 = list(read())
arr1.sort()
arr2 = list(read())
arr2.sort()
index1 = len(arr1) - 1
index2 = len(arr2) - 1
ans = 0
while(index1>=0 and index2>=0):
    number1 = arr1[index1]
    number2 = arr2[index2]
    if(number1 >number2):
        index1 -= 1
        index2 -= 1
    elif(number2 >= number1):
        ans += 1
        index2 -= 1

print(ans)