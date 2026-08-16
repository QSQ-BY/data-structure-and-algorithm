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
#define MAX_V 100000
int dp[MAX_V+5] = {0};
void test01(){
    int n,V;
    scanf("%d%d",&V,&n);
    for(int i=1,v,w,s;i<=n;i++){
        scanf("%d%d%d",&v,&w,&s);
        for(int k=0;k<s;k++){
            for(int j = V;j>=v;j--){
                dp[j] = max(dp[j],dp[j-v]+w);
            }
        }
    }
    printf("%d",dp[V]);
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}