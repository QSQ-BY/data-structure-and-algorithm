""" B – 无效选票/无效投票 / 
Time Limit: 2 sec / Memory Limit: 1024 MiB
时间限制：2 秒 / 内存限制：1024 MiB

Score : 
200 points  得分： 
200 分

Problem Statement  问题描述
N candidates 
1,2,…,N are running in an election. The name of each candidate consists of lowercase English letters, and the names are distinct. The name of candidate 
i is 
S 
i
​
 .
N 号候选人 
1,2,…,N 正在参加这次选举。每位候选人的名字都由小写英文字母组成，且各候选人的名字都不同。 
i 号候选人的名字是 
S 
i
​
  。

M ballots 
1,2,…,M were cast, and ballot 
j has a string 
T 
j
​
  consisting of lowercase English letters written on it.
共投出了 
M 张选票，其中第 
j 张选票上写着由小写英文字母组成的字符串 
T 
j
​
  。

If there is a candidate whose name exactly matches 
T 
j
​
 , that candidate receives 
1 vote. Otherwise, if there is exactly one candidate whose name can be obtained by changing 
1 character of 
T 
j
​
 , that candidate receives 
1 vote. Otherwise, the ballot is invalid.
如果存在某个候选人的名字与 
T 
j
​
  完全相同，那么该候选人将获得 
1 票。否则，如果存在恰好一个候选人的名字，只需将 
T 
j
​
  中的 
1 个字符进行替换就能得到该候选人的名字，那么该候选人将获得 
1 票。否则，该选票无效。

For each 
i=1,2,…,N, find how many votes candidate 
i receives.
对于每一个 
i=1,2,…,N ，统计候选人 
i 获得了多少票。

Constraints  约束
1≤N≤100
1≤M≤100
1≤∣S 
i
​
 ∣≤10
S 
i
​
 

=S 
j
​
  if 
i

=j.   
S 
i
​
 

=S 
j
​
  如果 
i

=j 的话。
1≤∣T 
j
​
 ∣≤10
S 
i
​
  and 
T 
j
​
  are strings consisting of lowercase English letters.
S 
i
​
  和 
T 
j
​
  是由小写英文字母组成的字符串。
N and 
M are integers.
N 和 
M 都是整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据以以下格式从标准输入端提供：

N 
M  
S 
1
​
   
S 
2
​
   
⋮  
S 
N
​
   
T 
1
​
   
T 
2
​
   
⋮  
T 
M
​
   
Output  输出结果
Print 
N lines in total.
总共打印 
N 行。
The 
i-th line should contain the number of votes candidate 
i receives.
第 
i 行应显示候选人 
i 所获得的票数。

Sample Input 1  示例输入 1 复制
Copy  副本
5 8
takahashi
aoki
sato
kato
kano
aoki
takanashi
sano
atcoder
chokudai
kato
aoki
yato
Sample Output 1  示例输出 1 复制
Copy  副本
1
2
0
1
0
There are 
5 candidates: takahashi, aoki, sato, kato, and kano.
共有 
5 位候选人： takahashi 、 aoki 、 sato 、 kato 和 kano 。
Ballot 
1 has aoki written on it.
选票上写着 aoki 。
Candidate 
2 receives 
1 vote.
候选人 
2 获得了 
1 票。

Ballot 
2 has takanashi written on it.
选票上写着 takanashi 。
Changing the 
5-th character from n to h makes it match the name of candidate 
1, and there is no other such candidate, so candidate 
1 receives 
1 vote.
将第 
5 个字符从 n 改为 h 后，该名称就与候选人 
1 的名称相符了。由于没有其他符合条件的候选人，因此候选人 
1 获得了 
1 票。

Ballot 
3 has sano written on it.
选票上写着 sano 。
Changing the 
3-rd character from n to t makes it match the name of candidate 
3, and changing the 
1-st character from s to k makes it match the name of candidate 
5, so this ballot is invalid.
将 
3 位置的字符从 n 改为 t 后，该字符就能与候选人 
3 的姓名相匹配；将 
1 位置的字符从 s 改为 k 后，该字符又能与候选人 
5 的姓名相匹配。因此，这张选票无效。

Sample Input 2  示例输入 2 复制
Copy  副本
2 5
a
b
a
b
c
a
aa
Sample Output 2  示例输出 2 复制
Copy  副本
2
1
 """
import sys
input = sys.stdin.buffer.readline

n, m = map(int, input().split())

score = {}
for _ in range(n):
    name = input().decode().strip()
    score[name] = 0

for _ in range(m):
    vote = input().decode().strip()

    # 完全匹配优先
    if vote in score:
        score[vote] += 1
        continue

    possible = []

    for name in score:
        # 替换一个字符不能改变长度
        if len(name) != len(vote):
            continue

        # 统计对应位置不同的字符数量
        diff = sum(a != b for a, b in zip(name, vote))
        if diff == 1:
            possible.append(name)
    # 只有唯一符合条件的候选人才能获得这张票
    if len(possible) == 1:
        score[possible[0]] += 1
# 字典保留候选人的输入顺序
for number in score.values():
    print(number)