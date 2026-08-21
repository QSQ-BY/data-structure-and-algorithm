#include <iostream>
#include <vector>
#include <set>
using namespace std;
int check(const vector<int>& len, long long K, int l) {
    long long cuts = 0;
    for (int x : len) {
        cuts += (x - 1)/l;
        if (cuts > K) return 0;
    }
    return 1;
}

int main(void){
    int N;//木材总数
    int K;//切割次数
    cin>>N>>K;
    vector<int> len;
    int left = 1;
    int right = 1;
    for(int i=0;i<N;i++){
        int number;
        cin>>number;
        len.push_back(number);
        right = max(right,number);
    }
    while(left < right){
        int mid = (left + right)/2;
        if(check(len,K,mid) == 0) left = mid + 1;
        else if(check(len,K,mid) == 1) right = mid;
    }
    cout<<left<<endl;
    //system("pause");
    return 0;
}