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


//使用哈希表和二分查找算法
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;
class Solution{
public:
//使用哈希表
    vector<int> twoSum1(vector<int>& nums, int target) {
        //<数组下标类型，存储的值的类型>
        //h[具体数值] = 对应的下标
        unordered_map<int,int> h;
        vector<int> ret(2);
        for(int i=0;i<nums.size();i++){
            if(h.find(target-nums[i])!=h.end()){
                ret[0] = h[target-nums[i]];
                ret[1] = i;
                break;
            }
            else{
                h[nums[i]] = i;
            }
        }
        return ret;
    }

//使用二分查找
    int binary_search(vector<int>& nums,vector<int>& index,int l,int r,int goal){
        int ret=-1;
        while(l<=r){
            int mid = l + (r-l)/2;
            if(nums[index[mid]] == goal) {
                ret = index[mid];
                break;
            }
            if(nums[index[mid]] < goal) l = mid+1;
            else r = mid-1;
        }
        return ret;
    }
    vector<int> twoSum(vector<int>& nums,int target){
        vector<int> ret(2);
        vector<int> index(nums.size());
        for(int i=0;i<nums.size();i++){
            index[i] = i;
        }
        sort(index.begin(),index.end(),[&](int i,int j)->bool{
            return nums[i]<nums[j];
        });
        for(int i = 0;i<nums.size();i++){
            int goal = target - nums[index[i]];
            int pos = binary_search(nums,index,i+1,nums.size()-1,goal);
            if(pos!=-1){
                ret[0] = index[i];
                ret[1] = pos;
                break;
            }
        }
        return ret;
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