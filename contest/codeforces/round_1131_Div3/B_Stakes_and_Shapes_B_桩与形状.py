""" Alice and Bob are playing the Rock, Scissors, Paper game.
爱丽丝和鲍勃正在玩石头、剪刀、纸游戏。

The game consists of multiple rounds. In each round, the player must choose one of the three possible outcomes: Rock, Scissors, or Paper. The rules for each round are as follows:
游戏由多个回合组成。每轮玩家必须选择三种可能的结果之一：石头、剪刀或布。每轮规则如下：

Rock beats Scissors;   摇滚胜剪刀;
Scissors beats Paper;
剪刀胜过纸牌;
Paper beats Rock;
纸牌胜石头;
If both players choose the same outcome, the round ends in a draw.
如果双方选择相同结果，该轮以平局结束。
It is given that the game consists of exactly x+y+z
 rounds. Also, Bob knows that Alice will play Rock exactly x
 times, Scissors exactly y
 times, and Paper exactly z
 times. However, Bob does not know the order of Alice's outcomes.
游戏由恰好 x+y+z
 的回合组成。此外，鲍勃知道爱丽丝会准确地弹出摇滚的 x
 次，剪刀准确地弹出 y
 次，纸牌的准确地弹出 z
 次。然而，鲍勃并不知道爱丽丝结果的顺序。

Before the game starts, Bob must choose all of his outcomes in advance. Help him find an optimal sequence of x+y+z
 outcomes such that, regardless of the order of Alice's outcomes, the number of rounds won by Bob is at least the number of rounds won by Alice.
游戏开始前，鲍勃必须提前决定所有结果。帮助他找到一个最优的 x+y+z
 结果序列，使得无论爱丽丝的结果顺序如何，鲍勃赢得的回合数至少等同于爱丽丝赢得的回合数。

It is guaranteed that such a sequence always exists.
保证这样的序列总是存在。

Input  输入
The first line of the input contains a single integer t
 (1≤t≤1000
) — the number of test cases. The description of each test case follows.
输入文件的第一行包含一个整数 t
 ( 1≤t≤1000
 )，表示测试用例的数量。每个测试用例的描述会在下一行中给出。

The only line of each test case contains three space-separated integers x
, y
, and z
 (0≤x,y,z≤100
; x+y+z>0
) — the number of times Alice will play Rock, Scissors, and Paper, respectively.
每个测试用例的唯一行包含三个空格分隔整数 x
 、 y
 和 z
 （ 0≤x,y,z≤100
 ; x+y+z>0
 ） —— 分别表示爱丽丝将出石头、剪刀和布的次数。

Output  输出结果
Print a string s
 of length x+y+z
 consisting only of the characters R, S, and P. The i
-th character si
 represents Bob's move in the i
-th round: R for Rock, S for Scissors, and P for Paper.
打印一个字符串 s
 ，长度为 x+y+z
 ，仅包含字符 R、S 和 P。 i
 -th 字符 si
 代表 Bob 在 i
 -th 轮中的走法：R 代表石头，S 代表剪刀，P 代表纸。

The output string s
 must satisfy the required condition. If multiple valid answers exist, output any one of them.
输出字符串 s
 必须满足所需条件。如果存在多个有效答案，请输出其中任意一个。

Example  示例
Input  输入Copy  副本
2
0 0 3
1 1 2
Output  输出结果Copy  副本
RPS
SPSS
Note  注意/备注
In the first test case, Alice can only play Paper in all three rounds.
在第一个测试案例中，爱丽丝只能在三轮中使用纸牌。

Bob chooses RPS. Thus, Bob loses once with Rock, wins once with Scissors, and draws once with Paper. Therefore, Bob wins 1
 round and Alice wins 1
 round, so the required condition is satisfied.
鲍勃选择了 RPS。因此，鲍勃用石头输过一次，用剪刀赢了一次，用纸牌赢了一次。因此，鲍勃赢得 1
 这一轮，爱丽丝赢得 1
 这一轮，因此满足了所需的条件。

 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
t = int(input())
for _ in range(t):
    x,y,z = read()
    maximum = max(x,y,z)
    s = (x+y+z)
    if(x == maximum):
        ans = "P"*s
    elif(y == maximum):
        ans = "R"*s
    elif(z == maximum):
        ans = "S"*s
    print(ans)
