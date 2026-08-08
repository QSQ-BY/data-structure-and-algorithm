/* 给一 n×n 的字母方阵，内可能蕴含多个 yizhong 单词。单词在方阵中是沿着同一方向连续摆放的。摆放可沿着 8 个方向的任一方向，同一单词摆放时不再改变方向，单词与单词之间可以交叉，因此有可能共用字母。输出时，将不是单词的字母用 * 代替，以突出显示单词。
输入格式
第一行输入一个数 n。(7≤n≤100)。
第二行开始输入 n×n 的字母矩阵。
输出格式
突出显示单词的 n×n 矩阵。
输入输出样例
输入 #1复制
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
输出 #1复制
*******
*******
*******
*******
*******
*******
*******
输入 #2复制
8
qyizhong
gydthkjy
nwidghji
orbzsfgz
hhgrhwth
zzzzzozo
iwdfrgng
yyyygggg
输出 #2复制
*yizhong
gy******
n*i*****
o**z****
h***h***
z****o**
i*****n*
y******g */
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <climits>
using namespace std;
#define MAX_N 100

int dir[8][2]={
    {1,1},{-1,-1},{1,-1},{-1,1},
    {0,1},{1,0},{0,-1},{-1,0},
};
vector<vector<char>> g(MAX_N+5,vector<char>(MAX_N+5,'0'));
vector<vector<int>> vis(MAX_N+5,vector<int>(MAX_N+5,0));//表示某个点已经被访问过
vector<vector<int>> ans(MAX_N+5,vector<int>(MAX_N+5,0));//表示某个位置成功匹配字符串
int n;
string target = "yizhong";

void dfs(int x,int y){
    if (x < 1 || x > n || y < 1 || y > n) return;
    if(vis[x][y] == 1) return;
    if(g[x][y] == 'y'){
        for(int i=0;i<8;i++){
            int flag = 1;
            for(int j=1;j<=6;j++){
                int dx = x + j*dir[i][0];
                int dy = y + j*dir[i][1];
                if (dx < 1 || dx > n || dy < 1 || dy > n) {
                    flag = 0;
                    break;
                }
                if(target[j] == g[dx][dy]){
                    continue;
                }
                flag = 0;
                break;
            }
            if(flag == 1){
                for(int j=0;j<=6;j++){
                    int dx = x + j*dir[i][0];
                    int dy = y + j*dir[i][1];
                    ans[dx][dy] = 1;
                }
            }
        }
    }
    vis[x][y] = 1;
    dfs(x,y+1);
    dfs(x+1,y);
    return;
}


int main(void){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cin>>g[i][j];//坐标从1到n
        }
    }
    dfs(1,1);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(ans[i][j] == 1) cout<<g[i][j];
            else cout<<'*';
        }
        printf("\n");
    }
    return 0;
}