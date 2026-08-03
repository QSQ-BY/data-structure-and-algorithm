/* 题目描述
? 小明要去一个国家旅游。这个国家有 N 个城市，编号为 1 至 N，
并且有 M 条道路连接着，小明准备从其中一个城市出发，
并只往东走到城市 i 停止。
? 所以他就需要选择最先到达的城市，并制定一条路线以城市 i 为终点，
使得线路上除了第一个城市，每个城市都在路线前一个城市东面，
并且满足这个前提下还希望游览的城市尽量多。
? 现在，你只知道每一条道路所连接的两个城市的相对位置关系，
但并不知道所有城市具体的位置。现在对于所有的 i，
都需要你为小明制定一条路线，
并求出以城市 i 为终点最多能够游览多少个城市。
输入
? 第 1 行为两个正整数 N,M。
? 接下来 M 行，每行两个正整数 x,y，
表示了有一条连接城市 x 与城市 y 的道路，
保证了城市 x 在城市 y 西面。
输出
? N 行，第 i 行包含一个正整数，
表示以第 i 个城市为终点最多能游览多少个城市。
样例输入
5 6
1 2
1 3
2 3
2 4
3 4
2 5
样例输出
1
2
3
4
3 */
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
void test01(){
    
    int n= 0;
    int m = 0;
    scanf("%d %d",&n,&m);
    vector<int> in_degree(n+5);//in_degree[i]表示i号点的入度
    vector<vector<int>> g(n+5);
    for(int i=0;i<m;i++){
        int x= 0;
        int y = 0;
        scanf("%d %d",&x,&y);
        in_degree[y]++;
        g[x].push_back(y);
    }
    vector<int> ans(n+5,0);
    queue<int> q;
    for(int i=1;i<=n;i++){
        if(in_degree[i]!=0) continue;
        q.push(i);
        ans[i] = 1;
    }
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        for(int i = 0;i<g[cur].size();i++){
            int t = g[cur][i];
            in_degree[t]--;
            if(in_degree[t] == 0) q.push(t);
            ans[t] = max(ans[cur]+1,ans[t]);
        }
    }
    for(int i=1;i<=n;i++) printf("%d\n",ans[i]);
}

int main(void){
    test01();
    system("pause");
    return 0;
}