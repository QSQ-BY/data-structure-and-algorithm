/* 题目描述
? 给出两个整数 a,b，每次操作可以把 a 变成 a+1 或 a*k 。求把 a 变成 b 至少需要几步操作。

输入
? 第一行三个数 a,b,k。（0≤a,b,k≤1018）

输出
? 输出最少操作次数。

样例输入
2 10 2
样例输出
3 */
#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
    long long  a,b,k;
    cin>>a>>b>>k;
    long long  ans = 0;
    if(k==0 or k==1){
        cout<<b-a<<endl;
        return 0;
    }

    if(a==0){
        ans++;
        a++;
    }

    while(1){
        if(a*k <= b){
            ans+= 1+ b%k;
            b = b/k;
        }else{
            ans+=b-a;
            break;
        }
    }
    cout<<ans<<endl;
    //system("pause");
    return 0;
}