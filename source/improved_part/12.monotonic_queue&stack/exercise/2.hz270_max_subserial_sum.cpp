/* 题目描述
? 输入一个长度为 n 的整数序列，
从中找出一段不超过 m 的连续子序列，
使得整个序列的和最大。
? 例如 1，?3,5,1，?2,3：
? 当 m=4 时，S=5+1?2+3=7；
? 当 m=2 或 m=3 时，S=5+1=6。
输入
? 第一行两个数 n,m?。
? 第二行有 n 个数，要求在 n 个数找到最大子序和。
输出
? 一个数，数出他们的最大子序和。
样例输入
6 4
1 -3 5 1 -2 3
样例输出
7 */
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
    int m;
    cin>>n;
    cin>>m;
    vector<int> prefix(n+1,0);
    for(int i=1;i<n+1;i++){
        cin>>prefix[i];
        prefix[i] +=  prefix[i-1];
    }

    deque<int> q;
    q.push_back(0);
    int ans = INT_MIN;
    for(int i=1;i<n+1;i++){
        while(!q.empty() and i-q.front() > m) q.pop_front();
        ans = max(ans,prefix[i] - prefix[q.front()]);
        while(!q.empty() and prefix[q.back()] > prefix[i]) q.pop_back();
        q.push_back(i);
    }
    cout<<ans<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}