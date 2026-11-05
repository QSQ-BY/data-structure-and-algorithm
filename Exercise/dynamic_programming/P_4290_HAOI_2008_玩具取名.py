""" 题目描述
某人有一套玩具，并想法给玩具命名。首先他选择 W, I, N, G 四个字母中的任意一个字母作为玩具的基本名字。然后他会根据自己的喜好，将名字中任意一个字母用 W, I, N, G 中任意两个字母代替，使得自己的名字能够扩充得很长。

现在，他想请你猜猜某一个很长的名字，最初可能是由哪几个字母变形过来的。

输入格式
第一行四个整数 W,I,N,G。表示每一个字母能由几种两个字母所替代。

接下来 W 行，每行两个字母,表示 W 可以用这两个字母替代。

接下来 I 行，每行两个字母，表示 I 可以用这两个字母替代。

接下来 N 行，每行两个字母，表示 N 可以用这两个字母替代。

接下来 G 行，每行两个字母，表示 G 可以用这两个字母替代。

最后一行一个长为 L 的字符串。表示这个玩具的名字。

输出格式
一行字符串，该名字可能由哪些字母变形而得到。（按照 W, I, N, G 的顺序输出）

如果给的名字不能由任何一个字母变形而得到则输出 The name is wrong!。

输入输出样例
输入 #1复制

1 1 1 1
II
WW
WW
IG
IIII
输出 #1复制

IN
说明/提示
数据规模与约定
30% 数据满足 L≤20，W,I,N,G≤6；
100% 数据满足 L≤200，W,I,N,G≤16。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n1,n2,n3,n4 = read()#表示每个字母可以由几种两个字母代替
w = []
i = []
n = []
g = []
for _ in range(n1):
    cur = input().decode().strip()
    w.append(cur)
for _ in range(n2):
    cur = input().decode().strip()
    i.append(cur)
for _ in range(n3):
    cur = input().decode().strip()
    n.append(cur)
for _ in range(n4):
    cur = input().decode().strip()
    g.append(cur)
name = input().decode().strip()
m = len(name)
#dp[l][r] = 能够生成 name[l:r+1]的所有字母组成的集合
dp = [[set() for _ in range(m)] for _ in range(m)]

# 反向记录规则：两个字母可能由哪些原字母生成
parents = {}
#zip能将两边的元素按照位置对应关系进行配对
for letter, rules in zip("WING", (w, i, n, g)):
    for pair in rules:
        if pair not in parents:
            parents[pair] = set()
        parents[pair].add(letter)
#单个字符只能由他自己得到，因为每次的转变都是在把更少的字符变得更多，每次最少生成2个
#没有什么组合可以生成单个字符，所以以单个字符只能由自己不变生成
for i,ch in enumerate(name):
    dp[i][i].add(ch)

# 按区间长度递增，枚举左右两部分的分界点
for length in range(2, m + 1):#枚举长度
    for l in range(m - length + 1):#枚举左端点
        r = l + length - 1#根据长度和左端点计算出右端点
        #枚举分界点k，把[l,r]区间分成左右两部分
        for k in range(l, r):
            #分别遍历可以生成左右两个部分的字母集合
            for a in dp[l][k]:
                for b in dp[k + 1][r]:
                    pair = a + b
                    origins = parents.get(pair, ())
                    #可以理解为列表中的extend，往集合里面加入多个数字
                    dp[l][r].update(origins)
            # 四个字母都已找到，不需要继续枚举分界点
            if len(dp[l][r]) == 4:
                break

answer = ''.join(letter for letter in "WING" if letter in dp[0][m - 1])
print(answer if answer else "The name is wrong!")

