""" 题目背景
NOIP2007 普及组 T3

题目描述
恶魔猎手尤迪安野心勃勃，他背叛了暗夜精灵，率领深藏在海底的娜迦族企图叛变。

守望者在与尤迪安的交锋中遭遇了围杀，被困在一个荒芜的大岛上。

为了杀死守望者，尤迪安开始对这个荒岛施咒，这座岛很快就会沉下去。到那时，岛上的所有人都会遇难。

守望者的跑步速度为 17m/s，以这样的速度是无法逃离荒岛的。庆幸的是守望者拥有闪烁法术，可在 1s 内移动 60m，不过每次使用闪烁法术都会消耗魔法值 10 点。守望者的魔法值恢复的速度为 4 点每秒，只有处在原地休息状态时才能恢复。

现在已知守望者的魔法初值 M，他所在的初始位置与岛的出口之间的距离 S，岛沉没的时间 T。你的任务是写一个程序帮助守望者计算如何在最短的时间内逃离荒岛，若不能逃出，则输出守望者在剩下的时间内能走的最远距离。

注意：守望者跑步、闪烁或休息活动均以秒为单位，且每次活动的持续时间为整数秒。距离的单位为米。

输入格式
输入数据共一行三个非负整数，分别表示 M，S，T。

输出格式
输出数据共两行。

第一行一个字符串 Yes 或 No，即守望者是否能逃离荒岛。

第二行包含一个整数。第一行为 Yes 时表示守望者逃离荒岛的最短时间；第一行为 No 时表示守望者能走的最远距离。

输入输出样例
输入 #1复制

39 200 4
输出 #1复制

No
197
输入 #2复制

36 255 10
输出 #2复制

Yes
6
说明/提示
对于 30% 的数据，1≤T≤10，1≤S≤100；

对于 50% 的数据，1≤T≤10 
3
 ，1≤S≤10 
4
 ；

对于 100% 的数据，1≤T≤3×10 
5
 ，0≤M≤10 
3
 ，1≤S≤10 
8
 。 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#魔法初始值m，距离终点得路程s，限制时间t
m,s,t = read()
#best[i] = max(
#       i 秒全部跑步,
#       前 1 秒使用技能方案，后面跑步,
#       前 2 秒使用技能方案，后面跑步,
#       ...
#       前 i 秒全部使用技能方案
#   )

def test01():
    magic_dist = 0
    best_dist = 0
    for second in range(1,t+1):
        if(m>=10):
            m-=10
            magic_dist += 60
        else:
            m += 4

        best_dist = max(best_dist + 17,magic_dist)

        if(best_dist >= s):
            print("Yes")
            print(second)
            sys.exit()

    print("No")
    print(best_dist)

#使用枚举思维枚举,枚举使用技能的总时间与使用正常行走的总时间
def test02():
    m, s, t = map(int, input().split())
    mana = m
    magic_distance = 0

    min_time = None
    farthest = 0

    # 枚举前 skill_time 秒用于闪烁或休息
    for skill_time in range(t + 1):
        if skill_time > 0:
            if mana >= 10:
                mana -= 10
                magic_distance += 60
            else:
                mana += 4

        # 计算在规定的 t 秒内，这种分配能走多远
        running_time = t - skill_time
        distance = magic_distance + running_time * 17
        farthest = max(farthest, distance)

        # 计算采用这种分配时，最少还要跑多少秒才能到达出口
        remaining_distance = max(0, s - magic_distance)
        need_running_time = (remaining_distance + 16) // 17

        total_time = skill_time + need_running_time

        if total_time <= t:
            if min_time is None or total_time < min_time:
                min_time = total_time

    if min_time is not None:
        print("Yes")
        print(min_time)
    else:
        print("No")
        print(farthest)

test01()