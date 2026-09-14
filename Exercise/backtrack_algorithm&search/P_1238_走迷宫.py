""" 题目描述
农民 John 以拥有世界上最健康的奶牛为傲。他知道每种饲料中所包含的牛所需的最低的维他命量是多少。请你帮助农夫喂养他的牛，以保持它们的健康，使喂给牛的饲料的种数最少。

给出牛所需的最低的维他命量，输出喂给牛需要哪些种类的饲料，且所需的饲料剂量最少。

维他命量以整数表示，每种饲料最多只能对牛使用一次，数据保证存在解。

输入格式
第一行一个整数 v，表示需要的维他命的种类数。
第二行 v 个整数，表示牛每天需要的每种维他命的最小量。

第三行一个整数 g，表示可用来喂牛的饲料的种数。
下面 g 行，第 n 行表示编号为 n 饲料包含的各种维他命的量的多少。

输出格式
输出文件只有一行，包括牛必需的最小的饲料种数 p；后面有 p 个数，表示所选择的饲料编号（按从小到大排列）。

如果有多个解，输出饲料序号最小的（即字典序最小）。

输入输出样例
输入 #1复制

4
100 200 300 400
3
50  50  50  50
200 300 200 300
900 150 389 399
输出 #1复制

2 1 3 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,m = read()
g = [[0] + list(read())+ [0] for _ in range(n)]
g = [[0]*(m+2)] + g + [[0]*(m+2)]
startx,starty = read()
endx,endy = read()
ans = []
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
vis = [[False]*(m+2) for _ in range(n+2)]

def print_an_answer(answer:list):
    temp = answer[:]
    for index,(x,y) in enumerate(temp):
        temp[index] = f"({x},{y})"
    print("->".join(temp))
found = False
def dfs(cur_x:int,cur_y:int):
    global ans
    global found
    if(cur_x == endx and cur_y==endy):
        ans.append((endx,endy))
        if(found == False):
            found = True
        print_an_answer(ans)
        ans.pop()
        return

    if(g[cur_x][cur_y] == 0):
        return
    if(vis[cur_x][cur_y] == True):
        return
    vis[cur_x][cur_y] = True
    ans.append((cur_x,cur_y))
    for (dx,dy) in directions:
        nx = cur_x + dx
        ny = cur_y + dy
        dfs(nx,ny)
    ans.pop()
    vis[cur_x][cur_y] = False

dfs(startx,starty)
if(found == False):
    print(-1)
