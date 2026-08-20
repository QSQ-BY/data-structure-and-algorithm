#墙壁涂色重写
#动态规划优化方法2 ：状态重定义
""" f[n][j]表示前n块墙壁，用j颜色涂最后一块墙壁方法种类
默认第一块墙壁是0颜色，最后的方案数乘以总颜色数量即可，
因为每一中颜色状态对称 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
sys.set_int_max_str_digits(100000)

def test01():
    n,k = read()
    f = [[0]*(k+2) for _ in range(n+2)]
    f[1][0] = 1
    for i in range(2,n+1):
        for j in range(0,k):
            f[i][j] = 0
            for c in range(0,k):
                if c==j:continue
                f[i][j] += f[i-1][c]
    sum = 0
    for i in range(1,k): sum+=f[n][i]#把f[n][0]刨除因为已经定义了第一种颜色为0
    ans = sum*k
    print(ans)

def test02():
    #把状态降至1维
    """ f[n]表示前n块墙壁首尾颜色不同的方法总数
    倒数第二块与第一块颜色不同 (k-2)f[n-1]
    倒数第二块与第一块颜色相同 (k-1)f[n-2] """
    n,k = read()
    f = [0]*(n+2)
    f[2] = k*(k-1)
    f[3] = k*(k-1)*(k-2)
    for i in range(4,n+1):
        f[i] = f[i-1]*(k-2) + f[i-2]*(k-1)
    print(f[n])


#test01()
test02()