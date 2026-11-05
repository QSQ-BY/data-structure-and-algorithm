/* 题目描述
为了检测生产流水线上总共 N 件产品的质量，我们首先给每一件产品打一个分数 A 表示其品质，然后统计前 M 件产品中质量最差的产品的分值 Q 
M
​
 =min{A 
1
​
 ,A 
2
​
 ,⋯,A 
M
​
 }，以及第 2 至第 M+1 件的 Q 
M+1
​
 ,Q 
M+2
​
 ,⋯，最后统计第 N−M+1 至第 N 件的 Q 
N
​
 ，根据 Q 再做进一步评估。

请你尽快求出 Q 序列。

输入格式
输入共两行。

第一行共两个数 N,M，由空格隔开。含义如前述。

第二行共 N 个数，表示 N 件产品的质量。

输出格式
输出共 N−M+1 行。

第 1 至 N−M+1 行每行一个数，第 i 行的数表示 Q 
i+M−1
​
 。含义如前述。

输入输出样例
输入 #1复制

10 4
16 5 6 9 5 13 14 20 8 12
输出 #1复制

5
5
5
5
5
8
8
说明/提示
对于 30% 的数据，N≤1000。

对于 100% 的数据，1≤M≤N≤10 
5
 ，A 
i
​
 ≤10 
6
 。 */
#include <deque>
#include <iostream>
#include <vector>
using namespace std;
#define int long long

signed main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m;
    cin>>n>>m;
    vector<int> arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    deque<int> q;
    vector<int> ans(0);
    for(int i=0;i<n;i++){
        while(q.size()>0 and arr[q.back()] > arr[i]){
            q.pop_back();
        }
        int left = i - m+1;
        if(left < 0){
            left = 0;
        }
        while(q.size()>0 and q[0]<left){
            q.pop_front();
        }
        q.push_back(i);
        if(i-m+1 >= 0){
            ans.push_back(arr[q.front()]);
        }
    }
    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<endl;
    }
    return 0;
}
