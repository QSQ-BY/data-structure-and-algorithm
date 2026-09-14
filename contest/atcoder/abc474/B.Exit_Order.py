import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
arr = list(read())
ans = [i for i in range(1,n+1)]
window_right = 9
window_left = 0
while window_left < n:
    window_right = min(n-1,window_right)
    temp = arr[window_left : window_right+1]
    temp.sort()
    if(temp != ans[window_left : window_right+1]):
        print("No")
        sys.exit()
    window_left += 10
    window_right += 10
print("Yes")