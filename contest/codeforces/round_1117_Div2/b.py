""" 
Two giants, Bea and Ver, are playing a game. Each giant has his own mountain range. You have already measured all these mountains and now know that the heights of the mountains in Bea's range are a1,a2,…an
, and in Ver's range are b1,b2,…bm
, with the mountains numbered from left to right for Bea and from right to left for Ver. At the beginning of the game, the giants stand on the mountain numbered 1
. Thus, they face each other and see all their mountains and all the mountains of their opponent. It turns out that Bea and Ver are connoisseurs of beauty, so the mountains in their ranges are arranged in non-increasing order, specifically ai≥ai+1
 for 1≤i<n
 and bi≥bi+1
 for 1≤i<m
.
两个巨人，贝亚和维尔，正在玩游戏。每个巨人都有自己的山脉。你已经测量了所有这些山脉的高度：贝亚所在山脉的山峰高度分别为 a1,a2,…an
 ，而维尔所在山脉的山峰高度则为 b1,b2,…bm
 。对于贝亚来说，山脉中的山峰是从左到右编号的；而对于维尔来说，则是从右到左编号的。游戏开始时，贝亚和维尔分别站在编号为 1
 的山峰上。这样，他们就能看到彼此的所有山脉。原来，贝亚和维尔都是审美高手，因此他们所拥有山脉中的山峰都是按非递增顺序排列的。具体来说，贝亚所在山脉的山峰高度为 ai≥ai+1
 ，而维尔所在山脉的山峰高度则为 1≤i<n
 ；同样地， bi≥bi+1
 对应着维尔所在山脉的 1≤i<m
 。

In the illustration below, there is an example of the initial arrangement, where Bea has the range a1,a2,a3=3,2,1
, and Ver has the range b1,b2=4,2
. For simplicity, the mountains are depicted as rectangles, with Bea's mountains on the left and Ver's on the right. For your good mood, the giants Bea and Ver are represented as beavers.
在下图中，展示了最初的布局情况：贝娅的领地为 a1,a2,a3=3,2,1
 ，而维尔的领地为 b1,b2=4,2
 。为便于理解，这些“山脉”被描绘成矩形形状，贝娅的领地在左侧，维尔的领地在右侧。为了让画面更有趣些，贝娅和维尔这些“巨人”被描绘成了海狸的形象。


Bea and Ver are not very smart, so on each turn they perform the same action. Specifically, the giant on his turn takes a boulder and throws it at the mountain on which his opponent is standing; as a result, the height of that mountain decreases by 1. If the giant on his turn sees that the mountain directly in front of him is higher (with a number one greater) than the one he is standing on, he jumps to it. If, however, the giant discovers that he is standing on regular ground (the height of the current mountain is 0) and there are no more mountains in front of him, he admits defeat. Bea goes first.
贝娅和维尔都不太聪明，所以每轮他们都会做同样的动作。具体来说，轮到巨人时，他会拿起一块巨石，朝对手所站的山峰扔去。这样一来，那座山峰的高度就会减少 1。如果巨人发现正前方的山峰比他现在所站的山峰更高，他就会跳到那座山上。不过，如果巨人发现自己站在平地上（即当前所站山峰的高度为 0），且前方没有其他山峰了，他就会认输。贝娅先行动。

You know that their game can last a very long time, due to the enormous heights of the mountains and their quantities, so you want to determine who will win.
你知道，由于山脉的高度极高且数量众多，他们的游戏可能会持续很长时间。因此，人们想要知道谁会获胜。

Input  输入
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.
每个测试包含多个测试用例。第一行包含测试用例的数量 t
 ( 1≤t≤500
 )。测试用例的描述随后给出。

The first line of each test case contains two integers n
 and m
 — the number of mountains in the first and second giant's range, respectively (1≤n,m≤100
).
每个测试用例的第一行包含两个整数： n
 和 m
 。它们分别表示第一个巨人和第二个巨人领地内的山峰数量（ 1≤n,m≤100
 ）。

The second line of the test case contains n
 integers a1,a2,…an
 — the heights of the mountains of the first giant (1≤ai≤109
; ai≥ai+1
).
测试用例的第二行包含 、 n
 个整数 、 a1,a2,…an
 ——它们分别代表第一个巨人的山脉的高度（ 、 1≤ai≤109
 ； 、 ai≥ai+1
 ）。

The third line of the test case contains m
 integers b1,b2,…bm
 — the heights of the mountains of the second giant (1≤bi≤109
; bi≥bi+1
).
测试用例的第三行包含 、 m
 个整数 、 b1,b2,…bm
 ——它们分别代表第二个巨人的山脉的高度（ 、 1≤bi≤109
 ； 、 bi≥bi+1
 ）。

Output  输出结果
For each test case, output a single number — the number of the giant who will win.
对于每个测试用例，输出一个数字——即获胜的巨人的编号。

Example  示例
Input  输入Copy  副本
6
1 1
1
1
1 1
1
2
1 2
4
4 1
4 2
4 3 2 1
10 1
4 2
4 3 2 1
6 5
4 2
4 3 2 1
7 5
Output  输出结果Copy  副本
1
2
2
2
1
2 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())
def solve():
    n,m = read()
    height1 = n
    height2 = m
    list1 = []
    list2 = []
    list1 = list(read())
    height1 += list1[0]
    list2 = list(read())
    height2 += list2[0]
    if(height1 >= height2):
        print(1)
    elif(height2 > height1):
        print(2)
    return


def main():
    t = int(input())
    while t:
        solve()
        t -=1
    return

if( __name__ == "__main__"):
    main()