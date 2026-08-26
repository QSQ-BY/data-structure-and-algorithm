#check(i)表示在L的数值为i的时候能不能完成
""" 题目描述
在运动会上，小明从数轴的原点开始向正方向立定跳远。项目设置了 n 个检查点 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
  且 a 
i
​
 ≥a 
i−1
​
 >0。小明必须先后跳跃到每个检查点上且只能跳跃到检查点上。同时，小明可以自行再增加 m 个检查点让自己跳得更轻松。

在运动会前，小明制定训练计划让自己单次跳跃的最远距离达到 L，并且学会一个爆发技能可以在运动会时使用一次，使用时可以在该次跳跃时的最远距离变为 2L。小明想知道，L 的最小值是多少可以完成这个项目？

输入格式
输入共 2 行。

第一行为两个正整数 n,m。

第二行为 n 个由空格分开的正整数 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 。

输出格式
输出共 1 行，一个整数表示答案。

输入输出样例
输入 #1复制

5 3
1 3 5 16 21
输出 #1复制

3
说明/提示
【样例说明】

增加检查点 10,13,19，因此每次跳跃距离为 1,2,2,5,3,3,3,2，在第三次跳跃时使用技能即可。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n, m = read()
arr = list(read())
left = 1
right = arr[-1]

def check(l : int)->int:
    global arr
    global m
    temp = m
    pos = 0
    temp += 1#小明的技能和可插入的新检查点的作用本质是一样的
    index = 0#index表示小明要跳的下一个检查点
    while(pos != arr[-1] and index < len(arr)):
        if(temp < 0):
            return 0
        distance = arr[index] - pos
        if(l>=distance):
            pos = arr[index]
            index += 1
        elif(distance > l):
            jump = l
            while(jump <distance):
                jump += l
                temp -= 1
                if(temp<0):
                    return 0
            pos = arr[index]
            index += 1
    if(temp>=0):
        return 1


while(left < right):
    mid = (left + right)//2
    if(check(mid) == 1):
        right = mid
    else:
        left = mid+1
print(left)