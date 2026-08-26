""" 题目描述
你正在赌场玩一种新的纸牌游戏，规则如下：

游戏使用一副共 2n 张不同点数的牌。
牌堆被均匀分给玩家和庄家：每人获得 n 张牌。
在 n 轮比赛中，玩家和庄家同时打出手中最上面的一张牌。比较两张牌的点数，点数较大的一方获得 1 分。获胜的牌会被移出游戏，而失败的牌会返回持有者的手牌，并放在该玩家手牌堆的最上面。
注意游戏总是会进行恰好 n 轮。

你已经追踪了洗牌过程，知道庄家手牌的从上到下的顺序。为了最大化你的得分，你可以在游戏开始前交换手中任意两张牌的位置（最多交换一次以避免引起怀疑）。

请确定你能获得的最大分数。

输入格式
每个测试包含多个测试用例。第一行包含测试用例数量 t（1≤t≤5⋅10 
4
 ）。接下来是每个测试用例的描述。

每个测试用例的第一行包含一个整数 n（1≤n≤2⋅10 
5
 ）——玩家手牌的数量。

第二行包含 n 个整数 a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 （1≤a 
i
​
 ≤2n）——玩家手牌从上到下的点数。

第三行包含 n 个整数 b 
1
​
 ,b 
2
​
 ,…,b 
n
​
 （1≤b 
i
​
 ≤2n）——庄家手牌从上到下的点数。

保证所有牌的点数都是唯一的。

保证所有测试用例的 n 之和不超过 2⋅10 
5
 。

输出格式
对于每个测试用例，输出一个整数——你能获得的最大分数。

输入输出样例
输入 #1复制

3
7
13 7 4 9 12 10 2
6 1 14 3 8 5 11
3
1 6 5
2 3 4
5
8 6 3 10 1
7 9 5 2 4
输出 #1复制

6
2
3
说明/提示
在第一个测试用例中，可以不交换任何牌。游戏过程如下：

比较点数为 13 和 6 的牌。玩家获胜，得 1 分。
比较点数为 7 和 6 的牌。玩家获胜，得 1 分。
比较点数为 4 和 6 的牌。庄家获胜。
比较点数为 4 和 1 的牌。玩家获胜，得 1 分。
比较点数为 9 和 1 的牌。玩家获胜，得 1 分。
比较点数为 12 和 1 的牌。玩家获胜，得 1 分。
比较点数为 10 和 1 的牌。玩家获胜，得 1 分。
因此玩家总共获得 6 分。

在第二个测试用例中，可以交换点数为 1 和 5 的牌，交换后玩家手牌变为 [5,6,1]。游戏过程如下：

比较点数为 5 和 2 的牌。玩家获胜，得 1 分。
比较点数为 6 和 2 的牌。玩家获胜，得 1 分。
比较点数为 1 和 2 的牌。庄家获胜。
因此玩家总共获得 2 分。

在第三个测试用例中，可以交换点数为 3 和 10 的牌，交换后玩家手牌变为 [8,6,10,3,1]。游戏过程如下：

比较点数为 8 和 7 的牌。玩家获胜，得1分。
比较点数为 6 和 7 的牌。庄家获胜。
比较点数为 6 和 9 的牌。庄家获胜。
比较点数为 6 和 5 的牌。玩家获胜，得 1 分。
比较点数为 10 和 5的牌。玩家获胜，得 1 分。
因此玩家总共获得 3 分。 """

import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def competite(player:deque,competitor:deque,n:int)->int:
    #比赛一共会进行n轮
    score = 0
    for i in range(n):
        player_card = player[0]
        competitor_card = competitor[0]
        if(player_card > competitor_card):
            score += 1
            player.popleft()
        else:
            competitor.popleft()
    return score

def solve1()->int:
    ret = -1
    n = int(input())
    player = list(read())
    competitor = list(read())
    ret = competite(deque(player), deque(competitor), n)
    for i in range(n):
        for j in range(i):
            player[i] , player[j] = player[j],player[i]
            score = competite(deque(player) , deque(competitor),n)
            player[i] , player[j] = player[j],player[i]
            ret = max(ret,score)
    return ret


def solve2() -> int:
    n = int(input())
    player = list(read())
    competitor = list(read())
    # pref_min[i]：player[0:i+1] 中最小值的位置
    pref_min = [0] * n
    for i in range(1, n):
        pref_min[i] = pref_min[i - 1]
        if player[i] < player[pref_min[i]]:
            pref_min[i] = i
    # suf_max[i]：player[i:n] 中最大值的位置
    suf_max = [0] * n
    suf_max[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        suf_max[i] = suf_max[i + 1]
        if player[i] > player[suf_max[i]]:
            suf_max[i] = i
    # 不交换时的分数一定可行
    original_score = competite(
        deque(player),
        deque(competitor),
        n
    )
    left = original_score
    right = n-1
    if(original_score == n):
        return n
    def can_get(k:int)->bool:
        if(k == n):
            return False
        i = pref_min[k-1]
        j = suf_max[k]
        if(player[i] >= player[j]):
            return False
        player[i],player[j] = player[j],player[i]
        score = competite(deque(player),deque(competitor),n)
        player[i],player[j] = player[j],player[i]
        if(score >= k):
            return True
        else:
            return False

    while left < right:
        mid = (left + right+1)//2
        if(can_get(mid) == True):
            left = mid
        else:
            right = mid-1
    return left


def solve3() -> int:
    n = int(input())
    player = list(read())
    competitor = list(read())

    inf = 10**18

    # suffix_max[i] 表示 player[i:n] 中的最大值
    suffix_max = [-1] * (n + 1)#后缀最大值

    for i in range(n - 1, -1, -1):
        suffix_max[i] = max(
            suffix_max[i + 1],
            player[i]
        )

    # competitor_prefix_min[length]
    # 表示庄家前 length 张牌的最小值
    competitor_prefix_min = [inf] * (n + 1)#对手的前缀最小值

    for length in range(1, n + 1):
        competitor_prefix_min[length] = min(
            competitor_prefix_min[length - 1],
            competitor[length - 1]
        )

    min1 = inf#前缀最小值
    min2 = inf#前缀第二小值
    answer = 0

    for k in range(1, n + 1):
        value = player[k - 1]

        # 更新前 k 张牌的最小值和第二小值
        if value < min1:
            min2 = min1
            min1 = value
        elif value < min2:
            min2 = value

        # 不交换时，前 k 张牌的最小值
        best_min = min1#不交换的前缀最小值

        # k < n 时，才能从后半部分换一张牌进来
        if k < n:
            after_swap = min(
                min2,
                suffix_max[k]
            )#交换后的前缀最小值
            best_min = max(best_min, after_swap)#把交换和不交换的值取一个最大值

        # 庄家前 n-k+1 张中需要存在小于 best_min 的牌
        if best_min > competitor_prefix_min[n - k + 1]:
            answer = k
    return answer

def main():
    t = int(input())
    answers = []
    while(t!=0):
        #answers.append(solve1())
        #answers.append(solve2())
        answers.append(solve3())
        t -= 1
    for ans in answers:
        print(ans)

if(__name__ == "__main__"):
    main()