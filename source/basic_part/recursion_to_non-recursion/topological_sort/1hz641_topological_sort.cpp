/* 题目描述
? 给定一个有 N个点，M条边的有向无权图，现求其拓扑排序。
若有多个拓扑排序，则尽可能让小数在前大数在后。
输入
? 输入文件第一行是两个整数 n 和 m。接下来 m行，每行 2个整数 a,b
，表示有一条从 a点到 b点的边，保证数据中无环。
输出
? 输出文件包含1行，共有 N个整数，
表示拓扑排序，每两个数中间用空格隔开。
样例输入
7 6
1 2
1 4
2 3
4 5
3 6
5 6
样例输出
1 2 3 4 5 6 7 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>

using namespace std;
#define MAX_N 2000
int in_degree[MAX_N+5] = {0};//表示i节点的入度
vector<vector<int>> g(MAX_N+5);
void test01(){
    int n;
    int m;
    vector<int> ans;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        int a;
        int b;
        cin>>a>>b;
        in_degree[b]++;
        g[a].push_back(b);
    }
    set<int> q;
    for(int i=1;i<=n;i++){
        if(in_degree[i] == 0) q.insert(i);
    }
    while(q.size() >0){
        int cur = *q.begin();//取出堆顶元素
        ans.push_back(cur);
        q.erase(q.begin());//出队
        for(int i=0;i<g[cur].size();i++){
            int t = g[cur][i];
            in_degree[t]--;
            if(in_degree[t]==0) q.insert(t);
        }
    }
    for(int i=0;i<ans.size()-1;i++) cout<<ans[i]<<" ";
    cout<<ans[ans.size()-1]<<endl;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}