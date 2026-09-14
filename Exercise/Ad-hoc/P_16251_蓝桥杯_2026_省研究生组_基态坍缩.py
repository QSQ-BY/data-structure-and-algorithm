import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solve()->int:
    n = int(input())
    arr = list(read())
    ret = "L"
    cnt = 0
    for i in range(n-1,0,-1):
        if(arr[i] != 1):
            break
        cnt += 1
    if(cnt%2 == 0):
        ret = "L"
    elif(cnt%2 == 1):
        ret = "Q"
    return ret

def main():
    t = int(input())
    ans = []
    while t:
        t -= 1
        ans.append(solve())
    for number in ans:
        print(number)

if __name__ == "__main__":
    main()
