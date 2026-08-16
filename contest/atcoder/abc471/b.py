import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n = int(input())
ans = 0
d = {}
for i in range(n):
    cur = input()
    cur = cur.lower()
    if cur in d:
        d[cur] += 1
    else:
        d[cur] = 1

for i in d.values():
    ans = max(ans,i)

print(ans)