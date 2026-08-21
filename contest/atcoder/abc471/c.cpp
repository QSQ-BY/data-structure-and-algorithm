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
    int n;
    cin>>n;
    multiset<int> left_point;//左侧的点
    multiset<int> right_point;//右侧的点
    for(int i=0;i<n;i++){
        int point = 0;
        cin>>point;
        if(point>=0) left_point.insert(point);
        else right_point.insert(-point);
    }
    long long ans = 0;
    int current_pos = 0;
    for(int i=0;i<n;i++){
        int len_from_right;
        int len_from_left;
        if(right_point.empty()) len_from_right = INT_MAX;
        else len_from_right = (*right_point.begin()) - current_pos;
        if(left_point.empty()) len_from_left = INT_MAX;
        else len_from_left = current_pos+(*left_point.begin());
        if(len_from_right<=len_from_left){
            current_pos = *right_point.begin();
            ans+=len_from_right;
            right_point.erase(right_point.begin());
        }else{
            current_pos = -(*left_point.begin());
            ans += len_from_left;
            left_point.erase(left_point.begin());
        }
    }
    cout<<ans<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}