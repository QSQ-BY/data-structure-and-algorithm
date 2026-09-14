""" 题目描述
小蓝最近迷上了宝塔游戏，这是一款迷宫填数游戏，玩家需要按照规则将高度为 1 至 N 的宝塔放置在一个 N×N 大小的水平放置的棋盘当中，每个宝塔占据棋盘的一个方格。具体规则如下：

宝塔的高度只有 1,2,…,N。
每一行、每一列中不可以出现相同高度的宝塔。
棋盘周围的箭头中的数字表示从这个位置看向棋盘时可以看到的宝塔个数。
下图 1 是一个棋盘以及答案以供参考。图 2 是你需要解决的问题，你需要输出 25 个数字表示答案，按照棋盘布局从左至右、从上至下的顺序输出即可。例如对于图 1 对应的棋盘而言，输出的答案是：1432432121433214。题目保证答案只有一个。



输入格式
无

输出格式
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只需要编写一个程序输出这个整数，输出多余的内容将无法得分。

输入输出样例
无 """
import sys
input = sys.stdin.buffer.readline
up = [2,2,1,3,3]
down = [1,4,2,2,3]
left = [2,2,3,2,1]
right = [3,3,1,2,4]
ans = []
n = 5
g = [[0]*n for _ in range(n)]
init_state = (1<<n) - 1
init_row_state = [init_state]*n
init_column_state = [init_state]*n
def check(up,down,left,right,g):
    for i in range(n):
        tallest = 0
        cur_left = 0
        cur_right = 0
        for j in range(n):
            if(g[i][j] > tallest):
                cur_left += 1
                tallest = g[i][j]
        tallest = 0
        for j in range(n-1,-1,-1):
            if(g[i][j] > tallest):
                cur_right += 1
                tallest = g[i][j]
        if(left[i] != cur_left or right[i] != cur_right):
            return False

    for j in range(n):
        tallest = 0
        cur_up = 0
        cur_down = 0
        for i in range(n):
            if(g[i][j] > tallest):
                cur_up += 1
                tallest = g[i][j]
        tallest = 0
        for i in range(n-1,-1,-1):
            if(g[i][j] > tallest):
                cur_down += 1
                tallest = g[i][j]
        if(up[j] != cur_up or down[j] != cur_down):
            return False
    return True


def dfs(pos,row_state,column_state)->bool:
    global g
    global ans
    if(pos == 25):
        return check(up,down,left,right,g)
    x,y = divmod(pos,5)
    cur_state = row_state[x] & column_state[y]
    temp = cur_state
    while temp:
        bit = -temp&temp
        next_number = bit.bit_length()
        ans.append(next_number)
        g[x][y] = next_number
        row_state[x] ^= bit
        column_state[y] ^= bit
        if(dfs(pos+1,row_state,column_state)):
            return True
        row_state[x] ^= bit
        column_state[y] ^= bit
        g[x][y] = 0
        ans.pop()
        temp -= bit
    return False

dfs(0,init_row_state,init_column_state)
print(*ans,sep = "")
