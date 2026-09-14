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
#include <cmath>

using namespace std;
typedef pair<long long ,long long > PII;
struct Data{
    Data(long long  l,long long  r,long long  time){
        this->l = l;
        this->r = r;
        this->time = time;
    }
    long long  l;
    long long  r;
    long long  time;
};
vector<Data> datas;
vector<long long > ind(70000);
//t表示现在可用飞机的状态码，current_time表示现在的时间
bool dfs(long long  t,long long  current_time){
    if(t == 0){
        return true;
    }
    for(long long  temp = t;temp!=0;temp-=(-temp&temp)){
        long long  bit = -temp&temp;
        long long  next_plane_index = ind[bit];
        long long  next_t = t^bit;
        long long start_time =
            max(current_time, datas[next_plane_index].l);
        long long next_time =
            start_time + datas[next_plane_index].time;
        if(start_time>datas[next_plane_index].r){
            continue;
        }
        if(dfs(next_t,next_time)){
            return true;
        };
    }
    return false;
}

void solve(){
    long long  n=0;
    cin>>n;
    for(long long  i=0;i<n;i++){
        long long  left;
        long long  right;
        long long  t;
        cin>>left>>right>>t;
        right = left+right;
        Data new_data(left,right,t);
        datas.push_back(new_data);
    }
    for(long long  i=0,k=1;i<n;i++,k *=2){
        ind[k] = i;
    }
    long long  t = (1<<n) - 1;//状态码为1表示还没有起飞
    if(dfs(t,0)){
        cout<<"YES"<<endl;
    }else{
        cout<<"NO"<<endl;
    }
    return;
}

int main(void){
    long long  t;
    cin>>t;
    while(t--){
        datas.clear();
        solve();
    }
    return 0;
}