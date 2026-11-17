""" 【问题描述】
小苯需要从中恰好选择 3 个两两不重叠的 1 × 2 或 2 × 1 子矩形并染红，要求每个
小红给定如下一个 6 × 6 矩阵：
11 8 3 27 24 1
2 21 16 35 17 4
9 29 20 30 5 10
36 33 13 6 23 7
31 14 15 28 12 25
34 19 18 37 22 39
被染红区域内两个数的和都是奇数。
如果两个方案选出的 3 个区域每个都完全相同，则认为它们是同一种方案，选择顺
序不作区分。
你不需要输出具体方案，你的任务就是求出满足条件的方案数。
【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。
本题的结果为一个整数，在提交答案时只需要编写一个程序输出这个整数，输出多
余的内容将无法得分。 """
def solution():
    g = [
        [11,8,3,27,24,1],
        [2,21,16,35,17,4], 
        [9,29,20,30,5,10], 
        [36,33,13,6,23,7], 
        [31,14,15,28,12,25], 
        [34,19,18,37,22,39],
    ] 
    available = []
    for i in range(6):
        for j in range(6):
            pos = i*6 + j
            if(j+1<6 and (g[i][j] + g[i][j+1])%2 == 1):
                available.append((pos,pos+1))
            if(i+1 < 6 and (g[i][j] + g[i+1][j])%2 == 1):
                available.append((pos,pos+6))
    ans = 0
    arr = [(0,0)]*(3)
    n = len(available)
    def check():
        s = set()
        for t in arr:
            if(t[0] in s or t[1] in s):
                return False
            else:
                s.add(t[0])
                s.add(t[1])
        if(len(s) == 6):
            return True
        else:
            return False
    def dfs(index,min,max):
        nonlocal ans
        if(index == 3):
            if(check()):
                ans += 1
            return
        for i in range(min,max+1):
            arr[index] = available[i]
            dfs(index+1,i+1,max)
    dfs(0,0,n-1)
    print(ans)
solution()
