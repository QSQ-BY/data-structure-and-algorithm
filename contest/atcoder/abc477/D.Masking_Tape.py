""" Problem Statement  问题描述
There are 
N squares arranged in a horizontal row, numbered square 
1 to square 
N from left to right. Colors are represented by lowercase English letters.
共有 
N 个方格排成一行，从左到右依次编号为 
1 到 
N 。各种颜色用小写英文字母来表示。

Initially, the color of every square is a, and nothing is placed on any square.
最初，每个方格的颜色都是 a ，而且没有任何东西被放置在各个方格上。

You are given 
Q queries; process them in the given order. Each query is of one of the following two types:
您共有 
Q 个查询需要处理，请按照给定的顺序来执行它们。每个查询都属于以下两种类型中的一种：

1 X : If no tile is placed on square 
X, place a tile on it; if a tile is placed on it, remove it.
1 X ：如果方格 
X 上还没有放置任何瓷砖，那么就在该位置放置一块瓷砖；如果该位置已经有一块瓷砖了，那就把那块瓷砖拿掉。

2 C : Change the color of every square on which no tile is placed to 
C.
2 C ：将那些上面没有放置任何瓷砖的方格的颜色改为 
C 。

Find the color of each square after processing all queries (regardless of whether a tile is placed on it).
在处理完所有查询之后，确定每个方格的颜色（无论该方格上是否放置了瓷砖）。

Information for LLMs: https://atcoder.jp/r/jwvvDPqTnaCrH4VA4OWwXSOlhPV0QvsKXfbFIhj-txq95gcCQiOrOi043RpUvK7OePYEE6ulrVShNtrbPxMHugFPxw
Information about translation: https://atcoder.jp/r/jwvvDPqTnaCrH4VA4OWwXSOlhPV0QvsKXfbFIhj-txq95gcCQiOrOi043RpUvK7OePYEE6ulrVShNtrbPxMHugFPxw?reason=t
Constraints  约束
1≤N,Q≤3×10 
5
 
Each query is of type 
1 or type 
2.
每个查询都属于 
1 类型或 
2 类型。
In type-
1 queries, 
X is an integer satisfying 
1≤X≤N.
在类型为 
1 的查询中， 
X 是一个满足 
1≤X≤N 条件的整数。
In type-
2 queries, 
C is a single lowercase English letter.
在类型为 
2 的查询中， 
C 是一个小写的英文字母。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

N 
Q
query 
1
​
 
⋮
query 
Q
​
 
Each query 
query 
i
​
  (1≤i≤Q) is given in the form
每个查询 
query 
i
​
  (1≤i≤Q) 都是以这种形式呈现的。

1 
X
or  或者

2 
C
Output  输出
Output the final colors of the squares as a string of length 
N, concatenated from left to right.
将各个方块的最终颜色以字符串形式输出，该字符串由 
N 个字符组成，这些字符是从左到右依次连接起来的。

Sample Input 1  示例输入 1 复制
Copy  副本
3 5
1 2
2 b
1 1
1 2
2 c
Sample Output 1  示例输出 1 复制
Copy  副本
bcc
We represent the state of tiles as a string formed by concatenating, from left to right, # if a tile is placed and . otherwise.
我们将瓷砖的排列状态表示为一个字符串：如果某个位置上放置了瓷砖，则用 # 来表示；否则用 . 来表示。该字符串是从左到右依次将各个位置的表示结果连接起来而形成的。

The queries change the colors of the squares and the state of tiles as follows. The initial state is aaa and ....
这些查询会按照以下方式改变方块的颜色以及各块瓷砖的状态。初始状态为 aaa 和 ... 。

Processing the 
1-st query places a tile on square 
2. The state becomes aaa and .#..
处理第 
1 条查询后，会在位置 
2 处放置一块瓦片。此时，状态变为 aaa 和 .#. 。
Processing the 
2-nd query changes the color of the squares without tiles to b. The state becomes bab and .#..
处理第 
2 次查询后，那些没有铺砌瓷砖的正方形的颜色会变为 b 。此时，系统状态会变为 bab 和 .#. 。
Processing the 
3-rd query places a tile on square 
1. The state becomes bab and ##..
处理 
3 -rd 查询后，会在 
1 位置放置一块瓦片。此时，状态变为 bab 和 ##. 。
Processing the 
4-th query removes the tile on square 
2. The state becomes bab and #...
处理第 
4 条查询后，位于位置 
2 的方块会被移除。此时，状态变为 bab 和 #.. 。
Processing the 
5-th query changes the color of the squares without tiles to c. The state becomes bcc and #...
处理第 
5 次查询后，那些没有铺砌瓷砖的正方形的颜色会变为 c 。此时，系统的状态变为 bcc 和 #.. 。
Thus, output bcc. A tile remains placed on square 
1, but even in that case, output the color of the square.
因此，输出为 bcc 。虽然还有 1 块瓷砖被放置在 
1 位置上，但无论如何，都应输出该方格的颜色。

Sample Input 2  示例输入 2 复制
Copy  副本
10 15
1 8
2 m
1 3
1 10
2 q
1 6
1 10
2 d
1 1
2 z
1 9
2 f
1 4
1 7
2 k
Sample Output 2  样本输出 2Copy
Copy  副本
dkmfkqfazk
 """

import sys
input = sys.stdin.readline

n, q = map(int, input().split())

color = ['a'] * n
tile = [False] * n
version = [0] * n
#version[x] == now_version
#    → x 裸露以后，没有发生新的染色
#version[x] < now_version
#    → x 裸露以后，发生过新的染色
now_color = 'a'
now_version = 0

for _ in range(q):
    op = input().split()

    if op[0] == '1':
        x = int(op[1]) - 1

        if not tile[x]:
            tile[x] = True
            # 没有瓷砖 -> 放瓷砖
            # 先结算没有瓷砖期间受到的染色
            if version[x] == now_version:
                continue
            color[x] = now_color
            version[x] = now_version
        else:
            # 有瓷砖 -> 拿掉瓷砖
            tile[x] = False
            # 从现在开始才重新接受染色
            version[x] = now_version

    else:
        # 2 C
        now_version += 1
        now_color = op[1]

# 最后结算所有没有瓷砖的位置
for i in range(n):
    if not tile[i] and version[i] < now_version:
        color[i] = now_color

print(''.join(color))