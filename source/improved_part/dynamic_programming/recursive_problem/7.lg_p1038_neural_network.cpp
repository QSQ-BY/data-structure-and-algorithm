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
#define MAX_N 100
int c[MAX_N+5],u[MAX_N+5];//第i个节点的c和u
int w[MAX_N+5][MAX_N+5];//第i个节点到第j个节点的权值
vector<vector<int>> g(MAX_N+5,vector<int>());
int outdeg[MAX_N+5];
int indeg[MAX_N+5];

void test01(){
    int n;//n个节点
    int p;//p个链接关系
    cin>>n>>p;
    for(int i=1;i<=n;i++){
        cin>>c[i]>>u[i];
        if(c[i] == 0) c[i] = -u[i];
    }
    for(int i=0;i<p;i++){
        int node1;
        int node2;
        int weight;
        cin>>node1>>node2>>weight;
        w[node1][node2] = weight;
        outdeg[node1] +=1;
        indeg[node2] += 1;
        g[node1].push_back(node2);
    }
    queue<int> q;
    for(int i=1;i<=n;i++){
        if(indeg[i] != 0) continue;
        q.push(i);
    }
    while(!q.empty()){
        int index = q.front();
        q.pop();
        if(c[index] > 0){
            for(int i=0;i<g[index].size();i++){
                int next = g[index][i];
                c[next] += w[index][next]*c[index];
            }
        }
        for(int i=0;i<g[index].size();i++){
            int next = g[index][i];
            indeg[next] -=1;
            if(indeg[next] == 0){
                q.push(next);
            }
        }
    }
    int flag = 0;
    for(int i=1;i<=n;i++){
        if(outdeg[i] != 0) continue;
        if(c[i] <= 0) continue;
        flag = 1;
        cout<<i<<" "<<c[i]<<endl;
    }
    if(flag == 0) cout<<"NULL"<<endl;
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}