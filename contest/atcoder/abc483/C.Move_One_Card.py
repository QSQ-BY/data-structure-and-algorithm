""" Problem Statement  问题陈述
You are given sequences 
A=(A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ) and 
B=(B 
1
​
 ,B 
2
​
 ,…,B 
N
​
 ) of length 
N consisting of positive integers.
你有由正整数组成的、长度为 
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
 ) 和 
B=(B 
1
​
 ,B 
2
​
 ,…,B 
N
​
 ) 。

The following operation is performed on the sequence 
A exactly once.
对序列 
A 恰好执行一次以下操作。

Choose one element of 
A, take it out, and insert it at any position in the remaining sequence. More formally, perform the following two steps in order.
从 
A 中选择一个元素，将其取出，然后插入到剩余序列的任意位置上。更正式地说，需要按顺序执行以下两个步骤。
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
1≤j≤N, and let the sequence 
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
1≤j≤N 条件的整数 
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
Note that the element may be inserted at the left end or the right end of the sequence.
请注意，该元素可以插入到序列的左端或右端。

Determine whether it is possible to make 
A equal to 
B after the operation.
判断在操作之后是否可以让 
A 等于 
B 。

Constraints  约束条件
1≤N≤2×10 
5
 
1≤A 
i
​
 ≤N (1≤i≤N)
1≤B 
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
 
B 
1
​
  
B 
2
​
  
… 
B 
N
​
 
Output  输出
Print Yes in one line if it is possible to make 
A equal to 
B by performing the operation exactly once, and No otherwise.
如果可以通过恰好执行一次操作使 
A 等于 
B ，则在一行中打印 Yes ，否则打印 No 。

Sample Input 1  示例输入 1 复制
Copy  复制
6
1 4 1 4 2 1
1 4 1 1 4 2
Sample Output 1  示例输出 1 复制
Copy  复制
Yes
For example, by taking out 
A 
6
​
  and inserting it between the 
3-rd and 
4-th elements of the remaining sequence, 
A after the operation becomes 
(1,4,1,1,4,2).
例如，通过取出 
A 
6
​
  并将其插入到剩余序列中的第 
3 个元素与第 
4 个元素之间，操作后的 
A 就会变成 
(1,4,1,1,4,2) 。

Thus, print Yes.  因此，打印 Yes 。

Sample Input 2  示例输入 2 复制
Copy  复制
2
1 1
1 2
Sample Output 2  示例输出 2 复制
Copy  复制
No
No matter what operation is performed on 
A, it cannot be made equal to 
B.
无论对 
A 进行何种操作，都无法使其等于 
B 。

Sample Input 3  示例输入 3 复制
Copy  复制
3
1 2 3
1 2 3
Sample Output 3  示例输出 3 复制
Copy  复制
Yes
The element taken out may be inserted back at its original position.
取出的元素可以重新插入到原来的位置。

Sample Input 4  示例输入 4 复制
Copy  复制
30
25 11 21 15 30 20 17 19 17 21 10 13 22 10 22 14 30 25 17 25 11 19 27 27 15 18 16 16 20 16
25 11 15 30 20 17 19 17 21 10 13 22 10 22 14 30 25 17 25 11 19 27 27 15 21 18 16 16 20 16
Sample Output 4  示例输出 4 复制
Copy  复制
Yes """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = int(input())
a = list(read())
b = list(read())

# 找到最左边和最右边不同的位置
l = 0
while l < n and a[l] == b[l]:
    l += 1

if l == n:
    print("Yes")
    sys.exit()

r = n - 1
while a[r] == b[r]:
    r -= 1

# 将左端卡牌移到右端，或将右端卡牌移到左端
move_right = a[l] == b[r] and a[l + 1:r + 1] == b[l:r]
move_left = a[r] == b[l] and a[l:r] == b[l + 1:r + 1]

print("Yes" if move_right or move_left else "No")
