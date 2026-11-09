""" 题目描述
小明正在参加魔法科的期末考试，考生需要根据给定的口诀组合出有效的魔法。其中，老师给定了 n 个上半部分口诀 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
  和 m 个下半部分口诀 b 
1
​
 ,b 
2
​
 ,…,b 
m
​
 ，均用整数表示。完整的口诀包含一个上半部分口诀和一个下半部分口诀，当选用两个口诀 a 
i
​
  和 b 
j
​
 ，将组合出完整口诀 S=a 
i
​
 +b 
j
​
 。

当 S 满足 S≤n+m 且 S 为质数时，魔法是有效的。魔法的种类只和 S 的大小有关。如果每个上半部分口诀和每个下半部分口诀在不同的组合中可以重复使用，小明想知道一共可能组合出多少种不同的有效魔法？

输入格式
输入共三行。

第一行为两个正整数 n,m。
第二行为 n 个由空格分开的正整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 。
第三行为 m 个由空格分开的正整数 b 
1
​
 ,b 
2
​
 ,…,b 
m
​
 。
输出格式
输出共 1 行，一个整数表示答案。

输入输出样例
输入 #1复制

3 4
2 3 10
3 4 5 1
输出 #1复制

3
说明/提示
样例说明
可以组合出 3,5,7 这三个有效魔法。

评测用例规模与约定
对于 20% 的评测用例，n,m≤200。
对于 60% 的评测用例，n,m≤2000。
对于 100% 的评测用例，1≤n,m≤20000，1≤a 
i
​
 ,b 
i
​
 ≤20000。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,m = read()
a = list(read())
b = list(read())
a.sort()
b.sort()
limit = n+m
is_prime = [True]*(limit+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2,limit+1):
    if(is_prime[i] ==False):
        continue
    for j in range(i*2,limit+1,i):
        is_prime[j] = False
ans = 0
s = set()
for number1 in a:
    for number2 in b:
        if(number1 + number2 > limit):
            break
        if(is_prime[number1 + number2]):
            s.add(number1 + number2)
ans = len(s)
print(ans)
