""" 题目描述
小明创造了一个函数 f(x) 用来翻转 x 的二进制的数位（无前导 0）。比如 f(11)=13，因为 11=(1011) 
2
​
 ，将其左右翻转后，变为 13=(1101) 
2
​
 ；再比如 f(3)=3，f(0)=0，f(2)=f(4)=f(8)=1 等等。

小明随机出了一个长度为 n 的整数数组 {a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 }，他想知道，在这个数组中选择最多 m 个不相交的区间，将这些区间内的数进行二进制数位翻转（将 a 
i
​
  变为 f(a 
i
​
 )）后，整个数组的和最大是多少？

输入格式
输入共 2 行。

第一行为两个正整数 n,m。

第二行为 n 个由空格分开的整数 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 。

输出格式
输出共 1 行，一个整数表示答案。

输入输出样例
输入 #1复制

5 3
11 12 13 14 15
输出 #1复制

67
输入 #2复制

6 2
23 8 11 19 16 35
输出 #2复制

134
说明/提示
【样例说明 1】

只翻转 a 
1
​
 ，和为 13+12+13+14+15=67。

【样例说明 2】

翻转区间 [a 
3
​
 ,a 
4
​
 ] 和 [a 
6
​
 ]，和为 23+8+13+25+16+49=134。

【评测用例规模与约定】

对于 20% 的评测用例，保证 n,m≤20。
对于 100% 的评测用例，保证 n,m≤1000，0≤a 
i
​
 ≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m = read()
arr = list(read())

#数位翻转函数
def f(number:int)->int:
    return int(str(bin(number)[2:])[::-1],2)

reversed_arr = [f(number) for number in arr]
gain = [reversed_arr[i] - arr[i] for i in range(n)]

limit = min(m, n)
#end[k][i]表示恰好选择k个不相交的非空区间，且最后一个元素
#恰好在第i个元素结束时能获得的最大收益
end = [[0] * (n + 1) for _ in range(limit + 1)]

max_gain = 0  # 允许不选择任何区间

#恰好选择k个区间
for k in range(1, limit + 1):
    best = 0
    for i in range(1, n + 1):
        # 恰好选 k-1 个区间，且结束位置不超过 i-1
        best = max(best, end[k - 1][i - 1])

        # 延续第 k 个区间，或从当前位置新开第 k 个区间
        end[k][i] = max(end[k][i - 1], best) + gain[i - 1]
        max_gain = max(max_gain, end[k][i])

print(sum(arr) + max_gain)