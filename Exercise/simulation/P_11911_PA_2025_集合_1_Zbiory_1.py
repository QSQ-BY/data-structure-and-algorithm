""" PA 2025 trial round t1.

由于评测机性能差距，微调了 TL 和 ML。

请注意本题非同寻常的时空限制。

题目描述
给定正整数 n,m。定义全集 U={1,2,…,n}。

构造 (n+m) 个集合 A 
1
​
 ,A 
2
​
 ,…,A 
n+m
​
 ：

对于 1≤i≤n，A 
i
​
  里的元素为 U 中 i 的倍数。

对于 n+1≤i≤n+m，给定参数 op 
i
​
 ：

当 op 
i
​
 =1 时，给定参数 x,y，则 A 
i
​
 =A 
x
​
 ∪A 
y
​
 ；
当 op 
i
​
 =2 时，给定参数 x,y，则 A 
i
​
 =A 
x
​
 ∩A 
y
​
 ；
当 op 
i
​
 =3 时，给定参数 x，则 A 
i
​
 =U 
x
​
 （即 A 
i
​
 ={j:j∈U,j

∈A 
x
​
 }）。
接着有 q 次询问，每次询问给定两个正整数 x,y，问是否有 y∈A 
x
​
 。

输入格式
第一行，三个正整数 n,m,q。

以下 m 行，第 i 行要么是 1 或 2 后面跟两个正整数，要么是 3 后面跟一个正整数，表示第 n+i 个集合的构造方式。

接下来 q 行，每行两个正整数 x,y（1≤x≤n+m, 1≤y≤n），表示一次询问。

输出格式
对于每组询问，输出一行，如果 y∈A 
x
​
 ，输出 TAK，否则输出 NIE。

输入输出样例
输入 #1复制

7 8 9
1 5 7
2 2 3
3 8
2 10 8
3 3
1 12 12
2 10 13
1 9 14
2 4
5 7
11 5
15 1
15 2
15 3
15 4
15 5
15 6
输出 #1复制

TAK
NIE
NIE
TAK
TAK
NIE
TAK
NIE
TAK
说明/提示
1≤n≤5×10 
4
 ；
1≤m≤4×10 
5
 ；
1≤q≤10 
6
 ；
1≤x 
i
​
 ,y 
i
​
 <n+i。 """

import sys
def main():
    input = sys.stdin.buffer.readline
    n, m, q = map(int, input().split())

    # state[i] 是 A_i 的整数位集，第 y-1 位表示元素 y 是否属于 A_i。
    state = [0] * (n + m + 1)
    universe = (1 << n) - 1
    state[1] = universe

    # 直接设置整数的二进制位，元素 y 对应第 y-1 位。
    for i in range(2, n + 1):
        value = 0
        for y in range(i, n + 1, i):
            value |= 1 << (y - 1)
        state[i] = value

    # 引用的集合编号总是更小，因此可以按输入顺序直接构造。
    for i in range(n + 1, n + m + 1):
        operation = list(map(int, input().split()))
        op, x = operation[0], operation[1]
        if op == 1:
            state[i] = state[x] | state[operation[2]]
        elif op == 2:
            state[i] = state[x] & state[operation[2]]
        else:
            # 只翻转全集内的 n 位；直接用 ~ 会产生负数。
            state[i] = universe ^ state[x]

    answers = []
    for _ in range(q):
        x, y = map(int, input().split())
        answers.append('TAK\n' if (state[x] >> (y - 1)) & 1 else 'NIE\n')
    sys.stdout.write(''.join(answers))

if __name__ == '__main__':
    main()
