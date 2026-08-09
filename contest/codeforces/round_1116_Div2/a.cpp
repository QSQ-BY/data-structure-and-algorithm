#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int f(int& a,int& b,int& c){
    if(a==b and a==c and b==c) return 0;
    int m = max(a,max(b,c));
    int n = min(a,min(b,c));
    if(a+b+c - m < m){
        return a+b+c - m - n;
    }
    return m - n;
}

int main(void){
    int t;
    cin>>t;
    for(int a = 0;a<t;a++){
        vector<int> arr(3);
        for(int i=0;i<3;i++){
            cin>>arr[i];
        }
        cout<<f(arr[0],arr[1],arr[2])<<"\n";
    }
    return 0;
}