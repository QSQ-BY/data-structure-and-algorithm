#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
int main(void){
    int n;//配方数
    int k;//某个温度被判定为可接受温度的最少配方数
    int q;//询问个数
    cin>>n>>k>>q;
    unordered_map<int,int> h;
    for(int i=0;i<n;i++){
        int l,r;
        scanf("%d %d",&l,&r);
        for(int j=l;j<=r;j++) h[j]++;
    }


    for(int i=0;i<q;i++){
        int ans = 0;
        int a,b;
        cin>>a>>b;
        for(int j=a;j<=b;j++){
            if(h.find(j) == h.end()) continue;
            else {
                if(h[j] >= k) ans++;
            }
        }
        printf("%d\n",ans);
    }
    //system("pause");

    return 0;
}