""" 题目描述
给定一个栈，给出若干次如下类型的操作：

1 x: 将 x 加入栈顶。
2: 将栈顶的数弹出（如果栈是空的，则什么都不做）。
3 y: 查询栈内的最顶端 y 个数的乘积。如果大于等于 2 
32
 ，输出 OVERFLOW。如果栈内不足 y 个数，输出 ERROR。
输入格式
输入的第一行包含一个正整数 Q，表示操作次数。

接下来 Q 行，每行包含一个或两个正整数表示一个操作，如果一行包含两个整数，两个整数之间用一个空格分隔。

输出格式
对于每个 3 y 形式的操作，输出一行包含一个整数，表示答案。

输入输出样例
输入 #1复制

9
1 65536
1 65536
3 2
3 3
2
1 1024
1 2
3 2
3 3
输出 #1复制

OVERFLOW
ERROR
2048
134217728
说明/提示
评测用例规模与约定
对于 30% 的评测用例，Q≤5000；
对于所有评测用例，1≤Q≤10 
5
 ，0≤x<2 
30
 ，1≤y<2 
30
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
stack = []
limit = 2**32
zeros = []
factors = [] # 保存 (原栈下标, 数值)，只记录大于 1 的元素
for _ in range(n):
    data = list(read())
    scode = data[0]
    match(scode):
        case 1:
            number = data[1]
            pos = len(stack)
            stack.append(number)
            if number == 0:
                zeros.append(pos)
            elif number > 1:
                factors.append((pos, number))
        case 2:
            if(len(stack) == 0):
                continue
            else:
                number = stack.pop()
                if number == 0:
                    zeros.pop()
                elif number > 1:
                    factors.pop()
        case 3:
            y = data[1]
            if len(stack) < y:
                print("ERROR")
            else:
                left = len(stack) - y

                if zeros and zeros[-1] >= left:
                    print(0)
                else:
                    ans = 1
                    for pos, x in reversed(factors):
                        if pos < left:       # 已经超出查询范围
                            break
                        ans *= x
                        if ans >= limit:
                            break
                    print("OVERFLOW" if ans >= limit else ans)


