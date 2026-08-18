""" 题目描述
有一个数字序列，求其中最长严格上升子序列的长度

B28E0055CAC24D4D8F260936BD6F358F.jpg
输入
输入一个数字n (1≤n≤1000000)，代表数字序列的长度。

后跟 n​ 个整数，第 i​ 个整数 ai(1≤ai≤10000)​，代表数字序列中的第 i​ 个值。

输出
输出一个整数，代表所求的最长严格上升子序列的长度。

样例输入
10
3 2 5 7 4 5 7 9 6 8
样例输出
5
"""
""" dp[i]为以i位置作为结尾的最长上升子序列
dp[i] = max(dp[j]) + 1(j属于1到i-1，且j要小于i) """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())

def main():
    n = int(input())
    arr = [0]+list(read())
    if(n==1):
        print(1)
        print(arr[1])
        return
    dp = [1]*(n+1)
    pre = [0]*(n+1)#pre[i]=j表示i的前一位为j
    index = 0#全局最大的位置
    ans_arr = []
    ans_index = []
    dp[0] = 0
    dp[1] = 1
    if(arr[1] < arr[2]):dp[2] = 2
    else:dp[2] = 1
    if(n==2):
        print(dp[2])
        if(dp[2] == 1):
            print(arr[2])
        elif(dp[2] == 2):
            print("".join(map(str,arr)))
        return
    ans = float("-inf")
    for i in range(2,n+1):
        for j in range(1,i):
            if(arr[j] >= arr[i]):continue
            if(dp[j]+1 > dp[i]):
                dp[i] = dp[j] + 1
                pre[i] = j
        if(dp[i] > ans):
            ans = dp[i]
            index = i
    print(ans)
    while(index):
        ans_arr.append(arr[index])
        ans_index.append(index)
        index = pre[index]
    ans_arr.reverse()
    ans_index.reverse()
    print(" ".join(map(str,ans_index)))
    print(" ".join(map(str,ans_arr)))
    print("\n")
    return

if(__name__ == "__main__"):
    main()