/* 题目描述
? 在一次聚会中，每人拿着一张印有石头、剪刀、布的卡片，
每个人具体拿得是哪种卡片不得而知。
? 现在告诉你某些人之间的胜负关系，
并会询问某两个人之间的对战结果，人按照从 1 到 n 编号。
? 对于每个询问，请给出正确的回答： Win(胜)、Loss(负)、Tie(平)
输入
第一行输入两个整数 n,m(1≤n≤10000，3≤m≤10000)，
分别代表人数和信息数量。
接下来 m 行，每行三个整 a,b,c（a∈[1,2], 1≤b,c≤n）
当 a=1 时，代表新增一条已知信息，表示 b, c 对战中 b 胜
当 a=2 时，代表根据以上信息，询问 b,c 对战中 b? 的结果
如果出现某条新增的信息与之前的信息发生冲突，就忽略此条信息。
输出
对于每个 a=2 的操作，
输出 Win、Loss、Tie 或 Unknown 代表对战双方的结果。
样例输入
6 6
1 1 2
2 1 3
1 2 4
1 4 3
2 1 3
2 4 1
样例输出
Unknown
Tie
Win */
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

class WeightedUnionSet{
public:
    WeightedUnionSet(int n){
        for(int i=0;i<n;i++){
            father.push_back(i);
            size.push_back(1);
            val.push_back(0);
        }
    }

    int find(int x){
        if(father[x] == x) return x;
        int root = find(father[x]);
        val[x] += val[father[x]];
        father[x] = root;
        return root;
    }

    int merge(int a,int b,int t){
        int set_a = find(a);
        int set_b = find(b);
        if(set_a == set_b) return 0;
        father[set_a] = set_b;
        size[set_b] = size[set_b]+size[set_a];
        val[set_a] = (t - val[a] + val[b]);
        return 1;
    }

    vector<int> val;//存储的是i节点到father[i]节点的关系
    vector<int> father;
    vector<int> size;
};

void test01(){
    int n;//人数
    int m;//信息数
    scanf("%d %d",&n,&m);
    WeightedUnionSet u(n);
    for(int i=0,a,b,c;i<m;i++){
        scanf("%d%d%d",&a,&b,&c);
        if(a==1){
            u.merge(b,c,2);
        }else {
            if(u.find(b) != u.find(c)) printf("Unknown\n");
            else {
                switch((u.val[b]%3 - u.val[c]%3 + 3) %3){
                    case 0:{printf("Tie\n");};break;
                    case 1:{printf("Loss\n");};break;
                    case 2:{printf("Win\n");};break;
                }
            }
        }
    }
    return;
}

int main(void){
    test01();
    //system("pause");
    return 0;
}