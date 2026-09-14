""" Problem Statement
A certain shop sells 
N types of products. Each product can be purchased any number of times.

The 
i-th type of product 
(1≤i≤N) can be bought in the following two ways:

Buy it for 
A 
i
​
  yen without using a coupon, and receive one coupon.
Use one coupon and buy it for 
B 
i
​
  yen.
Initially, you have no coupons.

Find the minimum amount of money required to buy every product at least once.

You are given 
T test cases; solve each of them.

Constraints
1≤T≤2×10 
5
 
1≤N≤2×10 
5
 
1≤B 
i
​
 <A 
i
​
 ≤10 
9
 
The sum of 
N over all test cases is at most 
2×10 
5
 .
All input values are integers.
Input
The input is given from Standard Input in the following format:

T
case 
1
​
 
case 
2
​
 
⋮
case 
T
​
 
Each test case is given in the following format:

N
A 
1
​
  
B 
1
​
 
A 
2
​
  
B 
2
​
 
⋮
A 
N
​
  
B 
N
​
 
Output
Output the answers for the test cases in order, separated by newlines.

Sample Input 1
Copy
3
5
11 6
6 5
2 1
8 3
7 4
4
5 1
5 2
5 3
5 4
6
24 13
24 2
50 12
35 25
28 26
10 1
Sample Output 1
Copy
23
13
100
Consider the first test case.

For example, by acting as follows, you can buy every product at least once for 
23 yen:

Buy the second type of product for 
6 yen without using a coupon. You now have 
1 coupon.
Buy the third type of product for 
2 yen without using a coupon. You now have 
2 coupons.
Buy the third type of product for 
2 yen without using a coupon. You now have 
3 coupons.
Use a coupon to buy the first type of product for 
6 yen. You now have 
2 coupons.
Use a coupon to buy the fourth type of product for 
3 yen. You now have 
1 coupon.
Use a coupon to buy the fifth type of product for 
4 yen. You now have 
0 coupons.
It is impossible to buy every product at least once for less than 
23 yen, so output 
23 on the first line. """
import sys
input = sys.stdin.buffer.readline

def read():
    return map(int,input().split())

def solve() -> int:
    n = int(input())

    diff = []
    base = 0
    cost = 10**18

    for _ in range(n):
        a, b = map(int, input().split())
        base += b
        cost = min(cost, a)
        diff.append(a - b)

    diff.sort()
    # k = 0：额外买 n 张券，每种商品都用券购买
    ans = base + n * cost
    prefix = 0

    for k in range(1, n + 1):
        # 选择差价最小的 k 种商品原价购买
        prefix += diff[k - 1]
        # 还需要额外获取的优惠券数量
        missing = max(0, n - 2 * k)
        total = base + prefix + missing * cost
        ans = min(ans, total)
    return ans

def main():
    t = int(input())
    ans = []
    while t:
        t-=1
        ans.append(solve())
    for number in ans:
        print(number)

if __name__ == "__main__":
    main()

