/* 
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 
表示的高度图，在这种情况下，
可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9 */
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
    int trap(vector<int>& height) {
        if(height.size() == 0 or height.size()==1 or hright.size()==2 or height.empty()) return 0;
        int ans = 0;
        stack<int> s;
        for(int i=0;i<height.size();i++){
            while(!s.empty() and height[s.top()] < height[i]){
                int cur_h = height[s.top()];
                s.pop();
                if(s.empty()) break;
                ans += (min(height[s.top()],height[i]) -cur_h)*(i - s.top()-1);
            }
            s.push(i);
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