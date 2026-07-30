/* 给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：
输入：s = 7, nums = [3,1,2,1,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。 */

//滑动指针法
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> arr;
class Solution{
public:
    int minSubArrayLen(int target,vector<int>& arr){
        if(arr.empty()) return 0;
        int index1 = 0;
        int sum = 0;
        int result = (arr.size()) + 1;
        for(int index2 = 0; index2 < (arr.size()); index2++){
            sum += arr[index2];
            while(sum >= target){
                int temp = index2 - index1 + 1;
                if(temp < result) result = temp;
                sum -= arr[index1];
                ++index1;
            }
        }
        if(result == (arr.size()) + 1) result = 0;
        return result;
    }
};
void test01(){
    Solution s;
    arr = {3,1,2,1,4,3};
    int target = 7;
    int result = s.minSubArrayLen(target , arr);
    cout<<result;
}

int main(void){
    test01();
    system("pause");
    return 0;
}