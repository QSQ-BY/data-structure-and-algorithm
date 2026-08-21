//quick_union算法
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#define MAX_N 10000
using namespace std;
int father[MAX_N+5];//father[i]表示i元素的父亲是谁
int Size[MAX_N+5];

void init(int n){
    for(int i=0;i<=n;i++) {
        father[i] = i;
        Size[i] = 1;
    }
    return;
}

//寻找i节点的根节点
int find(int x){
    if(father[x] == x) return x;
    return father[x] = find(father[x]);
}

//按秩优化
int merge(int a,int b){
    int set_a = find(a);
    int set_b = find(b);
    if(set_a == set_b) return 0;
    if(Size[set_a] < Size[set_b]){
        father[set_a] = set_b;
        Size[set_b] = Size[set_b] + Size[set_a];
    }else{
        father[set_b] = set_a;
        Size[set_a] = Size[set_a] + Size[set_b];
    }
    return 1;
}

void output(int n){
    int ret = 0;
    for(int i=0;i<=n;i++){
        ret+=printf("%3d ",i);
    }
    printf("\n");
    for(int i=0;i<=n;i++){
        printf("%3d ",father[i]);
    }
    printf("\n");
    for(int i=0;i<=n;i++){
        printf("%3d ",Size[i]);
    }
    cout<<endl;
    for(int i=0;i<ret;i++) printf("-");
    printf("\n");

    return;
}

void test01(){
    int n;
    cin>>n;
    int a,b;
    init(n);
    while(cin>>a>>b){
        printf("合并%d和%d:%d\n",a,b,merge(a,b));
        output(n);
        printf("find(%d):%d\n",a,find(a));
        printf("find(%d):%d\n",b,find(b));
        printf("\n");
    }
}

int main(void){
    test01();
    system("pause");
    return 0;
}