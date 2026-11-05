import sys
input = sys.stdin.buffer.readline

arr1 = input().decode().strip()
arr2 = input().decode().strip()
if((arr1[0] == "A" and arr2[1] == "D") or (arr1[0] == "D" and arr2[1] == "A") or(arr1[1] == "A" and arr2[0] == "D") or (arr1[1] == "D" and arr2[0] == "A")):
    print("No")
else:
    print("Yes")