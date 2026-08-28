//检查数组中是否存在重复元素
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;
class Solution{
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> h;
        for(int i = 0;i<nums.size();i++){
            if(h.find(nums[i]) != h.end()) return true;
            h[nums[i]] = i;
        }
        return false;
    }
};

void test01(){
    Solution s;
}

int main(void){
    test01();
    system("pause");
    return 0;
}