#include <iostream>
#include <vector>
using namespace std;
int main(void){
    int N;
    cin>>N;
    vector<int> prefix(N+1,0);
    for(int i=1;i<N+1;i++){
        cin>>prefix[i];
        prefix[i] = prefix[i] + prefix[i-1];
        prefix[i] = prefix[i]%7;
    }
    int ans = 0;
    vector<int> first(7,-1);
    for(int i=0;i<N+1;i++){
        if(first[prefix[i]] == -1) first[prefix[i]] = i;
        else ans = max(ans,i - first[prefix[i]]);
    }

    cout<<ans<<endl;
}