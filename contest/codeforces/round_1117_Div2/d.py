""" D. Bermuda Rectangle
time limit per test2 seconds
memory limit per test256 megabytes
The Beaver is swimming across the ocean (yes, he can do that). Here, it aims to explore the Bermuda Rectangle. Of course, it poses no danger to The Beaver, but it is interesting from a scientific perspective.

Unlike the Bermuda Triangle, not much is known about the Bermuda Rectangle. Specifically, The Beaver knows for sure that the area of the rectangle is S
, its sides are integers, and the bottom left corner is located at the point (0,0)
.

The Beaver is interested in how many cells from a rectangle with sides x
 and y
, whose bottom left corner is at the point (0,0)
, can be located within the Bermuda Rectangle. A cell is considered to be within the Bermuda Rectangle if there exists a rectangle that satisfies the given constraints of the Bermuda Rectangle and contains that cell. Help The Beaver quickly respond to queries! You need to answer q
 such queries.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤10000
). The description of the test cases follows.

The first line of each test case contains two integers S
 and q
 — the area of the Bermuda Rectangle and the number of queries (1≤S≤1014
; 1≤q≤3⋅105
).

This is followed by q
 lines, each containing two integers x,y
 — the next query (1≤x,y≤S
).

It's guaranteed that the sum of q
 over all test cases doesn't exceed 3⋅105
.

It's guaranteed that the sum of S−−√
 over all test cases doesn't exceed 107
.

Output
For each query, output a single integer on a separate line — the answer to the query.

Example
InputCopy
3
6 4
2 3
4 5
6 6
1 1
5 2
2 2
3 4
8 2
3 1
5 6
OutputCopy
6
11
14
1
3
6
3
15
Note
In the first test case, every cell of the rectangle (2,3)
 is counted in the first query, since this rectangle itself can be the Bermuda Rectangle.

The second query of the first test case is illustrated in the figure. The answer to the query is the number of cells in the intersection of the blue and red shapes.

4 blue rectangles — possible positions of the Bermuda Rectangle. Red — the rectangle of the query (x,y)=(4,5)
In the third query of the first test case, every cell that can lie in at least one possible Bermuda Rectangle is counted.

In the fourth query of the first test case, the only cell of the query rectangle can lie in the Bermuda Rectangle, so the answer is 1
.



"""
import sys
from bisect import bisect_left,bisect_right
from math import isqrt
input = sys.stdin.buffer.readline

def build_matrix(n)->tuple[list[int],list[int]]:
    small_divisors = []
    large_divisors = []
    for i in range(1,isqrt(n)+1):
        if(n%i != 0):continue
        small_divisors.append(i)
        if(i*i != n):
            large_divisors.append(n//i)
    large_divisors.reverse()
    divisors = small_divisors + large_divisors
    prefix = [0]
    prev = 0
    for divisor in divisors:
        width = divisor-prev
        height = n//divisor
        prefix.append(prefix[-1]+width*height)
        prev = divisor
    return divisors,prefix


def get_area(x,n,divisors,prefix)->int:
    index = bisect_left(divisors,x)
    if(index>0):
        prev = divisors[index-1]
    else:
        prev = 0
    height = n//divisors[index]
    return prefix[index]+(x-prev)*height


def solve():
    n,q = map(int,input().split())
    divisors,prefix = build_matrix(n)
    ans = []
    while(q!=0):
        x,y = map(int,input().split())
        index = bisect_right(divisors,n//y)-1
        pos = min(x,divisors[index])

        if(pos == x):
            temp_ans = x*y
        else:
            temp_ans = y*pos
            temp_ans += get_area(x,n,divisors,prefix)-prefix[index+1]
        ans.append(str(temp_ans))
        q-=1
    return ans

def main()->None:
    t = int(input())
    ans = []
    while(t!=0):
        ans.extend(solve())
        t-=1
    sys.stdout.write('\n'.join(ans))

if __name__ == "__main__":
    main()
