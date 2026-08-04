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



//二分算法
//查找两个正序数组中排名第k位置的数字

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <cinttypes>

using namespace std;
class Solution{
public:
    int min(int a,int b){
        if(a<b) return a;
        else return b;
        return 0;
    }
    int findK(vector<int>& nums1,vector<int>& nums2,int index1,int index2,int k){
        if(k==1){
            int a = 0;
            int b = 0;
            if(nums1.size() == index1) a = INT32_MAX;
            else a = nums1[index1];
            if(nums2.size() == index2) b = INT32_MAX;
            else b = nums2[index2];
            return min(a,b);
        }
        if(index1 == nums1.size()) return nums2[index2 + k-1];
        if(index2 == nums2.size()) return nums1[index1+k-1];

        int cnt1 = min(k/2,nums1.size()-index1);
        int cnt2 = min(k - cnt1,nums2.size()-index2);
        cnt1 = k-cnt2;
        if(nums1[index1+cnt1-1] <= nums2[index2+cnt2-1]){
            return findK(nums1,nums2,index1+cnt1,index2,k-cnt1);
        }
        else return findK(nums1,nums2,index1,index2+cnt2,k-cnt2);
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if((nums1.size()+nums2.size())%2 == 1) return (double)findK(nums1,nums2,0,0,(nums1.size()+nums2.size())/2+1);
        if((nums1.size()+nums2.size())%2 == 0){
            int k1 = (nums1.size()+nums2.size())/2;
            int k2 = k1+1;
            int a = findK(nums1,nums2,0,0,k1);
            int b = findK(nums1,nums2,0,0,k2);
            double ans = (double)(((double)a+(double)b)/2.0);
            return ans;
        }
        return 0.0;
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