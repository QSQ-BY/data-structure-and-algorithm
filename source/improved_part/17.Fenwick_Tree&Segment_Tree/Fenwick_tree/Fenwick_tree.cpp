#include <iostream>
#include <vector>
using namespace std;
inline int lowbit(int x){
    return (x&(-x));
}

int a[10005];
int c[10005];

//单点修改
void add(int i,int x,int n){
    while(i <= n){
        c[i] += x;
        i += lowbit(i);
    }
    return;
}

//前缀和查询
int query(int i){
    int sum = 0;
    while(i){
        sum += c[i];
        i -= lowbit(i);
    }
    return sum;
}

int main(){
    int n = 0;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        add(i,a[i],n);
    }
    cout<<"a: ";
    for(int i = 1;i<=n;i++){
        printf("%4d",a[i]);
    }
    cout<<endl;
    cout<<"c: ";
    for(int i=1;i<=n;i++){
        printf("%4d",c[i]);
    }
    vector<int> pre(n+1,0);
    cout<<"s: ";
    for(int i = 1;i<=n;i++){
        int result = query(i);
        pre[i] = result;
        printf("%4d",result);
    }
    cout<<endl;
    int t = 0;
    cin>>t;
    for(int i=0;i<t;i++){
        int l = 0;
        int r = 0;
        cin>>l>>r;
        cout<<pre[r] - pre[l-1]<<" ";
    }
    cout<<endl;
    return 0;
}