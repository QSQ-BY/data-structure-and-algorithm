""" Problem Statement  问题描述
You are given a length-
N integer sequence 
A=(A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ).
给你一个长度为 
N 的整数序列 
A=(A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ) 。

You will perform the following operation on 
A exactly once.
你将对 
A 执行以下操作，且每条操作只能执行一次。

Choose an integer 
i between 
1 and 
N−K+1, inclusive. Sort 
A 
i
​
 ,A 
i+1
​
 ,…,A 
i+K−1
​
  in ascending order. More formally, let 
B 
1
​
 ,B 
2
​
 ,…,B 
K
​
  be 
A 
i
​
 ,A 
i+1
​
 ,…,A 
i+K−1
​
  arranged in increasing order, and simultaneously replace 
A 
i+j−1
​
  with 
B 
j
​
  for 
1≤j≤K.
请在 
1 到 
N−K+1 之间选择一个整数 
i ，包括 
1 和 
N−K+1 。然后把 
A 
i
​
 ,A 
i+1
​
 ,…,A 
i+K−1
​
  中的元素按升序排列。更正式地说，让 
B 
1
​
 ,B 
2
​
 ,…,B 
K
​
  表示按升序排列后的 
A 
i
​
 ,A 
i+1
​
 ,…,A 
i+K−1
​
  中的元素；同时，用 
B 
j
​
  替换 
1≤j≤K 中的元素。
Determine whether it is possible that, after this operation, 
A is in ascending order, that is, 
A 
i
​
 ≤A 
i+1
​
  holds for all 
1≤i<N.
判断在这样的操作之后， 
A 是否有可能处于升序状态，也就是说，对于所有的 
1≤i<N 来说， 
A 
i
​
 ≤A 
i+1
​
  都成立。

Constraints  约束
1≤K<N≤2×10 
5
 
1≤A 
i
​
 ≤N (1≤i≤N)
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

N 
K
A 
1
​
  
A 
2
​
  
… 
A 
N
​
 
Output  输出
If 
A can be sorted in ascending order by performing the operation once, output Yes; otherwise, output No.
如果通过执行一次该操作，能够使 
A 按升序排列，则输出 Yes ；否则，输出 No 。

Sample Input 1  示例输入 1 复制
Copy  副本
9 6
1 4 1 4 2 1 3 5 6
Sample Output 1  示例输出 1 复制
Copy  副本
Yes
For example, if you choose 
2 as 
i, then 
(A 
2
​
 ,A 
3
​
 ,A 
4
​
 ,A 
5
​
 ,A 
6
​
 ,A 
7
​
 )=(4,1,4,2,1,3) is replaced with 
(1,1,2,3,4,4). After the operation, 
A is 
(1,1,1,2,3,4,4,5,6), which satisfies the condition.
例如，如果你将 
2 设置为 
i ，那么 
(A 
2
​
 ,A 
3
​
 ,A 
4
​
 ,A 
5
​
 ,A 
6
​
 ,A 
7
​
 )=(4,1,4,2,1,3) 就会被替换为 
(1,1,2,3,4,4) 。操作完成后， 
A 就变成了 
(1,1,1,2,3,4,4,5,6) ，这样就满足了条件。

Thus, output Yes.  因此，输出为 Yes 。

Sample Input 2  示例输入 2 复制
Copy  副本
3 1
3 2 1
Sample Output 2  样本输出 2Copy
Copy  副本
No
K=1, so 
A does not change regardless of which 
i the operation is performed on. Thus, output No.
K=1 ，因此，无论对哪个 
i 进行操作， 
A 的值都不会改变。所以，输出结果为 No 。

Sample Input 3  示例输入 3 复制
Copy  副本
30 25
1 2 2 22 14 10 14 10 18 5 15 8 17 22 10 17 11 25 13 16 9 19 26 7 11 12 23 3 30 30
Sample Output 3  示例输出 3 复制
Copy  副本
Yes """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,k = read()
arr = list(read())
target = sorted(arr)
bad = [i for i in range(n) if arr[i] != target[i]]

if not bad:
    print("Yes")
elif bad[-1] - bad[0] + 1 <= k:
    print("Yes")
else:
    print("No")