""" Problem Statement  问题描述
There are 
N types of stones, 
1,2,…,N. Stones of the same type all have the same weight.
共有 
N 种类型的石头，即 
1,2,…,N 种。同一种类型的石头，其重量都是一样的。
Takahashi and Aoki have 
A 
i
​
  and 
B 
i
​
  stones of type 
i, respectively.
高桥和青木分别拥有 
i 类型的 
A 
i
​
  颗和 
B 
i
​
  颗石头。
Determine whether there exists a sequence of positive integers 
W=(W 
1
​
 ,W 
2
​
 ,…,W 
N
​
 ) satisfying the following conditions, and if it exists, construct one such sequence.
判断是否存在这样一列正整数 
W=(W 
1
​
 ,W 
2
​
 ,…,W 
N
​
 ) ，使其满足以下条件。如果存在，那么请构造出这样的一列数。

1≤W 
i
​
 ≤10 
18
 
If the weight of a type-
i stone is 
W 
i
​
 , the total weight of the stones Takahashi has is strictly greater than the total weight of the stones Aoki has.
如果某种类型的石头重量为 
W 
i
​
  ，那么高桥所拥有的所有石头的总重量，肯定大于青木所拥有的所有石头的总重量。
Constraints  约束
1≤N≤10 
5
 
1≤A 
i
​
 ≤10 
9
 
1≤B 
i
​
 ≤10 
9
 
All input values are integers.
所有输入值都是整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

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
   
Output  输出结果
If there exists 
W=(W 
1
​
 ,W 
2
​
 ,…,W 
N
​
 ) satisfying the conditions, output it in the following format:
如果存在满足条件的 
W=(W 
1
​
 ,W 
2
​
 ,…,W 
N
​
 ) ，请以以下格式输出：

Yes  
W 
1
​
  
W 
2
​
  
… 
W 
N
​
   
If there is no 
W=(W 
1
​
 ,W 
2
​
 ,…,W 
N
​
 ) satisfying the conditions, output No in one line.
如果没有满足条件的 
W=(W 
1
​
 ,W 
2
​
 ,…,W 
N
​
 ) ，则在一行中输出 No 。

Sample Input 1  示例输入 1 复制
Copy  副本
3
4 7 4
5 5 5
Sample Output 1  示例输出 1 复制
Copy  副本
Yes
4 7 4
If 
W=(4,7,4),  如果 
W=(4,7,4) ，
the total weight of the stones Takahashi has is 
4×4+7×7+4×4=81.
高桥所拥有的那些石头的总重量为 
4×4+7×7+4×4=81 。
The total weight of the stones Aoki has is 
4×5+7×5+4×5=75.
青木所拥有的所有石头的总重量为 
4×5+7×5+4×5=75 。

Sample Input 2  示例输入 2 复制
Copy  副本
3
3 3 3
4 7 4
Sample Output 2  示例输出 2 复制
Copy  副本
No
Sample Input 3  示例输入 3 复制
Copy  副本
1
2
2
Sample Output 3  示例输出 3 复制
Copy  副本
No """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr1 = list(read())
arr2 = list(read())
maximum = max(max(arr1),max(arr2))
index = -1
ans = [1]*n
for i in range(n):
    if(arr1[i] <= arr2[i]):
        continue
    index = i

if(index == -1):
    print("No")
else:
    print("Yes")
    ans[index] = maximum*n*100
    print(*ans)