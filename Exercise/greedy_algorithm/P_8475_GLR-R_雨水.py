""" 给定一个长为 n 的整数序列 A，下标从 1 开始。你可以任取一个自然数 k 以及一个序列 ⟨1,2,…,n⟩ 的，长度为 2k (k∈N) 的子序列 P，并对于所有 i=1,2,…,k，交换 A 
P 
2i−1
​
 
​
  与 A 
P 
2i
​
 
​
  的值。求在所有可能得到的新序列 A 
′
  中，字典序 最小的序列。 """


import sys
from array import array

input = sys.stdin.buffer.readline

n, k1, k2, thres = map(int, input().split())
MASK = (1 << 64) - 1

a = array('I', [0]) * n
pos = array('I', [0]) * n
# 生成原始序列
for i in range(n):
    x, y = k1, k2
    k1 = y
    x ^= x << 23
    x &= MASK
    k2 = (x ^ y ^ (x >> 17) ^ (y >> 26)) & MASK

    a[i] = ((k2 + y) & MASK) % thres

# 预处理后缀最小值的最右位置
best = n - 1

for i in range(n - 1, -1, -1):
    if a[i] < a[best]:
        best = i
    pos[i] = best

# 贪心交换
i = 0
while i < n:
    j = pos[i]
    if a[j] < a[i]:
        a[i], a[j] = a[j], a[i]
        i = j + 1
    else:
        i += 1

# 最后统一计算答案
ans = 0

for i in range(n):
    ans += (i + 1) * a[i]

print(ans & MASK)
