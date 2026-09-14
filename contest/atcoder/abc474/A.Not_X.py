import sys
a = int(input())
for i in range(1,4):
    if(i == a):
        continue
    print(i)
    sys.exit()