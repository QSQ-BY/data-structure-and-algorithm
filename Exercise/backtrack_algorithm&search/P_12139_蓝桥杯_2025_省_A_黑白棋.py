""" 题目描述
小蓝最近迷上了一款名为“黑白棋填充”的游戏。该游戏在一个方形网格棋盘上进行，其中部分格子已经填有黑色或白色的棋子，而其他格子为空，等待玩家填入棋子。

游戏规则是，玩家需要按照以下规则填满整个棋盘，才能算作胜利：

黑白棋子数量均等：
在每一行和每一列中，黑色棋子和白色棋子的数量必须相等。
相邻棋子限制：
在棋盘的任何一行或一列中，不能有超过两个相同颜色的棋子连续排列（即不允许出现“黑黑黑”或“白白白”的情况）。
行列唯一性：
每一行的棋子排列方式必须是唯一的，不能与棋盘中的任何其他行完全相同。
每一列的棋子排列方式必须是唯一的，不能与棋盘中的任何其他列完全相同。
行与列之间的棋子排列不作比较，即行可以与列相同，无需满足行列间的唯一性。


现在有一个 6×6 的棋盘，如上图所示，其中部分格子已填入棋子（黑色或白色），其余格子需要你填充，题目保证有唯一解。

请给出唯一的正确解，并按照以下格式输出答案：

黑色棋子用 1 表示，白色棋子用 0 表示。
从左到右、从上到下的顺序，依次遍历棋盘上的所有格子，并将这些值拼接成一个长度为 36 的字符串。
例如，假设最终填充完成后的棋盘如下（仅为示例，并非真实答案）：

1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 0 0
0 0 1 1 0 0
0 0 1 1 1 1

则输出结果应为：100000000000000000001000001100001111。

输入格式
无

输出格式
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只需要编写一个程序输出这个整数，输出多余的内容将无法得分。

输入输出样例
无 """

g = [
    [1,0,-1,0,-1,-1],
    [-1,-1,-1,0,-1,-1],
    [-1,-1,-1,-1,0,0],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,1,-1,-1,1],
    [-1,0,-1,-1,1,-1],
]

row_set = set()
column_set = set()

def print_ans():
    ans = []
    for i in range(6):
        for j in range(6):
            ans.append(str(g[i][j]))
    print("".join(ans))

def check(x,y):
    row = g[x]
    column = [g[i][y] for i in range(6)]

    for line in (row,column):
        # 每种颜色最多三个；填满后自然各有三个。
        if(line.count(0) > 3 or line.count(1) > 3):
            return False

    # 遍历到行末、列末时，用集合检查重复。
    if(y == 5):
        row_code = "".join(map(str,row))
        if(row_code in row_set):
            return False
    if(x == 5):
        column_code = "".join(map(str,column))
        if(column_code in column_set):
            return False

    # 全部检查通过后再加入，避免失败时留下部分状态。
    if(y == 5):
        row_set.add(row_code)
    if(x == 5):
        column_set.add(column_code)
    return True

def dfs(index):
    if(index == 36):
        print_ans()
        return
    x,y = divmod(index,6)
    one_available = True
    zero_available = True
    if(x - 2 >= 0 and g[x-1][y] == 1 and g[x-2][y] == 1):
        one_available = False
    if(x - 2 >= 0 and g[x-1][y] == 0 and g[x-2][y] == 0):
        zero_available = False
    if(y - 2 >= 0 and g[x][y-1] == 1 and g[x][y-2] == 1):
        one_available = False
    if(y - 2 >= 0 and g[x][y-1] == 0 and g[x][y-2] == 0):
        zero_available = False

    if(g[x][y] != -1):
        # 预填棋子同样不能与前两个棋子组成三连。
        if(g[x][y] == 1 and not one_available):
            return
        if(g[x][y] == 0 and not zero_available):
            return
        if(check(x,y)):
            dfs(index+1)
            if(y == 5):
                row_set.remove("".join(map(str,g[x])))
            if(x == 5):
                column_set.remove("".join(str(g[i][y]) for i in range(6)))
        return

    if(one_available):
        g[x][y] = 1
        if(check(x,y)):
            dfs(index+1)
            if(y == 5):
                row_set.remove("".join(map(str,g[x])))
            if(x == 5):
                column_set.remove("".join(str(g[i][y]) for i in range(6)))
        g[x][y] = -1
    if(zero_available):
        g[x][y] = 0
        if(check(x,y)):
            dfs(index+1)
            if(y == 5):
                row_set.remove("".join(map(str,g[x])))
            if(x == 5):
                column_set.remove("".join(str(g[i][y]) for i in range(6)))
        g[x][y] = -1
    return

dfs(0)

