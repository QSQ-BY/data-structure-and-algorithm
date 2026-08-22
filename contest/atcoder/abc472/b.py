import sys
from bisect import bisect_left,bisect_right
from itertools import accumulate
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())
prefix = [0,*accumulate(arr)]
sum = prefix[n]
mid = sum/2
index = bisect_left(prefix,mid)
number1 = prefix[index]
number2 = prefix[index-1]
print(min(abs(sum-2*number1),abs(sum-2*number2)))