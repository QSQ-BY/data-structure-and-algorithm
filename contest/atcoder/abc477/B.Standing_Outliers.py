import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

n,d = read()
arr = list(read())
index = list(range(n))

index.sort(key = lambda i:arr[i])
ans = []
for i in range(n):
    if(i == 0):
        dis = arr[index[i+1]] - arr[index[i]]
        if(dis >= d):
            ans.append(index[i] + 1)
    if(i == n-1):
        dis = arr[index[i]] - arr[index[i-1]]
        if(dis >= d):
            ans.append(index[i] + 1)
    else:
        dis1 = arr[index[i+1]] - arr[index[i]]
        dis2 = arr[index[i]] - arr[index[i-1]]
        if(dis1 >= d and dis2 >= d):
            ans.append(index[i] + 1)
ans.sort()
print(len(ans))
print(*ans)
