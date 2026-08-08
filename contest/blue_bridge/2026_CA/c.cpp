#include <iostream>
#include <vector>
using namespace std;
int main(void){
    long long t;
    cin>>t;
    vector<long long> ans;
    for(long long i=0;i<t;i++){
        long long L,V,T;
        cin>>L>>V>>T;
        long long a = V*T;
        long long b = L-a;
        long long pos = (abs(a + b) )/2;
        ans.push_back(max(abs(pos - a),abs(pos - b)));
    }
    for(long long i=0;i<ans.size();i++) cout<<ans[i]<<endl;
    //system("pause");
    return 0;
}