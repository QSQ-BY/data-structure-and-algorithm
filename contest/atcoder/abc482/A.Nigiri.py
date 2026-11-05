import sys
input = sys.stdin.buffer.readline

string = input().decode().strip()

number = string.count("o")
if(number %2 == 1):
    print("odd")
else:
    print("even")