/* 题目描述
? 有 C 头奶牛需要挤奶，每头奶牛需要在规定的时间开始挤奶，并在规定的时间结束挤奶，每头奶牛挤奶时会占据一台机器。求 C 头奶牛在规定的时间挤奶至少需要多少台挤奶机。

输入
? 第一行输入一个数 C。（1≤C≤50000）

? 接下来 C 行，每行两个数表示每头奶牛开始挤奶的时间和结束挤奶的时间。（均小于 1,000,000）

输出
? 第一行输出最少需要的机器数量。

? 接下来 C 行，每行输出一个数，表示第 i 头奶牛使用的挤奶机编号。（奶牛优先使用编号小的机器）

样例输入
5
1 10
2 4
3 6
5 8
4 7
样例输出
4
1
2
3
2
4 */

#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;
#define MAX_N 50005
struct Data{
    int l;
    int r;
    int ind;
};

bool cmp(const Data& a,const Data& b){
    return a.l < b.l;
}

vector<Data> arr(MAX_N + 5);
vector<int> ans(MAX_N+5);

int m_time[MAX_N+5];//time[i]记录第i台机器结束挤奶的时间
int cnt = 0;
int main(void){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>arr[i].l>>arr[i].r;
        arr[i].ind = i;
    }
    stable_sort(arr.begin(),arr.begin() + n,cmp);
    for(int i=0;i<n;i++){
        int pos = -1;
        for(int j=0;j<cnt;j++){
            if(m_time[j] < arr[i].l){
                pos = j;
                break;
            }
        }
        if(pos == -1){
            pos = cnt;
            cnt++;
        }
        m_time[pos] = arr[i].r;
        ans[arr[i].ind] = pos+1;
    }
    cout<<cnt<<endl;
    for(int i = 0;i<n;i++){
        cout<<ans[i]<<endl;
    }
    return 0;
}