""" 题目描述
给定 3 行 3 列的图像各像素点灰度值，给定最终图像，求最短、字典序最小的非空操作序列。

其中，可能的操作及对应字符有如下四种：

A：顺时针旋转 90 度；

B：逆时针旋转 90 度；

C：左右翻转；

D：上下翻转。

输入格式
一个矩阵，表示初始的图像。

一个矩阵，表示最终的图像。

输出格式
最短、字典序最小的非空操作序列，保证长度不超过 10 
8
 ，不保证有解。

若长度超过 10 
8
  无解则输出 Poland cannot into space!!! 。

输入输出样例
输入 #1复制

3 4 5
6 7 8
1 2 3
1 2 3
6 7 8
3 4 5
输出 #1复制

D
说明/提示
字符串长度不超过 10 
8
 。 """


#任何一个图形都可以只用四个操作中的两个得到
import sys
input = sys.stdin.buffer.readline

def read():
    return list(map(int, input().split()))


initial = []
target = []

for _ in range(3):
    initial.append(read())

for _ in range(3):
    target.append(read())


def operate(mat, op):
    # A：顺时针旋转90度
    if op == 'A':
        return [
            [mat[2][0], mat[1][0], mat[0][0]],
            [mat[2][1], mat[1][1], mat[0][1]],
            [mat[2][2], mat[1][2], mat[0][2]]
        ]

    # B：逆时针旋转90度
    elif op == 'B':
        return [
            [mat[0][2], mat[1][2], mat[2][2]],
            [mat[0][1], mat[1][1], mat[2][1]],
            [mat[0][0], mat[1][0], mat[2][0]]
        ]

    # C：左右翻转
    elif op == 'C':
        return [
            mat[0][::-1],
            mat[1][::-1],
            mat[2][::-1]
        ]

    # D：上下翻转
    else:
        return [
            mat[2][:],
            mat[1][:],
            mat[0][:]
        ]


operations = "ABCD"

# 先枚举长度为1
for a in operations:
    temp = operate(initial, a)

    if temp == target:
        print(a)
        sys.exit()

# 再枚举长度为2
for a in operations:
    for b in operations:
        temp = operate(initial, a)
        temp = operate(temp, b)

        if temp == target:
            print(a + b)
            sys.exit()


print("Poland cannot into space!!!")