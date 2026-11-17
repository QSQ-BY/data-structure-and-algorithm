import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
t = int(input())
for _ in range(t):
    n,m = read()
    number = list(input().decode().strip())
    operation = input().decode().strip()
    cur = 0
    for op in operation:
        if op == "L":
            if(cur==0):
                continue
            cur -= 1
        elif op == "R":
            if(cur == n-1):
                continue
            cur += 1
        elif op == "U":
            if(number[cur] == "9"):
                number[cur] = "0"
                continue
            number[cur] = str(int(number[cur]) + 1)
        elif op == "D":
            if(number[cur] == "0"):
                number[cur] = "9"
                continue
            number[cur] = str(int(number[cur]) - 1)
    print("".join(number))
