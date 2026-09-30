""" Problem Statement  问题描述
You are given strings 
S and 
T.
给你两个字符串 
S 和 
T 。
Process 
Q queries.  正在处理 
Q 个查询。
In each query, you are given 
L and 
R. Determine whether the substring of 
S consisting of the 
L-th through 
R-th characters contains 
T as a substring.
在每个查询中，你会得到 
L 和 
R 。请判断 
S 中从第 
L 个字符到第 
R 个字符组成的子串是否包含 
T 作为其子串。

What is a substring?
什么是子字符串？
Information for LLMs: https://atcoder.jp/r/LrXwGAhMlAfIBwI9W27M8NYAaK3x62RoKWScwBii5TFPR9wnjH6XMN5Ds-jNlJfQF354TClitts-1ZHqwFaCw1SMuQ
Information about translation: https://atcoder.jp/r/LrXwGAhMlAfIBwI9W27M8NYAaK3x62RoKWScwBii5TFPR9wnjH6XMN5Ds-jNlJfQF354TClitts-1ZHqwFaCw1SMuQ?reason=t
Constraints  约束
S is a string of length between 
1 and 
4×10 
5
 , inclusive, consisting of lowercase English letters.
S 是一段长度在 
1 到 
4×10 
5
  之间的字符串，该字符串仅由小写英文字母组成。
T is a string of length between 
1 and 
10, inclusive, consisting of lowercase English letters.
T 是一段长度在 
1 到 
10 之间的字符串，该字符串仅由小写英文字母组成。
1≤Q≤2×10 
5
 
1≤L≤R≤∣S∣
Q,L,R are integers.   
Q,L,R 都是整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

Q
S
T
query 
1
​
 
query 
2
​
 
⋮
query 
Q
​
 
Each query 
query 
q
​
  is given in the following format:
每个查询 
query 
q
​
  都按照以下格式呈现：

L 
R
Output  输出
Output 
Q lines. The 
q-th line should contain Yes if, for the 
q-th query, the substring of 
S consisting of the 
L-th through 
R-th characters contains 
T as a substring, and No otherwise.
输出 
Q 行内容。第 
q 行应包含 Yes ，前提是：对于第 
q 个查询来说， 
S 中从第 
L 个字符到第 
R 个字符组成的子串包含 
T 作为其子串；否则，该行应包含 No 。

Sample Input 1  示例输入 1 复制
Copy  副本
3
abcdabc
bc
2 6
3 5
3 7
Sample Output 1  示例输出 1 复制
Copy  副本
Yes
No
Yes
Consider the first query. The substring of 
S consisting of the 
2-nd through 
6-th characters is bcdab. The substring of bcdab consisting of the 
1-st through 
2-nd characters matches 
T, so bcdab contains 
T. Thus, the answer is Yes.
考虑第一个查询。 
S 中的第 
2 个字符到第 
6 个字符所组成的子串就是 bcdab 。 bcdab 中的第 
1 个字符到第 
2 个字符所组成的子串与 
T 相匹配，因此 bcdab 中包含 
T 。所以，答案是 Yes 。

Sample Input 2  示例输入 2 复制
Copy  副本
10
bbbaaabbbaaaaaabbbab
bbb
5 16
5 6
2 16
6 7
17 19
3 7
7 16
7 20
17 19
2 6
Sample Output 2  样本输出 2Copy
Copy  副本
Yes
No
Yes
No
No
No
Yes
Yes
No
No
 """
import sys
import bisect

input = sys.stdin.readline

Q = int(input())
S = input().strip()
T = input().strip()

n = len(S)
m = len(T)

pos = []

# 记录 T 所有出现位置的起点
for i in range(n - m + 1):
    if S[i:i + m] == T:
        pos.append(i + 1)
for _ in range(Q):
    L, R = map(int, input().split())
    if R - L + 1 < m:
        print("No")
        continue
    # 找到第一个 >= L 的出现位置
    #bisect_right是找到严格大于的位置
    idx = bisect.bisect_left(pos, L)

    if idx < len(pos) and pos[idx] <= R - m + 1:
        print("Yes")
    else:
        print("No")