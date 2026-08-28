/* 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出
和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1] */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        int p1 = 0;
        int p2 = nums.size()-1;
        vector<int> ans;
        vector<int> index(nums.size());
        for(int i = 0;i<nums.size();i++) index[i] = i;
        sort(index.begin(),index.end(),[&](int i,int j)->bool{
            return nums[i]<nums[j];
        });
        while(p1 < p2){
            int temp_num = nums[index[p1]] + nums[index[p2]];
            if(temp_num == target){
                ans.push_back(index[p1]);
                ans.push_back(index[p2]);
                break;
            }else if(temp_num > target) p2--;
            else if(temp_num < target) p1++;
        }
        return ans;
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