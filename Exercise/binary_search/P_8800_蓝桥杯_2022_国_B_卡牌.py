""" 题目描述
这天，小明在整理他的卡牌。

他一共有 n 种卡牌，第 i 种卡牌上印有正整数数 i(i∈[1,n])，且第 i 种卡牌现有 a 
i
​
  张。

而如果有 n 张卡牌，其中每种卡牌各一张，那么这 n 张卡牌可以被称为一套牌。小明为了凑出尽可能多套牌，拿出了 m 张空白牌，他可以在上面写上数 i，将其当做第 i 种牌来凑出套牌。然而小明觉得手写的牌不太美观，决定第 i 种牌最多手写 b 
i
​
  张。

请问小明最多能凑出多少套牌?

输入格式
输入共 3 行，第一行为两个正整数 n，m 。

第二行为 n 个正整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
  。

第三行为 n 个正整数 b 
1
​
 ,b 
2
​
 ,…,b 
n
​
  。

输出格式
一行，一个整数表示答案。

输入输出样例
输入 #1复制

4 5
1 2 3 4
5 5 5 5
输出 #1复制

3
说明/提示
【样例说明】

这 5 张空白牌中，拿 2 张写 1，拿 1 张写 2，这样每种牌的牌数就变为了 3,3,3,4，可以凑出 3 套牌，剩下 2 张空白牌不能再帮助小明凑出一套。

【评测用例规模与约定】

对于 30% 的数据，保证 n≤2000；

对于 100% 的数据，保证 n≤2×10 
5
 ;a 
i
​
 ,b 
i
​
 ≤n;m≤n 
2
 。

蓝桥杯 2022 国赛 B 组 C 题。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m = read()#一共有m张空白牌
a = list(read())
b = list(read())#第i张手写牌最多写b[i]张
index = list(range(n))
index.sort(key = lambda x:a[x])
left = 0
right = a[index[-1]] + m

#检查能不能凑齐k套卡牌
def check(k):
    remain = m#还剩多少张空白牌
    for i in range(n):
        cur = a[index[i]]
        if(cur >= k):
            return True
        diff = k-cur
        if(remain<diff or b[index[i]] < diff):
            return False
        remain -= diff
    return True
#10二分模型
while left<right:
    mid = (left+right+1)//2
    if(check(mid) == True):
        left = mid
    else:
        right = mid-1

print(left)
