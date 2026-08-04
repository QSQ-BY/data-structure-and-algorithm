//二分查找算法
//双指针法
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> arr(10);
class Solution{
public:
    int search(vector<int>& arr,int target){
        int left = 0;
        int right = arr.size()-1;//定义target在左闭右闭得区间里[left,right]
        while(left<=right){
            //int mid = (left + right)/2
            int mid = right + ((left - right))/2;//防止int大小不够，造成溢出，与上一句等效
            if(arr[mid]>target){
                right = mid-1;//target在左侧区间内
            }else if(arr[mid] < target){
                left = mid+1;//target在右侧区间内
            }else if(arr[mid] == target){
                cout<<"find "<<target<<" successfully at position "<<mid<<endl;
                return 1;
            }
        }
        cout<<"don't find "<<target<<endl;
        return 0;
    }
};

void test01(){
    Solution s;
    for(int i=0;i<10;i++){
        arr[i] = 1;
    }
    for(int i =0 ;i<arr.size();i++){
        arr[i] = i+1;
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    s.search(arr,8);

    for(int i =0 ;i<arr.size();i++){
        arr[i] = i+1;
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    s.search(arr,6);
}
int main(void){
    test01();
    system("pause");
    return 0;
}
