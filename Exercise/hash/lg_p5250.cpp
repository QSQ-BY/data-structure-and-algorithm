#include <iostream>
#include <set>
#include <unordered_set>
#include <climits>
using namespace std;
int main(void){
    int m;
    unordered_set<int> h;
    cin>>m;
    for(int i=0;i<m;i++){
        int scode = 0;
        cin>>scode;
        int length;
        cin>>length;
        switch(scode){
            case 1:{
                if(h.find(length) == h.end()){
                    h.insert(length);
                }else if(h.find(length) != h.end()){
                    cout<<"Already Exist"<<endl;
                }
            };break;
            case 2:{
                if(h.empty()){
                    cout<<"Empty"<<endl;
                }else{
                    int temp = INT_MAX;
                    int ans = INT_MAX;
                    for(auto x:h){
                        if(abs(x-length) < temp){
                            temp = abs(x-length);
                            ans = x;
                        }else if(abs(x-length) == temp){
                            ans = min(ans,x);
                        }
                    }
                    h.erase(ans);
                    cout<<ans<<endl;
                }
            };break;
        }
    }
    //system("pause");
    return 0;
}