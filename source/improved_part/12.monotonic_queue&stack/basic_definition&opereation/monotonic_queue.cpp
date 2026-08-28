//单调队列->单调队列的第一个元素永远是当前维护区间的最值
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

using namespace std;

void output(vector<int>& arr){
    int n = arr.size();
    int len = 0;
    for(int i=0;i<n;i++){
        len+=printf("%3d",i);
    }
    printf("\n");
    for(int i=0;i<n;i++){
        printf("%3d",arr[i]);
    }
    printf("\n");
    for(int i=0;i<len;i++) printf("-");
    printf("\n\n");
    return;
}


//单调队列用于维护区间最值
void test01(){
    int n;//队列的总长度
    int k;//滑动窗口的长度
    cin>>n>>k;
    deque<int> q;
    vector<int> arr;
    vector<int> ans;
    for(int i=0;i<n;i++){
        int a;
        cin>>a;
        arr.push_back(a);
    }
    output(arr);
    for(int i=0;i<n;i++){
        while(!q.empty() and arr[q.back()] > arr[i]) q.pop_back();
        q.push_back(i);//index
        if(i - q.front()>=k) q.pop_front();
        printf("min(%d,%d) = arr[%d] = %d\n",max(i-k+1,0),i,q.front(),arr[q.front()]);
        if(ans.size() ==0 ) ans.push_back(arr[q.front()]);
        else{
            if(ans[ans.size()-1] != arr[q.front()]) ans.push_back(arr[q.front()]);
        }
    }

    printf("\n");
    sort(ans.begin(),ans.end());
    output(ans);
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}