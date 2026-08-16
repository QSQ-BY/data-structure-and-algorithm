import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def is_prime(number:int)->bool:
    if(number <2):
        return False
    if(number == 2):
        return True
    if(number %2 == 0):
        return False
    for i in range(3,math.isqrt(number)+1,2):
        if(number %i == 0):
            return False
    return True

def dfs(state:int,index:list[int],string:list[str])->int|None:
    if(state == 0):
        if(is_prime(int("".join(string))) == True):
            return int("".join(string))
        return
    bit = (-state&state)
    string_index = index[bit.bit_length() - 1]
    for digit in range(10):
        string[string_index] = str(digit)
        new_state = state^bit
        ans = dfs(new_state,index,string)
        if(ans is not None):
            return ans
        string[string_index] = "*"
    return

def solve()->int:
    string = list(input()).strip()
    index = []
    for i , ch in enumerate(string):
        if(ch == "*"):
            index.append(i)
    state = (1<<len(index)) - 1
    ans = dfs(state,index,string)
    if(ans is not None):
        return ans
    else :
        return -1

def main()->None:
    test_number = int(input())
    answers = []
    while(test_number>0):
        answers.append(str(solve()))
        test_number-=1
    print("\n".join(answers))

if(__name__ == "__main__"):
    main()