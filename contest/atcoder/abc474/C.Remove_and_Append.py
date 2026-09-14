""" Problem Statement
You are given a permutation 
P=(P 
1
​
 ,P 
2
​
 ,…,P 
N
​
 ) of 
(1,2,…,N).
For 
q=1,2,…,Q in this order, perform the following operation.

Remove the element with value 
a 
q
​
  from 
P, and append it to the end of 
P.
Find the value of each element of 
P after performing the 
Q operations.

Constraints
1≤N≤2×10 
5
 
1≤Q≤2×10 
5
 
(P 
1
​
 ,P 
2
​
 ,…,P 
N
​
 ) is a permutation of 
(1,2,…,N).
1≤a 
q
​
 ≤N
All input values are integers.
Input
The input is given from Standard Input in the following format:

N 
Q  
P 
1
​
  
P 
2
​
  
… 
P 
N
​
 
a 
1
​
   
a 
2
​
   
⋮  
a 
Q
​
   
Output
Output 
P 
1
​
 ,P 
2
​
 ,…,P 
N
​
  after performing the 
Q operations, in this order, separated by spaces, in one line.

Sample Input 1
Copy
4 2
2 4 3 1
3
2
Sample Output 1
Copy
4 1 3 2
Initially, 
P=(2,4,3,1).
After the first operation, 
P=(2,4,1,3).
After the second operation, 
P=(4,1,3,2).

Sample Input 2
Copy
3 3
1 2 3
1
1
1
Sample Output 2
Copy
2 3 1
Sample Input 3
Copy
2 5
2 1
1
1
2
2
1
Sample Output 3
Copy
2 1 """
import sys

input = sys.stdin.buffer.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
ops = [int(input()) for _ in range(q)]

seen = [False] * (n + 1)
tail = []

# 找到每个数的最后一次操作，得到从晚到早的顺序
for x in reversed(ops):
    if not seen[x]:
        seen[x] = True
        tail.append(x)

# 没被操作过的数，保留原来的相对顺序
ans = [x for x in arr if not seen[x]]

# 被操作过的数，按最后操作时间从早到晚放到末尾
ans.extend(reversed(tail))

print(*ans)