#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

string f(vector<int>& nums){
    if(nums.size() == 1 or nums.size() == 2 or nums.size()==0) return "YES";
    for(int i=0;i<nums.size()-1;i++){
        if(nums[nums.size()-1] % nums[i] == 0){
            return "NO";
        }
    }
    return "YES";
}

int main(void){
    int t;
    cin>>t;//测试数
    for(int i=0;i<t;i++){
        int number;
        cin>>number;
        vector<int> nums;
        for(int k=0;k<=number-1;k++){
            nums.push_back(k+2);
        }
        cout<<f(nums)<<endl;
    }
    //system("pause");
    return 0;
}