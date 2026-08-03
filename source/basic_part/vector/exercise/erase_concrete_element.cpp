/* 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 
你不需要考虑数组中超出新长度后面的元素。
示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 
并且 nums 中的前五个元素为 0, 1, 3, 0, 4。 */

//快慢指针法
#include <iostream>
#include <vector>
using namespace std;
vector<int> arr;
class Solution{
public:
    int erase(vector<int>& arr,int val){
        //快慢指针法
        //快指针i遍历数组寻找删除的目标元素，慢指针j记录下一个不等于目标元素的元素应该放置的位置
        int slow = 0;
        for(int fast = 0;fast<arr.size();fast++){
            if(arr[fast] != val){
                arr[slow] = arr[fast];
                slow++;
            }
        }
        return slow;
    }
};


void test01(){
    Solution s;
    arr = {0,1,2,2,3,0,4,2};
    for(int i = 0;i<arr.size();i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    int newLength = s.erase(arr,2);
    for(int i = 0;i<newLength;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}


int main(void){
    test01();
    system("pause");
    return 0;
}