""" Problem Statement  问题陈述
There is a rectangular chocolate bar divided into a grid with 
30 rows and 
30 columns, where each cell corresponds to one piece of chocolate.
有一块矩形巧克力，被划分成了 
30 行和 
30 列的网格，每个格子代表一块巧克力。

The following operations are performed on this chocolate bar in order.
依次对这块巧克力进行以下操作。

Perform the operation of removing the bottommost row 
B times.
执行删除最底行操作 
B 次。
Perform the operation of removing the rightmost column 
R times.
执行删除最右列的操作，共 
R 次。
How many pieces of chocolate remain in the chocolate bar after all operations are finished?
所有操作完成后，巧克力棒里还剩下多少块巧克力？

Constraints  约束条件
All input values are integers.
所有输入值均为整数。
1≤B,R≤29
Input  输入
The input is given from Standard Input in the following format:
输入数据从标准输入以如下格式给出：

B 
R
Output  输出
Print the answer.  打印答案。

Sample Input 1  示例输入 1 复制
Copy  复制
8 8
Sample Output 1  示例输出 1 复制
Copy  复制
484
First, the operation of removing the bottommost row is performed 
8 times.
首先，执行删除最底行的操作共 
8 次。
After this, the chocolate bar has 
22 rows and 
30 columns.
此后，这块巧克力棒有 
22 行和 
30 列。
Then, the operation of removing the rightmost column is performed 
8 times.
然后，执行删除最右列的操作 
8 次。
After this, the chocolate bar has 
22 rows and 
22 columns.
此后，这块巧克力棒有 
22 行和 
22 列。
The number of remaining pieces of chocolate is 
484.
剩余的巧克力块数为 
484 。
Sample Input 2  示例输入 2 复制
Copy  复制
10 24
Sample Output 2  示例输出 2 复制
Copy  复制
120
Sample Input 3  示例输入 3 复制
Copy  复制
21 7
Sample Output 3  示例输出 3 复制
Copy  复制
207 """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())

a,b = read()
print((30 - a)*(30 - b))