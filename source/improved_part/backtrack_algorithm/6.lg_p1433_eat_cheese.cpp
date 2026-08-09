/* 题目描述
房间里放着 n 块奶酪。一只小老鼠要把它们都吃掉，问至少要跑多少距离？老鼠一开始在 (0,0) 点处。
输入格式
第一行有一个整数，表示奶酪的数量 n。
第 2 到第 (n+1) 行，每行两个实数，第 (i+1) 行的实数分别表示第 i 块奶酪的横纵坐标 x 
i
?
 ,y 
i
?
 。
输出格式
输出一行一个实数，表示要跑的最少距离，保留 2 位小数。

输入输出样例
输入 #1复制

4
1 1
1 -1
-1 1
-1 -1
输出 #1复制

7.41 */
#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
#include <algorithm>
using namespace std;
#define MAX_N 15
double ans = (double)INT_MAX;
double x[MAX_N+5];
double y[MAX_N+5];
double dis[MAX_N+5][MAX_N+5];//第i个点到第j个点的距离
vector<vector<double>> dp(70000,vector<double>(MAX_N+5,INT_MAX));
double index[70000];//权值映射

//当前状态码，当前位置，当前总路程
void dfs(int t,int pos,double s){
    if(t == 0){
        if(s < ans) ans = s;
        return;
    }
    for(int k= t;k!=0;k -= (k&-k)){
        int bit = k&-k;
        int next_index = index[bit];//当前枚举的点的编号
        int next_t = bit^t;//下一个状态码
        double new_dis = dis[pos][next_index] + s;
        if(new_dis>=ans) continue;
        if(new_dis >= dp[next_t][next_index]) continue;
        dp[next_t][next_index] = new_dis;
        dfs(next_t,next_index,new_dis);
    }
    return;
}

int main(void){
    int n;
    cin>>n;
    x[0] = y[0] = 0.0;
    for(int i=1;i<=n;i++){
        double cur_x;
        double cur_y;
        scanf("%lf%lf",&cur_x,&cur_y);
        x[i] = cur_x;
        y[i] = cur_y;
    }

    for(int i=0;i<=n;i++){
        for(int j = i;j<=n;j++){
            dis[i][j] = dis[j][i] = sqrt((x[i] - x[j])*(x[i]-x[j]) + (y[i] - y[j])*(y[i] - y[j]));
        }
    }

    for(int k = 1,i = 0;i<=MAX_N;i++,k=k*2) index[k] = i;
    dfs((1<<(n+1)) - 2,0,0);
    printf("%.2lf\n",ans);

    return 0;
}