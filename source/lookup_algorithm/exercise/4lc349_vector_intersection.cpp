/* 给定两个数组 nums1和nums2，返回它们的交集。
输出结果中的每个元素一定是 唯一 的。
我们可以 不考虑输出结果的顺序 。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的 */
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
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        unordered_set<int> h;
        set<int> s;
        for(auto x:nums2) s.insert(x);
        for(auto x:nums1) h.insert(x);
        for(auto x:s) if(h.find(x) != h.end()) ans.push_back(x);
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