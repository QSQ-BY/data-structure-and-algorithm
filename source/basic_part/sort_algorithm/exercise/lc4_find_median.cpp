/* 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
class Solution{
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int p1 = 0;
        int p2 = 0;
        vector<int> nums;
        while(p1 < nums1.size() or p2<nums2.size()){
            if((p1<nums1.size() and p2<nums2.size() and nums1[p1] < nums2[p2]) or p2>=nums2.size()){
                nums.push_back(nums1[p1]);
                p1++;
            }else{
                nums.push_back(nums2[p2]);
                p2++;
            }
        }

        double ans = 0.0;
        int n = nums.size();
        if(n%2 == 0){
            int n1 = n/2;
            int n2 = n1-1;
            ans = (double)(((double)nums[n1] + (double)nums[n2])/2.0);
        }else if(n%2 == 1){
            ans = (double)nums[n/2];
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