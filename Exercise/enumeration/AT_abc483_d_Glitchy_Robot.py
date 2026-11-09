""" D - Glitchy Robot 
D - 故障机器人编辑部 / 
Time Limit: 2 sec / Memory Limit: 1024 MiB
时间限制：2 秒 / 内存限制：1024 MiB

Score : 
400 points  得分： 
400 分

Problem Statement  问题描述
There is a robot on a number line. Initially, the robot is at coordinate 
0. Also, Takahashi has an integer sequence 
A=(A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ) of length 
N.
在数轴上有一个机器人，它初始位于坐标 
0 处。此外，Takahashi 还有一个整数序列，该序列的长度为 
N 。

Takahashi performs the following steps in order.
Takahashi 按照以下顺序执行各个步骤。

Choose at most 
1 element of 
A and flip its sign. That is, choose 
0 or 
1 index 
i satisfying 
1≤i≤N, and replace 
A 
i
​
  with 
−A 
i
​
 .
请选择 
A 中最多 
1 个元素，并使其符号反转。也就是说，选择满足 
1≤i≤N 条件的 
0 或 
1 索引 
i 元素，然后将 
A 
i
​
  替换为 
−A 
i
​
  。

Start the robot. After starting, the robot makes 
N moves. In the 
i-th move 
(1≤i≤N), letting 
x be its current coordinate, the robot moves in a straight line to coordinate 
x+A 
i
​
 .
启动机器人。启动后，机器人会进行 
N 次移动。在 
i 次移动中，当机器人位于 
x 坐标时，它会沿直线移动到 
x+A 
i
​
  坐标。

Takahashi wants to maximize the number of integer coordinates that the robot passes through at least once.
Takahashi 希望最大化机器人至少经过的整数坐标的数量。
Find the maximum possible value of "the number of integer coordinates that the robot passes through at least once" when Takahashi acts optimally.
当 Takahashi 采取最优行动时，机器人至少会经过多少个整数坐标点？请找出这个数值的最大值。

Here, the robot moves continuously. When a move takes the robot from coordinate 
S to coordinate 
T, it is considered to have passed through every integer coordinate between 
S and 
T, inclusive.
在这里，机器人持续地移动。当机器人的位置从坐标 
S 移动到坐标 
T 时，就表示它已经经过了从坐标 
S 到 
T 之间的每一个整数坐标点，包括这些点本身。

Constraints  约束
1≤N≤2×10 
5
 
−10 
9
 ≤A 
i
​
 ≤10 
9
 
A 
i
​
 

=0
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

N
A 
1
​
  
A 
2
​
  
⋯ 
A 
N
​
 
Output  输出结果
Print the maximum possible value of the number of integer coordinates that the robot passes through at least once when Takahashi acts optimally.
请输出在塔哈什优化操作下，机器人经过的整数坐标点数量的最大值。

Sample Input 1  示例输入 1 复制
Copy  副本
3
-2 3 -2
Sample Output 1  示例输出 1 复制
Copy  副本
8
Initially, 
A=(−2,3,−2). If Takahashi flips the sign of 
A 
2
​
 , then 
A=(−2,−3,−2). In this case, the robot moves as follows.
最初， 
A=(−2,3,−2) 。如果 Takahashi 改变 
A 
2
​
  的符号，那么 
A=(−2,−3,−2) 也会随之改变。在这种情况下，机器人的移动方式如下：

In its 
1-st move, the robot moves from 
0 to 
−2. The integer coordinates it passes through in this move are 
−2,−1,0.
在它的 
1 到 
−2 的移动过程中，机器人从 
0 移动到 
−2 。该移动过程中它经过的整数坐标为 
−2,−1,0 。
In its 
2-nd move, the robot moves from 
−2 to 
−5. The integer coordinates it passes through in this move are 
−5,−4,−3,−2.
在这一步操作中，机器人从 
2 移动到 
−2 ，而它在这一步中经过的整数坐标为 
−5,−4,−3,−2 。
In its 
3-rd move, the robot moves from 
−5 to 
−7. The integer coordinates it passes through in this move are 
−7,−6,−5.
在这次移动中，机器人从 
3 移动到 
−5 。它在这次移动中经过的整数坐标为 
−7,−6,−5 。
Thus, the integer coordinates the robot passes through at least once are the 
8 coordinates 
−7,−6,−5,−4,−3,−2,−1,0, and this is the maximum possible count, so print 
8.
因此，机器人至少会经过一个整数坐标点，这个坐标点是 
8 ，而这样的坐标点的最大数量就是 
8 个，所以请输出 
8 的值。

Note that if Takahashi did not flip the sign of any element, the robot would move as 
0→−2→1→−1, and the integer coordinates it passes through at least once would be the 
4 coordinates 
−2,−1,0,1.
请注意，如果 Takahashi 没有改变任何元素的符号，那么机器人将会按照 
0→−2→1→−1 的方式移动。而它至少会经过一次的整数坐标，就是 
4 坐标 
−2,−1,0,1 。

Sample Input 2  示例输入 2 复制
Copy  副本
2
2 3
Sample Output 2  示例输出 2 复制
Copy  副本
6
If no element of 
A is changed, the robot moves as 
0→2→5, and the integer coordinates it passes through at least once are the 
6 coordinates 
0,1,2,3,4,5.
如果 
A 的元素未被更改，机器人运动速度为 
0→2→5 ，它至少经过一次的整数坐标是 
6 坐标 
0,1,2,3,4,5 。
This is the maximum possible count, so print 
6.
这是最大可能计数，因此打印 
6 。 """

n = int(input())
a = list(map(int, input().split()))

# 计算前缀和
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]

# 预处理后缀最值
suf_max = s[:]
suf_min = s[:]

for i in range(n - 1, -1, -1):
    suf_max[i] = max(suf_max[i], suf_max[i + 1])
    suf_min[i] = min(suf_min[i], suf_min[i + 1])

# 不进行翻转的情况
ans = max(s) - min(s) + 1

# 维护翻转位置之前的最值
pre_max = pre_min = 0

for i in range(1, n + 1):
    # 翻转第 i 个元素
    d = -2 * a[i - 1]

    r = max(pre_max, suf_max[i] + d)
    l = min(pre_min, suf_min[i] + d)

    ans = max(ans, r - l + 1)

    # 更新前缀最值
    pre_max = max(pre_max, s[i])
    pre_min = min(pre_min, s[i])

print(ans)
