/* 题目描述
? 输入 N 组数据，对每组数据输出逆序对个数。
输入
? 对于每组测试用例，第一行输入此组数据元素个数 x，
接下来 x 行，每行一个数，表示元素。（1≤x≤500000）
? 当读入的元素个数 x 为零时，程序结束。
输出
? 对于每组测试用例，输出一个数，表示逆序对个数。
样例输入
5
9
1
0
5
4
3
1
2
3
0
样例输出
6
0 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int inverse_pairs(vector<int>& arr,int l,int r){
    if(r-l <= 1) return 0;
    if(r-l == 2){
        if(arr[l] <= arr[l+1]) return 0;
        if(arr[l] > arr[l+1]) return 1;
    }
    int mid = (r+l)/2;

    int sum = 0;
    vector<int> arr1;
    vector<int> arr2;
    for(int i = l;i<mid;i++) arr1.push_back(arr[i]);
    for(int i = mid;i<r;i++) arr2.push_back(arr[i]);
    sort(arr1.begin(),arr1.end());
    sort(arr2.begin(),arr2.end());

    int p1 = 0;
    int p2 = 0;
    while(p1<arr1.size() or p2<arr2.size()){
        if((p1<arr1.size() and p2<arr2.size() and arr1[p1] <= arr2[p2]) or p2>=arr2.size()) p1++;
        else{
            p2++;
            sum+=arr1.size()-p1;
        }
    }
    int ans = 0;
    ans = sum + inverse_pairs(arr,l,mid) + inverse_pairs(arr,mid,r);
    return ans;
}

void test01(){
    int n = 0;
    cin>>n;
    vector<int> arr(n);
    for(int i = 0;i<n;i++) cin>>arr[i];
    int ans = 0;
    ans = inverse_pairs(arr,0,n);
    cout<<ans;
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}
