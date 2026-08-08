/* 有一个 n×m 的棋盘，在某个点 (x,y) 上有一个马，要求你计算出马到达棋盘上任意一个点最少要走几步。

输入格式
输入只有一行四个整数，分别为 n,m,x,y。

输出格式
一个 n×m 的矩阵，代表马到达某个点最少要走几步（不能到达则输出 ?1）。

输入输出样例
输入 #1复制

3 3 1 1
输出 #1复制

0 3 2    
3 -1 1    
2 1 4   */
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <queue>
using namespace std;

//方向数组
int dir[8][2] = {
    {2,1},{-2,1},{2,-1},{-2,-1},
    {1,2},{1,-2},{-1,2},{-1,-2},
};

void dfs(int cur_x,int cur_y,int n,int m,int cnt,vector<vector<int>>& g){
    if(g[cur_x][cur_y] != -1 and g[cur_x][cur_y] <= cnt){
        return;
    }else g[cur_x][cur_y] = cnt;
    for(int k = 0;k<8;k++){
        int dx = cur_x + dir[k][0];
        int dy = cur_y + dir[k][1]; 
        if(dx<1 or dx>n) continue;
        if(dy<1 or dy>m) continue;
        dfs(dx,dy,n,m,cnt+1,g);
    }
    return ;
}

//广搜队列
struct Node{
    Node(int x,int y,int s){
        this->x = x;
        this->y = y;
        this->s = s;
    }
    int x,y,s;//x,y坐标以及到达该点的最短距离s
};

void bfs(int x,int y,int n,int m,vector<vector<int>>& g2){
    queue<Node> q;
    q.push(Node(x,y,0));
    g2[x][y] = 0;
    while(!q.empty()){
        Node temp = q.front();
        q.pop();
        for(int k=0;k<8;k++){
            int dx = temp.x + dir[k][0];
            int dy = temp.y + dir[k][1];
            if(dx<1 or dx>n) continue;
            if(dy<1 or dy>m) continue;
            if(g2[dx][dy] != -1) continue;
            q.push(Node(dx,dy,temp.s+1));
            g2[dx][dy] = temp.s + 1;
        }
    }
}


int main(void){
    int n;//棋盘行数
    int m;//棋盘列数
    int x;//马纵坐标
    int y;//马的横坐标
    scanf("%d %d %d %d",&n,&m,&x,&y);
    vector<vector<int>> g(n+1,vector<int>(m+1,-1));
    vector<vector<int>> g2(n+1,vector<int>(m+1,-1));
    //dfs(x,y,n,m,0,g);
    /* for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(j>1) printf(" ");
            printf("%d",g[i][j]);
        }
        printf("\n");
    } */
    bfs(x,y,n,m,g2);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(j>1) printf(" ");
            printf("%d",g2[i][j]);
        }
        printf("\n");
    }
    //system("pause");
    return 0;
}