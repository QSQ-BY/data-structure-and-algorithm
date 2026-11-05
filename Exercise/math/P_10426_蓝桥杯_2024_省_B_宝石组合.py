""" 题目描述
在一个神秘的森林里，住着一个小精灵名叫小蓝。有一天，他偶然发现了一个隐藏在树洞里的宝藏，里面装满了闪烁着美丽光芒的宝石。这些宝石都有着不同的颜色和形状，但最引人注目的是它们各自独特的 “闪亮度” 属性。每颗宝石都有一个与生俱来的特殊能力，可以发出不同强度的闪光。小蓝共找到了 n 枚宝石，第 i 枚宝石的 “闪亮度” 属性值为 H 
i
​
 ，小蓝将会从这 n 枚宝石中选出三枚进行组合，组合之后的精美程度 S 可以用以下公式来衡量：

S=H 
a
​
 H 
b
​
 H 
c
​
 ⋅ 
LCM(H 
a
​
 ,H 
b
​
 )⋅LCM(H 
a
​
 ,H 
c
​
 )LCM(H 
b
​
 ,H 
c
​
 )
LCM(H 
a
​
 ,H 
b
​
 ,H 
c
​
 )
​
 
其中 LCM 表示的是最小公倍数函数。

小蓝想要使得三枚宝石组合后的精美程度 S 尽可能的高，请你帮他找出精美程度最高的方案。如果存在多个方案 S 值相同，优先选择按照 H 值升序排列后字典序最小的方案。

输入格式
第一行一个整数 n 表示宝石个数。
第二行有 n 个整数 H 
1
​
 ,H 
2
​
 ,…H 
n
​
  表示每个宝石的闪亮度。

输出格式
输出一行包含三个整数表示满足条件的三枚宝石的 “闪亮度”。

输入输出样例
输入 #1复制

5
1 2 3 4 9
输出 #1复制

1 2 3
说明/提示
数据规模与约定
对 30% 的数据，n≤100，H 
i
​
 ≤10 
3
 。
对 60% 的数据，n≤2×10 
3
 。
对全部的测试数据，保证 3≤n≤10 
5
 ，1≤H 
i
​
 ≤10 
5
 。 """
#原题中的表达式化简之后就是求解
#这一整串数字中最大的最大公因数
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
limit = max(arr)
cnt = [0]*(limit+1)
for x in arr:
    cnt[x] += 1

#从大到小枚举最大公约数
for d in range(limit,0,-1):
    chosen = []
    #从小到大枚举d的倍数，保证字典序最小
    for x in range(d,limit+1,d):
        if(cnt[x]):
            take = min(cnt[x],3- len(chosen))
            for _ in range(take):
                chosen.append(x)
            if(len(chosen) == 3):
                print(*chosen)
                sys.exit()

