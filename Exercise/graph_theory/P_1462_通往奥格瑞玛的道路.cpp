/* 题目背景
在艾泽拉斯大陆上有一位名叫歪嘴哦的神奇术士，他是部落的中坚力量。

有一天他醒来后发现自己居然到了联盟的主城暴风城。

在被众多联盟的士兵攻击后，他决定逃回自己的家乡奥格瑞玛。

题目描述
在艾泽拉斯，有 n 个城市。编号为 1,2,3,…,n。

城市之间有 m 条双向的公路，连接着两个城市，从某个城市到另一个城市，会遭到联盟的攻击，进而损失一定的血量。

每次经过一个城市，都会被收取一定的过路费（包括起点和终点）。路上并没有收费站。

假设 1 为暴风城，n 为奥格瑞玛，而他的血量最多为 b，出发时他的血量是满的。如果他的血量降低至负数，则他就无法到达奥格瑞玛。

歪嘴哦不希望花很多钱，他想知道，在所有可以到达奥格瑞玛的道路中，对于每条道路所经过的城市单次收费的最大值，其最小值为多少。

输入格式
第一行 3 个正整数，n,m,b。分别表示有 n 个城市，m 条公路，歪嘴哦的血量为 b。

接下来有 n 行，每行 1 个非负整数，f 
i
​
 。表示经过城市 i，需要交费 f 
i
​
  元。

再接下来有 m 行，每行 3 个正整数，a 
i
​
 ,b 
i
​
 ,c 
i
​
 （1≤a 
i
​
 ,b 
i
​
 ≤n）。表示城市 a 
i
​
  和城市 b 
i
​
  之间有一条公路，如果从城市 a 
i
​
  到城市 b 
i
​
 ，或者从城市 b 
i
​
  到城市 a 
i
​
 ，会损失 c 
i
​
  的血量。

输出格式
仅一个整数，表示歪嘴哦经过城市单次交费最大值的最小值。

如果他无法到达奥格瑞玛，输出 AFK。

输入输出样例
输入 #1复制

4 4 8
8
5
6
10
2 1 2
2 4 1
1 3 4
3 4 3
输出 #1复制

10
说明/提示
对于 60% 的数据，满足 n≤200，m≤10 
4
 ，b≤200；

对于 100% 的数据，满足 1≤n≤10 
4
 ，1≤m≤5×10 
4
 ，1≤b≤10 
9
 ；

对于 100% 的数据，满足 1≤c 
i
​
 ≤10 
9
 ，0≤f 
i
​
 ≤10 
9
 ，可能有两条边连接着相同的城市。 */

#include <iostream>
#include <vector>
#include <climits>
#include <set>
using namespace std;
#define int long long
int n,m,b;
typedef pair<int,int> PII;
vector<int> f(0);

//检查收费都不超过 limit 时，能否在血量耗尽前到达终点
int check(int limit,vector<vector<PII>>& g){
    if(f[0]>limit || f[n-1]>limit) return false;
    vector<int> dist(n,LLONG_MAX);
    set<PII> q;
    dist[0] = 0;
    //到达城市的累计耗血量，城市编号
    q.insert({0,0}); 
    while(!q.empty()){
        auto [d,u] = *q.begin();
        q.erase(q.begin());
        if(d != dist[u]){
            continue;
        }
        //最高血量为b
        if(d > b){
            return false;
        }
        if(u == n-1){
            return true;
        }

        for (auto [v,c] : g[u]){
            if(f[v] > limit){
                continue;
            }
            if(d+c < dist[v]){
                dist[v] = d+c;
                q.insert({dist[v],v});
            }
        }
    }
    return false;
}

signed main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m>>b;
    int left = LLONG_MAX;
    int right = -1;
    vector<vector<PII>> g(n,vector<PII>(0));
    for(int i=0;i<n;i++){
        int number;
        cin>>number;
        f.push_back(number);
        left = min(left,number);
        right = max(right,number);
    }
    for(int i=0;i<m;i++){
        int a,b,c;
        cin>>a>>b>>c;
        g[a-1].push_back(PII(b-1,c));
        g[b-1].push_back(PII(a-1,c));
    }
//检查能否保证每次收费都在m以内
//01二分模型
    if(check(right,g) == 0){
        cout<<"AFK"<<"\n";
        return 0;
    }
    while(left < right){
        int mid = left + (right-left)/2;
        if(check(mid,g) == 1){
            right = mid;
        }else{
            left = mid+1;
        }
    }
    cout<<left;
    return 0;
}

