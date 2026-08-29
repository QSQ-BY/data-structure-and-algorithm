""" 题目描述
伐木工人 Mirko 需要砍 
M
M 米长的木材。对 Mirko 来说这是很简单的工作，因为他有一个漂亮的新伐木机，可以如野火一般砍伐森林。不过，Mirko 只被允许砍伐一排树。

Mirko 的伐木机工作流程如下：Mirko 设置一个高度参数 
H
H（米），伐木机升起一个巨大的锯片到高度 
H
H，并锯掉所有树比 
H
H 高的部分（当然，树木不高于 
H
H 米的部分保持不变）。Mirko 就得到树木被锯下的部分。例如，如果一排树的高度分别为 
20
,
15
,
10
20,15,10 和 
17
17，Mirko 把锯片升到 
15
15 米的高度，切割后树木剩下的高度将是 
15
,
15
,
10
15,15,10 和 
15
15，而 Mirko 将从第 
1
1 棵树得到 
5
5 米，从第 
4
4 棵树得到 
2
2 米，共得到 
7
7 米木材。

Mirko 非常关注生态保护，所以他不会砍掉过多的木材。这也是他尽可能高地设定伐木机锯片的原因。请帮助 Mirko 找到伐木机锯片的最大的整数高度 
H
H，使得他能得到的木材至少为 
M
M 米。换句话说，如果再升高 
1
1 米，他将得不到 
M
M 米木材。

输入格式
第 
1
1 行 
2
2 个整数 
N
N 和 
M
M，
N
N 表示树木的数量，
M
M 表示需要的木材总长度。

第 
2
2 行 
N
N 个整数表示每棵树的高度。

输出格式
1
1 个整数，表示锯片的最高高度。

输入输出样例
输入#1
4 7
20 15 10 17
输出#1
15
输入#2
5 20
4 42 40 26 46
输出#2

36
说明/提示
对于 
100
%
100% 的测试数据，
1
≤
N
≤
10
6
1≤N≤10 
6
 ，
1
≤
M
≤
2
×
10
9
1≤M≤2×10 
9
 ，树的高度 
≤
4
×
10
5
≤4×10 
5
 ，所有树的高度总和 
>
M
>M。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,m = read()#n表示树木的个数，m表示需要的木材总长度
heights = list(read())
right = max(heights)
left = 0

#如果高度为k的电锯可不可以获得长度为m的木材
def check(k:int)->int:
    global m
    global heights
    get = 0
    for height in heights:
        if(height > k):
            get += height - k
        if(get >= m):
            return 1
    if(get < m):
        return 0
    elif(get >= m):
        return 1

while(left < right):
    mid = (left + right + 1)//2
    if(check(mid) == 1):
        left = mid
    else:
        right = mid - 1
print(left)