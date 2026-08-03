/* 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121] */


//双指针法
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        vector<int> result(nums.size(), 0);
        int left = 0;
        int right = nums.size() - 1;
        int pos = nums.size() - 1;
        while (left <= right)
        {
            int left_sq = nums[left] * nums[left];
            int right_sq = nums[right] * nums[right];
            if (left_sq >= right_sq)
            {
                result[pos] = (left_sq);
                left++;
            }
            else
            {
                result[pos] = right_sq;
                right--;
            }
            pos--;
        }
        return result;
    }
};
void test01()
{
    Solution s;
    vector<int> arr;
    arr = {-3, -1, 0, 2, 3, 4};
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    vector<int> result = s.sortedSquares(arr);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    cout << endl;
    cout << endl;
}

int main(void)
{
    test01();
    system("pause");
    return 0;
}