/* 题目描述
由数字 0 组成的方阵中，有一任意形状的由数字 1 构成的闭合圈。现要求把闭合圈内的所有空间都填写成 2。例如：6×6 的方阵（n=6），涂色前和涂色后的方阵如下：

如果从某个 0 出发，只向上下左右 4 个方向移动且仅经过其他 0 的情况下，无法到达方阵的边界，就认为这个 0 在闭合圈内。闭合圈不一定是环形的，可以是任意形状，但保证闭合圈内的 0 是连通的（两两之间可以相互到达）。

0 0 0 0 0 0
0 0 0 1 1 1
0 1 1 0 0 1
1 1 0 0 0 1
1 0 0 1 0 1
1 1 1 1 1 1

0 0 0 0 0 0
0 0 0 1 1 1
0 1 1 2 2 1
1 1 2 2 2 1
1 2 2 1 2 1
1 1 1 1 1 1

输入格式
每组测试数据第一行一个整数 n(1≤n≤30)。

接下来 n 行，由 0 和 1 组成的 n×n 的方阵。

方阵内只有一个闭合圈，圈内至少有一个 0。

输出格式
已经填好数字 2 的完整方阵。

输入输出样例
输入 #1复制

6
0 0 0 0 0 0
0 0 1 1 1 1
0 1 1 0 0 1
1 1 0 0 0 1
1 0 0 0 0 1
1 1 1 1 1 1
输出 #1复制

0 0 0 0 0 0
0 0 1 1 1 1
0 1 1 2 2 1
1 1 2 2 2 1
1 2 2 2 2 1
1 1 1 1 1 1 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <climits>
using namespace std;
class Unionset{
public:
    Unionset(long long  n){
        for(long long  i=0;i<n;i++){
            father.push_back(i);
            size.push_back(1);
        }
        this->collection_sum = n;
        this->elements_sum = n;
    }

    long long  find(long long  x){
        if(father[x] == x) return x;
        else return father[x] = find(father[x]);
    }

    long long  merge(long long  a,long long  b){
        long long  set_a = find(a);
        long long  set_b = find(b);
        if(set_a == set_b) return 0;
        if(size[set_a] < size[set_b]){
            father[set_a] = set_b;
            size[set_b] += size[set_a];
        }else{
            father[set_b]  = set_a;
            size[set_a] +=size[set_b];
        }
        collection_sum--;
        return 1;
    }

    vector<long long > father;
    vector<long long > size;
    long long  collection_sum;
    long long  elements_sum;
};



typedef pair<long long ,long long > PII;
int main(void){
    long long  n;
    cin>>n;
    Unionset u((n+2)*(n+2));
    vector<vector<long long >> g(n+2,vector<long long >(n+2,1));
    vector<vector<long long >> ans(n+2,vector<long long >(n+2,1));
    map<PII,long long > ind;
    for(long long  i=1;i<=n;i++){
        for(long long  j=1;j<=n;j++){
            long long  number;
            cin>>number;
            g[i][j] = number;
            ans[i][j] = number;
            ind[PII(i,j)] = (i-1)*n+j;
        }
    }
    for(long long  i=1;i<=n;i++){
        for(long long  j=1;j<=n;j++){
            long long  index = ind[PII(i,j)];
            if(g[i][j] == 1) continue;
            if(i==1 or i==n or j==1 or j==n)  u.merge(0,index);
            if(j+1<=n and j+1>=0 and g[i][j+1]==0) u.merge(index,ind[PII(i,j+1)]);
            if(i+1<=n and i+1>=0 and g[i+1][j]==0) u.merge(index,ind[PII(i+1,j)]);
        }
    }

    for(long long  i=1;i<=n;i++){
        for(long long  j=1;j<=n;j++){
            if(g[i][j] == 1) continue;
            long long  index = ind[PII(i,j)];
            if(u.find(0) == u.find(index)) continue;
            else ans[i][j] = 2;
        }
    }

    for(long long  i=1;i<=n;i++){
        for(long long  j=1;j<=n;j++){
            cout<<ans[i][j]<<" ";
        }
        cout<<endl;
    }
    //system("pause");
    return 0;
}