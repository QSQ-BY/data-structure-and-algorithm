""" 题目描述
Rebecca 是一名导游，正在为她的杂志推广落基山脉。她最近拍了一张包含 N 座山的美丽照片，其中从左到右第 i 座山的高度为 h 
i
​
 。她将为她的杂志裁剪这张照片，可能会从照片的左侧移除一些山，也可能会从照片的右侧移除一些山。也就是说，裁剪包括从第 l 座山到第 r 座山的连续山峰，其中 l≤r。为了取悦她的杂志读者，Rebecca 将尝试找到最对称的裁剪。

我们将裁剪的不对称值定义为从裁剪的中点开始，每对等距山峰的高度差的绝对值之和。为了帮助理解这个定义，注意到一个数 v 的绝对值，记为 ∣v∣，是 v 的非负值：例如 ∣−6∣=6 和 ∣14∣=14。裁剪的不对称值是所有 ∣h 
l+i
​
 −h 
r−i
​
 ∣ 的和，其中 0≤i≤ 
2
r−l
​
 。换句话说，我们从外向内配对山峰，计算每对山峰高度差的绝对值，并将它们相加。

因为 Rebecca 不知道照片需要多宽，所以对于所有可能的裁剪长度，找到不对称值最小的裁剪（即最对称的裁剪）。

输入格式
第一行由一个整数 N 组成，表示照片中山的数量。

第二行由 N 个以空格分隔的整数组成，其中从左到右第 i 个整数表示 h 
i
​
 。

下表显示了可用的 15 分的分配方式：

分数	N 的范围	h 
i
​
  的范围	额外限制
5	1≤N≤300	0≤h 
i
​
 ≤10 
5
 	无。
5	1≤N≤5000	0≤h 
i
​
 ≤10 
5
 	山的高度从左到右单调不减。
5	1≤N≤5000	0≤h 
i
​
 ≤10 
5
 	无。
输出格式
输出一行 N 个以空格分隔的整数，其中从左到右第 i 个整数是长度为 i 的裁剪中最对称的裁剪的不对称值。

输入输出样例
输入 #1复制

7
3 1 4 1 5 9 2
输出 #1复制

0 2 0 5 2 10 10
输入 #2复制

4
1 3 5 6
输出 #2复制

0 1 3 7
说明/提示
对样例输入 1 的输出解释：

我们将展示为什么从左数第五个值是 2。让我们尝试计算所有长度为 5 的裁剪的不对称值。

第一个裁剪中山的高度是 [3,1,4,1,5]。这个裁剪的不对称值是 ∣3−5∣+∣1−1∣+∣4−4∣=2。

第二个裁剪中山的高度是 [1,4,1,5,9]。这个裁剪的不对称值是 ∣1−9∣+∣4−5∣+∣1−1∣=9。

最后一个裁剪中山的高度是 [4,1,5,9,2]。这个裁剪的不对称值是 ∣4−2∣+∣1−9∣+∣5−5∣=10。

因此，长度为 5 的最对称裁剪是不对称值为 2 的裁剪。

对样例输入 2 的输出解释：

这个样例满足第二个子任务。注意，唯一长度为 4 的裁剪是 [1,3,5,6]，其不对称值为 ∣1−6∣+∣3−5∣=7。

本题采用捆绑测试：

子任务 1（5 分）：1≤N≤300，0≤h 
i
​
 ≤10 
5
 。

子任务 2（5 分）：1≤N≤5000，0≤h 
i
​
 ≤10 
5
 ，保证山的高度从左到右单调不减。

子任务 3（5 分）：1≤N≤5000，0≤h 
i
​
 ≤10 
5
 。

题面翻译由 ChatGPT-4o 提供。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())
ans = [0]
#dp[i][j]表示从i位置到j位置的不整齐度
dp = [[0]*(n)for _ in range(n)]
#先初始化长度为2和长度为3的不整齐度
left = 0
right = 1
new_ans = float("inf")
while(right < n):
    dp[left][right] = abs(arr[left] - arr[right])
    new_ans = min(new_ans,dp[left][right])
    left += 1
    right += 1
ans.append(new_ans)
left = 0
right = 2
new_ans = float("inf")
while(right < n):
    dp[left][right] = abs(arr[left] - arr[right])
    new_ans = min(new_ans,dp[left][right])
    left+=1
    right += 1
ans.append(new_ans)
new_ans = float("inf")
#长度从4开始进行枚举
for length in range(4,n+1):
    new_ans = float("inf")
    for right in range(length-1,n):
        left = right - length+1
        dp[left][right] = dp[left+1][right-1]+abs(arr[left] - arr[right])
        new_ans = min(new_ans,dp[left][right])
    ans.append(new_ans)
print(*ans[:n])
