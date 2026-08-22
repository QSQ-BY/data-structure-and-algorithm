import sys
s = list(input().strip())
for i,ch in enumerate(s):
    if(ch != "A"):
        s[i] = "."
print("".join(s))