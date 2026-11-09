#include <iostream>
using namespace std;
inline int lowbit(int x){
    return x & -x;
}

int main(void){
    int x = 0;
    cin>>x;
    cout<<x<<" = ";
    while(x){
        cout<<lowbit(x);
        x ^= lowbit(x);
        if(x) cout<<" + ";
    }
    cout<<"\n";
    system("pause");
    return 0;
}