import sys
input = sys.stdin.buffer.readline
n = int(input())
arr = list(map(int,input().split()))
prefix = [0]
for number in arr:
    prefix.append(prefix[-1] + number)

m = int(input())
ans = []

for i in range(m):
    left,right = map(int,input().split())
    ans.append(prefix[right] - prefix[left-1])

for i in range(len(ans)):
    print(ans[i])