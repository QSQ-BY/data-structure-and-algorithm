import sys
input = sys.stdin.readline

cur = str(input().strip())
if(cur == "B"):
    print("Y")
elif(cur == "R"):
    print("B")
elif(cur == "Y"):
    print("R")