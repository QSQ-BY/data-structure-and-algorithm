""" 链接：https://ac.nowcoder.com/acm/contest/139660/D
来源：牛客网

题目描述 
小月收集了 
𝑛
n 个长度为 
𝑏
b 且仅包含 
0
,
1
0,1 的互不相同的字符串 
𝑠
1
,
𝑠
2
,
…
,
𝑠
𝑛
s 
1
​
 ,s 
2
​
 ,…,s 
n
​
 ，其中 
𝑠
𝑖
=
𝑠
𝑖
1
𝑠
𝑖
2
…
𝑠
𝑖
𝑏
s 
i
​
 =s 
i1
​
 s 
i2
​
 …s 
ib
​
 。若两个字符串恰好只有一位的字符不同，则称这两个字符串构成一对「单点差分码」。
请你计算这 
𝑛
n 个字符串总共能构成多少对不同的「单点差分码」，以及对于从 
1
1 到 
𝑏
b 的每一位，有多少对「单点差分码」在这一位产生差异。
输入描述:
第一行输入两个整数 
𝑛
,
𝑏
(
1
≦
𝑛
≦
min
⁡
(
2
×
1
0
5
,
2
𝑏
)
;
 
1
≦
𝑏
≦
20
)
n,b(1≦n≦min(2×10 
5
 ,2 
b
 );1≦b≦20)，表示字符串数量、每个字符串的长度。
之后的 
𝑛
n 行，第 
𝑖
i 行输入一个长度为 
𝑏
b 且仅包含 
0
,
1
0,1 的字符串 
𝑠
𝑖
s 
i
​
 。保证所有字符串两两不同。
输出描述:
第一行输出一个整数，表示「单点差分码」的总数。
第二行输出 
𝑏
b 个整数。第 
𝑖
i 个整数表示在第 
𝑖
i 位产生差异的「单点差分码」对数。
示例1
输入
复制
4 3
000
001
010
101
输出
复制
3
1 1 1
示例2
输入
复制
2 3
000
001
输出
复制
1
0 0 1 """
import sys
input = sys.stdin.buffer.readline 
def read():
    return map(int,input().split())

n , b = read()#字符串的数量，每一个字符串的长度
h = set()
ans = 0
num = [0]*b
for _ in range(n):
    bit = int(input(),2)
    if(n == 0):
        h.add(bit)
        continue
    for i in range(b):
        new_bit = (1<<(i))^bit
        if(new_bit in h):
            ans += 1
            num[i] += 1
            
    h.add(bit)
print(ans)
num.reverse()
print(*num)
