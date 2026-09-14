""" 题目描述
给定一个 3×3 的九宫格，每个格子内分别含有一个数字，每个格子里的数字互不相同。每步我们可以选择任意一个 2×2 的区域将其顺时针旋转，例如：

例如

1 2 3
4 5 6
7 8 9

将其旋转右上角，可得：

1 5 2
4 6 3
7 8 9

问最少需要几步才能将给定的状态旋转为

1 2 3
4 5 6
7 8 9

输入格式
输入的第一行包含一个整数 T 表示询问的组数。

接下来依次输入每组询问。

每组询问包含三行，每行包含三个数，表示询问的九宫格的状态。

输出格式
输出 T 行，每行包含一个整数表示本次询问的答案。

输入输出样例
输入 #1复制

2
1 2 3
4 5 6
7 8 9
1 5 2
4 6 3
7 8 9
输出 #1复制

0
3
说明/提示
对于 60% 的评测用例，T=1;
对于所有评测用例，T≤10 
5
 。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
# 从目标状态反向 BFS，使用逆时针旋转
def read():
    return map(int,input().split())

rotate = {
    (0,1,3,4) : (1,4,0,3),
    (1,2,4,5) : (2,5,1,4),
    (3,4,6,7) : (4,7,3,6),
    (4,5,7,8) : (5,8,4,7),
}
def solve()->dict:
    init = "123456789"
    q = deque()
    s = {init: 0}
    q.append((init,0))
    while(q):
        cur,step = q.popleft()
        cur = list(cur)
        for (pos1,pos2,pos3,pos4),(next1,next2,next3,next4) in rotate.items():
            next = cur.copy()
            next[pos1],next[pos2],next[pos3],next[pos4] = next[next1],next[next2],next[next3],next[next4]
            state = "".join(next)
            if(state in s):
                continue
            s[state] = step+1
            q.append((state,step+1))
    return s

def main():
    t = int(input())
    s = solve()
    ans = []
    while t:
        init = list(read()) + list(read()) + list(read())
        init = "".join(str(x) for x in init)
        ans.append(s[init])
        t -= 1
    for number in ans:
        print(number)

if __name__ == "__main__":
    main()
