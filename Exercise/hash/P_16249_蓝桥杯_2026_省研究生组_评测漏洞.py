""" 题目描述
“判题机又卡住了！”小蓝眉头紧锁，盯着屏幕上的评测错误日志。

经过深入排查，他发现评测系统的校验逻辑存在一个隐蔽的漏洞：当系统先后读入两个参数 x 和 y 时，如果这两个数字的组合满足特定的算术性质，就会导致内存溢出，进而触发异常中止。

具体来说，若先后出现的两个参数 a 
i
​
  和 a 
j
​
 （其中 i<j）满足以下等式，系统就会崩溃：

(a 
i
​
 +a 
j
​
 ) 
2
 =a 
i
​
 +a 
j
​
 
​
 
为了修复这个漏洞，小蓝导出了当前崩溃用例中的全部 n 个测试参数，按读入顺序排列为 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 。现在，他需要你帮忙统计，这串参数中究竟存在多少对下标组合 (i,j)，满足 1≤i<j≤n 且会触发上述异常。

输入格式
第一行包含一个整数 n，表示测试参数的总数。

第二行包含 n 个整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 ，表示按顺序读入的参数值。

输出格式
输出一个整数，表示能够触发异常的参数对数量。

输入输出样例
输入 #1复制

4
-1 0 1 2
输出 #1复制

3
说明/提示
【评测用例规模与约定】
对于 40% 的评测用例，2≤n≤1000。

对于所有的评测用例，2≤n≤10 
5
 ，−10 
9
 ≤a 
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
arr = list(read())
s = {}
ans = 0
for number in arr:
    number1 = -number
    number2 = 1 - number
    if(number1 in s):
        ans += s[number1]
    if((number2) in s):
        ans += s[number2]
    if(number in s):
        s[number] += 1
    else:
        s[number] = 1
print(ans)
