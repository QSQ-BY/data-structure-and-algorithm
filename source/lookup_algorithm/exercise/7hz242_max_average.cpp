/* 题目描述
? 给定一个有 N 个元素的非负序列，
求长度大于等于 M 的连续子序列的最大平均值。 
输入
? 第一行输入两个数 N,M。（1≤N,M≤100000）
? 接下来 N 行，每行输入一个数表示非负序列。
输出
? 输出一个整数表示最大平均值乘 1000 的结果。
样例输入
10 6
6 
4
2
10
3
8
5
9
4
1 
样例输出
6500*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

//平均值A  0 1 2 ....... X X+1 ......... Z
//是否存在 1 1 1 ....... 1  0  ......... 0
//01二分算法模型

using namespace std;

long long check(vector<long long> nums, long long len, long long target) {
    for (long long i = 0; i < nums.size(); i++) {
        nums[i] = nums[i] - target;
    }
    vector<long long> prefix(nums.size() + 1, 0);//前缀和
    for (long long i = 0; i < nums.size(); i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    // 当前合法左端点中的最小前缀和
    long long minPrefix = prefix[0];
    for (long long right = len; right <= nums.size(); right++) {
        // right增加后，新加入的合法左端点
        minPrefix = min(minPrefix, prefix[right - len]);
        if (prefix[right] - minPrefix >= 0) {
            return 1;
        }
    }
    return 0;
}

void test01(){
    vector<long long> nums;
    long long n = 0;
    long long m = 0;
    cin>>n>>m;
    for(long long i=0;i<n;i++){
        long long num = 0;
        cin>>num;
        nums.push_back(num);
    }
    vector<long long> nums2 = nums;
    sort(nums2.begin(),nums2.end());
    long long head = nums2[0]*1000;
    long long tail = nums2[nums2.size()-1]*1000;
    long long mid = head + (tail - head +1)/2;
    vector<long long> nums3;
    for(long long i=0;i<nums.size();i++) nums3.push_back(nums[i]*1000);
    while(head < tail){
        mid = head + (tail - head +1)/2;
        if(check(nums3,m,mid) == 1) head = mid;
        else tail = mid-1;
    }
    long long ans = head;
    cout<<ans;
}

int main(void){
    test01();
    system("pause");
    return 0;
}