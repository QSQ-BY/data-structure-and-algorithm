""" 题目描述
Luka 画了一张 3 行 N 列的表格，然后将整数 1 到 N 写进表格。对于表格第一行，每个整数只出现一次。对于其余两行，每个数字可以出现任意次或者不出现。

Luka 现在可以删去任意一些列。完成后，他对这个表的每一行进行升序排序。

他希望得到一张表，使得表中的三行在升序排序后完全相同。请您求出他至少需要删去多少列。

输入格式
第一行，一个整数 N，表示表中数字的列数。

接下来三行，每行包含 N 个整数。这些整数都在 1 到 N 之间，第一行每个数字有且仅出现一次。

输出格式
一行，一个整数，表示 Luka 至少需要删除的列数。

输入输出样例
输入 #1复制

7
5 4 3 2 1 6 7
5 5 1 1 3 4 7
3 7 1 4 5 6 2 
输出 #1复制

4
输入 #2复制

9
1 3 5 9 8 6 2 4 7
2 1 5 6 4 9 3 4 7
3 5 1 9 8 6 2 8 7
输出 #2复制

2
说明/提示
对于 40% 的测试点，N≤100。

对于 70% 的测试点，N≤10000。

对于 100% 的测试点，1≤N≤10 
5
 。

样例 1 解释：
对于样例 1，Luka 需要删除第二、第四、第六和第七列。删除并排序后，这三行都只包含 1,3,5 三个整数。

本题分值按照原比赛设置，满分 60 分。 """
import sys
from collections import deque
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
a = [[0]for _ in range(3)]
for i in range(3):
    a[i] = list(read())

#cnt[r][x]表示在第r行种数字x出现的次数
cnt = [[0]*(n+1)for _ in range(3)]
pos = [[]for _ in range(n+1)]#包含数字x的列的下标

for r in range(3):
    for i,x in enumerate(a[r]):
        cnt[r][x] += 1
        pos[x].append(i)
q = deque()
#数字x是否已经加入过队列
bad = [False]*(n+1)
for x in range(1,n+1):
    #如果有数字在三行之一没有出现过就把他加入队列
    #这个数字所在的列必须要删除
    if(any(cnt[r][x] == 0 for r in range(3))):
        bad[x] = True#数字x已经加入了队列
        q.append(x)
delete = [False]*n
ans = 0
while q:
    x = q.popleft()
    #遍历所有包含了x的列下标
    for i in pos[x]:
        if(delete[i]):
            continue
        delete[i] = True
        ans += 1
        for r in range(3):
            y = a[r][i]
            cnt[r][y] -= 1
            if(cnt[r][y] == 0 and bad[y] ==False):
                bad[y] = True
                q.append(y)
print(ans)
