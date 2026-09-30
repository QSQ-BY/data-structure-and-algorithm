""" 题目描述
Freda 和 rainbow 饲养了 N(N≤18) 只小猫，这天，小猫们要去爬山。经历了千辛万苦，小猫们终于爬上了山顶，但是疲倦的它们再也不想徒步走下山了。

Freda 和 rainbow 只好花钱让它们坐索道下山。索道上的缆车最大承重量为 W，而 N 只小猫的重量分别是 C 
1
​
 ,C 
2
​
 ,…C 
N
​
 。当然，每辆缆车上的小猫的重量之和不能超过 W(1≤C 
i
​
 ,W≤10 
8
 )。每租用一辆缆车，Freda 和 rainbow 就要付 1 美元，所以他们想知道，最少需要付多少美元才能把这 N 只小猫都运送下山？

输入格式
第一行包含两个用空格隔开的整数，N 和 W。 接下来 N 行每行一个整数，其中第 i+1 行的整数表示第 i 只小猫的重量 C 
i
​
 。

输出格式
输出一个整数，最少需要多少美元，也就是最少需要多少辆缆车。

输入输出样例
输入 #1复制

5 1996
1
2
1994
12
29
输出 #1复制

2 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,limit = read()
weight = []
for _ in range(n):
    number = int(input())
    weight.append(number)

if(n <= 0):
    print(0)
    sys.exit()
depth = 1
#现在一共有多少组cnt，s数组记录现在每一组的总重量，index现在将要处理哪一个,depth深度
def dfs(cnt:int,s:list,index:int,depth:int):
    if(cnt > depth):
        return False
    if(index >= n):
        return True
    w = weight[index]
    if(w > limit):
        return False
    target = -1
    for i in range(cnt):
        if(s[i] + w <= limit):
            next_s = s.copy()
            next_s[i] += w
            next_cnt = cnt
            if(dfs(cnt,next_s,index + 1,depth)):
                return True
    else:
        next_s = s.copy()
        next_s.append(w)
        next_cnt = cnt+1
        if(dfs(next_cnt,next_s,index+1,depth)):
            return True
    return False

while dfs(0,[],0,depth) == False:
    depth += 1
print(depth)