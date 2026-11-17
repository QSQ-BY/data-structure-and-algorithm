import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
t = int(input())
for _ in range(t):
    n,k = read()#选手的数量和比赛进行的回合数
    a = list(read())
    if(k == 0):
        print(*a)
        continue
    def simulation(arr:list,m:int)->list:
        ret = deque(arr)
        for i in range(m):
            if(ret[0] > ret[1]):
                head = ret.popleft()
                tail = ret.popleft()
                ret.append(tail)
                ret.appendleft(head)
            elif(ret[0] < ret[1]):
                tail = ret.popleft()
                ret.append(tail)
        return list(ret)

    if(k>=n-1):#进行n-1轮的比赛，后面的每一个选手都会参加一次
        pass
    else:
        new_arr = simulation(a,k)#直接模拟n-1轮的比赛
        print(*new_arr)
        continue
    new_arr = simulation(a,n-1)#先模拟n-1轮的比赛,之后肯定可以进入循环
    k = k%(n-1)
    if(k == 0):
        print(*new_arr)
        continue
    ans = [new_arr[0]] + new_arr[k+1:] + (new_arr[1:k+1])
    print(*ans)
