
import sys
input = sys.stdin.buffer.readline
n = int(input())
bank = {}
cur = 1
for _ in range(n):
    string = input().decode().strip()
    if(string not in bank):
        bank[string] = cur
        print(cur)
        cur += 1
    elif(string in bank):
        print(bank[string])
