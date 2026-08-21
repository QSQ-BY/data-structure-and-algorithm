#include <iostream>
#include <vector>
#include <climits>
#include <cmath>
#include <unordered_set>
using namespace std;
typedef pair<int,int> PII;
int f(const vector<PII>& arr) {
    int m = static_cast<int>(arr.size());

    //m+2的情况
    for (int i = 0; i<m-1; i++) {
        if (arr[i].second >= 2 && arr[i + 1].second >= 2) {
            return m + 2;
        }
    }

    //m+1的情况
    for (int i = 0; i < m; i++) {
        if (arr[i].second < 2) {
            continue;
        }
        
        bool left =
            i >= 1 &&
            (i == 1 || arr[i - 2].first != arr[i].first);

        bool right =
            i + 1 < m &&
            (i + 2 >= m || arr[i + 2].first != arr[i].first);

        if (left || right) {
            return m + 1;
        }
    }

    return m;
}

int main(void){
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int j=0;j<n;j++){
            scanf("%d",&arr[j]);
        }
        vector<PII> new_arr;
        new_arr.push_back(PII(arr[0],1));
        for(int j=1;j<n;j++){
        if(arr[j] == new_arr[new_arr.size()-1].first){
            new_arr[new_arr.size()-1].second++;
        }else if(arr[j] != new_arr[new_arr.size()-1].first){
            new_arr.push_back(PII(arr[j],1));
        }
    }
        cout<<f(new_arr)<<endl;
    }
    return 0;
}