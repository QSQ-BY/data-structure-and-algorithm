""" 题目背景
对应的选择、判断题：https://ti.luogu.com.cn/problemset/1169

题目描述
小杨有 n 种武器和 m 种强化材料。第 i 种强化材料会适配第 p 
i
​
  种武器，小杨可以花费 c 
i
​
  金币将该材料对应的适配武器修改为任意武器。

小杨最喜欢第 1 种武器，因此他希望适配该武器的强化材料种类数严格大于其他的武器，请你帮小杨计算为了满足该条件最少需要花费多少金币。

输入格式
第一行包含两个正整数 n,m，含义如题面所示。

之后 m 行，每行包含两个正整数 p 
i
​
 ,c 
i
​
 ，代表第 i 种强化材料的适配武器和修改花费。

输出格式
输出一个整数，代表能够使适配第 1 种武器的强化材料种类数严格大于其他的武器最少需要花费的金币。

输入输出样例
输入 #1复制

4 4
1 1
2 1
3 1
3 2
输出 #1复制

1
说明/提示
样例解释
花费 1，将第三种强化材料的适配武器由 3 改为 1。此时，武器 1 有 2 种强化材料适配，武器 2 和武器 3 都各有 1 种强化材料适配，满足适配第 1 种武器的强化材料种类数严格大于其他的武器。

数据范围
对于 100% 的数据，保证 1≤n,m≤1000，1≤p 
i
​
 ≤n，1≤c 
i
​
 ≤10 
9
 。

子任务编号	得分占比	n	m
1	20%	≤2	≤1000
2	20%	≤1000	≤2
3	60%	≤1000	≤1000 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
#一共m种材料，n种武器
n,m = read()
g = [[]for _ in range(n+1)]
cnt = [0]*(n+1)
for _ in range(m):
    weapon,cost = read()
    cnt[weapon] += 1
    if(weapon == 1):
        continue
    g[weapon].append(cost)

diff = max(cnt) - cnt[1]

# 每把武器的材料按修改费用升序排列
for costs in g:
    costs.sort()

ans = float('inf')
#枚举武器1要达到的数量t
for t in range(cnt[1], m + 1):
    have = cnt[1]
    total = 0
    optional = []

    for i in range(2, n + 1):
        # 为了让武器i最多剩t-1个，必须转走k个
        k = max(0, len(g[i]) - t + 1)
        #转移走的武器i应该全部交给武器1
        have += k
        #计算总花费，增加了这么多
        total += sum(g[i][:k])

        # 剩下的材料可以用于补足武器1的数量
        optional.extend(g[i][k:])

    #如果把其他所有武器的数量都控制在了t-1，现在的武器1还是不足t的话
    #就需要在剩下的里面找补
    need = max(0, t - have)

    optional.sort()
    total += sum(optional[:need])

    ans = min(ans, total)

print(ans)