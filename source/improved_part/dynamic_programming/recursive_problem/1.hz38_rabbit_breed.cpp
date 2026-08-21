/* 题目描述
如果有一对小兔，每一个月都生下一对小兔，而所生下的每一对小兔在出生后的第三个月也都生下一对小兔。那么，由一对兔子开始，n 个月后有多少对小兔子呢？

输入
输入一个数字 n（1≤n≤100），代表题目中询问的月份。

输出
对于每个询问，输出一行整数，代表 n 月的时候，小兔子的数量。

样例输入1
4
样例输出1
5
样例输入2
65
样例输出2
27777890035288 */
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
#define MAX_N 100
map<long,long> dp;
//会进行大量的重复运算
long long f(long long n){
    if(dp.find(n) != dp.end()) return dp[n]; 
    if(n<=2) return dp[n] = n;
    return dp[n] = f(n-1)+f(n-2);
}
//使用记忆化数组把已经求结果的值进行存储
void test01(){
    long long n;
    cin>>n;
    cout<<f(n)<<endl;
    return ;
}

//从下往上进行递推求解
long long  dp2[105] = {0};
void test02(){
    long long  n;
    cin>>n;
    dp2[1] = 1;
    dp2[2] = 2;
    for(long long  i=3;i<=n;i++){
        dp2[i] = dp2[i-1]+dp2[i-2];
    }
    cout<<dp2[n]<<endl;
}

int main(void){
    //test01();
    test02();
    return 0;
}