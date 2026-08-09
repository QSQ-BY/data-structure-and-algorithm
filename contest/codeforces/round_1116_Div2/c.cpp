#include <iostream>
#include <string>
#include <vector>
using namespace std;

void f(string s,int n){
    int red_score = 0;
    int cnt = 0;
    for(int i=0;i<n;i++){
        if(s[i] == '0') continue;
        else if(s[i] == '1') cnt++;
        int next;
        if(i==n-1) next = 0;
        else next = i+1;
        if(i%2==0){
            if(s[next] == '0') red_score++;
        }else if(i%2 == 1){
            if(s[next] == '1') red_score++;
        }
    }
    int blue_score = cnt - red_score;
    cout<<red_score<<" "<<blue_score<<endl;
}

int main(void){
    int t;
    cin>>t;
    for(int a=0;a<t;a++){
        int n;
        cin>>n;
        int k;
        cin>>k;
        string s;
        cin>>s;
        f(s,2*n);
    }
}