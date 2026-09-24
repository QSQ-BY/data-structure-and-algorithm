""" 
Problem Statement  问题描述
S is a string of length 
N consisting of lowercase English letters.
S 是一串长度为 
N 的字符串，由小写英文字母组成。
T is a string of length 
N consisting of lowercase English letters and *.
T 是一串长度为 
N 的字符串，由小写英文字母和 * 组成。
We say that 
S matches 
T if and only if 
T can be made equal to 
S by replacing each * in 
T with some lowercase English letter.
我们说，当且仅当可以通过将 
T 中的每个 * 替换为某个小写英文字母，使得 
T 等于 
S 时， 
S 才与 
T 相匹配。
Determine whether 
S matches 
T.
判断 
S 是否与 
T 相匹配。

Constraints  约束
1≤N≤100
S is a string of length 
N consisting of lowercase English letters.
S 是一串长度为 
N 的字符串，由小写英文字母组成。
T is a string of length 
N consisting of lowercase English letters and *.
T 是一串长度为 
N 的字符串，由小写英文字母和 * 组成。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

N  
S  
T  
Output  输出
Output Yes if 
S matches 
T, and No otherwise, in one line.
如果 
S 与 
T 相匹配，则输出 Yes ；否则输出 No 。所有内容均输出在同一行上。

Sample Input 1  示例输入 1 复制
Copy  副本
8
chokudai
**o*u*ai
Sample Output 1  示例输出 1 复制
Copy  副本
Yes
By replacing the first, second, fourth, and sixth characters of 
T, which are *, with c, h, k, and d, respectively, 
T can be made equal to 
S.
通过将 
T 中的第一个、第二个、第四个和第六个字符分别替换为 c 、 h 、 k 和 d ，就可以使 
T 等于 
S 。

Sample Input 2  示例输入 2 复制
Copy  副本
5
snuke
snake
Sample Output 2  样本输出 2Copy
Copy  副本
No
Sample Input 3  示例输入 3 复制
Copy  副本
5
yiwiy
*****
Sample Output 3  示例输出 3 复制
Copy  副本
Yes """

import sys
input = sys.stdin.buffer.readline

n = int(input())
string1 = list(input().decode().strip())
string2 = list(input().decode().strip())
for i in range(n):
    if(string2[i] == "*"):
        continue
    if(string1[i] != string2[i]):
        print("No")
        sys.exit()

print("Yes")