/* 题目描述
? 给出一个长度为 N 的数组，一个长为 K 的滑动窗口从最左移动到最右，
每次窗口移动，如下图：
找出窗口在各个位置时的极大值和极小值。
输入
? 第一行两个数 N,K。
? 第二行有 N 个数，表示数组中的元素。
输出
? 输出两行，第一行为窗口在各个位置时的极小值，第二行为窗口在各个位置时的极大值。
样例输入
8 3
1 3 -1 -3 5 3 6 7
样例输出
-1 -3 -3 -3 3 3
3 3 5 5 6 7 */
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

void test01(){
    int n;
    int k;
    cin>>n>>k;
    vector<int> arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    deque<int> q;

    //输出滑动窗口的极小值
    for(int i=0;i<n;i++){
        while(!q.empty() and arr[q.back()] > arr[i]) q.pop_back();
        q.push_back(i);
        if(i - q.front() >= k) q.pop_front();
        if(i+1 >= k){
            if(i>=k) cout<<" ";
            cout<<arr[q.front()];
        }
    }
    cout<<endl;

    q.clear();

    //输出滑动窗口的极大值
    for(int i=0;i<n;i++){
        while(!q.empty() and arr[q.back()] < arr[i]) q.pop_back();
        q.push_back(i);
        if(i - q.front() >= k) q.pop_front();
        if(i+1 >= k){
            if(i>=k) cout<<" ";
            cout<<arr[q.front()];
        }
    }
    cout<<endl;
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}