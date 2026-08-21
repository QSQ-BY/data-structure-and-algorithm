/* 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;
//二分查找
class Solution{
public:
    int searchInsert(vector<int>& nums, int target) {
        //可将原问题抽象为01二分模型
        //小于target的设为0大于则设为1
        //寻找第一个1的位置即可
        int left = 0;
        int right = nums.size();//最后一位也是合法的插入位置
        int mid = 0;
        while(left<right){
            mid = (left+right)/2;
            if(nums[mid] < target) left = mid+1;
            else right = mid;
            if(target == nums[mid]) return mid;
        }
        return mid;
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