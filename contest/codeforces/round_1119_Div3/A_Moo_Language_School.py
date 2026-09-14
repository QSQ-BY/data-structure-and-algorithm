""" memory limit per test256 megabytes
Farmer John is trying to increase literacy rates in the United Cows of Farmer John (UCFJ). The UCFJ consists of n
 fields and nk
 farms (where n
 is a multiple of k
), with each farm consisting of k
 consecutive fields. In other words, the i
-th field is in the ⌈ik⌉
-th farm: Fields 1,2,…,k
 are in the first farm, fields k+1,k+2,…,2k
 are in the second farm, etc.

Farmer John wants to build schools such that each farm has at least one school. However, some fields are owned by Farmer Nhoj, who will charge Farmer John extra to build a school there. Farmer John wants to know the minimum number of times that he would have to build a school on Farmer Nhoj's land in order to ensure that each farm has at least one school.

Input
The first line of each input contains an integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains two integers n
 and k
 (1≤k≤n≤20
, n
 is a multiple of k
) — the number of fields and size of each farm.

The second line of each test case contains a binary string s
 of length n
 — the fields owned by Farmer Nhoj. If si=1
, the i
-th field is owned by Farmer Nhoj. If si=0
, the i
-th field is not owned by Farmer Nhoj.

Output
For each test case, output a single integer — the minimum number of times that Farmer John must build a school on Farmer Nhoj's land.

Example
InputCopy
6
8 2
10011100
5 1
11111
8 4
01111110
5 1
00101
4 4
1101
4 4
1111
OutputCopy
1
5
0
2
0
1 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def solve()->int:
    n , k = read()#一共n个田地，每个农场有k个田地
    set = n//k
    arr = list(input().decode().strip())
    ret = 0
    for set_index in range(set):
        start = set_index*k
        flag = 0
        for j in range(start,start+k):
            if(arr[j] == "0"):
                flag = 1
        if(flag == 0):
            ret+=1
    return ret

def main():
    ans = []
    t = int(input())
    while t:
        ans.append(solve())
        t-=1
    for number in ans:
        print(number)

if(__name__ == "__main__"):
    main()