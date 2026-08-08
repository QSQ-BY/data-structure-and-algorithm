/* 题目描述
给定一个 N×M 方格的迷宫，迷宫里有 T 处障碍，障碍处不可通过。
在迷宫中移动有上下左右四种方式，每次只能移动一个方格。数据保证起点上没有障碍。
给定起点坐标和终点坐标，每个方格最多经过一次，问有多少种从起点坐标到终点坐标的方案。
输入格式
第一行为3个正整数 N,M,T，分别表示迷宫的长宽和障碍总数。
第二行为四个正整数 SX,SY,FX,FY。SX,SY 代表起点坐标，FX,FY 代表终点坐标。
接下来 T 行，每行两个正整数，表示障碍点的坐标。
输出格
输出从起点坐标到终点坐标的方案总数。
输入输出样例
输入 #1复制
2 2 1
1 1 2 2
1 2
输出 #1复制
1 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int ans = 0;
int dir[4][2] = {
    {0,1},{1,0},{0,-1},{-1,0},
};

void dfs(int cur_x,int cur_y,int target_x,int target_y,vector<vector<int>>& g){
    if(cur_x == target_x and cur_y == target_y){
        ans++;
        return ;
    }
    g[cur_x][cur_y] = 0;
    for(int i=0;i<4;i++){
        int dx = cur_x + dir[i][0];
        int dy = cur_y + dir[i][1];
        if(g[dx][dy] == 0) continue;
        dfs(dx,dy,target_x,target_y,g);
    }

    g[cur_x][cur_y] = 1;
    return ;
}

int main(void){
    int N;//迷宫纵向长度
    int M;//迷宫横向长度
    int T;//障碍总数
    scanf("%d %d %d",&N,&M,&T);
    vector<vector<int>> g(N+2,vector<int> (M+2,0));//状态图
    int begin_x,begin_y,target_x,target_y;
    scanf("%d%d%d%d",&begin_x,&begin_y,&target_x,&target_y);
    for(int i=1;i<=N;i++){
        for(int j=1;j<=M;j++){
            g[i][j] = 1;
        }
    }
    for(int i=0;i<T;i++){
        int x;
        int y;
        scanf("%d%d",&x,&y);
        g[x][y] = 0;
    }
    dfs(begin_x,begin_y,target_x,target_y,g);
    cout<<ans<<endl;
    return 0;
}