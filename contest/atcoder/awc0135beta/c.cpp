/* Problem Statement  问题描述/问题陈述
Takahashi is exploring a dungeon represented as a grid with 
N rows and 
M columns. The cell at the 
i-th row from the top and the 
j-th column from the left is denoted as 
(i,j). Each cell 
(i,j) (
1≤i≤N, 
1≤j≤M) contains one gem with a value of 
A 
i,j
?
 .
高桥正在探索一个由网格构成的迷宫，该迷宫有 
N 行和 
M 列。位于第 
i 行、第 
j 列的单元格被标记为 
(i,j) 。每个位于 
(i,j) 位置的单元格（即坐标为 
1≤i≤N , 
1≤j≤M 的单元格）里都有一颗价值为 
A 
i,j
?
  的宝石。

Takahashi is currently at the top-left cell 
(1,1) of the dungeon. He wants to move to the bottom-right cell 
(N,M), which is the goal. In one move, Takahashi can advance exactly one cell to the right-adjacent cell or the down-adjacent cell from his current cell. That is, from cell 
(i,j), he can move to cell 
(i,j+1) (when 
j+1≤M) or cell 
(i+1,j) (when 
i+1≤N).
高桥目前位于地牢的左上角位置 
(1,1) 。他想要移动到右下角的位置 
(N,M) ，那里才是他的目标位置。在一次移动中，高桥可以从当前位置向右或向下移动一个单元格。也就是说，从位置 
(i,j) 出发，他可以移动到位置 
(i,j+1) （当 
j+1≤M 为真时）或位置 
(i+1,j) （当 
i+1≤N 为真时）。

Takahashi collects the gems placed on all cells he passes through (including the starting cell 
(1,1) and the ending cell 
(N,M)).
高桥会收集他经过的所有单元格中的宝石（包括起始单元格 
(1,1) 和结束单元格 
(N,M) ）。

Takahashi wants to maximize the total value of the gems he collects. Among all paths from 
(1,1) to 
(N,M), find and output the maximum possible total value of gems on the cells along the path.
高桥希望将自己收集到的宝石的总价值最大化。在从 
(1,1) 到 
(N,M) 的所有路径中，找出并输出路径上各节点上宝石总价值的最大值。

Constralong longs  约束
1≤N≤1000
1≤M≤1000
0≤A 
i,j
?
 ≤10 
9
 
All input values are long longegers.
所有输入值都是整数。
Input  输入复制
Copy  副本
N 
M
A 
1,1
?
  
A 
1,2
?
  
… 
A 
1,M
?
 
A 
2,1
?
  
A 
2,2
?
  
… 
A 
2,M
?
 
?
A 
N,1
?
  
A 
N,2
?
  
… 
A 
N,M
?
 
The first line contains an long longeger 
N representing the number of rows and an long longeger 
M representing the number of columns of the dungeon, separated by a space.
第一行包含两个整数： 
N 表示地牢的行数， 
M 表示地牢的列数。这两个数字之间用空格分隔。
In the following 
N lines, the 
i-th line (
1≤i≤N) contains the gem values 
A 
i,1
?
 ,A 
i,2
?
 ,…,A 
i,M
?
  of each cell in the 
i-th row of the grid, separated by spaces.
在接下来的 
N 行中，第 
i 行（即 
1≤i≤N 行）包含了网格中第 
i 行中每个单元格的宝石价值 
A 
i,1
?
 ,A 
i,2
?
 ,…,A 
i,M
?
  ，这些数值以空格分隔。
Output  输出
Output the maximum total value of gems that Takahashi can collect, on a single line.
在一行上输出高桥能够收集到的宝石的总价值最大值。

Sample Input 1  示例输入 1 复制
Copy  副本
3 3
1 2 3
4 5 6
7 8 9
Sample Output 1  示例输出 1 复制
Copy  副本
29
Sample Input 2  示例输入 2 复制
Copy  副本
4 5
3 1 4 1 5
9 2 6 5 3
5 8 9 7 9
3 2 3 8 4
Sample Output 2  示例输出 2 复制
Copy  副本
54
Sample Input 3  示例输入 3 复制
Copy  副本
6 8
100 200 50 300 10 400 150 80
250 30 500 20 600 70 90 200
80 700 100 800 50 300 400 100
150 60 900 200 100 1000 50 350
300 400 50 150 200 80 600 700
100 200 300 400 500 600 700 800
Sample Output 3  示例输出 3 复制
Copy  副本
5610
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
vector<vector<long long>> g(1005,vector<long long>(1005,INT_MIN));
vector<vector<long long>> dp(1005,vector<long long>(1005,INT_MIN));
long long n;//n行
long long m;//m列
void dfs(long long x,long long y,long long sum){
    if(dp[x][y] >= sum) return;
    dp[x][y] = sum;
    if(x == n and y == m){
        return;
    }
    long long dx;
    long long dy;
    dx = x+1;
    dy = y;
    if(dx<=n and dx>=1){
        dfs(dx,dy,sum+g[dx][dy]);
    }

    dx = x;
    dy = y+1;
    if(dy<=m and dy>=1){
        dfs(dx,dy,sum+g[dx][dy]);
    }
    return;
}
void test01(){
    cin>>n>>m;
    for(long long i=1;i<=n;i++){
        for(long long j=1;j<=m;j++){
            cin>>g[i][j];
        }
    }

    dfs(1,1,g[1][1]);
    cout<<dp[n][m]<<endl;
    return;
}

/* dp[i][j]表示从起点走到第(i,j)点所能获得的最大价值
dp[i][j] = g[i][j] + max(dp[i-1][j],dp[i][j-1]) */
void test02(){
    cin>>n>>m;
    for(long long i=1;i<=n;i++){
        for(long long j=1;j<=m;j++){
            cin>>g[i][j];
        }
    }
    dp[1][1] = g[1][1];
    for(long long i=1;i<=n;i++){
        for(long long j=1;j<=m;j++){
            if(i==1 and j==1) continue;
            dp[i][j] = g[i][j] + max(dp[i-1][j],dp[i][j-1]);
        }
    }
    cout<<dp[n][m]<<endl;
}

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    //test01();
    test02();
    //system("pause");
    return 0;
}
