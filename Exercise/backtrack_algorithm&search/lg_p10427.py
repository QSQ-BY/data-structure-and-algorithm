import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())

ans = []
n = 1
k = 1
dir = [
    [-1,-1],[0,-1],[1,-1],[1,0],
    [1,1],[0,1],[-1,1],[-1,0]
]
dir_ans = [0,1,2,3,4,5,6,7]
dir.reverse()#返回值是none，原地翻转
def dfs(pos:int,g:list[list[int]],visit:int,diagonal_visit:int,cur_number:int)->bool:
    global n
    global k
    global ans
    global dir
    global dir_ans
    if(visit == 0 and pos == (n)*(n)-1):
        return True
    if(pos == ((n)*(n)-1) and visit!=0):
        return False
    cur_x = pos//n
    cur_y = pos%n
    next_number = (cur_number%k+1)%k
    for i in range(8):
        dx = cur_x + dir[i][0]
        dy = cur_y + dir[i][1]
        if(dx<0 or dx>=n or dy<0 or dy>=n): continue
        if(g[dx][dy] != next_number):continue
        next_pos = dy + dx*n
        if((visit>>next_pos) % 2 == 0): continue
        new_diagonal_visit = diagonal_visit
        if(abs(cur_x-dx)==1 and abs(cur_y - dy)==1):
            diagonal_x = min(cur_x,dx)
            diagonal_y = min(cur_y,dy)
            diagonal_pos = diagonal_x*(n-1) + diagonal_y
            diagonal_bit = 1<<diagonal_pos
            if(((diagonal_visit^diagonal_bit)>>diagonal_pos)%2 == 0):
                continue
            else :
                new_diagonal_visit = diagonal_bit^diagonal_visit
        next_visit = (1<<next_pos)^visit
        ans.append(dir_ans[i])
        temp_ans = dfs(next_pos,g,next_visit,new_diagonal_visit,next_number)
        if(temp_ans == True):
            return True
        ans.pop()
    return False


def main()->None:
    global n
    global k
    global ans
    global dir
    global dir_ans
    n,k = read()
    g = [[0]*n for _ in range(n)]
    for i in range(n):
        g[i] = list(read())

    if(g[0][0] != 0):
        print(-1)
        return
    visit = (1<<(n*n))-2
    if(dfs(0,g,visit,0,0) == False):
        print(-1)
        return
    final = "".join(map(str,ans))
    print(final)

if( __name__ == "__main__"):
    main()