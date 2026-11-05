""" 题目描述
小蓝正在画三角形，他先规定了三角形的一条边的边长为 x，你需要找出有多少个正整数 y 满足以下所有条件：

1≤y≤x；
x,y 以及 x∣y 这三个数可以构成一个非退化的三角形的边长。
其中，x∣y 表示 x 和 y 的二进制按位或（Bitwise OR）运算结果。

提示：一个三角形是非退化的，意味着它的三条边长 a,b,c 都必须为正，并且满足三角不等式：a+b>c、a+c>b、b+c>a。

如果其中任何一个不等式取等号（例如 a+b=c），则该三角形是退化的（三点共线）。

输入格式
输入一行包含一个正整数 x。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

10
输出 #1复制

7
说明/提示
样例说明
符合条件的 y 有：2,3,6,7,8,9,10。

评测用例规模与约定
对于 30% 的评测用例，1≤x≤10 
3
 ；

对于所有评测用例，1≤x≤10 
16
 。 """
import sys
input = sys.stdin.buffer.readline
#利用数学性质x + y = x|y + x&y
#直接暴力遍历所有的数字
def solution1():
    n = int(input())
    ans = 0
    def check(i:int,j:int,k:int)->bool:
        if(i+j > k and i+k>j and k+j > i):
            return True
    for i in range(1,n+1):
        cur = n|i
        if(check(i,cur,n)):
            ans +=1
    print(ans)

#利用数学性质x + y = x|y + x&y
def solution2():
    n = int(input())
    # 计算二进制中 0 的数量（不含前导零）
    zeros = n.bit_length() - n.bit_count()
    # 总数减去不合法的 y
    ans = n - (1 << zeros) + 1
    print(ans)

#solution1()
solution2()