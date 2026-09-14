import sys
import math
ans = 0
N = 5
sys.setrecursionlimit(1000000)
def check(g:list[list[int]])->bool:
    sum = 0
    for i in range(5):
        sum+=g[i][i]
    if(sum==0 or sum==5):
        return False

    sum = 0
    for i in range(5):
        sum+=g[i][4-i]
    if(sum == 0 or sum==5):
        return False
    
    sum = 0
    for i in range(5):
        sum = 0
        for j in range(5):
            sum+=g[i][j]
        if(sum == 0 or sum==5):
            return False
        
    sum = 0
    for i in range(5):
        sum = 0
        for j in range(5):
            sum+=g[j][i]
        if(sum==0 or sum==5):
            return False
    return True

def dfs(
    g: list[list[int]],
    pos: int,
    white_left: int,
    black_left: int
) -> None:
    global ans

    # 25 个格子全部填完
    if pos == N * N:
        if check(g):
            ans += 1
        return

    x, y = divmod(pos, N)

    # 当前格子放白棋
    if white_left > 0:
        g[x][y] = 1
        dfs(g, pos + 1, white_left - 1, black_left)

    # 当前格子放黑棋
    if black_left > 0:
        g[x][y] = 0
        dfs(g, pos + 1, white_left, black_left - 1)

    # 回溯，恢复为空格
    g[x][y] = -1


def main() -> None:
    # -1 表示空格，1 表示白棋，0 表示黑棋
    g = [[-1] * N for _ in range(N)]

    # 白棋先手，所以最终有 13 枚白棋、12 枚黑棋
    dfs(g, 0, 13, 12)

    print(ans)


if __name__ == "__main__":
    main()