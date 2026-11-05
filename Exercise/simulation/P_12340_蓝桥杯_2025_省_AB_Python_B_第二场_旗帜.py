""" 题目描述
小蓝要画一个 LANQIAO 图形，并把这个图形做成一个旗帜。图形的形状为一个 h×w 的矩形，其中 h 表示图形的高，w 表示图形的宽。当 h=5,w=10 时，图形如下所示：

LANQIAOLAN
ANQIAOLANQ
NQIAOLANQI
QIAOLANQIA
IAOLANQIAO

图形的规律是：第一行用 LANQIAO 重复填入，第二行开始，每行向左移动一个字符，用 LANQIAO 重复填入。

小蓝需要把图形中的每个字母都剪出来，以粘贴到旗帜上，他想知道，给定图形的高和宽，图形中有多少个 A。

输入格式
输入的第一行包含两个正整数 h,w，用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

输入输出样例
输入 #1复制

5 10
输出 #1复制

14
说明/提示
评测用例规模与约定
对于 30% 的评测用例，h=1，1≤w≤20；
对于 60% 的评测用例，1≤h,w≤20；
对于所有评测用例，1≤h,w≤100。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
h,w = read()
string = "LANQIAO"
start = ""
index = 0
while(index+7<w):
    start = start+string
    index += 7
start += string[:w-index]
index = w - index
g = [[]for _ in range(h)]
g[0] = start
for i in range(1,h):
    cur = g[i-1][1:] + string[index%7]
    g[i] = cur
    index += 1
ans = 0
#for row in g:
#    print(row)
for i in range(h):
    for j in range(w):
        if(g[i][j] == "A"):
            ans += 1
print(ans)