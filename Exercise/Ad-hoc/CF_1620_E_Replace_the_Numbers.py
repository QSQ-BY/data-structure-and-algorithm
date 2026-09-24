""" 题目描述
你有一个整数数组（初始为空）。

你需要进行 q 次操作。每次操作有两种类型之一：

“1 x” —— 将元素 x 添加到数组末尾；
“2 x y” —— 将数组中所有等于 x 的元素替换为 y。
请在所有操作完成后，输出最终的数组。

输入格式
第一行包含一个整数 q（1≤q≤5⋅10 
5
 ），表示操作次数。

接下来的 q 行，每行一个操作（每行一个操作）。

每个操作有两种类型之一：

“1 x” （1≤x≤5⋅10 
5
 ）；
“2 x y” （1≤x,y≤5⋅10 
5
 ）。
保证至少有一次第一种类型的操作。

输出格式
在一行中输出 k 个整数，表示所有操作完成后得到的数组，其中 k 是第一种类型操作的次数。

输入输出样例
输入 #1复制

7
1 3
1 1
2 1 2
1 2
1 1
1 2
2 1 3
输出 #1复制

3 2 2 3 2
输入 #2复制

4
1 1
1 2
1 1
2 2 2
输出 #2复制

1 2 1
输入 #3复制

8
2 1 4
1 1
1 4
1 2
2 2 4
2 4 3
1 2
2 2 7
输出 #3复制

1 3 3 7
说明/提示
在第一个样例中，数组变化如下：

[]→[3]→[3,1]→[3,2]→[3,2,2]→[3,2,2,1]→[3,2,2,1,2]→[3,2,2,3,2]。

在第二个样例中，数组变化如下：

[]→[1]→[1,2]→[1,2,1]→[1,2,1]。

在第三个样例中，数组变化如下：

[]→[]→[1]→[1,4]→[1,4,2]→[1,4,4]→[1,3,3]→[1,3,3,2]→[1,3,3,7]。

由 ChatGPT 4.1 翻译 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

q = int(input())
arr = []
replace = {}
operations = []
for i in range(q):
    operation = tuple(read())
    operations.append(operation)
for operation in reversed(operations):
    scode = operation[0]
    match(scode):
        case 1:
            number = operation[1]
            arr.append(replace.get(number,number))
        case 2:
            x, y = operation[1], operation[2]
            # x -> y
            # 而 y 之后可能还会继续变化
            replace[x] = replace.get(y, y)

arr.reverse()
print(*arr)
