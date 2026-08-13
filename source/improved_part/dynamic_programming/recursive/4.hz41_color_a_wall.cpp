/* 题目描述
给一个环形的墙壁涂颜色，颜色一共有 k 种，墙壁被竖直地划分成 n 个部分，相邻的部分颜色不能相同。请你写程序计算出一共有多少种给墙壁上色的方案？

例如，当 n=5,k=3? 时，下面是一种合法的涂色方案

44934979.jpg

而由于墙壁是环形的，所以下面就是一种非法的方案

10258141.jpg

输入
输入两个数字 n，k（1≤n≤103，2≤k≤10），分别代表墙壁数量和颜色种类。

输出
对于每个询问，输出一行整数，合法的墙壁涂色方案数。

样例输入1
5 3
样例输出1
30
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <cmath>

using namespace std;
#define MAX_N 1000//墙壁数量
#define MAX_K 10//颜色种数
//f[n][i][j] n块 首i 尾j 方案数
long long  f[MAX_N+5][MAX_K+5][MAX_K+5];
void test01(){
    long long  n,k;
    cin>>n>>k;
    for(long long  i=1;i<=k;i++) f[1][i][i] = 1;
    for(long long  i=1;i<=k;i++){
        for(long long  j=1;j<=k;j++){
            if(i==j){
                f[2][i][j] = 0;
            }else{
                f[2][i][j] = 1;
            }
        }
    }
    for(long long  wallsize=2;wallsize<=n;wallsize++){
        for(long long  i = 1;i<=k;i++){
            for(long long  j=1;j<=k;j++){
                f[wallsize][i][j] = 0;
                for(long long  l=1;l<=k;l++){
                    if(l==j) continue;
                    f[wallsize][i][j] += f[wallsize-1][i][l];
                }
            }
        }
    }
    long long  ans = 0;
    for(long long  i=1;i<=k;i++){
        for(long long  j=1;j<=k;j++){
            if(i==j) continue;
            ans += f[n][i][j];
        }
    }
    cout<<ans<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}