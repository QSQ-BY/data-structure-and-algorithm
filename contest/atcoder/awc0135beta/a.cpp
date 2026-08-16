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

void test01(){
    long long n;
    long long r;
    cin>>n>>r;
    long long m = INT_MAX;
    vector<long long> arr;
    for(long long i=0;i<n;i++){
        long long number;
        cin>>number;
        m = min(number ,m);
        arr.push_back(number);
    }
    long long ans = 0;
    for(long long i=0;i<n;i++){
        ans += arr[i] - m;
    }
    cout<<ans<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}