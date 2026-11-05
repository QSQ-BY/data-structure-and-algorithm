""" Problem Statement  问题描述
Takahashi is using a shower at a public bath. This shower has a button. If the button is pressed at time 
t, hot water comes out for 
K seconds, from time 
t to time 
t+K. Even if the button is pressed again while hot water is coming out, hot water comes out for 
K seconds from the time the button was last pressed.
高桥正在公共浴场用淋浴。这个淋浴间有个按钮。如果按钮在时间 
t 按下，热水流出时间为 
K ，时间从 
t 到时间 
t+K 。即使热水流出来时再按一次按钮，热水也会从按钮最后按下时间起持续 
K 秒。

There are 
N Aokis, each of whom presses the button once. The 
i-th Aoki presses the button at time 
A 
i
​
 .
有 
N 青木，每个人按一次按钮。 
i -th 青木在 
A 
i
​
  时刻按下按钮。

Find the minimum number of times Takahashi needs to press the button so that hot water is always coming out from time 
0 to time 
T. Here, hot water is considered to be coming out both at the moment the button is pressed and at the moment exactly 
K seconds after the last press.
找出高桥需要按下按钮的最少次数，使热水始终从时间 
0 流出到时间 
T 。这里，热水既在按钮按下的瞬间，也在最后一次按下后恰好 
K 秒时流出。

Constraints  约束
1≤N≤2×10 
5
 
1≤K≤10 
9
 
1≤T≤10 
9
 
0≤A 
i
​
 ≤10 
9
 
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

N 
K 
T  
A 
1
​
  
A 
2
​
  
… 
A 
N
​
   
Output  输出结果
Print the answer in a single line.
把答案写成一行。

Sample Input 1  示例输入 1 复制
Copy  副本
3 4 20
6 7 12
Sample Output 1  示例输出 1 复制
Copy  副本
4
If Takahashi presses the button at times 
0,2,10,16, hot water is always coming out from time 
0 to time 
20.
如果高桥有时按 
0,2,10,16 按钮，热水总是从 
0 到 
20 不断流出。
If he presses the button 
3 times or fewer, it is impossible to keep hot water always coming out, so the answer is 
4.
如果他按按钮 
3 或更少，热水就不可能一直流出来，所以答案是 
4 。

Sample Input 2  示例输入 2 复制
Copy  副本
9 37 480
12 123 132 213 231 312 321 500 1000
Sample Output 2  示例输出 2 复制
Copy  副本
11
 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,k,t = read()
arr = list(read())
intervals = []
for number in arr:
    if(number > t):
        continue
    intervals.append((number,number + k))
del arr
if not intervals:
    print((t + k-1)//k)
    sys.exit()
intervals.sort()
merged_intervals = []
left = intervals[0][0]
right = intervals[0][1]
for i in range(1,len(intervals)):
    (l,r) = intervals[i]
    if(right >= l):
        right = max(right,r)
    else:
        merged_intervals.append((left,right))
        left,right = l,r
merged_intervals.append((left, right))
del intervals
lengths = []
left = merged_intervals[0][0]
right = merged_intervals[0][1]
if(left > 0):
    lengths.append(left)
for i in range(1,len(merged_intervals)):
    (l,r) = merged_intervals[i]
    lengths.append(l - right)
    right = r
    if(right >= t):
        break
if(right < t):
    lengths.append(t - right)
del merged_intervals
ans = 0
for length in lengths:
    ans += (length + k-1)//k
print(ans)

