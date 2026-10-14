""" 题目描述
2020 年春节期间，有一个特殊的日期引起了大家的注意：2020 年 2 月 2 日。因为如果将这个日期按 yyyymmdd 的格式写成一个 8 位数是 20200202，恰好是一个回文数。我们称这样的日期是回文日期。

有人表示 20200202 是“千年一遇” 的特殊日子。对此小明很不认同，因为不到 2 年之后就是下一个回文日期：20211202 即 2021 年 12 月 2 日。

也有人表示 20200202 并不仅仅是一个回文日期，还是一个 ABABBABA 型的回文日期。对此小明也不认同，因为大约 100 年后就能遇到下一个 ABABBABA 型的回文日期：21211212 即 2121 年12 月12 日。算不上“千年一遇”，顶多算“千年两遇”。

给定一个 8 位数的日期，请你计算该日期之后下一个回文日期和下一个 ABABBABA 型的回文日期各是哪一天。

输入格式
输入包含一个八位整数 N，表示日期。

输出格式
输出两行，每行 1 个八位数。第一行表示下一个回文日期，第二行表示下 一个 ABABBABA 型的回文日期。

输入输出样例
输入 #1复制

20200202
输出 #1复制

20211202
21211212
说明/提示
对于所有评测用例，10000101≤N≤90900908，保证 N 是一个合法日期的 8 位数表示。

蓝桥杯 2020 第二轮省赛 A 组 G 题（B 组 G 题）。 """
import sys

input = sys.stdin.buffer.readline

N = input().decode().strip()

n = len(N)

# 判断日期是否合法
def check_date(s):
    y = int(s[:4])
    m = int(s[4:6])
    d = int(s[6:])
    if m < 1 or m > 12:
        return False
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    # 闰年
    if m == 2:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            return d <= 29
        else:
            return d <= 28
    return d <= days[m-1]

# 生成普通回文
def make_pal(x):
    s = str(x)
    return s + s[::-1]
# 生成ABABBABA
def make_ab(x):
    s = str(x)[:2]
    return s + s + s[::-1] + s[::-1]
# 找普通回文日期
x = int(N[:4])

while True:
    ans1 = make_pal(x)
    if ans1 > N and check_date(ans1):
        break
    x += 1

# 找ABABBABA型日期
x = int(N[:2])
while True:
    ans2 = make_ab(x)
    if ans2 > N and check_date(ans2):
        break
    x += 1

print(ans1)
print(ans2)