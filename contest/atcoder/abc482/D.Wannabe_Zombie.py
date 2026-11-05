""" Problem Statement  问题描述
There are 
N people, numbered 
1 to 
N, standing on a number line.
有 
N 个人，他们的编号分别是 
1 到 
N ，他们站在数轴上。
Person 
i is standing at coordinate 
X 
i
​
 . Here, 
X 
i
​
  is even for 
i=1,2,…,N, and 
X 
1
​
 <X 
2
​
 <⋯<X 
N
​
  holds.
用户 
i 位于坐标 
X 
i
​
  处。此时， 
X 
i
​
  的值与 
i=1,2,…,N 相等，而 
X 
1
​
 <X 
2
​
 <⋯<X 
N
​
  的数值保持不变。

For each 
k=1,2,…,N, solve the following problem.
对于每一个 
k=1,2,…,N ，请解决以下问题。

At time 
0, person 
k becomes a zombie. Everyone other than person 
k remains human.
在时间 
0 时，人物 
k 变成了僵尸。除了人物 
k 之外，其他所有人仍然保持人类形态。
From time 
0 onward, humans and zombies can move freely on the number line at a speed of at most 
1 per unit time.
从时间 
0 开始，人类和僵尸可以在数轴上自由移动，其移动速度每单位时间最多为 
1 。
When a zombie and a human are at the same coordinate, that human becomes a zombie.
当僵尸和人类处于同一坐标位置时，那个人类就会变成僵尸。
Find the minimum possible time at which everyone has become a zombie.
找出让所有人都变成僵尸所需的最短时间。

It can be proved that the answer is an integer under the constraints of this problem.
可以证明，在该问题的约束条件下，答案一定是一个整数。

Constraints  约束
1≤N≤2×10 
5
 
0≤X 
1
​
 <X 
2
​
 <⋯<X 
N
​
 ≤10 
9
 
X 
i
​
  is even.   
X 
i
​
  是偶数。
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

N
X 
1
​
  
X 
2
​
  
… 
X 
N
​
 
Output  输出结果
Print 
N lines. The 
i-th line 
(1≤i≤N) should contain the answer to the problem for 
k=i.
打印 
N 行内容。第 
i 行中，第 
(1≤i≤N) 个字符应包含 
k=i 这个问题的答案。

Sample Input 1  示例输入 1 复制
Copy  副本
5
2 4 10 14 18
Sample Output 1  示例输出 1 复制
Copy  副本
8
7
6
6
8
For 
k=1, if person 
1 moves in the positive direction of the number line at speed 
1 and persons 
2,3,4,5 move in the negative direction at speed 
1, everyone will have become a zombie by time 
8.
对于 
k=1 来说，如果人物 
1 以速度 
1 沿数轴的正方向移动，而人物 
2,3,4,5 以速度 
1 沿数轴的负方向移动，那么到时间 
8 时，所有人都会变成僵尸。

For 
k=2, if each person moves as follows, everyone will have become a zombie by time 
7.
对于 
k=2 来说，如果每个人都按照这样的方式行动，那么到 
7 时刻时，所有人都会变成僵尸。

Person 
1: Moves in the positive direction at speed 
1.
用户 
1 ：以速度 
1 向正方向移动。
Person 
2: Moves in the positive direction at speed 
1 until time 
3, and in the negative direction at speed 
1 from time 
3 onward.
用户 
2 ：在时间点 
3 之前，以速度 
1 向正方向移动；从时间点 
3 开始，则以速度 
1 向负方向移动。
Person 
3: Moves in the negative direction at speed 
1 until time 
3, and in the positive direction at speed 
1 from time 
3 onward.
用户 
3 ：在时间点 
3 之前，以速度 
1 向负方向移动；从时间点 
3 开始，则以速度 
1 向正方向移动。
Person 
4: Moves in the negative direction at speed 
1.
人 
4 ：以速度 
1 向负方向移动。
Person 
5: Moves in the negative direction at speed 
1.
人 
5 ：以速度 
1 向负方向移动。
Sample Input 2  示例输入 2 复制
Copy  副本
9
140322306 171833796 356303608 595703832 701965684 798563428 857902324 933683272 971602066
Sample Output 2  示例输出 2 复制
Copy  副本
415639880
399884135
307649229
280821689
280821689
329120561
358790009
396680483
415639880 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
pos = list(read())
#特殊情况讨论
if(n == 1):
    print(0)
    sys.exit()
if(n==2):
    print(((pos[-1]-pos[0])+1)//2)
    print(((pos[-1]-pos[0])+1)//2)
    sys.exit()
if(n==3):
    print(((pos[-1]-pos[0])+1)//2)
    print(((pos[-1]-pos[0])+1)//2)
    print(((pos[-1]-pos[0])+1)//2)
    sys.exit()
    sys.exit()

ans = []
for i in range(n):
    if i == 0 or i == n - 1:
        ans.append((pos[-1] - pos[0]+1) // 2)
    else:
        # 先感染左侧相邻的人
        left = max(
            (pos[i] - pos[0]+1) // 2,
            (pos[-1] - pos[i - 1]+1) // 2
        )

        # 先感染右侧相邻的人
        right = max(
            (pos[-1] - pos[i]+1) // 2,
            (pos[i + 1] - pos[0]+1) // 2
        )

        ans.append(min(left, right))

print('\n'.join(map(str, ans)))