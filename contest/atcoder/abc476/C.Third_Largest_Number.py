""" roblem Statement  问题描述
You are given an integer 
N not less than 
3 and a length-
N sequence of positive integers 
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
给定一个不小于 
3 的整数 
N ，以及一个由 
N 个正整数组成的序列 
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

For each 
k=3,4,…,N, solve the following problem:
对于每一个 
k=3,4,…,N ，请解决以下问题：

When 
A 
1
​
 ,A 
2
​
 ,…,A 
k
​
  are sorted in descending order, find the third value from the front.
当 
A 
1
​
 ,A 
2
​
 ,…,A 
k
​
  按降序排列后，找出从前往数的第三个数值。
Constraints  约束
3≤N≤5×10 
5
 
1≤A 
i
​
 ≤10 
9
 
All input values are integers.
所有输入值均为整数。
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
 
Output  输出
Output 
N−2 lines.  输出 
N−2 行内容。

The 
i-th line 
(1≤i≤N−2) should contain the answer for 
k=i+2.
第 
i 行 
(1≤i≤N−2) 应该包含 
k=i+2 的答案。

Sample Input 1  示例输入 1 复制
Copy  副本
5
1 2 1 2 3
Sample Output 1  示例输出 1 复制
Copy  副本
1
1
2
For 
k=3: sorting 
A 
1
​
 ,A 
2
​
 ,A 
3
​
  in descending order gives 
2,1,1. The third value from the front is 
1, so output 
1 on the first line.
对于 
k=3 来说：将 
A 
1
​
 ,A 
2
​
 ,A 
3
​
  按降序排序后得到 
2,1,1 。从前往数第三个数值是 
1 ，因此第一行应输出 
1 。
For 
k=4: sorting 
A 
1
​
 ,A 
2
​
 ,A 
3
​
 ,A 
4
​
  in descending order gives 
2,2,1,1. The third value from the front is 
1, so output 
1 on the second line.
对于 
k=4 来说：将 
A 
1
​
 ,A 
2
​
 ,A 
3
​
 ,A 
4
​
  按降序排序后得到 
2,2,1,1 。从前往数第三个数值是 
1 ，因此第二行应输出 
1 。
For 
k=5: sorting 
A 
1
​
 ,A 
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
  in descending order gives 
3,2,2,1,1. The third value from the front is 
2, so output 
2 on the third line.
对于 
k=5 来说：将 
A 
1
​
 ,A 
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
  按降序排序后得到的结果就是 
3,2,2,1,1 。从前往数第三个数值是 
2 ，因此第三行应输出 
2 。
Sample Input 2  示例输入 2 复制
Copy  副本
10
1 1 1 3 2 5 4 3 6 5
Sample Output 2  样本输出 2Copy
Copy  副本
1
1
1
2
3
3
4
5
Sample Input 3  示例输入 3 复制
Copy  副本
10
11 9 1 3 17 19 10 19 17 3
Sample Output 3  示例输出 3 复制
Copy  副本
1
3
9
11
11
17
17
17
 """
import sys

def solve():
    input = sys.stdin.buffer.readline
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 维护当前前 k 个元素中的前 3 大值
    # 初始先取前 3 个元素并降序排序
    top3 = sorted(arr[:3], reverse=True)

    ans = []
    # k = 3 的答案就是当前的第 3 大值
    ans.append(str(top3[2]))
    
    # 从第 4 个元素 (索引为 3) 开始遍历到第 N 个元素
    for i in range(3, n):
        val = arr[i]
        # 如果新元素比当前的第 3 大值还大，说明它能进入前 3 名
        if val > top3[2]:
            top3.append(val)
            top3.sort(reverse=True)
            top3.pop()  # 保持 top3 只留前 3 大的元素
        ans.append(str(top3[2]))
        
    # 一次性快速输出，提高 I/O 效率
    print('\n'.join(ans))

if __name__ == '__main__':
    solve()