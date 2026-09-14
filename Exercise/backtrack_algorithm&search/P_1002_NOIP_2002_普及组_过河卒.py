import sys
from functools import cache
input = sys.stdin.buffer.readline
target_x,target_y,block_x,block_y = map(int,input().split())

blocks = set()
blocks.add((block_x,block_y))
dir = [
    (1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)
]
for (dx,dy) in dir:
    new_block_x = block_x + dx
    new_block_y = block_y + dy
    blocks.add((new_block_x,new_block_y))

if((target_x,target_y) in blocks):
    print(0)
    sys.exit()

dir2 = [
    (1,0),(0,1)
]

@cache
def dfs(cur_x:int,cur_y:int)->int:
    if((cur_x,cur_y) in blocks):
        return None
    elif(cur_x == target_x and cur_y == target_y):
        return 1

    ret = 0
    for (dx,dy) in dir2:
        next_x = cur_x + dx
        next_y = cur_y + dy
        if(next_x > target_x or next_y > target_y):
            continue
        if((next_x,next_y) in blocks):
            continue
        ret+=dfs(next_x,next_y)

    return ret

print(dfs(0,0))