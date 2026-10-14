""" Problem Statement  问题描述
Takahashi is at a ramen shop.
高桥现在在一家拉面店里。

This shop has 
N kinds of toppings, and the 
i-th topping has a price of 
i and a happiness of 
W 
i
​
 .
这家店有 
N 种配料可供选择。第 
i 种配料的价格为 
i ，能带来的快乐值为 
W 
i
​
  。

Takahashi chooses three distinct kinds of toppings so that the total price is at most 
V. Find the maximum possible total happiness of the toppings he chooses.
高桥选择了三种不同的配料，使得总价格不超过 
V 。请找出他所能选择的配料组合所带来的最大总幸福感。

The constraints guarantee that there is at least one way to choose three distinct kinds of toppings so that the total price is at most 
V.
这些约束条件确保了：总共有至少一种方式可以选择三种不同的配料，使得总价格不超过 
V 。

Constraints  约束
3≤N≤100
6≤V≤3N−3
1≤W 
i
​
 ≤10 
6
 
All input values are integers.
所有输入值均为整数。
Input  输入
The input is given from Standard Input in the following format:
输入从标准输入以以下格式给出：

N 
V
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
 
Output  输出
Output the answer in one line.
用一句话输出答案。

Sample Input 1  示例输入 1 复制
Copy  副本
5 9
31 41 59 26 53
Sample Output 1  示例输出 1 复制
Copy  副本
143
When choosing the first, third, and fifth toppings, the total price is 
1+3+5=9, and the total happiness is 
31+59+53=143.
当选择第一、第三和第五种配料时，总价格为 
1+3+5=9 ，总满意度为 
31+59+53=143 。

Sample Input 2  示例输入 2 复制
Copy  副本
10 16
102228 448944 131224 326172 500169 670309 976672 579051 974511 773940
Sample Output 2  样本输出 2Copy
Copy  副本
2095925
When choosing the second, sixth, and seventh toppings, the total price is 
2+6+7=15, and the total happiness is 
448944+670309+976672=2095925.
在选择第二、第六和第七种配料时，总价格为 
2+6+7=15 ，总幸福值为 
448944+670309+976672=2095925 。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,limit = read()#一共有n种配料，价格限制为limit
ans = float("-inf")
arr = [0]+list(read())#每一种配料的价格为i，能获得的最大哇快乐值为arr[i]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        for k in range(j+1,n+1):
            price = i+j+k
            if(price > limit):
                continue
            ans = max(ans,arr[i]+arr[j]+arr[k])

print(ans)

