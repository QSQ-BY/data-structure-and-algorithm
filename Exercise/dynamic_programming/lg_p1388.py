import sys
import itertools
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
n = 0
k = 0
arr = []

def main():
    global n
    global k
    global arr
    
    n,k = read()
    arr = list(read())
    #dp[l][r][i]表示l到r区间之间使用i个乘号能得到的最大数值
    
    dp = [[[-1]*(k+2) for _ in range(n+2) ] for _ in range(n+2)]
    prefix = [0,*itertools.accumulate(arr)]
    arr = [0]+arr
    for l in range(1,n+1):
        for r in range(l,n+1):
            dp[l][r][0] = prefix[r] - prefix[l-1]


    for length in range(2, n + 1):
        for l in range(1, n - length + 2):
            r = l + length - 1
            for cnt in range(min(k, length - 1) + 1):
                for mid in range(l, r):
                    # 最外层是加号
                    for left_cnt in range(cnt + 1):
                        right_cnt = cnt - left_cnt
                        left = dp[l][mid][left_cnt]
                        right = dp[mid + 1][r][right_cnt]
                        if left != -1 and right != -1:
                            dp[l][r][cnt] = max(
                                dp[l][r][cnt],
                                left + right
                            )

                    # 最外层是乘号
                    for left_cnt in range(cnt):
                        right_cnt = cnt - 1 - left_cnt
                        left = dp[l][mid][left_cnt]
                        right = dp[mid + 1][r][right_cnt]
                        if left != -1 and right != -1:
                            dp[l][r][cnt] = max(
                                dp[l][r][cnt],
                                left * right
                            )
    print(dp[1][n][k])


if(__name__ == "__main__"):
    main()
