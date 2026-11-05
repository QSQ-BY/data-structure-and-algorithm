""" 题目背景
2023-10-08 update: 新增两组 hack。

2023-12-16 update: 新增两组 hack。

题目描述
给定一个数字字符串，用最小次数的加法让字符串等于一个给定的目标数字。每次加法就是在字符串的某个位置插入一个加号。在里面要的所有加号都插入后，就像做普通加法那样来求值。

例如，考虑字符串12，做 0 次加法，我们得到数字 12。如果插入 1 个加号，我们得到 3，因此，这个例子中，最少用 1 次加法就得到数字 3。

再举一例，考虑字符串303和目标数字 6，最佳方法不是3+0+3。而是3+03。能这样做是因为一个数的前导 0 不会改变它的大小。

输入格式
第一行：一个字符串 s。

第二行：一个整数 n。

输出格式
一行一个整数表示最少的加法次数让 s 等于 n。如果怎么做都不能让 s 等于 n ，则输出 −1。

输入输出样例
输入 #1复制

99999
45
输出 #1复制

4
说明/提示
数据规模与约定
对于 100% 的数据，保证 1≤len(s)≤40，1≤n≤10 
5
 。 """
import sys

input = sys.stdin.buffer.readline

s = input().decode().strip()
target = int(input())
length = len(s)

# dp[i][total]：用完前i个字符凑出 total 时，最少的数字段数
#使用字典保存可以凑出来的数字避免含有太多无效的数字占据内存
dp = [{} for _ in range(length + 1)]
dp[0][0] = 0
INF = length + 1
for i in range(length):
    number = 0

    # 枚举新的一段 s[i:j+1]
    #枚举把加号刚好插在这里的情况
    for j in range(i, length):
        number = number * 10 + int(s[j])
        # 后面继续增加数字，这一段也不会变小
        if number > target:
            break
        for total, count in dp[i].items():
            new_total = total + number
            if new_total > target:
                continue
            if count + 1 < dp[j+1].get(new_total, INF):
                dp[j+1][new_total] = count + 1

#如果找不到结果就为0，最后减一一样输出为-1
segments = dp[length].get(target,0)
print(segments - 1)
