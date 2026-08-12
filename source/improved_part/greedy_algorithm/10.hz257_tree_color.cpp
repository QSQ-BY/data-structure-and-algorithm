/* 题目描述
? 有一棵树，它的所有节点都需要染色，每个节点都有一个代价基础值 Ci。第一个染色的是根节点，其余节点染色的时候其父节点必须已染色。染色一个节点会用掉一个时间单位，每个节点染色的代价是染完此节点时的总时间 T 乘上这个节点的基础值 Ci。求染完所有节点所需的最小代价。

输入
? 第一行包含两个整数 N,R 其中，N 是树中节点个数，R 是根节点编号。

? 第二行输入 N 个整数，编号为 i 的节点的代价基础值 Ci。（1≤Ci≤500）

? 接下来 N?1 行为边的信息，每行两个数分别表示父节点编号和子节点编号。

输出
? 输出一个整数，表示最小代价。

样例输入
5 1
1 2 1 2 4
1 2
1 3
2 4
3 5
样例输出
33 */
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
#define MAX_N 1000
using namespace std;
int n;//总结点数量
int r;//根节点编号
vector<int> c(MAX_N+5,0);//代表第i个节点的权值
vector<int> father(MAX_N+5,0);//代表第i个节点父节点的编号
vector<int> vis(MAX_N+5,0);//1表示该节点已经被合并
vector<double> w(MAX_N+5,0);//合并后每个节点的真实权重
vector<int> cnt(MAX_N+5,1);
long long ans = 0;

int find_max(){
    int m = INT_MIN;
    for(int i=1;i<=n;i++){
        if(i == r or vis[i]==1) continue;
        if(m == INT_MIN or w[i]>w[m]) m=i;
    }
    return m;
}

int find_father(int x){
    if(vis[father[x]] == 1) return find_father(father[x]);
    else return father[x];
}
int main(void){
    cin>>n>>r;
    for(int i=1;i<=n;i++){
        cin>>c[i];
        ans+=c[i];
        father[i] = i;//每个节点最开始的父节点都是自己
        w[i] = c[i];
    }

    for(int i=1;i<=n-1;i++){
        int a;
        int b;
        cin>>a>>b;//边由a指向b,a是父节点是子节点
        father[b] = a;
    }

    //进行n-1轮的合并,每次合并权值最大的节点
    for(int i=1;i<=n-1;i++){
        int x = find_max();
        int father_x = find_father(x);
        //把x和father[x]进行合并
        ans+=cnt[father_x]*c[x];
        c[father_x] += c[x];
        cnt[father_x] += cnt[x];
        w[father_x] = 1.0*c[father_x]/cnt[father_x];
        vis[x] = 1;
    }
    cout<<ans<<endl;
    //system("pause");
    return 0;
}