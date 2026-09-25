""" 题目描述
我们将含有不少于 6 个 6 的数视为一个好数。例如 666666、162636465666 是好数，12366666 不是好数。

给定 n 个正整数 a 
i
​
 ，你可以把这些数分成若干组拼起来，每组内的数可以按任意顺序拼，但一组最多只能有 3 个数。求最多可以得到多少个好数。

输入格式
输入的第一行包含一个正整数 n。

第二行包含 n 个正整数 a 
1
​
 ,a 
2
​
 ,⋯,a 
n
​
 ，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案，即最多可以得到的好数的数量。

输入输出样例
输入 #1复制

3
66 66 66
输出 #1复制

1
输入 #2复制

7
666666 16166 6696 666 6 6 6
输出 #2复制

2
说明/提示
评测用例规模与约定
对于 20% 的评测用例，1≤n≤20；
对于所有评测用例，1≤n≤1000，0≤a 
i
​
 ≤10 
9
 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
#一个数字大于等于6的时候视为一个好数
for i,number in enumerate(arr):
    res = 0
    while(number):
        tail = number%10
        if(tail == 6):
            res += 1
        number = number//10
    arr[i] = res


ans = sum(x >= 6 for x in arr)
arr = [x for x in arr if 0 < x < 6]
n = len(arr)

cnt = [0] * 6
for x in arr:
    cnt[x] += 1

# 5：优先搭配最小的数
for x in range(1, 5):
    k = min(cnt[5], cnt[x])
    ans += k
    cnt[5] -= k
    cnt[x] -= k

ans += cnt[5] // 2  # 剩下的 5 两两组合

# 4：优先使用两个 1
k = min(cnt[4], cnt[1] // 2)
ans += k
cnt[4] -= k
cnt[1] -= 2 * k

# 然后考虑 4+2、4+3
for x in (2, 3):
    k = min(cnt[4], cnt[x])
    ans += k
    cnt[4] -= k
    cnt[x] -= k

ans += cnt[4] // 2  # 剩下的 4 两两组合

# 3：先考虑 3+2+1
k = min(cnt[3], cnt[2], cnt[1])
ans += k
cnt[3] -= k
cnt[2] -= k
cnt[1] -= k

# 再考虑 3+3
ans += cnt[3] // 2
cnt[3] %= 2

# 最多剩一个 3，考虑 3+2+2
k = min(cnt[3], cnt[2] // 2)
ans += k
cnt[3] -= k
cnt[2] -= 2 * k

# 最后考虑 2+2+2
ans += cnt[2] // 3
print(ans)
