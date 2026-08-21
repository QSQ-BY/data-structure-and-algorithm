/* 题目描述
上体育课的时候，小蛮的老师经常带着同学们一起做游戏。这次，老师带着同学们一起做传球游戏。

游戏规则是这样的：n 个同学站成一个圆圈，其中的一个同学手里拿着一个球，当老师吹哨子时开始传球，每个同学可以把球传给自己左右的两个同学中的一个（左右任意），当老师再次吹哨子时，传球停止，此时，拿着球没有传出去的那个同学就是败者，要给大家表演一个节目。

聪明的小蛮提出一个有趣的问题：有多少种不同的传球方法可以使得从小蛮手里开始传的球，传了 m 次以后，又回到小蛮手里。两种传球方法被视作不同的方法，当且仅当这两种方法中，接到球的同学按接球顺序组成的序列是不同的。比如有三个同学 1 号、2 号、3 号，并假设小蛮为 1 号，球传了 3 次回到小蛮手里的方式有 1→2→3→1 和 1→3→2→1，共 2 种。

输入格式
一行，有两个用空格隔开的整数 n,m(3≤n≤30,1≤m≤30)。

输出格式
1 个整数，表示符合题意的方法数。

输入输出样例
输入 #1复制

3 3
输出 #1复制

2

4 */

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
//f[i][j]经过j轮传球之后球在第i个人手里的方法总数
//f[i][j] = f[i+1][j-1]+f[i-1][j-1]
#define MAX_N 30
#define MAX_M 30
int f[MAX_N+5][MAX_M+5];
void test01(){
    int n;//总人数
    int m;//传球人数
    cin>>n>>m;
    f[0][0] = 0;
    f[1][0] = 1;
    f[1][1] = 0;
    f[n][1] = 1;
    f[2][1] = 1;
    for(int i=2;i<=n;i++){
        f[i][0] = 0;
    }
    for(int i=3;i<=n-1;i++){
        f[i][1] = 0;
    }
    for(int j=1;j<=m;j++){
        for(int i=1;i<=n;i++){
            int index1 = (i+1)%n;
            if(index1 == 0) index1=n;
            int index2 = (i-1)%n;
            if(index2 == 0) index2=n;
            f[i][j] = f[index1][j-1]+f[index2][j-1];
        }
    }
    cout<<f[1][m]<<endl;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}