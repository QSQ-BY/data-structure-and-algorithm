""" Problem Statement
There are 
N points on the 
xy-plane, numbered 
1,2,…,N. The coordinates of point 
i are 
(i,A 
i
​
 ).

For 
i=1,2,…,N−1, connect point 
i and point 
i+1 with a line segment to form one polyline.

Find the number of points on this polyline (including its endpoints) whose 
y-coordinate is 
K.

Here, the constraints guarantee that the number of points satisfying the condition is finite.

Constraints
2≤N≤100
1≤A 
i
​
 ≤100 
(1≤i≤N)
A 
i
​
 

=A 
i+1
​
  
(1≤i<N)
1≤K≤100
All input values are integers.
Input
The input is given from Standard Input in the following format:

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
 
Output
Print the number of points on the polyline whose 
y-coordinate is 
K.

Sample Input 1
Copy
5 3
1 3 1 5 1
Sample Output 1
Copy
3
As shown in the figure below, there are 
3 points satisfying the condition: 
(2,3), 
( 
2
7
​
 ,3), and 
( 
2
9
​
 ,3).

Note that the point 
(2,3) is a common endpoint of the segment connecting points 
1 and 
2 and the segment connecting points 
2 and 
3, but it is counted as one point.



Sample Input 2
Copy
3 3
3 1 3
Sample Output 2
Copy
2
There are 
2 points satisfying the condition: 
(1,3) and 
(3,3). Note that the points at the ends of the polyline are also counted.

Sample Input 3
Copy
2 100
1 2
Sample Output 3
Copy
0
 """

import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n,k = read()

arr = list(read())
if( n == 1):
    if(arr[0] == k):
        print(1)
    else:
        print(0)
    sys.exit()
if(n==2):
    if(arr[0] > arr[1]):
        arr[0],arr[1] = arr[1],arr[0]
    if(arr[0]<k<arr[1]):
        print(1)
        sys.exit()
    ans = 0
    if(arr[0] == k):
        ans += 1
    if(arr[1] == k):
        ans += 1
    print(ans)
    sys.exit()
ans = 0
for i in range(n-1):
    a = arr[i]
    b = arr[i+1]
    if(a>b):
        a,b = b,a
    if(a<k<b):
        ans += 1
    if(a == k or b == k):
        ans += 1
if(arr[0] == k):
    ans += 1
if(arr[-1] == k):
    ans += 1

print(ans - arr.count(k))
