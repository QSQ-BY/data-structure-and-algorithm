#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> diff(200005);
vector<int> cur(200005);
int main(void){
    int n;//配方数
    int k;//某个温度被判定为可接受温度的最少配方数
    int q;//询问个数
    cin>>n>>k>>q;
    for(int i=0;i<n;i++){
        int l,r;
        scanf("%d %d",&l,&r);
        diff[l]++;
        diff[r+1]--;
    }
    for(int i=0;i<=200000;i++){
        if(i==0) cur[i] = diff[i];
        else{
            cur[i] = cur[i-1] + diff[i];
        }
    }
    vector<int> good(200005);
    good[0] = cur[0];
    if(good[0] >= k) good[0] = 1;
    else good[0] = 0;
    for(int i=1;i<=200000;i++){
        good[i] = cur[i];
        if(good[i] >= k) good[i] = 1;
        else good[i] = 0;
        good[i] += good[i-1];
    }

    for(int i=0;i<q;i++){
        int a,b;
        cin>>a>>b;
        cout<<good[b] - good[a-1]<<"\n";
    }
    //system("pause");

    return 0;
}