""" 题目描述
为了对抗附近恶意国家的威胁，R 国更新了他们的导弹防御系统。

一套防御系统的导弹拦截高度要么一直严格单调上升要么一直严格单调下降。

例如，一套系统先后拦截了高度为 3 和高度为 4 的两发导弹，那么接下来该系统就只能拦截高度大于 4 的导弹。

给定即将袭来的一系列导弹的高度，请你求出至少需要多少套防御系统，就可以将它们全部击落。

输入格式
输入包含多组测试用例。

对于每个测试用例，第一行包含整数 n，表示来袭导弹数量。

第二行包含 n 个不同的整数，表示每个导弹的高度。

当输入测试用例 n=0 时，表示输入终止，且该用例无需处理。

输出格式
对于每个测试用例，输出一行，一个整数，表示所需的防御系统数量。

输入输出样例
输入 #1复制

5 
3 5 2 4 1 
0
输出 #1复制

2
说明/提示
样例解释
对于样例，需要两套系统。一套击落高度为 3,4 的导弹，另一套击落高度为 5,2,1 的导弹。

数据规模与约定
1≤n≤50。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
ans = []

def solve(n:int,arr:list)->int:
    up = [0]*(n)#用来记录每一组上升序列末尾的值
    down = [0]*(n)#用来记录每一组下降序列末尾的值
    #当前所处理的导弹的编号，
    # 当前已经有多少个上升系统，
    # 当前已经有多少个下降系统
    #当前递归的深度
    def dfs(index,su,sd,depth):
        if(su + sd > depth):
            return False
        if(index == n):
            return True
        number = arr[index]
        k = -1

        for i in range(su):
            if(number > up[i]):
                if(k==-1 or up[i] > up[k]):
                    k = i
        if(k != -1):
            temp = up[k]
            up[k] = number
            if dfs(index+1,su,sd,depth):
                return True
            up[k] = temp
        else:
            up[su] = number
            if(dfs(index+1,su+1,sd,depth)):
                return True

        k = -1
        for i in range(sd):
            if down[i] > number:
                if k == -1 or down[i] < down[k]:
                    k = i
        if k != -1:
            # 加入已有下降系统
            old = down[k]
            down[k] = number
            if dfs(index + 1, su, sd,depth):
                return True
            down[k] = old
        else:
            # 新建下降系统
            down[sd] = number
            if dfs(index + 1, su, sd + 1,depth):
                return True

        return False

    depth = 1
    while True:
        if(dfs(0,0,0,depth)):
            return depth
        depth += 1

while True:
    n = int(input())
    if(n == 0):
        break
    arr = list(read())
    ans.append(solve(n,arr))

for number in ans:
    print(number)
