""" 链接：https://ac.nowcoder.com/acm/contest/139660/C
来源：牛客网

题目描述 
小月正在维护一条灯带，每个灯都有打开或熄灭两种状态，分别用 
1
,
0
1,0 表示（
1
1 表示打开，
0
0 表示熄灭）。灯带分为 
𝑚
m 段，每段包含灯的数量用一个数组 
𝑎
1
,
𝑎
2
,
…
,
𝑎
𝑚
a 
1
​
 ,a 
2
​
 ,…,a 
m
​
  表示，第 
𝑖
i 段包含 
𝑎
𝑖
a 
i
​
  盏灯，每一段中所有灯的状态都相同，且相邻两段灯的状态不同。
现在给定第一段灯带中灯的状态 
𝑏
∈
{
0
,
1
}
b∈{0,1}，你需要处理 
𝑞
q 次询问，第 
𝑖
i 次询问包含一个整数 
𝑝
𝑖
(
1
≤
𝑝
𝑖
≤
∑
𝑗
=
1
𝑚
𝑎
𝑗
)
p 
i
​
 (1≤p 
i
​
 ≤ 
j=1
∑
m
​
 a 
j
​
 )，你需要计算：第 
𝑝
p 盏灯的状态、它在第几段内、它是所在段的第几盏灯。
输入描述:
第一行输入三个整数 
𝑚
,
𝑞
,
𝑏
(
1
≦
𝑚
,
𝑞
≦
2
×
1
0
5
;
 
𝑏
∈
{
0
,
1
}
)
m,q,b(1≦m,q≦2×10 
5
 ; b∈{0,1})，表示段数、查询数、第 
1
1 段的颜色。
第二行输入 
𝑚
m 个整数 
𝑎
1
,
𝑎
2
,
…
,
𝑎
𝑚
(
1
≦
𝑎
𝑖
≦
1
0
18
;
 
∑
𝑖
=
1
𝑚
𝑎
𝑖
≦
1
0
18
)
a 
1
​
 ,a 
2
​
 ,…,a 
m
​
 (1≦a 
i
​
 ≦10 
18
 ; 
i=1
∑
m
​
 a 
i
​
 ≦10 
18
 )，表示各段长度。
此后 
𝑞
q 行，每行输入一个整数 
𝑝
𝑖
(
1
≦
𝑝
𝑖
≦
∑
𝑖
=
1
𝑚
𝑎
𝑖
)
p 
i
​
 (1≦p 
i
​
 ≦ 
i=1
∑
m
​
 a 
i
​
 )，表示第 
𝑖
i 次查询。
输出描述:
对于每个查询，新起一行。对于第 
𝑖
i 次查询，输出三个整数，表示第 
𝑝
𝑖
p 
i
​
  盏灯的状态、它在第几段内、它是所在段的第几盏灯。
示例1
输入
复制
4 4 1
3 2 4 1
1
3
4
9
输出
复制
1 1 1
1 1 3
0 2 1
1 3 4
说明

示例2
输入
复制
1 2 0
5
2
5
输出
复制
0 1 2
0 1 5
 """
import sys
from bisect import bisect_left,bisect_right
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

answers = []

m,q,b = read()#段数，查询数量，第一段的颜色
lengths = list(read())#表示每一段的长度
prefix = [0,*accumulate(lengths)]
#对于每个查询，新起一行。对于第 
#𝑖
#i 次查询，输出三个整数，表示第 
#𝑝
#𝑖
#p 
#i
#​
#  盏灯的状态、它在第几段内、它是所在段的第几盏灯。
while(q > 0):
    p = int(input())
    index = bisect_left(prefix,p) 
    state = b
    if(index % 2 == 0):
        state = 1-b
    if(index % 2 == 1):
        state = b
    number = p - prefix[index-1]
    answers.append([state,index,number])
    q -= 1

for ans in answers:
    print(*ans)