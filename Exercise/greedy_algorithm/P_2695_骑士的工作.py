""" 题目背景
你作为一个村的村长，保卫村庄是理所当然的了。今天，村庄里来了一只恶龙，他有 n 个头，恶龙到处杀人放火。你着急了。不过天无绝人之路，现在来了一个骑士团。里面有 m 位成员（往下看）。

题目描述
每个人都可以砍掉至多一个大小不超过 z 
i
​
  的头，需要 z 
i
​
  个金币，求最小花费。

输入格式
第一行两个整数 n，m。

下接 n 行，第 i 个整数 a 
i
​
 ，表示第 i 个头的大小。

下接 m 行，每个人可以砍的头大小和需要的金币数 z 
1
​
 ,⋯,z 
m
​
 。

输出格式
一个整数，最小花费。如果无解，输出 you died!。

输入输出样例
输入 #1复制

2 3
5 
4
7 
8
4
输出 #1复制

11
说明/提示
对于所有数据，1≤n,m≤2×10 
4
 ，1≤a 
i
​
 ,z 
i
​
 ≤10 
5
 。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

#n:头的数量,m:能砍掉的头的大小
n,m = read()
head = []
money = []
for _ in range(n):
    number = int(input())
    head.append(number)
for _ in range(m):
    number = int(input())
    money.append(number)

head.sort()
money.sort()
index = 0
ans = 0
for size in head:
    while index < m and money[index] < size:
        index += 1
    if index == m:
        print("you died!")
        sys.exit()
    ans += money[index]
    index += 1

print(ans)
