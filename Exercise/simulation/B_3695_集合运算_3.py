""" 题目背景
关于集合、交集、并集的定义请参考 https://www.luogu.com.cn/problem/B3633 。

以下给出对称差的定义：

对两个集合 A,B，规定 A 和 B 的对称差 AΔB 为在 A 中出现但不在 B 中出现，或在 B 中出现但不在 A 中出现的元素。
例如，A={1,2,3}，B={2,3,5}，则 AΔB={1,5}。

题目描述
给定 n 个集合 s 
1
​
 ,s 
2
​
 ,…s 
n
​
 ，每个集合都含有 [1,m] 之间的若干个整数。

现在，有 q 次操作，每次操作如下：

1 x y：将 s 
x
​
  中的每个元素都加上 y，再删去其中大于 m 的；
2 x y：将 s 
x
​
  中的每个元素都减去 y，再删去其中小于 1 的；
3 x y：查询 s 
x
​
  和 s 
y
​
  的交集的元素个数；
4 x y：查询 s 
x
​
  和 s 
y
​
  的并集的元素个数；
5 x y：查询 s 
x
​
  和 s 
y
​
  的对称差的元素个数；
输入格式
第一行有三个数，依次表示集合的个数 n，集合元素的最大值 m 和操作次数 q。

第 2 到第 (n+1) 行，每行有若干个整数，第 (i+1) 行的整数描述集合 s 
i
​
  的元素：
每行首先有一个整数 c 
i
​
  表示 s 
i
​
  的元素个数，接下来有 c 个互不相同的整数 s 
i,1
​
 ,s 
i,2
​
 ,…s 
i,c 
i
​
 
​
  表示集合 s 
i
​
  里的元素。

接下来 q 行，每行三个整数 o,x,y，表示一次操作。具体见『题目描述』。

输出格式
对于每个查询操作，请输出一行一个整数表示答案。

输入输出样例
输入 #1复制

2 5 5
3 1 2 3
4 1 2 4 5
1 2 1
2 1 1
3 1 2
4 1 2
5 1 2
输出 #1复制

1
4
3
说明/提示
数据规模与约定
对于全部的测试点，保证 1≤n,m,q≤3×10 
4
 ，1≤∑ 
i=1
n
​
 c 
i
​
 ≤10 
6
 ，1≤x,y≤n，1≤o≤5。集合里的元素都是不超过 m 的正整数。

感谢 @Zyingyzzz 提供 hack 数据一组。 """

import sys
input = sys.stdin.buffer.readline

# 预先统计每个字节中二进制 1 的个数。
_bit_counts = bytearray(256)
for i in range(1, 256):
    _bit_counts[i] = _bit_counts[i >> 1] + (i & 1)
_bit_counts = bytes(_bit_counts)

def bit_count(x):
    """返回整数绝对值的二进制表示中 1 的个数。"""
    x = abs(x)
    data = x.to_bytes((x.bit_length() + 7) // 8, 'little')
    return sum(data.translate(_bit_counts))

def read():
    return map(int,input().split())
n,m,q = read()
s = [0]
universe = (1<<(m)) - 1
for _ in range(n):
    cur = 0
    data = list(read())
    c = data[0]
    for i in range(1,c+1):
        number = data[i]
        cur |= 1<<(number - 1)
    s.append(cur)

for _ in range(q):
    o, x, y = read()
    if o == 1:
        s[x] = (s[x] << y) & universe
    elif o == 2:
        s[x] >>= y
    elif o == 3:
        print(bit_count(s[x] & s[y]))
    elif o == 4:
        print(bit_count(s[x] | s[y]))
    elif o == 5:
        print(bit_count(s[x] ^ s[y]))
