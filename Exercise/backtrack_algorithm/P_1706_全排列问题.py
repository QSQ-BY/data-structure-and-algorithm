""" 题目描述
按照字典序输出自然数 1 到 n 所有不重复的排列，即 n 的全排列，要求所产生的任一数字序列中不允许出现重复的数字。

输入格式
一个整数 n。

输出格式
由 1∼n 组成的所有不重复的数字序列，每行一个序列。

每个数字保留 5 个场宽。

输入输出样例
输入 #1复制

3
输出 #1复制

    1    2    3
    1    3    2
    2    1    3
    2    3    1
    3    1    2
    3    2    1
说明/提示
1≤n≤9。 """
#输出一个数字的全排列
import sys
input = sys.stdin.buffer.readline
n = int(input())
arr = [0]*(n)

def print_an_answer(ans:list):
    for i in range(len(ans)):
        ans[i] = str(ans[i])
    ans = [""] + ans
    print("    ".join(ans))

#即将填入第几个位置的数字，当前可选数字状态掩码
def dfs(pos:int,state:int):
    global arr
    if(pos == n):
        print_an_answer(arr)
        return
    temp = state
    while(temp != 0):
        bit = (-temp &temp)
        new_number = bit.bit_length()
        arr[pos] = new_number
        next_state = state^bit
        dfs(pos+1,next_state)
        arr[pos] = 0
        temp -= (-temp & temp)

original_state = (1<<n) - 1
dfs(0,original_state)
