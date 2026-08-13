/* 题目描述
将整数 n 分成 k 份，且每份不能为空，任意两个方案不相同（不考虑顺序）。

例如：n=7，k=3，下面三种分法被认为是相同的。

1,1,5；
1,5,1；
5,1,1。

问有多少种不同的分法。

输入格式
n,k（6<n≤200,2≤k≤6）。

输出格式
1 个整数，即不同的分法。

输入输出样例
输入 #1复制

7 3
输出 #1复制

4
说明/提示
四种分法为：
1,1,5；
1,2,4；
1,3,3；
2,2,3。

【题目来源】

NOIP 2001 提高组第二题 */

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
#define MAX_N 200
#define MAX_K 6
/* f[i][j]为把数字i拆分为j份的方案总数
f[i][j] = f[i-1][j-1]+f[i-j][j] */

int n;
int k;
int f[MAX_N+5][MAX_K+5];
void test01(){
    cin>>n>>k;

    for(int i=0;i<=n;i++){
        f[i][1] = 1;
        f[i][0] = 0;
    }

    for(int i=0;i<=k;i++){
        f[0][k] = 0;
        if(i!=0) f[i][i] = 1;
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i and j<=k;j++){
            f[i][j] = f[i-1][j-1]+f[i-j][j];
        }
    }
    cout<<f[n][k]<<endl;
    return;
}

int ans = 0;
//现在即将填入第几个位置的数字,现在填入的最小的数字，现在所有数字的和
void dfs(int pos,int min,int sum){
    if(pos == k and sum == n){
        ans++;
        return;
    }
    if(pos<k and sum>n){
        return;
    }
    if(pos == k and sum!=n){
        return;
    }

    for(int number = min;number<=n-sum;number++){
        dfs(pos+1,number,sum+number);
    }
    return;
}

void test02(){
    cin>>n>>k;
    dfs(0,1,0);
    cout<<ans<<endl;
}

int main(void){
    //test01();
    test02();
    //system("pause");
    return 0;
}