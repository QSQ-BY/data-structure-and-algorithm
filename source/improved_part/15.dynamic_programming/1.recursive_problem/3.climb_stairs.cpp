/* 题目描述
小海是一个顽皮的少年，对于爬楼梯这种事情，他从来都不愿意一步一步走，每次上楼梯的时候，要么往上跨两级，要么往上跨三级。对于有 n 级台阶的楼梯，小海想知道他从最下面走到最上面的方法总数。

83976316.jpg

输入
输入一个数字 n（1≤n≤500），代表台阶总数。

输出
输出一个整数，代表小海从最下面走到最上面的方法总数。

样例输入1
5
样例输出1
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
using namespace std;
#define MAX_N 500
vector<long long > dp(MAX_N+5,0);


void test01(){
    long long  n;
    cin>>n;
    dp[0] = 1;
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    for(long long  i=4;i<=n;i++){
        dp[i] = dp[i-2] + dp[i-3];
    }
    cout<<dp[n]<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}