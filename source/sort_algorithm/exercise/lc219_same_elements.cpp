/* 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个
不同的索引 i 和 j ，满足 nums[i] == nums[j]
且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
示例 1：
输入：nums = [1,2,3,1], k = 3
输出：true
示例 2：
输入：nums = [1,0,1,1], k = 1
输出：true
示例 3：
输入：nums = [1,2,3,1,2,3], k = 2
输出：false */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
class Solution{
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> index(n);
        for(int i = 0;i<n;i++) index[i] = i;
        sort(index.begin(),index.end(),[&](int i,int j)->bool{
            if(nums[i] != nums[j]) return nums[i]<nums[j];
            else return i<j;
        });
        for(int i=0;i<n-1;i++){
            if(nums[index[i]] != nums[index[i+1]]) continue;
            else if(index[i+1] - index[i] <= k) return true;
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