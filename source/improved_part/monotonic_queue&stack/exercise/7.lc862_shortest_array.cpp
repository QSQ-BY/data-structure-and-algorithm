/* 给你一个整数数组 nums 和一个整数 k ，
找出 nums 中和至少为 k 的 最短非空子数组 ，
并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。
子数组 是数组中 连续 的一部分。
示例 1：
输入：nums = [1], k = 1
输出：1
示例 2：
输入：nums = [1,2], k = 4
输出：-1
示例 3：
输入：nums = [2,-1,2], k = 3
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
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(nums.size()+1,0);
        prefix.push_back(0);
        for(int i=1;i<n+1;i++){
            prefix[i] = prefix[i-1] + nums[i-1 ];
        }
        deque<int> q;
        q.push_back(0);
        int ans = n+1;
        for(int i=1;i<n+1;i++){
            while(!q.empty() and prefix[i] - prefix[q.front()] >= k){
                ans = min(ans,i - q.front());
                q.pop_front();
            }
            while(!q.empty() and prefix[q.back()] > prefix[i]) q.pop_back();
            q.push_back(i);
        }
        if(ans == n+1) return -1;
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