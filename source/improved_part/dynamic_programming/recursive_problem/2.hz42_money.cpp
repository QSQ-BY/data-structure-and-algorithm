/* 题目描述
某个国家的货币系统中，有 m 种面额的钱币，现在要用这 m 种面额的钱币凑足 n 元钱，问一共有多少种方法。m 种钱币不一定要都被用到。

例如，有 3 种钱币，分别为1、2、5，那么有四种方法拼凑出5元钱

(1，1，1，1，1) 全是1元钱
(1，2，2)，(1，1，1，2) 使用1元和2元
(5) 只用5元钱
注意：方案中的钱币不分顺序，也就是说（1，2，2） 和（2，1，2）是同一种方法。

输入
输入两个数字 m, n（1≤m≤20,200≤n≤10000），第二行 m 个数字，代表 m 种钱币的面额，钱币面额大于0，数据中保证 m 种钱币各不相同。

输出
输出一个整数，代表拼凑出 n 元钱的方法数，答案有可能过大，请对 9973 取余。

样例输入1
8 200
1 2 5 10 20 50 100 200
样例输出1
3871 */
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
#define MAX_N 10000
#define MAX_M 20
//确定递推状态
//f[i][j]表示的是用前i种钱币凑足j元钱的方法
//f[i][j] = f[i-1][j]+f[i][j-val[i]]
long long  f[MAX_M+5][MAX_N+5];
void test01(){
    long long  m,n;
    cin>>m>>n;
    vector<long long > val;
    for(long long  i=1;i<=m;i++){
        long long  number;
        cin>>number;
        val.push_back(number);
    }

    for(long long  i=1;i<=m;i++){
        f[i][0] = 1;
        for(long long  j=1;j<=n;j++){
            f[i][j] = f[i-1][j];
            if(j<val[i-1]) {
                f[i][j] = f[i][j]%9973;
                continue;
            }
            f[i][j] += f[i][j-val[i-1]];
            f[i][j] = f[i][j]%9973;
        }
    }
    cout<<f[m][n]%9973<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}