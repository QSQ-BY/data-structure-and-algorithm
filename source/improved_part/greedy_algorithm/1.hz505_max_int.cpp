/* 题目描述
? 现在有 n 个正整数，将他们连成一排，组成一个最大的整数。

? 例如，现在有三个整数 13,312,343，连接成最大整数为 34331213。

输入
? 第一行一个整数 n。（1≤n≤100000）

? 第二行 n 个不超过 int 类型范围的正整数。

输出
? 输出一个数表示组成的最大整数。

样例输入
3
121 12 96
 */
#include <iostream>
#include <climits>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool cmp(string a,string b){
    return stoll(a+b)> stoll(b+a);
}

int main(void){
    int n;
    cin>>n;
    vector<string> nums(n);
    for(int i=0;i<n;i++){
        cin>>nums[i];
    }

    sort(nums.begin(),nums.end(),cmp);
    for(int i=0;i<n;i++){
        cout<<nums[i];
    }
    cout<<"\n";
    //system("pause");
    return 0;
}