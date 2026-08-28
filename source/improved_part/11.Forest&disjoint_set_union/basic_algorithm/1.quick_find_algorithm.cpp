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

#define MAX_N 10000
int color[MAX_N+5];//color[i]表示第i个点的颜色

void init(int n){
    for(int i=0;i<=n;i++) color[i] = i;
    return;
}
//返回相关节点的颜色
int find(int a){
    return color[a];
}

int merge(int a,int b,int n){
    int color_a = find(a);
    int color_b = find(b);
    if(color_a == color_b) return 0;
    for(int i = 0;i<=n;i++){
        if(color[i] == color_a){
            color[i] = color_b;
        }
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
        printf("%3d ",color[i]);
    }
    printf("\n");
    for(int i=0;i<ret;i++) printf("-");
    printf("\n\n");
    return;
}

void test01(){
    int n,a,b;
    cin>>n;
    init(n);
    while(cin>>a>>b){
        int ret = merge(a,b,n);
        printf("把%d和%d合并:%d\n",a,b,ret);
        output(n);
    }
    return;
}

int main(void){
    test01();
    system("pause");
    return 0;
}