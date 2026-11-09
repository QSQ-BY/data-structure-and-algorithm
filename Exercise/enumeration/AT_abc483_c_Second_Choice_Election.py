""" Problem Statement  问题描述
AtCoder Village is holding an election to choose its mayor.
AtCoder Village 正在举行选举，以选出其市长。
There are 
N candidates, numbered candidate 
1, candidate 
2, 
…, candidate 
N.
共有 
N 名候选人，具体名单如下：候选人 
1 、候选人 
2 、 
… 、候选人 
N 。

There are 
M voters. The 
i-th voter 
(1≤i≤M) has candidate 
A 
i
​
  as their first choice and candidate 
B 
i
​
  as their second choice.
共有 
M 名选民。第 
i 名选民选择了候选人 
A 
i
​
  作为首选，而第 
(1≤i≤M) 名选民则选择了候选人 
B 
i
​
  作为第二选择。

When exactly one of the candidates withdraws, each voter votes as follows.
当其中一名候选人退出时，每位选民的投票方式如下：

If the voter's first-choice candidate has not withdrawn, the voter votes for their first-choice candidate.
如果选民的首选候选人没有撤回自己的提名，那么该选民就会投票给他们的首选候选人。
If the voter's first-choice candidate has withdrawn, the voter votes for their second-choice candidate.
如果选民的首选候选人已经退出竞选，那么该选民可以将选票投给他们的第二选择候选人。
Among the candidates who have not withdrawn, the candidate with the most votes wins. If there are multiple such candidates, the one with the smallest number wins.
在那些尚未撤回投票的候选人中，得票最多的候选人获胜。如果有多位候选人获得相同数量的票数，那么得票最少的候选人获胜。

For each 
k=1,2,…,N, find the number of the candidate who wins when only candidate 
k withdraws.
对于每一个 
k=1,2,…,N ，计算在只有候选人 
k 退出的情况下，哪位候选人能够获胜。

Constraints  约束
2≤N≤2×10 
5
 
1≤M≤2×10 
5
 
1≤A 
i
​
 ,B 
i
​
 ≤N
A 
i
​
 

=B 
i
​
 
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

N 
M
A 
1
​
  
B 
1
​
 
A 
2
​
  
B 
2
​
 
⋮
A 
M
​
  
B 
M
​
 
Output  输出结果
Print 
N lines. The 
i-th line should contain the number of the candidate who wins when only candidate 
i withdraws.
打印 
N 行内容。第 
i 行应该显示的是：当只有 
i 候选人退出时，谁会获胜。

Sample Input 1  示例输入 1 复制
Copy  副本
5 6
1 3
1 3
2 1
2 1
3 4
4 2
Sample Output 1  示例输出 1 复制
Copy  副本
3
1
1
2
1
When only candidate 
1 withdraws, the voters vote as follows.
当只有候选人 
1 退出时，选民的投票情况如下。

Voter 
1's first-choice candidate has withdrawn, so they vote for their second-choice candidate, candidate 
3.
选民 
1 的首选候选人已经退出竞选，所以他们选择投票给他们的第二选择候选人，即候选人 
3 。
Voter 
2's first-choice candidate has withdrawn, so they vote for their second-choice candidate, candidate 
3.
选民 
2 的首选候选人已经退出竞选，所以他们选择投票给他们的第二选择候选人，即候选人 
3 。
Voter 
3's first-choice candidate has not withdrawn, so they vote for their first-choice candidate, candidate 
2.
选民 
3 的首选候选人尚未退出竞选，因此他们选择投票给自己的首选候选人，即候选人 
2 。
Voter 
4's first-choice candidate has not withdrawn, so they vote for their first-choice candidate, candidate 
2.
选民 
4 的首选候选人尚未退出竞选，因此他们选择投票给自己的首选候选人，即候选人 
2 。
Voter 
5's first-choice candidate has not withdrawn, so they vote for their first-choice candidate, candidate 
3.
选民 
5 的首选候选人尚未退出竞选，因此他们选择投票给自己的首选候选人，即候选人 
3 。
Voter 
6's first-choice candidate has not withdrawn, so they vote for their first-choice candidate, candidate 
4.
选民 
6 的首选候选人尚未退出竞选，因此他们选择投票给自己的首选候选人，即候选人 
4 。
Thus, candidate 
2 receives 
2 votes, candidate 
3 receives 
3 votes, and candidate 
4 receives 
1 vote, so candidate 
3, who has the most votes, wins.  

When each of the other candidates withdraws instead, the results are as follows.  

When only candidate 
2 withdraws, candidate 
1 receives 
4 votes, candidate 
3 receives 
1 vote, and candidate 
4 receives 
1 vote, so candidate 
1, who has the most votes, wins.  
When only candidate 
3 withdraws, candidate 
1 receives 
2 votes, candidate 
2 receives 
2 votes, and candidate 
4 receives 
2 votes, so candidate 
1, who has the smallest number among those with the most votes, wins.  
When only candidate 
4 withdraws, candidate 
1 receives 
2 votes, candidate 
2 receives 
3 votes, and candidate 
3 receives 
1 vote, so candidate 
2, who has the most votes, wins.  
When only candidate 
5 withdraws, candidate 
1 receives 
2 votes, candidate 
2 receives 
2 votes, candidate 
3 receives 
1 vote, and candidate 
4 receives 
1 vote, so candidate 
1, who has the smallest number among those with the most votes, wins.  
Thus, print 
3,1,1,2,1 in this order, one per line.
   """

n, m = map(int, input().split())

cnt = [0] * (n + 1)
groups = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    groups[a].append(b)

# 找出原始票数最多的前两名
best1 = best2 = 0

for i in range(1, n + 1):
    if best1 == 0 or cnt[i] > cnt[best1]:
        best2 = best1
        best1 = i
    elif best2 == 0 or cnt[i] > cnt[best2]:
        best2 = i

# 统计临时增加的票数
add = [0] * (n + 1)
ans = []

for k in range(1, n + 1):
    # 排除已经退出的候选人
    winner = best2 if k == best1 else best1
    mx = cnt[winner]

    # 统计从 k 转移出去的选票
    changed = []

    for b in groups[k]:
        if add[b] == 0:
            changed.append(b)
        add[b] += 1

    # 只检查票数发生变化的候选人
    for b in changed:
        votes = cnt[b] + add[b]

        if votes > mx or (votes == mx and b < winner):
            mx = votes
            winner = b

        # 清空临时票数，供下一轮使用
        add[b] = 0

    ans.append(str(winner))

print('\n'.join(ans))
