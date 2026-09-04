""" 题目描述
数独是根据 9×9 盘面上的已知数字，推理出所有剩余空格的数字，并满足每一行、每一列、每一个粗线宫内的数字均含 1∼9，不重复。每一道合格的数独谜题都有且仅有唯一答案，推理方法也以此为基础，任何无解或多解的题目都是不合格的。

芬兰一位数学家号称设计出全球最难的“数独游戏”，并刊登在报纸上，让大家去挑战。

这位数学家说，他相信只有“智慧最顶尖”的人才有可能破解这个“数独之谜”。

据介绍，目前数独游戏的难度的等级有一到五级，一是入门等级，五则比较难。不过这位数学家说，他所设计的数独游戏难度等级是十一，可以说是所有数独游戏中，难度最高的等级。他还表示，他目前还没遇到解不出来的数独游戏，因此他认为“最具挑战性”的数独游戏并没有出现。

输入格式
一个未填的数独。

输出格式
填好的数独。

输入输出样例
输入 #1复制

8 0 0 0 0 0 0 0 0 
0 0 3 6 0 0 0 0 0 
0 7 0 0 9 0 2 0 0 
0 5 0 0 0 7 0 0 0 
0 0 0 0 4 5 7 0 0 
0 0 0 1 0 0 0 3 0 
0 0 1 0 0 0 0 6 8 
0 0 8 5 0 0 0 1 0 
0 9 0 0 0 0 4 0 0
输出 #1复制

8 1 2 7 5 3 6 4 9 
9 4 3 6 8 2 1 7 5 
6 7 5 4 9 1 2 8 3 
1 5 4 2 3 7 8 9 6 
3 6 9 8 4 5 7 2 1 
2 8 7 1 6 9 5 3 4 
5 2 1 9 7 4 3 6 8 
4 3 8 5 2 6 9 1 7 
7 9 6 3 1 8 4 5 2
说明/提示
2022-04-17 @farteryhr 贡献了三组 hack 数据。加入了其中两组。第三组过强（来源：https://www.dcc.fc.up.pt/~acm/sudoku.pdf），放在下边供自测。

9 0 0 8 0 0 0 0 0
0 0 0 0 0 0 5 0 0 
0 0 0 0 0 0 0 0 0 
0 2 0 0 1 0 0 0 3
0 1 0 0 0 0 0 6 0
0 0 0 4 0 0 0 7 0
7 0 8 6 0 0 0 0 0 
0 0 0 0 3 0 1 0 0 
4 0 0 0 0 0 2 0 0 

输出

9 7 2 8 5 3 6 1 4 
1 4 6 2 7 9 5 3 8 
5 8 3 1 4 6 7 2 9 
6 2 4 7 1 8 9 5 3 
8 1 7 3 9 5 4 6 2 
3 5 9 4 6 2 8 7 1 
7 9 8 6 2 1 3 4 5 
2 6 5 9 3 4 1 8 7 
4 3 1 5 8 7 2 9 6  """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
def test01():
    g = [[] for _ in range(9)]
    for i in range(9):
        g[i] = list(read())
    start_x = 0
    start_y = 0
    row_mask = [(1<<(9)) - 1]*9#每一行的状态掩码
    column_mask = [(1<<(9)) - 1]*9#每一列的状态掩码
    block_mask = [(1<<(9)) - 1]*9#九宫格状态掩码
    flag = 1
    for i in range(9):
        for j in range(9):
            if(g[i][j] == 0 and flag == 1):
                start_x = i
                start_y = j
                flag = 0
            elif(g[i][j] != 0):
                block_index = (i // 3) * 3 + j // 3
                row_mask[i] = row_mask[i]^(1<<(g[i][j] - 1))
                column_mask[j] = column_mask[j]^(1<<(g[i][j] - 1))
                block_mask[block_index] = block_mask[block_index]^(1<<(g[i][j] - 1))

    start = start_y + start_x * 9
    def dfs(pos)->bool:
        global g
        if(pos == 81):
            return True
        x = pos//9
        y = pos%9
        block = (x // 3) * 3 + y // 3
        if(g[x][y] != 0):
            return dfs(pos+1)

        #枚举可以填入的数字
        mask = row_mask[x] & column_mask[y] & block_mask[block]
        temp = mask
        while(temp != 0):
            bit = (-temp & temp)
            number = bit.bit_length()
            g[x][y] = number
            row_mask[x] = row_mask[x]^(1<<(number - 1))
            column_mask[y] = column_mask[y]^(1<<(number - 1))
            block_mask[block] = block_mask[block]^(1<<(number - 1))
            if(dfs(pos+1)):
                return True
            row_mask[x] = row_mask[x]^(1<<(number - 1))
            column_mask[y] = column_mask[y]^(1<<(number - 1))
            block_mask[block] = block_mask[block]^(1<<(number - 1))
            g[x][y] = 0
            temp -= (-temp & temp)
        return False

    if(dfs(start)):
        for i in range(9):
            print(*g[i])

def test02():
    ALL = (1<<9) - 1
    g = [[] for _ in range(9)]
    for i in range(9):
        g[i] = list(read())
    row_mask = [ALL] * 9
    column_mask = [ALL] * 9
    block_mask = [ALL] * 9

    #保存所有空格：（行，列，九宫格编号）
    empty_cells = []
    for x in range(9):
        for y in range(9):
            number = g[x][y]
            block = (x//3)*3 + y//3
            if(number == 0):
                empty_cells.append((x,y,block))
            else:
                bit = 1<<(number-1)
                row_mask[x] = row_mask[x]^bit
                column_mask[y] = column_mask[y]^bit
                block_mask[block] = block_mask[block]^bit

    def dfs(index):
        if(index == len(empty_cells)):
            return True
        #MRV:选择候选数字最少的空格
        best_index = index
        best_mask = 0
        minimum_count = 10
        for i in range(index,len(empty_cells)):
            x,y,block = empty_cells[i]
            mask = (row_mask[x] & column_mask[y] & block_mask[block])
            count = mask.bit_count()
            if(count < minimum_count):
                minimum_count = count
                best_index = i
                best_mask = mask

        if(minimum_count == 0):
            return False
        # 把候选最少的空格交换到当前位置
        empty_cells[index], empty_cells[best_index] = (
            empty_cells[best_index],
            empty_cells[index],
        )
        x, y, block = empty_cells[index]
        mask = best_mask

        while mask:
            # 取出最低位的 1
            bit = mask & -mask
            number = bit.bit_length()

            g[x][y] = number
            row_mask[x] ^= bit
            column_mask[y] ^= bit
            block_mask[block] ^= bit

            if dfs(index + 1):
                return True

            # 回溯，恢复现场
            row_mask[x] ^= bit
            column_mask[y] ^= bit
            block_mask[block] ^= bit
            g[x][y] = 0

            mask -= bit
        # 当前空格所有候选均失败，恢复空格顺序
        empty_cells[index], empty_cells[best_index] = (
            empty_cells[best_index],
            empty_cells[index],
        )

        return False
    if(dfs(0)):
        for row in g:
            print(*row)

test02()