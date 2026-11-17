""" Problem Statement  问题陈述
You are given a sequence 
A=(A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ) of length 
N consisting of positive integers.
你将得到一个由正整数组成的、长度为 
N 的序列 
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

The following operation is performed on the sequence 
A exactly once.
对序列 
A 恰好执行一次以下操作。

Choose one element of 
A, take it out, and insert it into the remaining sequence at its original position or earlier. More formally, perform the following two steps in order.
从 
A 中选择一个元素，将其取出，然后插入到剩余序列中的原位置或更早的位置上。更正式地说，需要按顺序执行以下两个步骤。
Choose an integer 
i satisfying 
1≤i≤N, let the sequence 
X=(X 
1
​
 ,X 
2
​
 ,…,X 
N−1
​
 ) of length 
N−1 be 
(A 
1
​
 ,A 
2
​
 ,…,A 
i−1
​
 ,A 
i+1
​
 ,A 
i+2
​
 ,…,A 
N
​
 ), and let the integer 
Y be 
A 
i
​
 .
选择一个满足 
1≤i≤N 条件的整数 
i ，令长度为 
N−1 的序列 
X=(X 
1
​
 ,X 
2
​
 ,…,X 
N−1
​
 ) 为 
(A 
1
​
 ,A 
2
​
 ,…,A 
i−1
​
 ,A 
i+1
​
 ,A 
i+2
​
 ,…,A 
N
​
 ) ，并令整数 
Y 等于 
A 
i
​
  。
Choose an integer 
j satisfying 
1≤j≤i, and let the sequence 
(X 
1
​
 ,X 
2
​
 ,…,X 
j−1
​
 ,Y,X 
j
​
 ,X 
j+1
​
 ,…,X 
N−1
​
 ) of length 
N be the new 
A.
选择一个满足 
1≤j≤i 条件的整数 
j ，并令长度为 
N 的序列 
(X 
1
​
 ,X 
2
​
 ,…,X 
j−1
​
 ,Y,X 
j
​
 ,X 
j+1
​
 ,…,X 
N−1
​
 ) 成为新的 
A 。
Note that in some cases the element can be inserted at the left end or the right end of the sequence.
请注意，在某些情况下，该元素可以插入到序列的左端或右端。

Find the number of distinct sequences that can be obtained as a result of the operation.
找出通过该操作能够得到的不同序列的个数。

Even if the pairs 
(i,j) chosen in the operation are different, the results are counted as the same if they are equal as sequences.
即使操作中选择的 
(i,j) 对不同，只要作为序列来看它们是相同的，其结果也视为相同。

Constraints  约束条件
1≤N≤2×10 
5
 
1≤A 
i
​
 ≤N (1≤i≤N)
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入数据从标准输入以如下格式给出：

N
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
Print the answer.  打印答案。

Sample Input 1  示例输入 1 复制
Copy  复制
6
1 4 1 4 2 1
Sample Output 1  示例输出 1 复制
Copy  复制
12
For example, performing the operation with 
i=6,j=4 yields 
(1,4,1,1,4,2).
例如，用 
i=6,j=4 执行该操作会得到 
(1,4,1,1,4,2) 。

Besides this, the following 
11 sequences can be obtained.
除此之外，还可以得到以下的 
11 序列。

(1,1,4,1,4,2)
(1,1,4,4,2,1)
(1,2,4,1,4,1)
(1,4,1,2,4,1)
(1,4,1,4,1,2)
(1,4,1,4,2,1)
(1,4,2,1,4,1)
(1,4,4,1,2,1)
(2,1,4,1,4,1)
(4,1,1,4,2,1)
(4,1,4,1,2,1)
Thus, print 12.  因此，打印 12 。

Sample Input 2  示例输入 2 复制
Copy  复制
5
1 1 1 1 1
Sample Output 2  示例输出 2 复制
Copy  复制
1
Note that sequences obtained by different pairs 
(i,j) are counted as one if they are equal as sequences.
请注意，如果由不同对 
(i,j) 生成的序列作为序列而言是相同的，则它们会被计为同一个。

Sample Input 3  示例输入 3 复制
Copy  复制
30
24 22 18 20 14 22 14 14 26 14 26 26 20 22 24 18 22 22 14 24 18 14 14 24 22 18 18 26 14 20
Sample Output 3  示例输出 3 复制
Copy  复制
303
 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())
n = int(input())
arr = list(read())
# s[x]：已经遍历过的数字中，x 出现了多少次
s = {}
ans = 1  # 原序列本身

for i, x in enumerate(arr):
    same = s.get(x, 0)
    # 只统计每段连续相同数字中的第一张卡牌
    if i > 0 and x != arr[i - 1]:
        ans += i - same
    # 无论当前卡牌是否贡献答案，都要更新出现次数
    s[x] = same + 1

print(ans)

