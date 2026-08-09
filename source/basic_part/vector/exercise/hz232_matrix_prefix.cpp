/* 题目描述
? 一种新型的激光炸弹，可以摧毁一个边长为 R 的正方形内的所有的目标。现在地图上有 N(N≤10000) 个目标，用整数 Xi,Yi(其值在[0,5000]) 表示目标在地图上的位置，每个目标都有一个价值 Wi。
? 激光炸弹的投放是通过卫星定位的，但其有一个缺点，就是其爆破范围，即那个边长为 R 的正方形的边必须和 x,y 轴平行。若目标位于爆破正方形的边上，该目标将不会被摧毁。求一颗炸弹最多能炸掉地图上总价值为多少的目标。
输入
? 输入的第一行为正整数 N 和正整数 R。（1≤N≤10000）
? 接下来的 N 行每行有 3 个正整数，分别表示 Xi,Yi,Wi。
输出
? 输出一颗炸弹最多能炸掉地图上总价值为多少的目标。（结果不会超过 32767）
样例输入
2 1
0 0 1
1 1 1
样例输出
1 */
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g(5005,vector<int>(5005,0));

int main(void){
    int n,r;
    cin>>n>>r;
    int max_x = r;
    int max_y =r;
    for(int i=0;i<n;i++){
        int x;
        int y;
        int w;
        cin>>x>>y>>w;
        g[x+1][y+1] += w;
        if(x + 1>max_x) max_x = x+1;
        if(y + 1>max_y) max_y = y+1;
    }

    for(int i=1;i<=max_x;i++){
        for(int j=1;j<=max_y;j++){
            g[i][j] = g[i][j]+g[i-1][j]+g[i][j-1]-g[i-1][j-1];
        }
    }
    int ans = 0;
    for(int i=1;i<=max_x-r+1;i++){
        for(int j=1;j<=max_y-r+1;j++){
            int k = i+r-1;
            int l = j+r-1;
            int sum = g[k][l] + g[i-1][j-1] - g[i-1][l]-g[k][j-1];
            ans = max(sum,ans);
        }
    }
    cout<<ans<<endl;
}