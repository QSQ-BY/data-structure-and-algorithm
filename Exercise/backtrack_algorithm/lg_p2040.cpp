/* pmshz 在玩一个益 (ruo) 智 (zhi) 的小游戏，目的是打开九盏灯所有的灯，这样的游戏难倒了 pmshz……

题目描述
这个灯很奇 (fan) 怪 (ren)，点一下就会将这个灯和其周围四盏灯的开关状态全部改变。现在你的任务就是就是告诉 pmshz 要全部打开这些灯。

例如

0  1  1
1  0  0
1  0  1

点一下最中间的灯 (2,2) 就变成了

0  0  1
0  1  1
1  1  1

再点一下左上角的灯 (1,1) 就变成了

1  1  1
1  1  1
1  1  1

达成目标。

最少需要 2 步。

输入格式
9 个数字，以 3×3 的格式输入，每两个数字中间只有一个空格，表示灯初始的开关状态。（0 表示关，1 表示开）

输出格式
一个整数，表示最少打开所有灯所需要的步数。

输入输出样例
输入 #1复制

0 1 1
1 0 0
1 0 1
输出 #1复制

2 */

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
#define N 9
using namespace std;
map<int,int> dp;
int dir[5][2] = {
    {0,1},{0,-1},{1,0},{-1,0},{0,0},
};
int target;

void dfs(int t,int step){
    if(dp.find(t) == dp.end()){
        dp[t] = step;
    }else{
        if(dp[t] <= step) return;
        else dp[t] = step;
    }

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            int next_t = t;
            for(int k=0;k<5;k++){
                int dx = i+dir[k][0];
                int dy = j+dir[k][1];
                if (dx >= 0 and dx < 3 and dy >= 0 and dy < 3) {
                    int index = dx * 3 + dy;
                    next_t ^= 1 << index;
                }
            }
            dfs(next_t,step+1);
        }
    }
    return;
}

int main(void){
    int t = (1<<N)-1;
    target = t;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            int number;
            cin>>number;
            if(number == 0) {
                int index = i*3+j;
                t = t^(1<<index);
            }
        }
    }
    dfs(t,0);
    if(dp.find(target) != dp.end()) cout<<dp[target]<<endl;
    else cout<<-1<<endl;
    return 0;
}