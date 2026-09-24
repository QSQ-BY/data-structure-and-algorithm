""" 题目描述
在蓝桥王国，国王统治着一支由 n 个小队组成的强大军队。每个小队都由相同职业的士兵组成。具体地，第 i 个小队包含了 b 
i
​
  名职业为 a 
i
​
  的士兵。

近日，国王计划在王宫广场举行一场盛大的士兵检阅仪式，以庆祝王国的繁荣昌盛。然而，在士兵们入场的过程中，一场突如其来的风暴打乱了他们的行列，使得不同小队的士兵混杂在一起，次序乱成一团，

尽管国王无法知道每个士兵的具体职业，但为了确保仪式能顺利进行，国王打算从这些混乱的士兵中选出一部分，组成 k 个“纯职业小组”进行检阅。一个“纯职业小组”定义为由 3 名同职业的士兵组成的队伍。

请问，国王至少需要选择多少名士兵，才能确保这些士兵可以组成 k 个“纯职业小组”？

输入格式
输入的第一行包含一个整数 T，表示每次输入包含 T 组数据。

接下来依次描述 T 组数据。

每组数据的第一行包含两个整数 n 
t
​
  和 k ，用一个空格分隔，表示小队的数量和要组成的纯职业小组的数量。

接下来的 n 
t
​
  行，每行包含两个整数 a 
i
​
  和 b 
i
​
 ，用一个空格分隔，表示第 i 个小队中士兵的职业和数量。

输出格式
输出 T 行，每行包含一个整数，依次表示每组数据的答案，即为了组成 k 个“纯职业小组”，国王至少需要选择的士兵数量。如果无论如何也无法组成 k 个“纯职业小组”，则输出 −1。

输入输出样例
输入 #1复制

2
3 2
1 3
2 3
3 3
3 5
1 3
2 3
3 3
输出 #1复制

8
-1
说明/提示
对于 50% 的评测用例，1≤T≤10，1≤∑ 
t=1
T
​
 n 
t
​
 ≤2×10 
3
 ,1≤a 
i
​
 ,b 
i
​
 ≤10 
5
 ,1≤k≤10 
7
 。

对于所有评测用例，1≤T≤100，1≤∑ 
t=1
T
​
 n 
t
​
 ≤2×10 
5
 ,1≤a 
i
​
 ,b 
i
​
 ≤10 
9
 ,1≤k≤10 
13
 。

样例解释
在第一个样例中，要想组成 2 个“纯职业小组”，国王至少需要选择 8 名士兵。若只选择了 7 名士兵，则这 7 名士兵的职业可能为 1,1,1,2,2,3,3，无法组成 2 个“纯职业小组”。

在第二个样例中，即使选择了所有士兵，也无法组成 5 个“纯职业小组”，因此输出 −1。 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

t = int(input())

def solve():
    n, k = read()

    group = {}

    for _ in range(n):
        kind, number = read()

        if kind in group:
            group[kind] += number
        else:
            group[kind] = number

    # cnt1: 再多 1 个人可以多组成一个小组
    # cnt2: 再多 2 个人可以多组成一个小组
    # cnt3: 再多 3 个人可以多组成一个小组
    cnt1 = cnt2 = cnt3 = 0

    total_groups = 0
    base = 0

    for kind, number in group.items():

        # 每种类型最多先拿 2 个，不会形成完整的 3 人组
        base += min(2, number)

        q, r = divmod(number, 3)

        total_groups += q

        # 连一个完整小组都没有
        if q == 0:
            continue

        if r == 0:
            # number = 3q
            # 最后一个小组只需要再拿 1 人
            # 前 q-1 个需要各拿 3 人
            cnt3 += q - 1
            cnt1 += 1

        elif r == 1:
            # number = 3q + 1
            # 最后一个小组需要再拿 2 人
            cnt3 += q - 1
            cnt2 += 1

        else:
            # number = 3q + 2
            # q 个小组都需要各拿 3 人
            cnt3 += q

    # 总共都凑不出 k 个小组
    if total_groups < k:
        return -1

    # 为了使答案尽可能大，
    # 在只组成 k-1 个小组的情况下尽可能多拿人
    remain = k - 1
    bad = base

    # 优先选择“一个小组可以多拿 3 人”的情况
    take = min(remain, cnt3)
    bad += take * 3
    remain -= take

    # 再选择多拿 2 人
    take = min(remain, cnt2)
    bad += take * 2
    remain -= take

    # 最后选择多拿 1 人
    take = min(remain, cnt1)
    bad += take
    remain -= take

    return bad + 1


ans = []

for _ in range(t):
    ans.append(solve())

for number in ans:
    print(number)