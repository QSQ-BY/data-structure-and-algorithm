import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
a,b = read()
n = a+b
ans = 0
while(n!=0):
    n = n//10
    ans += 1
print(ans)