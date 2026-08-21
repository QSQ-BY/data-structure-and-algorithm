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
//f[n]表示n的方案数  
//按照最后一个出栈的数字是几来进行拆分
//以x为结尾的方案数是f[x-1]*f[n-x]
#define MAX_N 18
int f[MAX_N+5];
void test01(){
    int n;
    cin>>n;
    f[0] = 1;
    f[1] = 1;
    f[2] = 2;
    for(int i=3;i<=n;i++){
        f[i] = 0;
        for(int x=1;x<=i;x++){
            f[i] += f[x-1]*f[i-x];
        }
    }
    cout<<f[n]<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}