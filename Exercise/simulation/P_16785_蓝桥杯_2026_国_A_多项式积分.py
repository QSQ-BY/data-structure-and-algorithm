""" 题目描述
小蓝正在学习微积分。今天他的作业是求一个关于 x 的多项式的不定积分，请你帮他完成这个任务。

给定一个关于 x 的多项式，请输出它的一个不定积分结果。积分常数不需要输出。

输入格式
输入一行，包含一个关于 x 的多项式。

该多项式由若干个系数为整数的项构成，每一项的次数为非负整数。其中，次数为 0 的项表示常数项。

输入多项式满足以下规则：

各项按照次数从高到低给出；
首项若为负数，可以带负号；首项若为正数，前方不带 +；
除首项外，其余各项以 + 或 − 作为分隔符，正负号归属于对应项；
次数为 0 的项直接写作整数常数；
次数为 1 的项写作 cx 或 x，其中系数为 1 或 −1 时可以省略数字 1；
次数大于 1 的项写作 cx 
∧
 k 或 x 
∧
 k，其中 k>1，系数为 1 或 −1 时可以省略数字 1；
所有项的系数均不为 0，不存在系数为 0 的冗余项。
输出格式
输出一行，表示输入多项式的不定积分结果。

输出时不需要写积分常数，结果中的各项应按照次数从高到低排列。

输出多项式时应遵守以下格式规则：

若首项系数为正，前方不输出 +；
对于非首项，若该项系数为正，则前方输出 +；若该项系数为负，则前方输出 −；
次数为 1 时，输出 x，不输出 x 
∧
 1；
单项系数为 1 或 −1 时，省略数字 1，只保留符号和字母部分；
若某一项的系数为分数  
q
p
​
 ，应输出为 p/q，其中 p 和 q 互质，且 q>0；
若分数系数为负数，负号应放在分子位置；
若化简后分母为 1，直接输出整数形式，不输出分数形式。
输出结果中不应包含系数为 0 的冗余项。
输入输出样例
输入 #1复制

4x^5-4x^3+2
输出 #1复制

2/3x^6-x^4+2x
输入 #2复制

-100x^100+105x^2
输出 #2复制

-100/101x^101+35x^3
输入 #3复制

7
输出 #3复制

7x
输入 #4复制

x-1
输出 #4复制

1/2x^2-x
说明/提示
【样例说明】
对于样例 1:

∫(4x 
5
 −4x 
3
 +2)dx= 
3
2
​
 x 
6
 −x 
4
 +2x+C.
积分常数 C 不需要输出，因此输出 2/3x 
∧
 6-x 
∧
 4+2x。

对于样例 2:

∫(−100x 
100
 +105x 
2
 )dx=− 
101
100
​
 x 
101
 +35x 
3
 +C.
因此输出 -100/101x 
∧
 101+35x 
∧
 3。

对于样例 3, 输入多项式为常数 7, 积分结果为 7x+C, 因此输出 7x。

对于样例 4:

∫(x−1)dx= 
2
1
​
 x 
2
 −x+C.
因此输出 1/2x 
∧
 2-x。

【评测用例规模与约定】
对于 50% 的数据，保证积分结果中每一项的系数均为正整数。

对于所有数据，保证：

输入多项式的项数不超过 10000；
每一项的次数不超过 10 
8
 ；
每一项系数的绝对值不超过 10 
8
 ；
输入多项式中的项按次数从高到低给出。 """
import sys
from math import gcd
input = sys.stdin.buffer.readline

string = input().decode().strip()
ans = []
index = 0
n = len(string)
def calculate(cur:str):
    if(cur[0] == "-" or cur[0] == "+"):
        sign_bit = cur[0]
        index = 1
    else:
        sign_bit = None
        index = 0
    ret = []
    if(sign_bit is not None):
        ret.append(sign_bit)
    coefficient = []

    while(index < len(cur) and cur[index] != "x"):
        coefficient.append(cur[index])
        index += 1
    coefficient = int("".join(coefficient)) if coefficient else 1
    if("x" not in cur):
        if(coefficient != 1):
            ret.append(str(coefficient))
        ret += ["x"]
        return ret
    if("^" not in cur):
        if(coefficient %2 != 0):
            ret += [str(coefficient),"/","2","x","^","2"]
        else:
            if(coefficient//2 != 1):
                ret.append(str(coefficient//2))
            ret += ["x","^","2"]
        return ret
    power = int(cur[index+2:])+1
    divisor = gcd(coefficient, power)
    coefficient //= divisor
    denominator = power//divisor
    if(denominator != 1):
        ret += [str(coefficient),"/",str(denominator)]
    elif(coefficient != 1):
        ret.append(str(coefficient))
    ret += ["x","^",str(power)]
    return ret


while index<n:
    cur = []
    if(string[index] == "-" or string[index] == "+"):
        cur.append(string[index])
        index += 1
    #先处理系数
    while(index<n and string[index] != "-" and string[index]!= "+"):
        cur.append(string[index])
        index += 1
    ans += calculate("".join(cur))

print("".join(ans))
