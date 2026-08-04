/* 给你一个整数数组 nums ，和一个表示限制的整数 limit，
请你返回最长连续子数组的长度，
该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit。
示例 1：
输入：nums = [8,2,4,7], limit = 4
输出：2
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4.
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4.
因此，满足题意的最长子数组的长度为 2 。
示例 2：
输入：nums = [10,1,2,4,7,2], limit = 5
输出：4
解释：满足题意的最长子数组是 [2,4,7,2]，
其最大绝对差 |2-7| = 5 <= 5 。
示例 3：
输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3 */
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

using namespace std;
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        if(nums.size() <= 0 or limit<0) return 0;
        deque<int> min_q;//维护滑动窗口内的最小值
        deque<int> max_q;//维护滑动窗口内的最大值
        int l = 0;
        min_q.push_back(0);
        max_q.push_back(0);
        int ans = 0;
        for(int r = 1;r<nums.size();r++){
            while(!min_q.empty() and nums[r] < nums[min_q.back()]) min_q.pop_back();
            while(!max_q.empty() and nums[r] > nums[max_q.back()]) max_q.pop_back();
            max_q.push_back(r);
            min_q.push_back(r);
            while(nums[max_q.front()] - nums[min_q.front()] > limit){
                if(min_q.front() == l) min_q.pop_front();
                if(max_q.front() == l) max_q.pop_front();
                l++;
            }
            ans = max(ans,r-l+1);
        }
        return ans;
    }
};

void test01(){

    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}